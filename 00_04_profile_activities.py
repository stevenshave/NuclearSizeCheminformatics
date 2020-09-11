import json
from pathlib import Path
cpdid_to_activity=json.load(open("dat-cpdchemblid-to-activity.json"))
target_ids=list(set([acitivity[0] for activities in cpdid_to_activity.values() for acitivity in activities]))
acitity_records=list(set([(acitivity[1],acitivity[3]) for activities in cpdid_to_activity.values() for acitivity in activities]))

for i,a in enumerate(acitity_records):
    
    if a[1] == None:
        acitity_records[i]=(acitity_records[i][0],"None")



acitity_records.sort(key=lambda x: x[0])
print(f"{acitity_records=}")

#print(target_ids)
print(f"{len(target_ids)=}")

for i in acitity_records:
    print(i)

print(acitity_records)