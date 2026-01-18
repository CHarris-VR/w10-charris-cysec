# Step 6: enum
from enum import Enum


# Parse each line into parts (Original)
# records = []
#for line in lines:
#    date, alert_type, asset, indicator = line.split(",")
#    records.append((date, alert_type, asset, indicator))


# Step 7 Adding definition to the enum (moved alert 7 above records
# to fix error at line 32.)
class AlertType(Enum):
    LOGIN_FAILURE = "login_failure"
    LOGIN_SUCCESS = "login_success"
    FILE_HASH_DETECTED = "file_hash_detected"
    DNS_QUERY = "dns_query"
    PORT_SCAN = "port_scan"

    # modifying and update Alert Class to use Enum and Severity Logic
class Alert:
    def __init__(self, date, alert_type, asset, indicator):
        self.date = date
        self.alert_type = alert_type  # now an AlertType
        self.asset = asset
        self.indicator = indicator

    # Severity def    
    def severity(self):
        if self.alert_type == AlertType.FILE_HASH_DETECTED:
            return "HIGH"
        elif self.alert_type in [AlertType.PORT_SCAN, AlertType.DNS_QUERY]:
            return "MEDIUM"
        else:
            return "LOW"
    # Classification indicator
    def classify_indicator(self):
        if self.indicator.startswith("10.") or self.indicator.startswith("192.168."):
            self.classification = "internal"
        elif "." in self.indicator:
            self.classification = "external"
        else:
            self.classification = "N/A"

        return self.classification
    
    #Challenge B
    def __str__(self):
        return f"{self.date} [{self.severity()}] {self.alert_type.value} on {self.asset} -> {self.indicator}"





with open("alerts.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

print(f"Loaded {len(lines)} alerts.")

# Convert lines → Alert objects
alerts = []
for line in lines:
    date, alert_type_str, asset, indicator = line.split(",")
    alert_type = AlertType(alert_type_str)  # string → enum

    alerts.append(Alert(date, alert_type, asset, indicator))


# Test
print(alerts[0].alert_type, alerts[0].severity())

# Severity counts
high = medium = low = 0

for a in alerts:
    sev = a.severity()
    if sev == "HIGH":
        high += 1
    elif sev == "MEDIUM":
        medium += 1
    else:
        low += 1

print("\n=== Summary ===")
print(f"HIGH: {high}")
print(f"MEDIUM: {medium}")
print(f"LOW: {low}")

print(AlertType.FILE_HASH_DETECTED)
# AlertType.FILE_HASH_DETECTED

print(AlertType.FILE_HASH_DETECTED.value)
# file_hash_detected
print(alerts[0].alert_type == AlertType.LOGIN_FAILURE)
# True or False

# Test Print:
for a in alerts:
    print(a)

# writes a report to incident_summary.txt
with open("incident_summary.txt", "w", encoding="utf-8") as out:
    out.write("Incident Triage Summary\n")
    out.write("======================\n")
    out.write(f"Total alerts: {len(alerts)}\n")
    out.write(f"HIGH: {high}\n")
    out.write(f"MEDIUM: {medium}\n")
    out.write(f"LOW: {low}\n")