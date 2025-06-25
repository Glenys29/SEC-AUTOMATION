# SEC-AUTOMATION
 A Python-based security automation system designed to parse and analyze Windows event logs for suspicious activity.

 
## Automated Security Log Analysis and Alerting System
This project is a Python-based security automation system designed to parse and analyze Windows event logs for suspicious activity. It detects anomalies such as unauthorized access attempts, service crashes, and malware indicators, and send alert. The system simulates SIEM-like functionality by automating log collection, anomaly detection, and alert presentation to assist in real-time threat monitoring and incident response.

### Features
- Reads and tails a simulated log file in real time.
- Parses log lines using regular expressions and keyword matching.
- Detects known anomaly types such as unauthorized access, malware activity, and service crashes.
- Prints alert messages to the terminal for detected threats.
- Modular and easy-to-extend Python code.

### Technologies Used
- Python 3.10+
- Standard Python libraries (`re`, `time`, `collections`, etc.)
- Git for version control
## Project Structure
SEC-AUTOMATION/
├── Logs/
│ └── windows_eventlogs.log # Windows event log data 
├── src/
│ ├── log_collector.py # Reads the log file line by line
│ ├── log_parser.py # Detects anomalies using keyword matching and regular expression
│ ├── alert_sender.py # Send an alert when an anomaly is detected
│ └── main.py # Runs the system



