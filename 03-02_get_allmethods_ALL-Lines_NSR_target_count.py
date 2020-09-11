"""
Generate NSR and NSW compounds for all methods across all cell lines

Generate a list of NSR, NSW, NSR but not NSW and NSW but not NSR targets
hitting all cell lines, and detected using all analysis methods - as given in 
Sup. tables 2,4,5, and 6.
HERE FOR COMPLETENESS - NO OUTPUT AS NOTHING MEETS THE CRITERIA.
"""

import json
from pathlib import Path
from nss_std_functions import get_cleaned_datasets

lookup_plateid_to_htargetname=json.load(open(Path("dat-plateid-to-hithumantargetnames.json")))

s2,s4,s5,s6 =get_cleaned_datasets()


# Boilerplate to obtain compounds
s2_NSR_compounds_PC3=set([c.replace("Plate","") for c in s2.query('Hit_PC3_6h == "-"  or Hit_PC3_36h =="-" ')['Compound'].values])
s4_NSR_compounds_PC3=set([c.replace("Plate","") for c in s4.query('Hit_PC3_6h == "-"  or Hit_PC3_36h =="-" ')['Compound'].values])
s5_NSR_compounds_PC3=set([c.replace("Plate","") for c in s5.query('Hit_PC3_6h == "-"  or Hit_PC3_36h =="-" ')['Compound'].values])
s6_NSR_compounds_PC3=set([c.replace("Plate","") for c in s6.query('Hit_PC3_6h == "-"  or Hit_PC3_36h =="-" ')['Compound'].values])
s2_NSW_compounds_PC3=set([c.replace("Plate","") for c in s2.query('Hit_PC3_6h == "+"  or Hit_PC3_36h =="+" ')['Compound'].values])
s4_NSW_compounds_PC3=set([c.replace("Plate","") for c in s4.query('Hit_PC3_6h == "+"  or Hit_PC3_36h =="+" ')['Compound'].values])
s5_NSW_compounds_PC3=set([c.replace("Plate","") for c in s5.query('Hit_PC3_6h == "+"  or Hit_PC3_36h =="+" ')['Compound'].values])
s6_NSW_compounds_PC3=set([c.replace("Plate","") for c in s6.query('Hit_PC3_6h == "+"  or Hit_PC3_36h =="+" ')['Compound'].values])

s2_NSR_compounds_HCT116=set([c.replace("Plate","") for c in s2.query('Hit_HCT116_6h == "-"  or Hit_HCT116_36h =="-" ')['Compound'].values])
s4_NSR_compounds_HCT116=set([c.replace("Plate","") for c in s4.query('Hit_HCT116_6h == "-"  or Hit_HCT116_36h =="-" ')['Compound'].values])
s5_NSR_compounds_HCT116=set([c.replace("Plate","") for c in s5.query('Hit_HCT116_6h == "-"  or Hit_HCT116_36h =="-" ')['Compound'].values])
s6_NSR_compounds_HCT116=set([c.replace("Plate","") for c in s6.query('Hit_HCT116_6h == "-"  or Hit_HCT116_36h =="-" ')['Compound'].values])
s2_NSW_compounds_HCT116=set([c.replace("Plate","") for c in s2.query('Hit_HCT116_6h == "+"  or Hit_HCT116_36h =="+" ')['Compound'].values])
s4_NSW_compounds_HCT116=set([c.replace("Plate","") for c in s4.query('Hit_HCT116_6h == "+"  or Hit_HCT116_36h =="+" ')['Compound'].values])
s5_NSW_compounds_HCT116=set([c.replace("Plate","") for c in s5.query('Hit_HCT116_6h == "+"  or Hit_HCT116_36h =="+" ')['Compound'].values])
s6_NSW_compounds_HCT116=set([c.replace("Plate","") for c in s6.query('Hit_HCT116_6h == "+"  or Hit_HCT116_36h =="+" ')['Compound'].values])

s2_NSR_compounds_H1299=set([c.replace("Plate","") for c in s2.query('Hit_H1299_6h == "+"  or Hit_H1299_36h =="+" ')['Compound'].values])
s4_NSR_compounds_H1299=set([c.replace("Plate","") for c in s4.query('Hit_H1299_6h == "+"  or Hit_H1299_36h =="+" ')['Compound'].values])
s5_NSR_compounds_H1299=set([c.replace("Plate","") for c in s5.query('Hit_H1299_6h == "+"  or Hit_H1299_36h =="+" ')['Compound'].values])
s6_NSR_compounds_H1299=set([c.replace("Plate","") for c in s6.query('Hit_H1299_6h == "+"  or Hit_H1299_36h =="+" ')['Compound'].values])
s2_NSW_compounds_H1299=set([c.replace("Plate","") for c in s2.query('Hit_H1299_6h == "-"  or Hit_H1299_36h =="-" ')['Compound'].values])
s4_NSW_compounds_H1299=set([c.replace("Plate","") for c in s4.query('Hit_H1299_6h == "-"  or Hit_H1299_36h =="-" ')['Compound'].values])
s5_NSW_compounds_H1299=set([c.replace("Plate","") for c in s5.query('Hit_H1299_6h == "-"  or Hit_H1299_36h =="-" ')['Compound'].values])
s6_NSW_compounds_H1299=set([c.replace("Plate","") for c in s6.query('Hit_H1299_6h == "-"  or Hit_H1299_36h =="-" ')['Compound'].values])



NSR_cpds=set(s2_NSR_compounds_PC3).intersection(
    s4_NSR_compounds_PC3,s5_NSR_compounds_PC3,s6_NSR_compounds_PC3,
    s2_NSR_compounds_HCT116,s4_NSR_compounds_HCT116,s5_NSR_compounds_HCT116,s6_NSR_compounds_HCT116, 
    s2_NSR_compounds_H1299,s4_NSR_compounds_H1299,s5_NSR_compounds_H1299,s6_NSR_compounds_H1299 
    )
NSW_cpds=set(s2_NSW_compounds_PC3).intersection(
    s4_NSW_compounds_PC3,s5_NSW_compounds_PC3,s6_NSW_compounds_PC3,
    s2_NSW_compounds_HCT116,s4_NSW_compounds_HCT116,s5_NSW_compounds_HCT116,s6_NSW_compounds_HCT116, 
    s2_NSW_compounds_H1299,s4_NSW_compounds_H1299,s5_NSW_compounds_H1299,s6_NSW_compounds_H1299 
    )



NSR_targets_list=[]
NSW_targets_list=[]
[NSR_targets_list.extend(lookup_plateid_to_htargetname[pid]) for pid in NSR_cpds if pid in lookup_plateid_to_htargetname.keys()]
[NSW_targets_list.extend(lookup_plateid_to_htargetname[pid]) for pid in NSW_cpds if pid in lookup_plateid_to_htargetname.keys()]



counts_of_NSR_targets=sorted([(NSR_targets_list.count(prot),prot) for prot in set(NSR_targets_list)], reverse=True)
counts_of_NSW_targets=sorted([(NSW_targets_list.count(prot),prot) for prot in set(NSW_targets_list)], reverse=True)


print("NSR")
for item in counts_of_NSR_targets:
    print(f"{item[0]}\t{item[1]}")

# Perofrm the output
print("NSW")
for item in counts_of_NSW_targets:
    print(f"{item[0]}\t{item[1]}")

print("NSR but not in NSW")
for item in counts_of_NSR_targets:
    if item[1] not in set(NSW_targets_list):
        print(f"{item[0]}\t{item[1]}")

print("NSW but not in NSR")
for item in counts_of_NSW_targets:
    if item[1] not in set(NSW_targets_list):
        print(f"{item[0]}\t{item[1]}")



