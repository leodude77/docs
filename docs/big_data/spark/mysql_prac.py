import mysql.connector
con = mysql.connector.connect(
  host="localhost",
  user="root",
  password="pass",
  database="scenarios"
)
cur = con.cursor()
def mysql_print():
  print()
  print (cur.column_names)
  for x in cur:
      print (x)
  print()
  
cur.execute("DROP TABLE IF EXISTS table1;")
cur.execute("CREATE TABLE table1 (id int);")
cur.execute("INSERT INTO table1 VALUES \
    (1),\
    (1),\
    (null),\
    (2),\
    (0);")

cur.execute("DROP TABLE IF EXISTS table2;")
cur.execute("CREATE TABLE table2 (id int);")
cur.execute("INSERT INTO table2 VALUES \
    (1),\
    (3),\
    (null);")

con.commit()

cur.execute("""
            select * from table2 a left join table1 b on a.id = b.id
            """)
mysql_print()
