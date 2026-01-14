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
