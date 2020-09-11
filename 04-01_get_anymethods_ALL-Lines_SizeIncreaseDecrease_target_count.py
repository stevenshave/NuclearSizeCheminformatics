"""
Generate INC target hit-count table

Generate a list of commonly hit (in all 4 analysis methods) targets which
produce a nuclear size worsening effect.
"""

import json
from pathlib import Path
from nss_std_functions import get_cleaned_datasets

lookup_plateid_to_htargetname=json.load(open(Path("dat-plateid-to-hithumantargetnames.json")))

s2,s4,s5,s6 =get_cleaned_datasets()


# Boilerplate to obtain compounds
s2_DEC_compounds_PC3=set([c.replace("Plate","") for c in s2.query('Hit_PC3_6h == "-"  or Hit_PC3_36h =="-" ')['Compound'].values])
s4_DEC_compounds_PC3=set([c.replace("Plate","") for c in s4.query('Hit_PC3_6h == "-"  or Hit_PC3_36h =="-" ')['Compound'].values])
s5_DEC_compounds_PC3=set([c.replace("Plate","") for c in s5.query('Hit_PC3_6h == "-"  or Hit_PC3_36h =="-" ')['Compound'].values])
s6_DEC_compounds_PC3=set([c.replace("Plate","") for c in s6.query('Hit_PC3_6h == "-"  or Hit_PC3_36h =="-" ')['Compound'].values])
s2_INC_compounds_PC3=set([c.replace("Plate","") for c in s2.query('Hit_PC3_6h == "+"  or Hit_PC3_36h =="+" ')['Compound'].values])
s4_INC_compounds_PC3=set([c.replace("Plate","") for c in s4.query('Hit_PC3_6h == "+"  or Hit_PC3_36h =="+" ')['Compound'].values])
s5_INC_compounds_PC3=set([c.replace("Plate","") for c in s5.query('Hit_PC3_6h == "+"  or Hit_PC3_36h =="+" ')['Compound'].values])
s6_INC_compounds_PC3=set([c.replace("Plate","") for c in s6.query('Hit_PC3_6h == "+"  or Hit_PC3_36h =="+" ')['Compound'].values])

s2_DEC_compounds_HCT116=set([c.replace("Plate","") for c in s2.query('Hit_HCT116_6h == "-"  or Hit_HCT116_36h =="-" ')['Compound'].values])
s4_DEC_compounds_HCT116=set([c.replace("Plate","") for c in s4.query('Hit_HCT116_6h == "-"  or Hit_HCT116_36h =="-" ')['Compound'].values])
s5_DEC_compounds_HCT116=set([c.replace("Plate","") for c in s5.query('Hit_HCT116_6h == "-"  or Hit_HCT116_36h =="-" ')['Compound'].values])
s6_DEC_compounds_HCT116=set([c.replace("Plate","") for c in s6.query('Hit_HCT116_6h == "-"  or Hit_HCT116_36h =="-" ')['Compound'].values])
s2_INC_compounds_HCT116=set([c.replace("Plate","") for c in s2.query('Hit_HCT116_6h == "+"  or Hit_HCT116_36h =="+" ')['Compound'].values])
s4_INC_compounds_HCT116=set([c.replace("Plate","") for c in s4.query('Hit_HCT116_6h == "+"  or Hit_HCT116_36h =="+" ')['Compound'].values])
s5_INC_compounds_HCT116=set([c.replace("Plate","") for c in s5.query('Hit_HCT116_6h == "+"  or Hit_HCT116_36h =="+" ')['Compound'].values])
s6_INC_compounds_HCT116=set([c.replace("Plate","") for c in s6.query('Hit_HCT116_6h == "+"  or Hit_HCT116_36h =="+" ')['Compound'].values])

s2_DEC_compounds_H1299=set([c.replace("Plate","") for c in s2.query('Hit_H1299_6h == "-"  or Hit_H1299_36h =="-" ')['Compound'].values])
s4_DEC_compounds_H1299=set([c.replace("Plate","") for c in s4.query('Hit_H1299_6h == "-"  or Hit_H1299_36h =="-" ')['Compound'].values])
s5_DEC_compounds_H1299=set([c.replace("Plate","") for c in s5.query('Hit_H1299_6h == "-"  or Hit_H1299_36h =="-" ')['Compound'].values])
s6_DEC_compounds_H1299=set([c.replace("Plate","") for c in s6.query('Hit_H1299_6h == "-"  or Hit_H1299_36h =="-" ')['Compound'].values])
s2_INC_compounds_H1299=set([c.replace("Plate","") for c in s2.query('Hit_H1299_6h == "+"  or Hit_H1299_36h =="+" ')['Compound'].values])
s4_INC_compounds_H1299=set([c.replace("Plate","") for c in s4.query('Hit_H1299_6h == "+"  or Hit_H1299_36h =="+" ')['Compound'].values])
s5_INC_compounds_H1299=set([c.replace("Plate","") for c in s5.query('Hit_H1299_6h == "+"  or Hit_H1299_36h =="+" ')['Compound'].values])
s6_INC_compounds_H1299=set([c.replace("Plate","") for c in s6.query('Hit_H1299_6h == "+"  or Hit_H1299_36h =="+" ')['Compound'].values])



DEC_cpds=set(s2_DEC_compounds_PC3|s4_DEC_compounds_PC3|s5_DEC_compounds_PC3|s6_DEC_compounds_PC3).intersection(
    s2_DEC_compounds_HCT116|s4_DEC_compounds_HCT116|s5_DEC_compounds_HCT116|s6_DEC_compounds_HCT116, 
    s2_DEC_compounds_H1299|s4_DEC_compounds_H1299|s5_DEC_compounds_H1299|s6_DEC_compounds_H1299 
    )
INC_cpds=set(s2_INC_compounds_PC3|s4_INC_compounds_PC3|s5_INC_compounds_PC3|s6_INC_compounds_PC3).intersection(
    s2_INC_compounds_HCT116|s4_INC_compounds_HCT116|s5_INC_compounds_HCT116|s6_INC_compounds_HCT116, 
    s2_INC_compounds_H1299|s4_INC_compounds_H1299|s5_INC_compounds_H1299|s6_INC_compounds_H1299 
    )

DEC_targets_list=[]
INC_targets_list=[]
[DEC_targets_list.extend(lookup_plateid_to_htargetname[pid]) for pid in DEC_cpds if pid in lookup_plateid_to_htargetname.keys()]
[INC_targets_list.extend(lookup_plateid_to_htargetname[pid]) for pid in INC_cpds if pid in lookup_plateid_to_htargetname.keys()]



counts_of_DEC_targets=sorted([(DEC_targets_list.count(prot),prot) for prot in set(DEC_targets_list)], reverse=True)
counts_of_INC_targets=sorted([(INC_targets_list.count(prot),prot) for prot in set(INC_targets_list)], reverse=True)


print("DEC")
for item in counts_of_DEC_targets:
    print(f"{item[0]}\t{item[1]}")

# Perofrm the output
print("INC")
for item in counts_of_INC_targets:
    print(f"{item[0]}\t{item[1]}")

print("DEC but not in INC")
for item in counts_of_DEC_targets:
    if item[1] not in set(INC_targets_list):
        print(f"{item[0]}\t{item[1]}")

print("INC but not in DEC")
for item in counts_of_INC_targets:
    if item[1] not in set(INC_targets_list):
        print(f"{item[0]}\t{item[1]}")



