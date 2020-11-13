"""
Determine how many compounds in ChEMBL27 meet our activity cutoff

Using SQLite, not the web service, as it would be too slow, we determine the
number of unique compounds involved in recorded activities that meet our
cutoff criteria.
"""


import sqlite3
from sqlite3 import Error

def create_connection():
    """ create a database connection to a database that resides in the memory"""
    conn = None
    try:
        conn = sqlite3.connect('chembl_27.db')
        cur = conn.cursor()
        cur.execute('select count(distinct MOLREGNO) from ACTIVITIES where STANDARD_VALUE<=10000 and STANDARD_TYPE in ("Inhibition", "IC50", "GI50", "Potency", "Ki", "Kd", "Ac50", "Activity", "MIC90", "MIC", "IC90", "EC50") and STANDARD_RELATION in ("<","<=","=")')

        rows = cur.fetchall()

        for row in rows:
            print(row)
    except Error as e:
            print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection()
