import pandas as pd
import sqlite3 as sq
query = "SELECT SUM(area_land),SUM(area_water) FROM facts WHERE area_land != '';"
conn = sq.connect("factbook.db")
df = pd.read_sql_query(query,conn)

rs = df["area_land"] / df["area_water"]

print(rs)