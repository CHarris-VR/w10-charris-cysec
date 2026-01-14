# Reading the files

with open("alerts.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

print(f"Loaded {len(lines)} alerts.")

# Parse each line into parts

records = []
for line in lines:
    date, alert_type, asset, indicator = line.split(",")
    records.append((date, alert_type, asset, indicator))

# Printing to see first tuple 
print(records[0])

# Create first Class checkpoint

class Alert:
    def __init__(self, date, alert_type, asset, indicator):
        self.date = date
        self.alert_type = alert_type
        self.asset = asset
        self.indicator = indicator

# Adding a severity string checkpoint

class Alert:
    def __init__(self, date, alert_type, asset, indicator):
        self.date = date
        self.alert_type = alert_type
        self.asset = asset
        self.indicator = indicator

    def severity(self):
        if self.alert_type == "file_hash_detected":
            return "HIGH"
        elif self.alert_type in ["port_scan", "dns_query"]:
            return "MEDIUM"
        else:
            return "LOW"
print (.severity())
