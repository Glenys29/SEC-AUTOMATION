def send_alert(anomaly_type, line):
    print(f"\n🚨 ALERT: {anomaly_type.upper()}")
    print(f"↳ Log Line: {line.strip()}")
    print("-" * 60)
