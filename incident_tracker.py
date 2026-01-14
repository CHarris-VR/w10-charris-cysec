# Step 6: enum
from enum import Enum


# Reading the files
with open("alerts.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

print(f"Loaded {len(lines)} alerts.")

# Parse each line into parts (Original)
# records = []
#for line in lines:
#    date, alert_type, asset, indicator = line.split(",")
#    records.append((date, alert_type, asset, indicator))

## Convert Strings into Enum Values
records = []
for line in lines:
    date, alert_type_str, asset, indicator = line.split(",")

    alert_type = AlertType(alert_type_str)
    records.append((date, alert_type, asset, indicator))

# Printing to see first tuple 
print(records[0])

# Step 7 Adding definition to the enum
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

def severity(self):
    if self.alert_type == AlertType.FILE_HASH_DETECTED:
        return "HIGH"
    elif self.alert_type in [AlertType.PORT_SCAN, AlertType.DNS_QUERY]:
        return "MEDIUM"
    else:
        return "LOW"

       
# adding step 4
alerts = []
for date, alert_type, asset, indicator in records:
    alerts.append(Alert(date, alert_type, asset, indicator))

print(alerts[0].alert_type, alerts[0].severity())

# replace "magic strings" with enum values
high = 0
medium = 0
low = 0

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



