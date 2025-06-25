import re

# List of keywords considered anomalies
anomaly_keywords = [
    "Multiple failed logins",
    "Unauthorized access attempt",
    "Service crash",
    "Unexpected shutdown",
    "Malware detection",
    "High CPU usage",
    "Port scanning activity",
    "Suspicious process started"
]

def is_anomaly(log_line):
    for keyword in anomaly_keywords:
        if keyword.lower() in log_line.lower():
            return keyword
    return None
