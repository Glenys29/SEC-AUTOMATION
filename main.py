
import time
from log_collector import tail_log
from log_parser import is_anomaly
from alert_sender import send_alert

LOG_FILE_PATH = "logs/windows_eventlogs.log" # Path to the generated windows event log file

if __name__ == "__main__":
    print("[*] Monitoring log file for anomalies...\n")
    # Continously read the log file and check for anomalies
    for log_entry in tail_log(LOG_FILE_PATH):
        anomaly = is_anomaly(log_entry) # Check if the log entry contains any anamaly keyword
        if anomaly:
            send_alert(anomaly, log_entry) # send an alert of anomaly is detected
        time.sleep(1)
