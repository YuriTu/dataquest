import pandas as pd
import sqlite3 as sq
query = "SELECT * FROM facts;"
conn = sq.connect("factbook.db")
df = pd.read_sql_query(query,conn)
null = pd.isnull(df)
df = df.dropna()
df = df[df["area_land"] != 0 ]

def pg(row):
    n = row['population']*(math.e**((row['population_growth']/100)*35))
    return round(n,0)

df["2050_pop"] = df.apply(pg, axis=1)
    
    



