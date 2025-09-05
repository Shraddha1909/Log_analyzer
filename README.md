#  Log Analyzer Automation  

[![Python Tests](https://github.com/Shraddha1909/Log_analyzer/actions/workflows/python-app.yml/badge.svg)](https://github.com/Shraddha1909/Log_analyzer/actions)

A Python-based **log analyzer** that automates parsing of log files, counts log levels, and generates CSV reports.  
Includes **automated testing with pytest** and **CI/CD using GitHub Actions** .  

---

##  Features  
-  Reads any log file  
-  Counts `INFO`, `WARNING`, and `ERROR` messages  
-  Exports results into a **CSV report**  
-  Unit-tested with **pytest**  
-  Continuous Integration with **GitHub Actions**  

---

##  Project Structure  

log_analyzer.py # Main script
system.log # Sample log file
test_log_analyzer.py # Unit tests (pytest)
requirements.txt # Dependencies
README.md # Documentation
.github/workflows/ # GitHub Actions workflow (CI/CD)


---

##  Getting Started  

### 1. Clone the repo  
```bash
git clone https://github.com/Shraddha1909/Log_analyzer.git
cd Log_analyzer

2. Install dependencies

pip install -r requirements.txt

3. Run the analyzer

python log_analyzer.py

4. Run tests

pytest -v

 Example

Sample log file (system.log):

2025-09-05 10:01:23 INFO System started
2025-09-05 10:02:10 WARNING High memory usage
2025-09-05 10:03:45 ERROR Disk not found

Generated report (report.csv):
Level	Count
INFO	1
WARNING	1
ERROR	1
 Tech Stack

    Python 3.x

    Pytest (for testing)

    GitHub Actions (CI/CD)

 Future Improvements

    Support JSON & Excel reports

    Log visualization with graphs

    CLI arguments for custom log paths


