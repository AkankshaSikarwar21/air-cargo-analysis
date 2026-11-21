import glob
import os
import sqlite3
import pandas as pd

con = sqlite3.connect("air.db")
for f in glob.glob("data/sample/*.csv"):
    pd.read_csv(f).to_sql(os.path.splitext(os.path.basename(f))[0], con, if_exists="replace", index=False)

for q in open("sql/analysis.sql", encoding="utf-8").read().split(";"):
    if q.strip():
        print(pd.read_sql(q, con).to_string(index=False))
        print("-" * 40)