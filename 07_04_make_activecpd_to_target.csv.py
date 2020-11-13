import json
from pathlib import Path
print("Loading targets list")
dict_plateid_to_smiles = json.load(open(Path("dat-plateid-to-smiles.json")))
dict_plateid_to_hithumantargetnames = json.load(open(Path("dat-plateid-to-hithumantargetnames.json")))
dict_plateid_to_chemblid_and_name=json.load(open(Path("dat-plateid-to-chemblid.json")))
dict_plateid_to_smiles=json.load(open(Path("dat-plateid-to-smiles.json")))
dict_prefname_to_plateids = {}


with open("dat-hits-to-target.csv", "w") as f:
    for plateid in sorted(dict_plateid_to_hithumantargetnames.keys()):
        line=plateid+";"+str(len(set(dict_plateid_to_hithumantargetnames[plateid])))+";"
        line+=";".join(set(dict_plateid_to_hithumantargetnames[plateid]))
        f.write(line+"\n")