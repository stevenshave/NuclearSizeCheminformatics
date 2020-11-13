import sqlite3
import json
from pathlib import Path
print("Loading targets list")
targets_list=json.load(open(Path("dat-targetchemblid-to-targetinfo.json"))).keys()

target_to_hitcount={}

conn = sqlite3.connect("chembl_27.db")
outputfile = Path("dat-targetchemblid-to-numactives.json")
for cid in targets_list:
    cursor = conn.execute('select count(distinct MOLREGNO) from ACTIVITIES where ASSAY_ID in (select ASSAY_ID from ASSAYS where TID=(select TID from TARGET_DICTIONARY where CHEMBL_ID=?)) and STANDARD_VALUE<=10000 and STANDARD_TYPE in ("Inhibition", "IC50", "GI50", "Potency", "Ki", "Kd", "Ac50", "Activity", "MIC90", "MIC", "IC90", "EC50") and STANDARD_RELATION in ("<","<=","=")',[cid])
    #for row in cursor:
    #    print(row[0])
    target_to_hitcount[cid]=cursor.fetchall()[0][0]
    if len(target_to_hitcount.keys())%10==0:
        json.dump(target_to_hitcount, open(outputfile, "w"))
        print(target_to_hitcount)
        print(len(target_to_hitcount.keys()), "/", len(targets_list))


