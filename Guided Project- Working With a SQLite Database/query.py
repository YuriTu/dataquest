import sqlite3
conn = sqlite3.connect("factbook.db")
query = "select name,population from facts order by population desc limit 10;"

rs = conn.execute(query).fetchall()
conn.close()
print(rs)