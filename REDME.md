# Log Analyzer Automation

#  Overview
A simple log analyzer built in Python that:
- Reads a log file.
- Counts `INFO`, `WARNING`, and `ERROR` messages.
- Generates a CSV report.
- Includes automated tests using pytest.

#  How to Run
1. Clone this repo:
   ```bash
   git clone <your-repo-url>
   cd log-analyzer

#install dependencies
pip install -r requirements.txt

#Eun the analyzer
python log_analyzer.py

#run tests
pytest -v

