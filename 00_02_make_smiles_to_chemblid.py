import pandas as pd
from chembl_webresource_client.new_client import new_client
import json
import sys
from pathlib import Path


outfile=Path("dat-plateid-to-chemblid.json")

smiles_to_chemblids={}
if outfile.exists():
    smiles_to_chemblids=json.load(open(outfile))

molecule = new_client.molecule
plateid_to_smiles=json.load(open("dat-plateid-to-smiles.json"))
num_plate_ids=len(plateid_to_smiles.keys())
n_processed=0
for k,v in plateid_to_smiles.items():
    n_processed+=1
    print(f"Doing, {k}, {n_processed-1}/{len(plateid_to_smiles)}")
    if k in smiles_to_chemblids:continue
    res = molecule.filter(molecule_structures__canonical_smiles__flexmatch=v).only(['pref_name','molecule_chembl_id'])
    info=set()
    for r in res:
        info.add((r['molecule_chembl_id'], r['pref_name']))
    smiles_to_chemblids[k]=list(info)
    json.dump(smiles_to_chemblids,open(outfile,"w"))

incomplete=[x for x in smiles_to_chemblids.keys() if len(smiles_to_chemblids[x])==0]
print("incomplete")
for i in incomplete:
    print(i, smiles_to_chemblids[i])