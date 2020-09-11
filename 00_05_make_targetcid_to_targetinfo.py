import csv
import json
import sys
from chembl_webresource_client.new_client import new_client
from pathlib import Path

tcid_to_tinfo = {}

outputfile = Path("dat-targetchemblid-to-targetinfo.json")

if outputfile.exists():
    tcid_to_tinfo = json.load(open(outputfile))

cpd_to_activity = json.load(open(Path("dat-cpdchemblid-to-activity.json")))

target_chembl_ids = sorted(
    list(set([y[0] for x in cpd_to_activity.values() for y in x])))

targetcount = len(target_chembl_ids)

for i, tid in enumerate(target_chembl_ids):
    print(
        f"Doing {i}/{targetcount}, {tid}")
    if tid in tcid_to_tinfo.keys():
        print("Found")
        continue
    
    # we jump from compounds to targets through activities:
    targetqinfo = new_client.target.search(tid).only(
        ['target_type', 'pref_name', 'organism'])
    # extracting target ChEMBL IDs from activities:
    for t in targetqinfo:
        if t['organism']!='Homo sapiens':continue
        if t['target_type']!="SINGLE PROTEIN": continue
        tcid_to_tinfo[tid]=t
        json.dump(tcid_to_tinfo, open(outputfile, "w"))

        