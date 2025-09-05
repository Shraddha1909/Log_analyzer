import os
import pytest
from log_analyzer import analyze_log, save_report

@pytest.fixture
def sample_log(tmp_path):
    log_file = tmp_path / "test.log"
    log_file.write_text(
        "2025-09-05 10:01:23 INFO System started\n"
        "2025-09-05 10:02:10 WARNING High memory usage\n"
        "2025-09-05 10:03:45 ERROR Disk not found\n"
        "2025-09-05 10:05:11 INFO User login successful\n"
        "2025-09-05 10:07:32 ERROR File corruption detected\n"
    )
    return log_file

def test_analyze_log(sample_log):
    counts = analyze_log(sample_log)
    assert counts["INFO"] == 2
    assert counts["WARNING"] == 1
    assert counts["ERROR"] == 2

def test_save_report(sample_log, tmp_path):
    counts = analyze_log(sample_log)
    report_file = tmp_path / "report.csv"
    save_report(counts, report_file)

    assert os.path.exists(report_file)

    with open(report_file, "r") as f:
        content = f.read()
    assert "ERROR,2" in content
    assert "INFO,2" in content

