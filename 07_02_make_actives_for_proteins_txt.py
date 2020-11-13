import json
from pathlib import Path
print("Loading targets list")
targets_info = json.load(open(Path("dat-targetchemblid-to-targetinfo.json")))

print(targets_info)
exit()
hit_dict = {}

with open("dat-tsv-targetprefname-numtimeshitinChEMBL27.tsv", "w") as f:
    # Rather than just write out counts for each ChEMBL ID, we must merge
    # proteins sharing a common name - due to proteins having multiple ChEMBL
    # identifiers/entries
    for target_id in targets_hitcount.keys():
        if targets_info[target_id]['pref_name'] in hit_dict.keys():
            hit_dict[targets_info[target_id]['pref_name']
                     ] += targets_hitcount[target_id]
        else:
            hit_dict[targets_info[target_id]['pref_name']
                     ] = targets_hitcount[target_id]
    for prefname in hit_dict.keys():
        f.write(prefname+";"+str(hit_dict[prefname])+"\n")
