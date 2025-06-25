import time
from log_collector import tail_log
from log_parser import is_anomaly
from alert_sender import send_alert

LOG_FILE_PATH = "logs/windows_eventlogs.log"

if __name__ == "__main__":
    print("[*] Monitoring log file for anomalies...\n")
    for log_entry in tail_log(LOG_FILE_PATH):
        anomaly = is_anomaly(log_entry)
        if anomaly:
            send_alert(anomaly, log_entry)
        time.sleep(1)