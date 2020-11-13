"""
Make the semicolon separated datafile for import into excel mapping protein to hits.

"""

import json
from pathlib import Path
print("Loading targets list")
dict_plateid_to_smiles = json.load(open(Path("dat-plateid-to-smiles.json")))
dict_plateid_to_hithumantargetnames = json.load(open(Path("dat-plateid-to-hithumantargetnames.json")))
dict_plateid_to_chemblid_and_name=json.load(open(Path("dat-plateid-to-chemblid.json")))
dict_plateid_to_smiles=json.load(open(Path("dat-plateid-to-smiles.json")))
dict_prefname_to_plateids = {}

for plateid,prefname_list in dict_plateid_to_hithumantargetnames.items():
    for prefname in prefname_list:
        if prefname not in dict_prefname_to_plateids:
            dict_prefname_to_plateids[prefname]=set()
        dict_prefname_to_plateids[prefname].add(plateid)

with open("dat-targetprefname-to-hits.csv", "w") as f:
    for prefname in sorted(dict_prefname_to_plateids.keys()):
        counter=0
        line=""
        for plateid in dict_prefname_to_plateids[prefname]:
            for cpdinfo in dict_plateid_to_chemblid_and_name[plateid]:
                name=cpdinfo[1]
                if name==None:
                    name=""
                else:
                    name="("+name+")"
                line+=plateid+","+cpdinfo[0]+name+","+dict_plateid_to_smiles[plateid]+";"
                counter+=1
        f.write(prefname+";"+str(counter)+";"+line+"\n")