import os
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql import Window
from pyspark.sql.functions import *
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DateType, DoubleType, FloatType, \
    TimestampType
import sys

# For using SQLite
# import sqlite3
# con = sqlite3.connect("scenarios.db")
# cur = con.cursor()
# def print_sqlite_table(query):
#     for x in cur.execute(query).fetchall():
#         print(x)
        
# Using Mysql
import mysql.connector
con = mysql.connector.connect(
  host="localhost",
  user="root",
  password="pass",
  database="scenarios"
)
cur = con.cursor()
def mysql_print():
  print (cur.column_names)
  for x in cur:
      print (x)

python_path = sys.executable
os.environ['PYSPARK_PYTHON'] = python_path
os.environ['HADOOP_HOME'] = r'C:\Code\docs\docs\big_data\spark\hadoop'
os.environ['JAVA_HOME'] = r'C:\Program Files\Java\jdk1.8.0_202'

# os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages com.datastax.spark:spark-cassandra-connector_2.12:3.5.1 pyspark-shell'
# os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-avro_2.12:3.5.4 pyspark-shell'
# os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.4 pyspark-shell'


conf = SparkConf().setAppName("pyspark").setMaster("local[*]").set("spark.driver.host", "localhost").set(
    "spark.default.parallelism", "1")
sc = SparkContext(conf=conf)

spark = SparkSession.builder.getOrCreate()








# =======================================================================================================================
# Scenario Template
# =======================================================================================================================

# +----------+----------+                                       
# | sell_date|   product|            ==>>            +----------+--------------------+---------+
# +----------+----------+                            | sell_date|            products|null_sell|

# MYSQL ---------------------------------------------------------------------------------------------------------------------------

# cur.execute("DROP TABLE IF EXISTS df_36;")
# cur.execute("CREATE TABLE df_36 (sell_date string, product string);")
# cur.execute("INSERT INTO df_36 VALUES \
#     ('2020-05-30', 'Headphone'), \
#     ('2020-05-30', 'T-Shirt');")

# con.commit()

# print_sqlite_table("\
# ")

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
# 
# )
# schema = ""

# df = spark.createDataFrame(data=data, schema=schema)
# df.createOrReplaceTempView("df")







# =======================================================================================================================
# Scenario 36
# =======================================================================================================================

# +----------+----------+                                       
# | sell_date|   product|            ==>>            +----------+--------------------+---------+
# +----------+----------+                            | sell_date|            products|null_sell|           
# |2020-05-30| Headphone|                            +----------+--------------------+---------+           
# |2020-06-01|    Pencil|                            |2020-05-30|[T-Shirt, Basketb...|        3|           
# |2020-06-02|      Mask|                            |2020-06-01|      [Pencil, Book]|        2|           
# |2020-05-30|Basketball|                            |2020-06-02|              [Mask]|        1|           
# |2020-06-01|      Book|                            +----------+--------------------+---------+
# |2020-06-02|      Mask|
# |2020-05-30|   T-Shirt|
# +----------+----------+

# SQLITE =======================================================================================================================

# cur.execute("DROP TABLE IF EXISTS df_36;")
# cur.execute("CREATE TABLE df_36 (sell_date string, product string);")
# cur.execute("INSERT INTO df_36 VALUES \
#     ('2020-05-30', 'Headphone'), \
#     ('2020-05-30', 'Headphone'), \
#     ('2020-06-01', 'Pencil'), \
#     ('2020-06-02', 'Mask'), \
#     ('2020-05-30', 'Basketball'), \
#     ('2020-06-01', 'Book'), \
#     ('2020-06-02', 'Mask'), \
#     ('2020-05-30', 'T-Shirt');")
# con.commit()

# print_sqlite_table("\
#     select sell_date, GROUP_CONCAT(product) as products, count(1) as 'SOLD_PRODUCT_COUNT'\
#     from df_36 group by sell_date;\
# ")

# SPARK=======================================================================================================================

# data = (
#     ("2020-05-30", "Headphone"),
#     ("2020-05-30", "Headphone"),
#     ("2020-06-01", "Pencil"),
#     ("2020-06-02", "Mask"),
#     ("2020-05-30", "Basketball"),
#     ("2020-06-01", "Book"),
#     ("2020-06-02", "Mask"),
#     ("2020-05-30", "T-Shirt"),
# )
# schema = "sell_date string, product string"

# df = spark.createDataFrame(data=data, schema=schema)
# df.createOrReplaceTempView("df")

# (
#     df
#     .groupBy("sell_date")
#     .agg(collect_list("product").alias("products"), size(col("products")).alias("null_sell"))
#     .show()
# )
# spark.sql("""
#             select sell_date, GROUP_CONCAT(product) as products
#             from df
#             group by sell_date
#           """).show(truncate=False)

# =======================================================================================================================
# Scenario 34
# =======================================================================================================================

# +-----------+------+---+------+
# |customer_id|  name|age|gender|     =>>     +---------+-----+
# +-----------+------+---+------+             |age_group|count|
# |          1| Alice| 25|     F|             +---------+-----+
# |          2|   Bob| 40|     M|             |    19-35|    3|
# |          3|   Raj| 46|     M|             |    36-50|    3|
# |          4| Sekar| 66|     M|             |      51+|    2|
# |          5|  Jhon| 47|     M|             +---------+-----+
# |          6|Timoty| 28|     M|
# |          7|  Brad| 90|     M|
# |          8|  Rita| 34|     F|
# +-----------+------+---+------+

# SQLITE ---------------------------------------------------------------------------------------------------------------------------

# cur.execute("DROP TABLE IF EXISTS df_34;")
# cur.execute("CREATE TABLE df_34 (customer_id integer, name string, age integer, gender string);")
# cur.execute("INSERT INTO df_34 VALUES \
#     (1, 'Alice', 25, 'F'), \
#     (2, 'Bob', 40, 'M'), \
#     (3, 'Raj', 46, 'M'), \
#     (4, 'Sekar', 66, 'M'), \
#     (5, 'Jhon', 47, 'M'), \
#     (6, 'Timoty', 28, 'M'), \
#     (7, 'Brad', 90, 'M'), \
#     (8, 'Rita', 34, 'F');")

# con.commit()

# print_sqlite_table(""" 
#                     select age_group, count(1) from 
#                         ( select case
#                             when age between 18 and 35 then '19-35'
#                             when age between 36 and 50 then '36-50'
#                             when age > 50 then '51+' end as age_group from df_34
#                         )
#                         group by age_group;
#                     """)

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#     (1, "Alice", 25, "F"),
#     (2, "Bob", 40, "M"),
#     (3, "Raj", 46, "M"),
#     (4, "Sekar", 66, "M"),
#     (5, "Jhon", 47, "M"),
#     (6, "Timoty", 28, "M"),
#     (7, "Brad", 90, "M"),
#     (8, "Rita", 34, "F"),
# )
# schema = "customer_id integer, name string, age integer, gender string"

# df = spark.createDataFrame(data=data, schema=schema)
# df.createOrReplaceTempView("df")

# df.withColumn("age_group", expr("case when age between 19 and 35 then '19-35' when age between 36 and 50 then '36-50' when (age > 50) then '51+' end"))\
#     .groupBy("age_group").agg(count(lit('1')).alias("Count")).show()

# =======================================================================================================================
# Scenario 33
# =======================================================================================================================

# +--------------------+--------------+-----------+                   +--------------------+------------+--------+--------+
# |                  id|          name|family_size|                   |                  id|        name|min_size|max_size|
# +--------------------+--------------+-----------+                   +--------------------+------------+--------+--------+
# |c00dac11bde74750b111|   Alex Thomas|          9|                   |023fd23615bd4ff4b111|     Bolivia|       2|       4|
# |eb6f2d3426694667a111|    Chris Gray|          2|                   |be247f73de0f4b2d8111|Cook Islands|       4|       8|
# |3f7b5b8e835d4e1c8111| Emily Johnson|          4|                   |3e85ab80a6f84ef3b111|      Brazil|       4|       7|
# |9a345b079d9f4d3ca111| Michael Brown|          6|                   |e571e164152c4f7c8111|   Australia|       5|       9|
# |e0a5f57516024de2a111|Jessica Wilson|          3|                   |f35a7bb7d44342f7a111|      Canada|       3|       5|
# +--------------------+--------------+-----------+                   |a1b5a4b5fc5f46f89111|       Japan|      10|      12|
#                                                                     +--------------------+------------+--------+--------+


#      =>>     +-------------+-------------------+
#              |         name|number_of_countries|
#              +-------------+-------------------+
#              |Emily Johnson|                  4|
#              +-------------+-------------------+

# SQLITE ---------------------------------------------------------------------------------------------------------------------------

# cur.execute("DROP TABLE IF EXISTS df_33;")
# cur.execute("CREATE TABLE df_33 (id string, name string, family_size integer);")
# cur.execute("INSERT INTO df_33 VALUES \
#     ('c00dac11bde74750b111', 'Alex Thomas', 9), \
#     ('eb6f2d3426694667a111', 'Chris Gray', 2), \
#     ('3f7b5b8e835d4e1c8111', 'Emily Johnson', 4), \
#     ('9a345b079d9f4d3ca111', 'Michael Brown', 6), \
#     ('e0a5f57516024de2a111', 'Jessica Wilson', 35);")

# cur.execute("DROP TABLE IF EXISTS df_33_1;")
# cur.execute("CREATE TABLE df_33_1 (id string, name string, min_size integer, max_size integer);")
# cur.execute("INSERT INTO df_33_1 VALUES \
#     ('023fd23615bd4ff4b111', 'Bolivia', 2, 4), \
#     ('be247f73de0f4b2d8111', 'Cook Islands', 4, 8), \
#     ('3e85ab80a6f84ef3b111', 'Brazil', 4, 7), \
#     ('e571e164152c4f7c8111', 'Australia', 5, 9), \
#     ('f35a7bb7d44342f7a111', 'Canada', 3, 5), \
#     ('a1b5a4b5fc5f46f89111', 'Japan', 10, 12);")

# con.commit()

# print_sqlite_table("\
#                    select name, count(1) as count from \
#                    ( select *, case when family_size between min_size and max_size then 1 else 0 end as eligibility from df_33 cross join df_33_1 where eligibility == 1 ) \
#                    group by name \
#                     order by count desc limit 1; \
#                    ")

# print_sqlite_table(""" 
#                     select one.name, count(1) as count
#                     from df_33 as one inner join df_33_1 as two on one.family_size between two.min_size and two.max_size
#                     group by one.name
#                     order by count desc
#                     limit 1;
#                    """)

# print_sqlite_table("""
#                    select name, number_of_countries from
#                    (
#                         select name, count as number_of_countries , RANK() over (order by count desc) as rank from 
#                         (
#                             select one.name, count(1) as count
#                             from df_33 as one inner join df_33_1 as two on one.family_size between two.min_size and two.max_size
#                             group by one.name
#                         )
#                     )
#                     where rank == 1;
#                    """)

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#     ("c00dac11bde74750b111", "Alex Thomas", 9),
#     ("eb6f2d3426694667a111", "Chris Gray", 2),
#     ("3f7b5b8e835d4e1c8111", "Emily Johnson", 4),
#     ("9a345b079d9f4d3ca111", "Michael Brown", 6),
#     ("e0a5f57516024de2a111", "Jessica Wilson", 35)
# )
# schema = "id string, name string, family_size integer"

# df1 = spark.createDataFrame(data=data, schema=schema)
# df1.createOrReplaceTempView("df1")

# data = (
#     ("023fd23615bd4ff4b111", "Bolivia", 2, 4),
#     ("be247f73de0f4b2d8111", "Cook Islands", 4, 8),
#     ("3e85ab80a6f84ef3b111", "Brazil", 4, 7),
#     ("e571e164152c4f7c8111", "Australia", 5, 9),
#     ("f35a7bb7d44342f7a111", "Canada", 3, 5),
#     ("a1b5a4b5fc5f46f89111", "Japan", 10, 12)
# )
# schema = "id string, name string, min_size integer, max_size integer"

# df2 = spark.createDataFrame(data=data, schema=schema)
# df2.createOrReplaceTempView("df2")

# window = Window.orderBy(col("number_of_countries").desc())

# df1.join(df2, df1.family_size.between(df2.min_size, df2.max_size)).groupBy(df1.name).agg(count(lit(1)).alias("number_of_countries"))\
#     .withColumn("rank", dense_rank().over(window)).filter("rank = 1").drop("rank")\
#     .show()

# spark.sql("""
#           select name,count from (
#             select name, count, DENSE_RANK() over (order by count desc) as rank from
#                 ( select df1.name, count(1) as count from df1 inner join df2 on df1.family_size between df2.min_size and df2.max_size group by df1.name )
#             ) where rank = 1;
#           """).show()


# =======================================================================================================================
# Scenario 32
# =======================================================================================================================

# +-------+-------------------+                         +-------+------+
# |food_id|          food_item|                         |food_id|rating|
# +-------+-------------------+                         +-------+------+
# |      1|        Veg Biryani|                         |      1|     5|
# |      2|     Veg Fried Rice|                         |      2|     3|
# |      3|    Kaju Fried Rice|                         |      3|     4|
# |      4|    Chicken Biryani|                         |      4|     4|
# |      5|Chicken Dum Biryani|                         |      5|     5|
# |      6|     Prawns Biryani|                         |      6|     4|
# |      7|      Fish Birayani|                         |      7|     4|
# +-------+-------------------+                         +-------+------+

#      =>>     +-------+-------------------+------+---------------+
#              |food_id|          food_item|rating|stats(out of 5)|
#              +-------+-------------------+------+---------------+
#              |      1|        Veg Biryani|     5|          *****|
#              |      2|     Veg Fried Rice|     3|            ***|
#              |      3|    Kaju Fried Rice|     4|           ****|
#              |      4|    Chicken Biryani|     4|           ****|
#              |      5|Chicken Dum Biryani|     5|          *****|
#              |      6|     Prawns Biryani|     4|           ****|
#              |      7|      Fish Birayani|     4|           ****|
#              +-------+-------------------+------+---------------+

# MYSQL ---------------------------------------------------------------------------------------------------------------------------

# cur.execute("DROP TABLE IF EXISTS df_32;")
# cur.execute("CREATE TABLE df_32 (food_id int, food_item varchar(100))")
# cur.execute("INSERT INTO df_32 VALUES \
#     (1, 'Veg Biryani'), \
#     (2, 'Veg Fried Rice'), \
#     (3, 'Kaju Fried Rice'), \
#     (4, 'Chicken Biryani'), \
#     (5, 'Chicken Dum Biryani'), \
#     (6, 'Prawns Biryani'), \
#     (7, 'Fish Birayani');")

# cur.execute("DROP TABLE IF EXISTS df_32_1;")
# cur.execute("CREATE TABLE df_32_1 (food_id int, rating int);")
# cur.execute("INSERT INTO df_32_1 VALUES \
#     (1, 5), \
#     (2, 3), \
#     (3, 4), \
#     (4, 4), \
#     (5, 5), \
#     (6, 4), \
#     (7, 4);")
# con.commit()

# cur.execute(""" 
#               select a.food_id, food_item, rating, repeat('*', rating) as stars 
#               from df_32 as a inner join df_32_1 as b on a.food_id = b.food_id
#             """)
# mysql_print()

# cur.execute("""
#                    select a.food_id, food_item, rating,
#                         case 
#                             when rating = 5 then '*****'
#                             when rating = 4 then '****'
#                             when rating = 3 then '***'
#                             when rating = 2 then '**'
#                             when rating = 1 then '*' end
#                         as stars 
#                     from df_32 as a inner join df_32_1 as b on a.food_id = b.food_id
#                    """)
# mysql_print()

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#     (1, "Veg Biryani"),
#     (2, "Veg Fried Rice"),
#     (3, "Kaju Fried Rice"),
#     (4, "Chicken Biryani"),
#     (5, "Chicken Dum Biryani"),
#     (6, "Prawns Biryani"),
#     (7, "Fish Birayani")
# )
# schema = "food_id int, food_item string"

# df1 = spark.createDataFrame(data=data, schema=schema)
# df1.createOrReplaceTempView("df1")

# data = (
#     (1, 5),
#     (2, 3),
#     (3, 4),
#     (4, 4),
#     (5, 5),
#     (6, 4),
#     (7, 4)
# )
# schema = "food_id int, rating int"

# df2 = spark.createDataFrame(data=data, schema=schema)
# df2.createOrReplaceTempView("df2")

# df1.join(df2, ["food_id"]).withColumn("stars", expr("repeat('*', rating)")).show()

# =======================================================================================================================
# Second highest salary
# =======================================================================================================================

# cur.execute("DROP TABLE IF EXISTS employee;")
# cur.execute("CREATE TABLE employee (id int, name varchar(100));")
# cur.execute("""INSERT INTO employee VALUES 
#     (1, 'NAME1'),
#     (2, 'NAME2'),
#     (3, 'NAME3'),
#     (4, 'NAME4');""")

# cur.execute("DROP TABLE IF EXISTS salaries;")
# cur.execute("CREATE TABLE salaries (id int, employee_id int, salary bigint);")
# cur.execute("""
#             INSERT INTO salaries VALUES 
#             (1, 4, 6600001),
#             (2, 2, 12600001),
#             (3, 3, 5600001),
#             (4, 1, 8600001);
#     """)
# con.commit()

# cur.execute("""
#             select id, name, salary from (
#               select e.id, name, salary, RANK() over (order by salary desc) as sal_rank from employee as e inner join salaries as s on e.id = s.employee_id
#             ) as rank_table where sal_rank = 4
#             """)
# cur.execute("""
#             select id, name from employee where id in (
#                 select * from
#                 (
#                 select employee_id from salaries order by salary desc limit 1
#                 ) as second
#               )
#             """)
# mysql_print()

# =======================================================================================================================
# Scenario 31
# =======================================================================================================================

# +----+-----+--------+-----------+     =>>     +-----------+
# |col1| col2|    col3|       col4|             |        col|
# +----+-----+--------+-----------+             +-----------+
# |  m1|m1,m2|m1,m2,m3|m1,m2,m3,m4|             |         m1|
# +----+-----+--------+-----------+             |      m1,m2|
#                                               |   m1,m2,m3|
#                                               |m1,m2,m3,m4|
#                                               |           |
#                                               +-----------+

# MYSQL ---------------------------------------------------------------------------------------------------------------------------

# cur.execute("DROP TABLE IF EXISTS df_31;")
# cur.execute("CREATE TABLE df_31 (col1 varchar(100), col2 varchar(100), col3 varchar(100), col4 varchar(100));")
# cur.execute("INSERT INTO df_31 VALUES \
#     ('m1', 'm1,m2', 'm1,m2,m3', 'm1,m2,m3,m4');")

# con.commit()

# cur.execute("""
#             SELECT col1 as col from df_31 union
#             SELECT col2 as col from df_31 union
#             SELECT col3 as col from df_31 union
#             SELECT col4 as col from df_31
#             """)
# mysql_print()

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#     ("m1", "m1,m2", "m1,m2,m3", "m1,m2,m3,m4"),
#     ("s1", "s1,s2", "s1,s2,s3", "s1,s2,s3,s4")
# )
# schema = "col1 string, col2 string, col3 string, col4 string"

# df = spark.createDataFrame(data=data, schema=schema)
# df.createOrReplaceTempView("df")

# df.show()
# df.withColumn("col", expr("explode(split(concat_ws('-',*), '-'))")).select("col").show()

# =======================================================================================================================
# Scenario 30
# =======================================================================================================================

# +------+----+-------+-------+               +--------+---------+
# |emp_id|name|dept_id| salary|               |dept_id1|dept_name|
# +------+----+-------+-------+               +--------+---------+
# |     1|   A|      A|1000000|               |       A|    AZURE|
# |     2|   B|      A|2500000|               |       G|      GCP|
# |     3|   C|      G| 500000|               |       W|      AWS|
# |     4|   D|      G| 800000|               +--------+---------+
# |     5|   E|      W|9000000|
# |     6|   F|      W|2000000|
# +------+----+-------+-------+

#      =>>     +------+----+---------+-------+
#              |emp_id|name|dept_name| salary|
#              +------+----+---------+-------+
#              |     1|   A|    AZURE|1000000|
#              |     6|   F|      AWS|2000000|
#              |     3|   C|      GCP| 500000|
#              +------+----+---------+-------+

# MYSQL ---------------------------------------------------------------------------------------------------------------------------

# cur.execute("DROP TABLE IF EXISTS df_30;")
# cur.execute("CREATE TABLE df_30 (emp_id varchar(100), name varchar(100), dept_id varchar(100), salary varchar(100));")
# cur.execute("INSERT INTO df_30 VALUES \
#     ('1', 'A', 'A', '1000000'), \
#     ('2', 'B', 'A', '2500000'), \
#     ('3', 'C', 'G', '500000'), \
#     ('4', 'D', 'G', '800000'), \
#     ('5', 'E', 'W', '9000000'), \
#     ('6', 'F', 'W', '2000000');")

# cur.execute("DROP TABLE IF EXISTS df_30_1;")
# cur.execute("CREATE TABLE df_30_1 (dept_id1 varchar(10), dept_name varchar(100));")
# cur.execute("INSERT INTO df_30_1 VALUES \
#     ('A', 'AZURE'), \
#     ('G', 'GCP'), \
#     ('W', 'AWS');")

# con.commit()

# cur.execute("""
#             select emp_id, name, dept_name, salary from
#             (select *, RANK() over (partition by dept_id order by salary desc) as sal_rank from df_30) as rank_table
#             inner join df_30_1 on dept_id = dept_id1
#             where sal_rank = 2
#             """)
# mysql_print()

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#     ("1", "A", "A", "1000000"),
#     ("2", "B", "A", "2500000"),
#     ("3", "C", "G", "500000"),
#     ("4", "D", "G", "800000"),
#     ("5", "E", "W", "9000000"),
#     ("6", "F", "W", "2000000")
# )
# schema = "emp_id string, name string, dept_id string, salary string"

# df1 = spark.createDataFrame(data=data, schema=schema)
# df1.createOrReplaceTempView("df1")

# data = (
#     ("A", "AZURE"),
#     ("G", "GCP"),
#     ("W", "AWS")
# )
# schema = "dept_id1 string, dept_name string"

# df2 = spark.createDataFrame(data=data, schema=schema)    
# df2.createOrReplaceTempView("df2")

# df1.withColumn("sal_rank", rank().over(Window.partitionBy(col("dept_id")).orderBy(col("salary").desc()))).filter("sal_rank = 2")\
#   .join(df2, df1.dept_id == df2.dept_id1).select(df1.emp_id, df1.name, df2.dept_name, df1.salary).show()
  
# spark.sql("""
#           select emp_id, name, dept_name, salary from
#               (
#                 select * from
#                 (
#                   (select *, RANK() over (partition by dept_id order by salary desc) as sal_rank from df1) as rank_table
#                 ) where sal_rank = 2
#               ) as rank_table1
#              inner join df2 on dept_id = dept_id1
#           """).show()

