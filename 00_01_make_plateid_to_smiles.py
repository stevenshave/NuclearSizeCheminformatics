import pandas as pd
import json
import sys
from pathlib import Path
from nss_std_functions import *

plateid_to_smiles={}

prestwick_info=pd.read_excel("../Prestwick Chemical Library_Ver19.xlsx")


for sheet in get_cleaned_datasets():
    sheet=sheet.iloc[:,0:2]
    for id, (plate, chemical_name) in sheet.iterrows():
        plateid_to_smiles[plate.replace('Plate','')]=prestwick_info.query(f"PositionNumber=='{plate.replace('Plate','')}'")['Smiles code'].values[0]


json.dump(plateid_to_smiles, open("dat-plateid-to-smiles.json", "w"))
print(len(plateid_to_smiles.keys()))
