# Nuclear size study standard functions

import pandas as pd
import numpy as np



def get_cleaned_datasets():
    def replace_bad_values(df):
        df.replace("  ", np.nan, inplace=True)
        df.replace(" ", np.nan, inplace=True)
        df.replace("- ", "-", inplace=True)
        df.replace("-  ","-", inplace=True)
        df.replace("+/- ","+/-", inplace=True)
        df.replace(r'\n',' ', regex=True, inplace=True)
    
    s2=pd.read_excel("2020-08-17_NucSupportingTablesS2456_SS1.xlsx", "s2")
    s2.columns = [c.replace(' ', '_') for c in s2.columns]
    replace_bad_values(s2)

    s4=pd.read_excel("2020-08-17_NucSupportingTablesS2456_SS1.xlsx", "s4")
    s4.columns = [c.replace(' ', '_') for c in s4.columns]
    replace_bad_values(s4)

    s5=pd.read_excel("2020-08-17_NucSupportingTablesS2456_SS1.xlsx", "s5")
    s5.columns = [c.replace(' ', '_') for c in s5.columns]
    replace_bad_values(s5)

    s6=pd.read_excel("2020-08-17_NucSupportingTablesS2456_SS1.xlsx", "s6")
    s6.columns = [c.replace(' ', '_') for c in s6.columns]
    replace_bad_values(s6)

    return s2,s4,s5,s6