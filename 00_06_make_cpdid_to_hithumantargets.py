import json
import sys
from pathlib import Path


outputfile_cids = Path("dat-plateid-to-hithumantargets.json")
outputfile_target_names = Path("dat-plateid-to-hithumantargetnames.json")

lookup_plateid_to_hithumantargets={}

# Load plateids
lookup_plateid_to_chemblcid = json.load(open(Path("dat-plateid-to-chemblid.json")))
plateids=sorted(list(lookup_plateid_to_chemblcid.keys()))

lookup_chemblcid_to_activity = json.load(open(Path("dat-cpdchemblid-to-activity.json")))
lookup_targetid_to_targetinfo = json.load(open(Path("dat-targetchemblid-to-targetinfo.json")))
lookup_tid_to_tinfo=json.load(open(Path("dat-targetchemblid-to-targetinfo.json")))

for plateid in plateids:
    chemblcids=[x[0] for x in lookup_plateid_to_chemblcid[plateid]]
    #print(plateid, chemblcids)
    for chemblcid in chemblcids:
        if not chemblcid in lookup_chemblcid_to_activity.keys():continue
        activities=lookup_chemblcid_to_activity[chemblcid]
        for a in activities:
            if not a[0] in lookup_tid_to_tinfo.keys():continue
            #if not lookup_tid_to_tinfo[a[0]]=="SINGLE PROTEIN":continue
            if a[1] not in ["EC50","GI50","IC50","Kd","MIC","MIC90","Potency"]:continue
            if a[3] not in ["<=","<","="]:continue
            if float(a[2]) > 10000: continue
            if plateid not in lookup_plateid_to_hithumantargets.keys():
                lookup_plateid_to_hithumantargets[plateid]=set()
            lookup_plateid_to_hithumantargets[plateid].add(a[0])

writeable_lookup_plateid_to_hithumantargets={k:list(v) for k,v in lookup_plateid_to_hithumantargets.items()}
json.dump(writeable_lookup_plateid_to_hithumantargets, open(outputfile_cids, "w"))
print(f"{len(writeable_lookup_plateid_to_hithumantargets.keys())=}")

writeable_lookup_plateid_to_hithumantargetnames={}
for plateid,tids in writeable_lookup_plateid_to_hithumantargets.items():
    writeable_lookup_plateid_to_hithumantargetnames[plateid]=[]
    for tid in tids:
        writeable_lookup_plateid_to_hithumantargetnames[plateid].append(lookup_tid_to_tinfo[tid]['pref_name'])
json.dump(writeable_lookup_plateid_to_hithumantargetnames, open(outputfile_target_names, "w"))
