import csv
import json
import sys
from chembl_webresource_client.new_client import new_client
from pathlib import Path

chembl_id_to_activity = {}

outputfile = Path("dat-cpdchemblid-to-activity.json")

if outputfile.exists():
    chembl_id_to_activity = json.load(open(outputfile))

#ids_to_skip = ["CHEMBL1454780", "CHEMBL1441", "CHEMBL1571851", "CHEMBL1616875", "CHEMBL1698267", "CHEMBL197",
#               "CHEMBL2112201", "CHEMBL240597", "CHEMBL3989715", "CHEMBL43452", "CHEMBL454950", "CHEMBL46102"]
ids_to_skip=[]
smiles_to_chemblids = json.load(open(Path("dat-plateid-to-chemblid.json")))

compound_chembl_ids = sorted(
    list(set([y[0] for x in smiles_to_chemblids.values() for y in x])))

activitycount = len([1 for x in chembl_id_to_activity for y in x])

for i, cpdid in enumerate(compound_chembl_ids):
    if cpdid in ids_to_skip:
        continue
    print(
        f"Doing {i}/{len(compound_chembl_ids)}, activitycount={activitycount}, {cpdid}")
    if cpdid in chembl_id_to_activity.keys():
        print("Found")
        continue
    if cpdid not in chembl_id_to_activity.keys():
        chembl_id_to_activity[cpdid] = []
    # we jump from compounds to targets through activities:
    activities = new_client.activity.filter(molecule_chembl_id=cpdid).only(
        ['target_chembl_id', 'standard_type', 'standard_value', 'standard_relation'])
    # extracting target ChEMBL IDs from activities:
    activitycount += len(activities)
    for act in activities:
        if act['standard_value'] is None:
            continue
        if act['standard_type'] in ["Inhibition", "IC50", "GI50", "Potency", "Ki", "Kd", "Ac50", "Activity", "MIC90", "MIC", "IC90", "EC50", ]:
            chembl_id_to_activity[cpdid].append(
                (act['target_chembl_id'], act['standard_type'], act['standard_value'], act['standard_relation']))
    json.dump(chembl_id_to_activity, open(outputfile, "w"))


print("Missing")
missing = [x for x in compound_chembl_ids if x not in chembl_id_to_activity.keys()]
for m in missing:
    print(missing)
