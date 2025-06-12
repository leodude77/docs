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
# import mysql.connector
# con = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="pass",
#   database="scenarios"
# )
# cur = con.cursor()
def mysql_print():
  print()
  print (cur.column_names)
  for x in cur:
      print (x)
  print()

python_path = sys.executable
os.environ['PYSPARK_PYTHON'] = python_path
os.environ['HADOOP_HOME'] = r'/home/leo/Downloads/Code/docs/hadoop/bin'
os.environ['JAVA_HOME'] = r'/usr/lib/jvm/java-8-openjdk-amd64/jre'

# os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages com.datastax.spark:spark-cassandra-connector_2.12:3.5.1 pyspark-shell'
# os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-avro_2.12:3.5.4 pyspark-shell'
# os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.4 pyspark-shell'
# os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages mysql:mysql-connector-java:8.0.17 pyspark-shell'


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

# cur.execute("""
#             """)
# mysql_print()

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

# df1 = spark.sql("""
#           with CTE1 as (
#             select cust_col as col from df
#             unpivot (
#               cust_col FOR var in (col1, col2, col3, col4)
#             )
#           )
#           , CTE2 as (
#             select case when LENGTH(col) < LENGTH(LAG(col) over (order by (SELECT NULL))) then 1 else 0 end as grouping, col
#             from CTE1
#           )
#           , CTE3 as (
#             select sum(grouping) over (order by (select NULL) rows between unbounded preceding and current row) as grouping_id, col
#             from CTE2
#           )
#           , CTE4 as (
#             select *, concat('col_', ROW_NUMBER() OVER (partition by grouping_id order by (select null))) as column_name
#             from CTE3
#           )
          
#           select *
#           from CTE4
             
#           """)

# df1.groupBy("grouping_id").pivot("column_name").agg(collect_list("col")).drop("grouping_id").show()

# data = [("m1",), ("m1,m2",), ("m1,m2,m3",), ("m1,m2,m3,m4",), ("",)]

# df = spark.createDataFrame(data, ["col"])

# df = df.filter(df.col != "")
# df = df.withColumn("id", monotonically_increasing_id())

# df_pivot = df.groupBy().pivot("id").agg({"col": "last"})
# df_pivot.show()

# df_pivot = df_pivot.toDF("col1", "col2", "col3", "col4")
# df_pivot.show()

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

# =======================================================================================================================
# Scenario 29
# =======================================================================================================================

# +---+                +----+   
# |col|                |col1|
# +---+                +----+
# |  1|                |   1|
# |  2|                |   2|
# |  3|                |   3|
# +---+                |   4|
#                      |   5|
#                      +----+



#      =>>     +---+
#              |col|
#              +---+
#              |  1|
#              |  2|
#              |  4|
#              |  5|
#              +---+

# MYSQL ---------------------------------------------------------------------------------------------------------------------------

# cur.execute("DROP TABLE IF EXISTS df_29;")
# cur.execute("CREATE TABLE df_29 (col int);")
# cur.execute("INSERT INTO df_29 VALUES \
#     (1), \
#     (2), \
#     (3);")

# cur.execute("DROP TABLE IF EXISTS df_29_1;")
# cur.execute("CREATE TABLE df_29_1 (col1 int);")
# cur.execute("INSERT INTO df_29_1 VALUES \
#     (1), \
#     (2), \
#     (3), \
#     (4), \
#     (5);")

# con.commit()

# cur.execute("""
#             select * from df_29 where col not in (select max(col) from df_29) union
#             select col1 as col from df_29_1 where col1 not in (select max(col) from df_29)
# """)

# cur.execute("""
#             select col1 from df_29_1 where col1 NOT IN 
#             (
#               select max(col) as col from df_29
#             )
# """)
# mysql_print()

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = [
#     (1,),
#     (2,),
#     (3,),
# ]
# schema = "col int"

# df1 = spark.createDataFrame(data=data, schema=schema)
# df1.createOrReplaceTempView("df1")

# data = [
#     (1,),
#     (2,),
#     (3,),
#     (4,),
#     (5,)
# ]
# schema = "col1 int"

# df2 = spark.createDataFrame(data=data, schema=schema)    
# df2.createOrReplaceTempView("df2")

# df1.filter("col not in (select max(col) from df1)").union(df2.filter("col1 not in (select max(col) from df1)")).distinct().show()

# maxSalary = df1.selectExpr("max(col)").first()[0]
# df1.filter(col("col") != maxSalary).union(df2.filter(col("col1") != maxSalary)).distinct().show()

# maxSalary = df1.selectExpr("max(col)").first()[0]
# df1.join(df2, df1.col == df2.col1, "outer").drop("col").withColumnRenamed("col1","col").filter(~col("col").isin(maxSalary)).show()

# df1 = df1.withColumn("col", expr("max(col)"))
# df2.join(df1 , df1.col == df2.col1, "anti").show()

# =======================================================================================================================
# Scenario 28
# =======================================================================================================================

# +-----+------+
# |child|parent|     =>>     +-----+------+-----------+
# +-----+------+             |child|parent|grandparent|
# |    A|    AA|             +-----+------+-----------+
# |    B|    BB|             |    A|    AA|        AAA|
# |    C|    CC|             |    C|    CC|        CCC|
# |   AA|   AAA|             |    B|    BB|        BBB|
# |   BB|   BBB|             +-----+------+-----------+
# |   CC|   CCC|
# +-----+------+

# MYSQL ---------------------------------------------------------------------------------------------------------------------------

# cur.execute("DROP TABLE IF EXISTS df_28;")
# cur.execute("CREATE TABLE df_28 (child varchar(100), parent varchar(100));")
# cur.execute("INSERT INTO df_28 VALUES \
#     ('A', 'AA'), \
#     ('B', 'BB'), \
#     ('C', 'CC'), \
#     ('AA', 'AAA'), \
#     ('BB', 'BBB'), \
#     ('CC', 'CCC');")

# con.commit()

# cur.execute("""
#               select a.child, a.parent, b.parent as Grandparent from df_28 a inner join df_28 b on a.parent = b.child
#             """)
# mysql_print()

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#     ("A", "AA"),
#     ("B", "BB"),
#     ("C", "CC"),
#     ("AA", "AAA"),
#     ("BB", "BBB"),
#     ("CC", "CCC")
# )
# schema = "child string, parent string"

# df = spark.createDataFrame(data=data, schema=schema)
# df.createOrReplaceTempView("df")

# df.alias('a').join(df.alias('b'), col("a.parent") == col("b.child"))\
#   .drop(col("b.child")).selectExpr("child", "a.parent", "b.parent as Grandparent").show()
  
# =======================================================================================================================
# Scenario 27
# =======================================================================================================================

# +-----+------+----+     =>>     +-----+------+----+-----------+
# |empid|salary|year|             |empid|salary|year|incresalary|
# +-----+------+----+             +-----+------+----+-----------+
# |    1| 60000|2018|             |    1| 60000|2018|          0|
# |    1| 70000|2019|             |    1| 70000|2019|      10000|
# |    1| 80000|2020|             |    1| 80000|2020|      10000|
# |    2| 60000|2018|             |    2| 60000|2018|          0|
# |    2| 65000|2019|             |    2| 65000|2019|       5000|
# |    2| 65000|2020|             |    2| 65000|2020|          0|
# |    3| 60000|2018|             |    3| 60000|2018|          0|
# |    3| 65000|2019|             |    3| 65000|2019|       5000|
# +-----+------+----+             +-----+------+----+-----------+

# MYSQL ---------------------------------------------------------------------------------------------------------------------------

# cur.execute("DROP TABLE IF EXISTS df_28;")
# cur.execute("CREATE TABLE df_28 (empid varchar(100), salary varchar(100), year varchar(100));")
# cur.execute("INSERT INTO df_28 VALUES \
#     ('1', '60000', '2018'), \
#     ('1', '70000', '2019'), \
#     ('1', '80000', '2020'), \
#     ('2', '60000', '2018'), \
#     ('2', '65000', '2019'), \
#     ('2', '65000', '2020'), \
#     ('3', '60000', '2018'), \
#     ('3', '65000', '2019');")
# con.commit()

# cur.execute("""
#             select empid, salary, year, (salary - prev_year_sal) as incresalary from
#               ( select *, LAG(salary, 1, salary) OVER (partition by empid order by year) as prev_year_sal from df_28 ) as e
#             """)

# cur.execute("""
#               select empid, salary, year, COALESCE((salary - prev_year_sal), 0) as incresalary from 
#                 (
#                   select *, LAG(salary) OVER (partition by empid order by year) as prev_year_sal from df_28
#                 ) as e
#             """)
# mysql_print()

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#     ("1", "60000", "2018"),
#     ("1", "70000", "2019"),
#     ("1", "80000", "2020"),
#     ("2", "60000", "2018"),
#     ("2", "65000", "2019"),
#     ("2", "65000", "2020"),
#     ("3", "60000", "2018"),
#     ("3", "65000", "2019")
# )
# schema = "empid string, salary string, year string"

# df = spark.createDataFrame(data=data, schema=schema)
# df.createOrReplaceTempView("df")

# df.withColumn("prevyear_sal", lag("salary", 1, 0).over(Window.partitionBy("empid").orderBy("year")))\
#   .withColumn("incresalary", expr("case when prevyear_sal = 0 then 0 else (salary-prevyear_sal) end"))\
#   .drop("prevyear_sal").show()

# df.withColumn("prevyear_sal", lag("salary").over(Window.partitionBy("empid").orderBy("year")))\
#   .withColumn("incresalary", expr("(salary-prevyear_sal)")).na.fill({'incresalary': 0, 'prevyear_sal': 'Some_random_val'}).show()

# =======================================================================================================================
# Scenario 26
# =======================================================================================================================

# +---+----+            +---+-----+
# | id|name|            |id1|name1|
# +---+----+            +---+-----+
# |  1|   A|            |  1|    A|
# |  2|   B|            |  2|    B|
# |  3|   C|            |  4|    X|
# |  4|   D|            |  5|    F|
# +---+----+            +---+-----+

#      =>>     +---+-------------+
#              | id|      comment|
#              +---+-------------+
#              |  3|new in source|
#              |  4|     mismatch|
#              |  5|new in target|
#              +---+-------------+

# MYSQL ---------------------------------------------------------------------------------------------------------------------------

# cur.execute("DROP TABLE IF EXISTS df_26;")
# cur.execute("CREATE TABLE df_26 (id varchar(100), name varchar(100));")
# cur.execute("INSERT INTO df_26 VALUES \
#     ('1', 'A'), \
#     ('2', 'B'), \
#     ('3', 'C'), \
#     ('4', 'D');")

# cur.execute("DROP TABLE IF EXISTS df_26_1;")
# cur.execute("CREATE TABLE df_26_1 (id1 varchar(100), name1 varchar(100));")
# cur.execute("INSERT INTO df_26_1 VALUES \
#     ('1', 'A'), \
#     ('2', 'B'), \
#     ('4', 'X'), \
#     ('5', 'F');")
# con.commit()

# cur.execute("""
#               select COALESCE(id, id1) as id, comment from
#               (
#                 select *, 'New in source' as comment from df_26 left join df_26_1 on id=id1 where id1 is null union
#                 select *, 'New in target' as comment from df_26 right join df_26_1 on id=id1 where id is null union
#                 select *, 'Mismatched' as comment from df_26 inner join df_26_1 on id=id1 where name <> name1
#               ) as e
#             """)

# mysql_print()

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#     ("1", "A"),
#     ("2", "B"),
#     ("3", "C"),
#     ("4", "D")
# )
# schema = "id string, name string"

# df1 = spark.createDataFrame(data=data, schema=schema)
# df1.createOrReplaceTempView("df1")

# data = (
#     ("1", "A"),
#     ("2", "B"),
#     ("4", "X"),
#     ("5", "F")
# )
# schema = "id1 string, name1 string"

# df2 = spark.createDataFrame(data=data, schema=schema)
# df2.createOrReplaceTempView("df2")

# df1.join(df2, df1.id == df2.id1, "full").withColumn("comment", expr("case when id is null then 'New in source' when id1 is null then 'New in target' when name!=name1 then 'Mismatched' end"))\
#   .filter("comment is not null").withColumn("id", expr("coalesce(id, id1)")).select("id", "comment").show()

# =======================================================================================================================
# Scenario 25
# =======================================================================================================================

# emp_no,emp_name,dep
# 101,Murugan,HealthCare
# Invalid Entry,Description: Bad Record Entry
# 102,Kannan,Finance
# 103,Mani,IT
# Connection lost,Description: Poor Connection
# 104,Pavan,HR
# Bad Record,Description:Corrupt Record

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# schema = "emp_no int, emp_name string, dep string, bad_col string"
# df = spark.read.format('csv').options(header='true', columnNameOfCorruptRecord='bad_col', )\
#   .schema(schema).load('C:\Code\docs\docs\\big_data\spark\sc25.csv')
# df.filter("bad_col is not null").show(truncate=False)

# =======================================================================================================================
# Scenario 24
# =======================================================================================================================

# +------+------------+
# |userid|        page|     =>>     +------+--------------------------------------------------------------+
# +------+------------+             |userid|pages                                                         |
# |     1|        home|             +------+--------------------------------------------------------------+
# |     1|    products|             |1     |[home, products, checkout, confirmation]                      |
# |     1|    checkout|             |2     |[home, products, cart, checkout, confirmation, home, products]|
# |     1|confirmation|             +------+--------------------------------------------------------------+
# |     2|        home|
# |     2|    products|
# |     2|        cart|
# |     2|    checkout|
# |     2|confirmation|
# |     2|        home|
# |     2|    products|
# +------+------------+

# MYSQL ---------------------------------------------------------------------------------------------------------------------------

# cur.execute("DROP TABLE IF EXISTS df_24;")
# cur.execute("CREATE TABLE df_24 (userid int, page varchar(100));")
# cur.execute("INSERT INTO df_24 VALUES \
#     (1, 'home'), \
#     (1, 'products'), \
#     (1, 'checkout'), \
#     (1, 'confirmation'), \
#     (2, 'home'), \
#     (2, 'products'), \
#     (2, 'cart'), \
#     (2, 'checkout'), \
#     (2, 'confirmation'), \
#     (2, 'home'), \
#     (2, 'products');")

# con.commit()

# cur.execute("""
#             select userid, JSON_ARRAYAGG(page) as pages from df_24 group by userid
#             """)
# mysql_print()

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#     (1, "home"),
#     (1, "products"),
#     (1, "checkout"),
#     (1, "confirmation"),
#     (2, "home"),
#     (2, "products"),
#     (2, "cart"),
#     (2, "checkout"),
#     (2, "confirmation"),
#     (2, "home"),
#     (2, "products")
# )
# schema = "userid int, page string"

# df = spark.createDataFrame(data=data, schema=schema)
# df.createOrReplaceTempView("df")

# df.groupBy("userid").agg(collect_list("page").alias("pages")).show(truncate=False)

# =======================================================================================================================
# Scenario 23
# =======================================================================================================================

# +-----------+-----------+              +-----------+
# |customer_id|product_key|              |product_key|
# +-----------+-----------+              +-----------+
# |          1|          5|              |          5|
# |          2|          6|              |          6|
# |          3|          5|              +-----------+
# |          3|          6|
# |          1|          6|
# +-----------+-----------+


#      =>>     +-----------+
#              |customer_id|
#              +-----------+
#              |          1|
#              |          3|
#              +-----------+

# MYSQL ---------------------------------------------------------------------------------------------------------------------------

# cur.execute("DROP TABLE IF EXISTS df_23;")
# cur.execute("CREATE TABLE df_23 (customer_id int, product_key varchar(100));")
# cur.execute("INSERT INTO df_23 VALUES \
#     (1, '6'), \
#     (2, '6'), \
#     (3, '5'), \
#     (3, '6'), \
#     (1, '5');")

# cur.execute("DROP TABLE IF EXISTS df_23_1;")
# cur.execute("CREATE TABLE df_23_1 (product_key varchar(100));")
# cur.execute("INSERT INTO df_23_1 VALUES \
#     ('5'), \
#     ('6');")

# con.commit()

# cur.execute("""
#             select customer_id as product_key_list from df_23 
#             group by customer_id having group_concat(product_key order by product_key) 
#             IN ( select group_concat(product_key order by product_key ) from df_23_1 )
#             """)
# mysql_print()

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#     (1, 6),
#     (2, 6),
#     (3, 5),
#     (3, 6),
#     (1, 5)
# )
# schema = "customer_id int, product_key int"

# df1 = spark.createDataFrame(data=data, schema=schema)
# df1.createOrReplaceTempView("df1")

# data = (
#     (5,),
#     (6,)
# )
# schema = "product_key int"

# df2 = spark.createDataFrame(data=data, schema=schema)
# df2.createOrReplaceTempView("df2")

# df1.groupBy("customer_id").agg(sort_array(collect_list("product_key")).alias("product_key_list"))\
#   .filter("product_key_list IN (select sort_array(collect_list(product_key)) from df2)").show()

# =======================================================================================================================
# Scenario 22
# =======================================================================================================================

# +---+------+-----+     =>>     +---+------+-----+---------+
# |pid|  date|price|             |pid|  date|price|new_price|
# +---+------+-----+             +---+------+-----+---------+
# |  1|26-May|  100|             |  1|26-May|  100|      100|
# |  1|27-May|  200|             |  1|27-May|  200|      300|
# |  1|28-May|  300|             |  1|28-May|  300|      600|
# |  2|29-May|  400|             |  2|29-May|  400|      400|
# |  3|30-May|  500|             |  3|30-May|  500|      500|
# |  3|31-May|  600|             |  3|31-May|  600|     1100|
# +---+------+-----+             +---+------+-----+---------+

# MYSQL ---------------------------------------------------------------------------------------------------------------------------

# cur.execute("DROP TABLE IF EXISTS df_22;")
# cur.execute("CREATE TABLE df_22 (pid int, date varchar(100), price int);")
# cur.execute("INSERT INTO df_22 VALUES \
#     (1, '26-May', 100), \
#     (1, '27-May', 200), \
#     (1, '28-May', 300), \
#     (2, '29-May', 400), \
#     (3, '30-May', 500), \
#     (3, '31-May', 600);")

# con.commit()

# cur.execute("""
#             select pid, date, price, COALESCE(price+new_price_l1, price) as new_price from
#             (
#               select *, LAG(new_price) OVER (partition by pid order by date) as new_price_l1 from
#               (
#                 select *, COALESCE(price + older_price, price) as new_price from (
#                   select *, LAG(price) OVER (partition by pid order by date) as older_price from df_22
#                 ) as e
#               ) as f
#             ) as g
#             """)
# cur.execute("""
#               select *, SUM(price) OVER (PARTITION BY pid ORDER BY date) DIV 1 AS new_price from df_22
#             """)
# mysql_print()

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#     (1, "26-May", 100),
#     (1, "27-May", 200),
#     (1, "28-May", 300),
#     (2, "29-May", 400),
#     (3, "30-May", 500),
#     (3, "31-May", 600)
# )
# schema = "pid int, date string, price int"

# df = spark.createDataFrame(data=data, schema=schema)
# df.createOrReplaceTempView("df")

# df.withColumn("new_price", sum(df.price).over(Window.partitionBy(df.pid).orderBy(df.date))).show()

# =======================================================================================================================
# Scenario 21
# =======================================================================================================================

# +----+---+----+
# |from| to|dist|     =>>     +----+---+--------------+
# +----+---+----+             |from| to|roundtrip_dist|
# | SEA| SF| 300|             +----+---+--------------+
# | CHI|SEA|2000|             | SEA| SF|           600|
# |  SF|SEA| 300|             | CHI|SEA|          4000|
# | SEA|CHI|2000|             | LND|SEA|          1000|
# | SEA|LND| 500|             +----+---+--------------+
# | LND|SEA| 500|
# | LND|CHI|1000|
# | CHI|NDL| 180|
# +----+---+----+


# MYSQL ---------------------------------------------------------------------------------------------------------------------------

# cur.execute("DROP TABLE IF EXISTS df_21;")
# cur.execute("CREATE TABLE df_21 (from_cty varchar(100), to_cty varchar(100), dist int);")
# cur.execute("INSERT INTO df_21 VALUES \
#     ('SEA', 'SF', 300), \
#     ('CHI', 'SEA', 2000), \
#     ('SF', 'SEA', 300), \
#     ('SEA', 'CHI', 2000), \
#     ('SEA', 'LND', 500), \
#     ('LND', 'SEA', 500), \
#     ('LND', 'CHI', 1000), \
#     ('CHI', 'NDL', 180);")

# con.commit()

# cur.execute("""
#             select start_city, end_city, 2*main_dist as roundtrip_dist from
#             (
#               select *, RANK() over (partition by looping_cty order by start_city) as rank_city from
#               (
#                 select a.from_cty as start_city, a.to_cty as end_city, a.dist as main_dist,
#                   CONCAT (
#                   case when a.from_cty < a.to_cty then a.from_cty else a.to_cty end,
#                   '->',
#                   case when a.from_cty > a.to_cty then a.from_cty else a.to_cty end
#                   ) as looping_cty 
#                 from df_21 a inner join df_21 b on a.to_cty = b.from_cty 
#                 and a.from_cty = b.to_cty
#               ) e
#             ) f where rank_city = 1
#             """)

# cur.execute("""
#             select to_cty as from_city, from_cty as to_cty, 2*dist as roundtrip_dist from
#             (
#               select *, ROW_NUMBER() OVER (partition by looping_cty) as ranker_number from
#               (  select *, 
#                   CONCAT (
#                         case when from_cty < to_cty then from_cty else to_cty end,
#                         '->',
#                         case when from_cty > to_cty then from_cty else to_cty end
#                         ) as looping_cty
#                 from df_21
#               ) e
#             ) f where ranker_number=2
#             """)

# cur.execute("""
#               select from_cty, to_cty, 2 * dist as dist from
#               (
#                 select a.from_cty, a.to_cty, a.dist from df_21 a
#                 inner join df_21 b on
#                 a.to_cty = b.from_cty and
#                 b.to_cty = a.from_cty
#                 where a.from_cty < a.to_cty
#               ) e
#             """)

# mysql_print()

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#     ("SEA", "SF", 300),
#     ("CHI", "SEA", 2000),
#     ("SF", "SEA", 300),
#     ("SEA", "CHI", 2000),
#     ("SEA", "LND", 500),
#     ("LND", "SEA", 500),
#     ("LND", "CHI", 1000),
#     ("CHI", "NDL", 180)
# )
# schema = "from_cty string, to_cty string, dist int"

# df = spark.createDataFrame(data=data, schema=schema)
# df.createOrReplaceTempView("df")

# df.alias("a").join(df.alias("b"), (col("a.to_cty") == col("b.from_cty")) & (col("a.from_cty") == col("b.to_cty")))\
#   .where(col("a.from_cty")<col("a.to_cty")).selectExpr("a.from_cty as from_cty", "a.to_cty as to_cty","a.dist * 2 as round_trip").show()

# =======================================================================================================================
# Scenario 20250304
# =======================================================================================================================

# +---+-----+         +---+------+
# | id| name|         | id|salary|
# +---+-----+         +---+------+
# |  1|Henry|         |  1|   100|
# |  2|Smith|         |  2|   500|
# |  3| Hall|         |  4|  1000|
# +---+-----+         +---+------+

#      =>>     +---+-----+------+
#              | id| name|salary|
#              +---+-----+------+
#              |  1|Henry|   100|
#              |  2|Smith|   500|
#              |  3| Hall|     0|
#              +---+-----+------+

# MYSQL ---------------------------------------------------------------------------------------------------------------------------

# cur.execute("DROP TABLE IF EXISTS df_20250304;")
# cur.execute("CREATE TABLE df_20250304 (id int, name varchar(100));")
# cur.execute("INSERT INTO df_20250304 VALUES \
#             (1, 'Henry'), \
#             (2, 'Smith'), \
#             (3, 'Hall');")

# cur.execute("DROP TABLE IF EXISTS df_20250304_1;")
# cur.execute("CREATE TABLE df_20250304_1 (id int, salary int);")
# cur.execute("INSERT INTO df_20250304_1 VALUES \
#             (1, 100), \
#             (2, 500), \
#             (4, 1000);")

# con.commit()

# cur.execute("""
#             select a.id, a.name, coalesce(b.salary, 0) as salary from df_20250304 as a left join df_20250304_1 as b on a.id = b.id
#             """)
# mysql_print()

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data1 = [
#     (1, "Henry"),
#     (2, "Smith"),
#     (3, "Hall")
# ]
# columns1 = ["id", "name"]
# rdd1 = sc.parallelize(data1,1)
# df1 = rdd1.toDF(columns1)
# df1.show()
# data2 = [
#     (1, 100),
#     (2, 500),
#     (4, 1000)
# ]
# columns2 = ["id", "salary"]
# rdd2 = sc.parallelize(data2,1)
# df2 = rdd2.toDF(columns2)
# df2.show()

# df1.join(df2, ["id"], "left").na.fill({'salary': 0}).orderBy("id").show()

# =======================================================================================================================
# Scenario 20
# =======================================================================================================================

# root                                                     =>>             root
#  |-- code: long (nullable = true)                                        |-- code: long (nullable = true)
#  |-- commentCount: long (nullable = true)                                |-- commentCount: long (nullable = true)
#  |-- createAt: string (nullable = true)                                  |-- createdAt: string (nullable = true)
#  |-- createdAt: string (nullable = true)                                 |-- feedsComment: string (nullable = true)
#  |-- description: string (nullable = true)                               |-- imagePaths: string (nullable = true)
#  |-- dislikes: long (nullable = true)                                    |-- images: string (nullable = true)
#  |-- feedsComment: string (nullable = true)                              |-- isdeleted: boolean (nullable = true)
#  |-- id: long (nullable = true)                                          |-- lat: long (nullable = true)
#  |-- imagePaths: string (nullable = true)                                |-- likeDislike: struct (nullable = false)
#  |-- images: string (nullable = true)                                    |    |-- dislikes: long (nullable = true)
#  |-- isdeleted: boolean (nullable = true)                                |    |-- likes: long (nullable = true)
#  |-- lat: long (nullable = true)                                         |    |-- userAction: long (nullable = true)
#  |-- likeCount: long (nullable = true)                                   |-- lng: long (nullable = true)
#  |-- likes: long (nullable = true)                                       |-- location: string (nullable = true)
#  |-- lng: long (nullable = true)                                         |-- msg: string (nullable = true)
#  |-- location: string (nullable = true)                                  |-- multiMedia: array (nullable = false)
#  |-- mediatype: long (nullable = true)                                   |    |-- element: struct (containsNull = false)
#  |-- msg: string (nullable = true)                                       |    |    |-- createAt: string (nullable = true)
#  |-- name: string (nullable = true)                                      |    |    |-- description: string (nullable = true)
#  |-- place: string (nullable = true)                                     |    |    |-- id: long (nullable = true)
#  |-- profilePicture: string (nullable = true)                            |    |    |-- likeCount: long (nullable = true)
#  |-- title: string (nullable = true)                                     |    |    |-- mediatype: long (nullable = true)
#  |-- totalFeed: long (nullable = true)                                   |    |    |-- name: string (nullable = true)
#  |-- url: string (nullable = true)                                       |    |    |-- place: string (nullable = true)
#  |-- userAction: long (nullable = true)                                  |    |    |-- url: string (nullable = true)
#  |-- userId: long (nullable = true)                                      |-- profilePicture: string (nullable = true)
#  |-- videoUrl: string (nullable = true)                                  |-- title: string (nullable = true)
#                                                                          |-- totalFeed: long (nullable = true)
#                                                                          |-- userId: long (nullable = true)
#                                                                          |-- videoUrl: string (nullable = true)
                                                                         
# SPARK ---------------------------------------------------------------------------------------------------------------------------

# df = spark.read.format("json").options(multiline=True).load("C:\\Code\\docs\\docs\\big_data\\spark\\sc_20.json")
# df.printSchema()

# cols_to_remove = ['dislikes', 'likes', 'userAction', 'createAt', 'description', 'id', 'likeCount', 'mediatype',\
#     'name', 'place', 'url' ]

# cols_filtered = [c for c, t in df.dtypes if c not in cols_to_remove]

# cols_to_add = ["likeDislike", "multiMedia"]

# cols_to_replace = {
#   'likeDislike' : struct(col("dislikes"), col("likes"), col("userAction")).alias("likeDislike"),
#   'multiMedia' : array(struct(
#             col("createAt"),
#             col("description"),
#             col("id"),
#             col("likeCount"),
#             col("mediatype"),
#             col("name"),
#             col("place"),
#             col("url")
#         ).alias("element")
#     ).alias("multiMedia")
# }

# cols_filtered = [*cols_filtered, *cols_to_add]
# cols_filtered.sort()

# struct_cols = []
# for x in cols_filtered:
#   if x in cols_to_replace.keys():
#     struct_cols.append(cols_to_replace[x])
#     continue
#   struct_cols.append(col(x))

# df.select([*struct_cols]).printSchema()

# =======================================================================================================================
# Scenario 19
# =======================================================================================================================

# root                                                              =>>      root
#  |-- code: long (nullable = true)                                          |-- code: long (nullable = true)
#  |-- commentCount: long (nullable = true)                                  |-- commentCount: long (nullable = true)
#  |-- createdAt: string (nullable = true)                                   |-- createdAt: string (nullable = true)
#  |-- description: string (nullable = true)                                 |-- description: string (nullable = true)
#  |-- feedsComment: string (nullable = true)                                |-- feedsComment: string (nullable = true)
#  |-- id: long (nullable = true)                                            |-- id: long (nullable = true)
#  |-- imagePaths: string (nullable = true)                                  |-- imagePaths: string (nullable = true)
#  |-- images: string (nullable = true)                                      |-- images: string (nullable = true)
#  |-- isdeleted: boolean (nullable = true)                                  |-- isdeleted: boolean (nullable = true)
#  |-- lat: long (nullable = true)                                           |-- lat: long (nullable = true)
#  |-- likeDislike: struct (nullable = true)                                 |-- dislikes: long (nullable = true)
#  |    |-- dislikes: long (nullable = true)                                 |-- likes: long (nullable = true)
#  |    |-- likes: long (nullable = true)                                    |-- userAction: long (nullable = true)
#  |    |-- userAction: long (nullable = true)                               |-- lng: long (nullable = true)
#  |-- lng: long (nullable = true)                                           |-- location: string (nullable = true)
#  |-- location: string (nullable = true)                                    |-- mediatype: long (nullable = true)
#  |-- mediatype: long (nullable = true)                                     |-- msg: string (nullable = true)
#  |-- msg: string (nullable = true)                                         |-- createAt: string (nullable = true)
#  |-- multiMedia: array (nullable = true)                                   |-- description: string (nullable = true)
#  |    |-- element: struct (containsNull = true)                            |-- id: long (nullable = true)
#  |    |    |-- createAt: string (nullable = true)                          |-- likeCount: long (nullable = true)
#  |    |    |-- description: string (nullable = true)                       |-- mediatype: long (nullable = true)
#  |    |    |-- id: long (nullable = true)                                  |-- name: string (nullable = true)
#  |    |    |-- likeCount: long (nullable = true)                           |-- place: string (nullable = true)
#  |    |    |-- mediatype: long (nullable = true)                           |-- url: string (nullable = true)
#  |    |    |-- name: string (nullable = true)                              |-- name: string (nullable = true)
#  |    |    |-- place: string (nullable = true)                             |-- profilePicture: string (nullable = true)
#  |    |    |-- url: string (nullable = true)                               |-- title: string (nullable = true)
#  |-- name: string (nullable = true)                                        |-- totalFeed: long (nullable = true)
#  |-- profilePicture: string (nullable = true)                              |-- userId: long (nullable = true)
#  |-- title: string (nullable = true)                                       |-- videoUrl: string (nullable = true)
#  |-- totalFeed: long (nullable = true)
#  |-- userId: long (nullable = true)
#  |-- videoUrl: string (nullable = true)
 
# SPARK ---------------------------------------------------------------------------------------------------------------------------

# def create_column_list(columns, parent_column):
#     return [f"{parent_column}.{column} as {column}" for column in columns]

# df = spark.read.format("json").options(multiline=True).load("C:\Code\docs\docs\\big_data\spark\sc_19.json")
# df.printSchema()

# cols_multiMedia = df.withColumn("multiMedia", explode(col("multiMedia"))).select("multiMedia.*").columns
# cols_likeDislike = df.select("likeDislike.*").columns

# other_cols = [ c for c in df.columns if c not in ['multiMedia', 'likeDislike'] ]

# all_cols = [*other_cols, *create_column_list(cols_multiMedia, 'multiMedia'), *create_column_list(cols_likeDislike, 'likeDislike')]
# all_cols.sort()

# df.withColumn("multiMedia", explode(col("multiMedia")))\
#   .selectExpr(all_cols).printSchema()

# =======================================================================================================================
# Scenario 18
# =======================================================================================================================

# +------------------+     =>>     +------------------+
# |              word|             |      reverse word|
# +------------------+             +------------------+
# |The Social Dilemma|             |ehT laicoS ammeliD|
# +------------------+             +------------------+

# MYSQL ---------------------------------------------------------------------------------------------------------------------------

# cur.execute("DROP TABLE IF EXISTS df_18;")
# cur.execute("CREATE TABLE df_18 (word varchar(100));")
# cur.execute("INSERT INTO df_18 VALUES \
#     ('The Social Dilemma');")

# con.commit()

# cur.execute("""
#             select CONCAT_WS( ' ',
#                               REVERSE(SUBSTRING_INDEX(word, ' ', 1)),
#                               REVERSE(SUBSTRING_INDEX(SUBSTRING_INDEX(word, ' ', 2), ' ', -1)),
#                               REVERSE(SUBSTRING_INDEX(word, ' ', -1)) 
#                             ) as word from df_18
#             """)
# mysql_print()

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#   ('The Social Dilemma',),
# )
# schema = "word string"

# df = spark.createDataFrame(data=data, schema=schema)
# df.createOrReplaceTempView("df")

# @udf(returnType=StringType())
# def reverse_udf(str):
#   return " ".join(word[::-1] for word in str.split(' '))

# df.withColumn("word", reverse_udf(df.word)).show()

# =======================================================================================================================
# Scenario 20250304
# =======================================================================================================================

# +-----+----+------+       =>>     +-----+----+------+-----------+
# |empid|name|salary|               |empid|name|salary|Designation|
# +-----+----+------+               +-----+----+------+-----------+
# |    1|   a| 10000|               |    1|   a| 10000|   Employee|
# |    2|   b|  5000|               |    2|   b|  5000|   Employee|
# |    3|   c| 15000|               |    3|   c| 15000|    Manager|
# |    4|   d| 25000|               |    4|   d| 25000|    Manager|
# |    5|   e| 50000|               |    5|   e| 50000|    Manager|
# |    6|   f|  7000|               |    6|   f|  7000|   Employee|
# +-----+----+------+               +-----+----+------+-----------+

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = [
#       ("1", "a", "10000"),
#       ("2", "b", "5000"),
#       ("3", "c", "15000"),
#       ("4", "d", "25000"),
#       ("5", "e", "50000"),
#       ("6", "f", "7000")
# ]
# myschema = ["empid","name","salary"]
# df = spark.createDataFrame(data,schema=myschema)
# df.show()
# df.createOrReplaceTempView("df")

# spark.sql("select *, case when salary > 10000 then 'Manager' else 'Employee' end as Designation from df").show()
# df.withColumn("Designation", when(col("salary") > 10000, "Manager").otherwise("Employee")).show()

# =======================================================================================================================
# Scenario 17
# =======================================================================================================================

# +------+-----+---+------+-------+					          +------+-----+---+-------+
# |emp_id| name|age| state|country|                   |emp_id| name|age|address|
# +------+-----+---+------+-------+                   +------+-----+---+-------+
# |     1|  Tim| 24|Kerala|  India|                   |     1|  Tim| 24|Comcity|
# |     2|Asman| 26|Kerala|  India|                   |     2|Asman| 26|bimcity|
# +------+-----+---+------+-------+                   +------+-----+---+-------+


#      =>>     +------+-----+---+------+-------+-------+
#              |emp_id| name|age| state|country|address|
#              +------+-----+---+------+-------+-------+
#              |     1|  Tim| 24|Kerala|  India|Comcity|
#              |     2|Asman| 26|Kerala|  India|bimcity|
#              +------+-----+---+------+-------+-------+

# MYSQL ---------------------------------------------------------------------------------------------------------------------------

# cur.execute("DROP TABLE IF EXISTS df_17;")
# cur.execute("CREATE TABLE df_17 (emp_id VARCHAR(100), name VARCHAR(100), age VARCHAR(100), state VARCHAR(100), country VARCHAR(100));")
# cur.execute("INSERT INTO df_17 VALUES \
#     ('1', 'Tim', '24', 'Kerala', 'India'), \
#     ('2', 'Asman', '26', 'Kerala', 'India');")

# cur.execute("DROP TABLE IF EXISTS df_17_1;")
# cur.execute("CREATE TABLE df_17_1 (emp_id VARCHAR(100), name VARCHAR(100), age VARCHAR(100), address VARCHAR(100));")
# cur.execute("INSERT INTO df_17_1 VALUES \
#     ('1', 'Tim', '24', 'Comcity'), \
#     ('2', 'Asman', '26', 'bimcity');")

# con.commit()

# cur.execute("""
#             select t1.*, t2.address from df_17 as t1 inner join df_17_1 as t2 on t1.emp_id = t2.emp_id
#             """)
# mysql_print()

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#     ("1", "Tim", "24", "Kerala", "India"),
#     ("2", "Asman", "26", "Kerala", "India")
# )
# schema = "emp_id string, name string, age string, state string, country string"

# df1 = spark.createDataFrame(data=data, schema=schema)
# df1.createOrReplaceTempView("df1")

# data = (
#     ("1", "Tim", "24", "Comcity"),
#     ("2", "Asman", "26", "bimcity")
# )
# schema = "emp_id string, name string, age string, address string"

# df2 = spark.createDataFrame(data=data, schema=schema)
# df2.createOrReplaceTempView("df2")

# df1.alias("t1").join(df2.alias("t2"), ["emp_id"]).select("t1.*", "t2.address").show()

# =======================================================================================================================
# Scenario 16
# =======================================================================================================================

# +---+----+-----------+------+     =>>     +---+----+-----------+------+
# | id|name|       dept|salary|             | id|name|       dept|salary|
# +---+----+-----------+------+             +---+----+-----------+------+
# |  1|Jhon|    Testing|  5000|             |  1|Jhon|    Testing|  5000|
# |  2| Tim|Development|  6000|             |  2| Tim|Development|  6000|
# |  3|Jhon|Development|  5000|             |  4| Sky| Prodcution|  8000|
# |  4| Sky| Prodcution|  8000|             +---+----+-----------+------+
# +---+----+-----------+------+

# MYSQL ---------------------------------------------------------------------------------------------------------------------------

# cur.execute("DROP TABLE IF EXISTS df_16;")
# cur.execute("CREATE TABLE df_16 (id VARCHAR(100), name VARCHAR(100), dept VARCHAR(100), salary VARCHAR(100));")
# cur.execute("INSERT INTO df_16 VALUES \
#     ('1', 'Jhon', 'Testing', '5000'), \
#     ('2', ' Tim', 'Development', '6000'), \
#     ('3', 'Jhon', 'Development', '5000'), \
#     ('4', ' Sky', ' Prodcution', '8000');")

# con.commit()

# cur.execute("""
#             select * from (
#               select t1.*, ROW_NUMBER() OVER(partition by name) as ranker from df_16 as t1
#             ) e where ranker = 1
#             """)
# cur.execute("""
#               DELETE FROM df_16 where id IN (
#                 select id from (
#                   select t1.id from df_16 t1 inner join df_16 t2 on t1.name = t2.name and t1.id > t2.id
#                 ) as e
#               )
#             """)
# cur.execute("select * from df_16")
# mysql_print()

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#     ("1", "Jhon", "Testing", "5000"),
#     ("2", " Tim", "Development", "6000"),
#     ("3", "Jhon", "Development", "5000"),
#     ("4", " Sky", " Prodcution", "8000")
# )
# schema = "id string, name string, dept string, salary string"

# df = spark.createDataFrame(data=data, schema=schema)
# df.createOrReplaceTempView("df")

# df.dropDuplicates(["name"]).show()

# =======================================================================================================================
# Scenario 14
# =======================================================================================================================

# +------+------+------+-------+-----+-------+------+     =>>     +------+------+------+-------+-----+-------+------+-----+
# |rollno|  name|telugu|english|maths|science|social|             |rollno|  name|telugu|english|maths|science|social|total|
# +------+------+------+-------+-----+-------+------+             +------+------+------+-------+-----+-------+------+-----+
# |203040|rajesh|    10|     20|   30|     40|    50|             |203040|rajesh|    10|     20|   30|     40|    50|  150|
# +------+------+------+-------+-----+-------+------+             +------+------+------+-------+-----+-------+------+-----+


# MYSQL ---------------------------------------------------------------------------------------------------------------------------

# cur.execute("DROP TABLE IF EXISTS df_15;")
# cur.execute("CREATE TABLE df_15 (rollno VARCHAR(100), name VARCHAR(100), telugu VARCHAR(100), english VARCHAR(100), maths VARCHAR(100), science VARCHAR(100), social VARCHAR(100));")
# cur.execute("INSERT INTO df_15 VALUES \
#     ('203040', 'rajesh', '10', '20', '30', '40', '50');")
# con.commit()

# cur.execute("""
#             select *, telugu+english+maths+science+social as total from df_15
#             """)
# mysql_print()

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#     ("203040", "rajesh", 10, 20, 30, 40, 50,),
# )
# schema = "rollno string, name string, telegu int, english int, maths int, science int, social int"

# df = spark.createDataFrame(data=data, schema=schema)
# df.createOrReplaceTempView("df")

# df.withColumn("total", col("telegu") + col("english") + col("maths") + col("science") + col("social")).show()

# df.selectExpr("*", "+".join(df.columns[2:]) + " as total").show()

# =======================================================================================================================
# Scenario 13
# =======================================================================================================================

# +------+--------+-----------+
# |emp_id|emp_name|       dept|     =>>   +-----------+-----+  
# +------+--------+-----------+           |       dept|total|
# |     1|    Jhon|Development|           +-----------+-----+
# |     2|     Tim|Development|           |Development|    2|
# |     3|   David|    Testing|           |    Testing|    3|
# |     4|     Sam|    Testing|           | Production|    4|
# |     5|   Green|    Testing|           +-----------+-----+
# |     6|  Miller| Production|
# |     7|  Brevis| Production|
# |     8|  Warner| Production|
# |     9|    Salt| Production|
# +------+--------+-----------+


# MYSQL ---------------------------------------------------------------------------------------------------------------------------

# cur.execute("DROP TABLE IF EXISTS df_13;")
# cur.execute("CREATE TABLE df_13 (emp_id VARCHAR(100), emp_name VARCHAR(100), dept VARCHAR(100));")
# cur.execute("INSERT INTO df_13 VALUES \
#     ('1', 'Jhon', 'Development'), \
#     ('2', 'Tim', 'Development'), \
#     ('3', 'David', 'Testing'), \
#     ('4', 'Sam', 'Testing'), \
#     ('5', 'Green', 'Testing'), \
#     ('6', 'Miller', 'Production'), \
#     ('7', 'Brevis', 'Production'), \
#     ('8', 'Warner', 'Production'), \
#     ('9', 'Salt', 'Production');")

# con.commit()

# cur.execute("""
#             select dept, count(1) as count, max(emp_id), min(emp_id) from df_13 group by dept
#             """)
# mysql_print()

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#     ("1", "Jhon", "Development"),
#     ("2", "Tim", "Development"),
#     ("3", "David", "Testing"),
#     ("4", "Sam", "Testing"),
#     ("5", "Green", "Testing"),
#     ("6", "Miller", "Production"),
#     ("7", "Brevis", "Production"),
#     ("8", "Warner", "Production"),
#     ("9", "Salt", "Production"),
# )
# schema = "emp_id string, emp_name string, dept string"

# df = spark.createDataFrame(data=data, schema=schema)
# df.createOrReplaceTempView("df")

# df.groupBy("dept").agg(count(lit(1)).alias("count"), max("emp_id").alias("max"), min("emp_id").alias("min")).show()

# =======================================================================================================================
# Scenario 12
# =======================================================================================================================

# +--------------------+----------+     =>>     +--------------------+----------+
# |               email|    mobile|             |               email|    mobile|
# +--------------------+----------+             +--------------------+----------+
# |Renuka1992@gmail.com|9856765434|             |R**********92@gma...|98*****434|
# |anbu.arasu@gmail.com|9844567788|             |a**********su@gma...|98*****788|
# +--------------------+----------+             +--------------------+----------+

# MYSQL ---------------------------------------------------------------------------------------------------------------------------

# cur.execute("DROP TABLE IF EXISTS df_12;")
# cur.execute("CREATE TABLE df_12 (email VARCHAR(100), mobile VARCHAR(100));")
# cur.execute("INSERT INTO df_12 VALUES \
#     ('Renuka1992@gmail.com', '9856765434'), \
#     ('anbu.arasu@gmail.com', '9844567788');")

# con.commit()

# cur.execute("""
#             select 
#               CONCAT(
#                 LEFT(SUBSTRING_INDEX(email, '@', 1), 1),
#                 REPEAT('*', LENGTH(SUBSTRING_INDEX(email, '@', 1))-3),
#                 RIGHT(SUBSTRING_INDEX(email, '@', 1), 2),
#                 '@',
#                 SUBSTRING_INDEX(email, '@', -1)
#               ) as email,
#               CONCAT(
#                 LEFT(mobile, 2),
#                 REPEAT('*', 5),
#                 RIGHT(mobile, 3)
#               ) as mobile
#             from df_12
#             """)

# mysql_print()

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#     ("Renuka1992@gmail.com", "9856765434"),
#     ("anbu.arasu@gmail.com", "9844567788"),
# )
# schema = "email string, mobile string"

# @udf
# def mask_email(email: str) -> str:
#     local_part, domain = email.split('@')
#     return f"{local_part[0]}{'*' * (len(local_part) - 3)}{local_part[-2:]}@{domain}"
  
# @udf
# def mobile_masker(mobile):
#     return mobile[:2] + 5 * '*' + mobile[-3:]

# df = spark.createDataFrame(data=data, schema=schema)
# df.createOrReplaceTempView("df")

# df.withColumn("email", mask_email("email")).withColumn("mobile", mobile_masker("mobile")).show(truncate=False)

# =======================================================================================================================
# Scenario 11
# =======================================================================================================================

# +------+---------------+------+     =>>     +------+---------------+------+-----+
# |emp_id|       emp_name|salary|             |emp_id|       emp_name|salary|grade|
# +------+---------------+------+             +------+---------------+------+-----+
# |     1|           Jhon|  4000|             |     1|           Jhon|  4000|    C|
# |     2|      Tim David| 12000|             |     2|      Tim David| 12000|    A|
# |     3|Json Bhrendroff|  7000|             |     3|Json Bhrendroff|  7000|    B|
# |     4|         Jordon|  8000|             |     4|         Jordon|  8000|    B|
# |     5|          Green| 14000|             |     5|          Green| 14000|    A|
# |     6|         Brewis|  6000|             |     6|         Brewis|  6000|    B|
# +------+---------------+------+             +------+---------------+------+-----+

# MYSQL ---------------------------------------------------------------------------------------------------------------------------

# cur.execute("DROP TABLE IF EXISTS df_11;")
# cur.execute("CREATE TABLE df_11 (emp_id VARCHAR(100), emp_name VARCHAR(100), salary VARCHAR(100));")
# cur.execute("INSERT INTO df_11 VALUES \
#     ('1', 'Jhon', '4000'), \
#     ('2', 'Tim David', '12000'), \
#     ('3', 'Json Bhrendroff', '7000'), \
#     ('4', 'Jordon', '8000'), \
#     ('5', 'Green', '14000'), \
#     ('6', 'Brewis', '6000');")

# con.commit()

# cur.execute("""
#             select 
#               emp_id,
#               emp_name,
#               salary,
#               CASE
#                 WHEN salary < 5000 THEN 'C'
#                 WHEN salary < 10000 THEN 'B'
#                 ELSE 'A'
#               END as grade
#             from df_11
#             """)

# mysql_print()

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#     ("1", "Jhon", "4000"),
#     ("2", "Tim David", "12000"),
#     ("3", "Json Bhrendroff", "7000"),
#     ("4", "Jordon", "8000"),
#     ("5", "Green", "14000"),
#     ("6", "Brewis", "6000"),
# )
# schema = "emp_id string, emp_name string, salary string"

# df = spark.createDataFrame(data=data, schema=schema)
# df.createOrReplaceTempView("df")

# df.withColumn("grade", when(df.salary < 5000, "C").when(df.salary < 10000, "B").otherwise("A")).show(truncate=False)

# =======================================================================================================================
# Scenario 10
# =======================================================================================================================

# +-----+-------------+-------------+
# |empid|commissionamt|monthlastdate|     =>>     +-----+-------------+-------------+
# +-----+-------------+-------------+             |empid|commissionamt|monthlastdate|
# |    1|          300|  31-Jan-2021|             +-----+-------------+-------------+
# |    1|          400|  28-Feb-2021|             |    1|          200|  31-Mar-2021|
# |    1|          200|  31-Mar-2021|             |    2|          900|  31-Dec-2021|
# |    2|         1000|  31-Oct-2021|             +-----+-------------+-------------+
# |    2|          900|  31-Dec-2021|
# +-----+-------------+-------------+

# MYSQL ---------------------------------------------------------------------------------------------------------------------------

# cur.execute("DROP TABLE IF EXISTS df_10;")
# cur.execute("CREATE TABLE df_10 (empid VARCHAR(100), commissionamt VARCHAR(100), monthlastdate VARCHAR(100));")
# cur.execute("INSERT INTO df_10 VALUES \
#     ('1', '300', '31-Jan-2021'), \
#     ('1', '400', '28-Feb-2021'), \
#     ('1', '200', '31-Mar-2021'), \
#     ('2', '1000', '31-Oct-2021'), \
#     ('2', '900', '31-Dec-2021');")

# con.commit()

# cur.execute("""
#               select empid, commissionamt, monthlastdate from
#               (
#                 select *, ROW_NUMBER() OVER (partition by empid order by STR_TO_DATE(monthlastdate, '%d-%b-%Y') desc) as ranker
#                 from df_10
#               ) e where ranker = 1;
#             """)

# cur.execute("""
#              SELECT df.empid, df.commissionamt, df.monthlastdate
#               FROM df_10 df
#               JOIN (
#                   SELECT empid, MAX(STR_TO_DATE(monthlastdate, '%d-%b-%Y')) AS latest_date
#                   FROM df_10
#                   GROUP BY empid
#               ) AS latest_commission
#               ON STR_TO_DATE(df.monthlastdate, '%d-%b-%Y') = latest_commission.latest_date
#               and df.empid = latest_commission.empid
#               ORDER BY df.empid; 
#              """)

# mysql_print()

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = [
#     (1, 300, "31-Jan-2021"),
#     (1, 400, "28-Feb-2021"),
#     (1, 200, "31-Mar-2021"),
#     (2, 1000, "31-Oct-2021"),
#     (2, 900, "31-Dec-2021")
# ]
# df = spark.createDataFrame(data, ["empid", "commissionamt", "monthlastdate"])
# df.show()

# maxdatedf = df.withColumn("conv_date", expr("to_date(monthlastdate, 'dd-MMM-yyyy')")).groupBy(col("empid").alias("empid1"))\
#   .agg(max('conv_date').alias("maxdate"))
# maxdatedf.show()

# joindf = df.join(maxdatedf, (df["empid"] == maxdatedf["empid1"]) & (to_date(df["monthlastdate"], 'dd-MMM-yyyy') == maxdatedf["maxdate"]),
#                  "inner").drop("empid1", "maxdate").orderBy("empid")
# joindf.show()

# =======================================================================================================================
# Scenario 9
# =======================================================================================================================

# +----+---------------+
# |name|           rank|     =>>     c
# +----+---------------+
# |   a|   [1, 1, 1, 3]|
# |   b|   [1, 2, 3, 4]|
# |   c|[1, 1, 1, 1, 4]|
# |   d|            [3]|
# +----+---------------+

# MYSQL ---------------------------------------------------------------------------------------------------------------------------

# cur.execute("DROP TABLE IF EXISTS df_9;")
# cur.execute("CREATE TABLE df_9 (name VARCHAR(100), ranker VARCHAR(100));")
# cur.execute("INSERT INTO df_9 VALUES \
#     ('a', '[1, 1, 1, 3]'), \
#     ('b', '[1, 2, 3, 4]'), \
#     ('c', '[1, 1, 1, 1, 4]'), \
#     ('d', '[3]');")

# con.commit()

# cur.execute("""
#               select name from (
#                 select *, (CHAR_LENGTH(ranker) - CHAR_LENGTH(REPLACE(ranker, '1', ''))) DIV CHAR_LENGTH('1') as counter from df_9
#                 order by counter desc
#                 limit 1
#               ) as e
#             """)
# mysql_print()

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#     ("a", [1, 1, 1, 3]),
#     ("b", [1, 2, 3, 4]),
#     ("c", [1, 1, 1, 1, 4]),
#     ("d", [3])
# )
# schema = "name string, rank array<int>"

# df = spark.createDataFrame(data=data, schema=schema)
# df.createOrReplaceTempView("df")

# print ( df.withColumn("exploded_ranks", explode(df.rank)).where("exploded_ranks=1").groupBy("name")\
#   .agg(count(lit(1)).alias("counter")).orderBy(col("counter").desc()).first() )

# =======================================================================================================================
# Scenario 8
# =======================================================================================================================

# +--------+     =>>     +--------------------+
# |   teams|             |             matches|
# +--------+             +--------------------+
# |   India|             |   India Vs Pakistan|
# |Pakistan|             |   India Vs SriLanka|
# |SriLanka|             |Pakistan Vs SriLanka|
# +--------+             +--------------------+

# MYSQL ---------------------------------------------------------------------------------------------------------------------------

# cur.execute("DROP TABLE IF EXISTS df_8;")
# cur.execute("CREATE TABLE df_8 (teams VARCHAR(100));")
# cur.execute("INSERT INTO df_8 VALUES \
#     ('India'), \
#     ('Pakistan'), \
#     ('SriLanka');")

# con.commit()

# cur.execute("""
#              select CONCAT( df.teams, ' vs ', df1.teams) as matches from df_8 as df 
#              inner join df_8 df1 on df.teams < df1.teams
#             """)
# mysql_print()

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#     ("India",),
#     ("Pakistan",),
#     ("SriLanka",)
# )
# schema = "teams string"

# df = spark.createDataFrame(data=data, schema=schema)
# df.createOrReplaceTempView("df")

# df.alias("a").join(df.alias("b"), (col("a.teams") < col("b.teams")), "inner")\
#   .select(concat(col("a.teams"), lit(" vs "), col("b.teams")).alias("matches")).show()

# =======================================================================================================================
# Scenario 7
# =======================================================================================================================

# +-------+----------+----+--------+-----+
# |sale_id|product_id|year|quantity|price|     =>>     +-------+----------+----+--------+-----+
# +-------+----------+----+--------+-----+             |sale_id|product_id|year|quantity|price|
# |      1|       100|2010|      25| 5000|             +-------+----------+----+--------+-----+
# |      2|       100|2011|      16| 5000|             |      6|       200|2012|      20| 7000|
# |      3|       100|2012|       8| 5000|             |      9|       300|2012|      20| 7000|
# |      4|       200|2010|      10| 9000|             |      1|       100|2010|      25| 5000|
# |      5|       200|2011|      15| 9000|             |      8|       300|2011|      18| 7000|
# |      6|       200|2012|      20| 7000|             +-------+----------+----+--------+-----+
# |      7|       300|2010|      20| 7000|
# |      8|       300|2011|      18| 7000|
# |      9|       300|2012|      20| 7000|
# +-------+----------+----+--------+-----+

# MYSQL ---------------------------------------------------------------------------------------------------------------------------

# cur.execute("DROP TABLE IF EXISTS df_7;")
# cur.execute("CREATE TABLE df_7 (sale_id int, product_id int, year int, quantity int, price int);")
# cur.execute("INSERT INTO df_7 VALUES \
#             (1, 100, 2010, 25, 5000), \
#             (2, 100, 2011, 16, 5000), \
#             (3, 100, 2012, 8, 5000), \
#             (4, 200, 2010, 10, 9000), \
#             (5, 200, 2011, 15, 9000), \
#             (6, 200, 2012, 20, 7000), \
#             (7, 300, 2010, 20, 7000), \
#             (8, 300, 2011, 18, 7000), \
#             (9, 300, 2012, 20, 7000);")

# con.commit()

# cur.execute("""
#             SELECT 
#               sale_id, product_id, year, quantity, price
#             FROM 
#               (
#                 SELECT 
#                   *, 
#                   RANK() OVER (
#                     PARTITION BY year 
#                     ORDER BY 
#                       quantity DESC
#                   ) AS ranker
#                 FROM 
#                   df_7
#               ) AS rankdf 
#             WHERE 
#               ranker = 1 
#             ORDER BY 
#               year, sale_id
#             """)
# mysql_print()

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#     (1, 100, 2010, 25, 5000),
#     (2, 100, 2011, 16, 5000),
#     (3, 100, 2012, 8, 5000),
#     (4, 200, 2010, 10, 9000),
#     (5, 200, 2011, 15, 9000),
#     (6, 200, 2012, 20, 7000),
#     (7, 300, 2010, 20, 7000),
#     (8, 300, 2011, 18, 7000),
#     (9, 300, 2012, 20, 7000),
# )
# schema = "sale_id int, product_id int, year int, quantity int, price int"

# df = spark.createDataFrame(data=data, schema=schema)
# df.createOrReplaceTempView("df")

# df.withColumn("ranker", rank().over(Window.partitionBy(col("year")).orderBy(col("quantity").desc())))\
#   .filter("ranker = 1").orderBy(col("year"), col("sale_id")).drop('ranker').show()

# =======================================================================================================================
# Scenario 6
# =======================================================================================================================

# +-----+----+------+     =>>     +-----+----+------+-----------+
# |empid|name|salary|             |empid|name|salary|Designation|
# +-----+----+------+             +-----+----+------+-----------+
# |    1|   a| 10000|             |    1|   a| 10000|   Employee|
# |    2|   b|  5000|             |    2|   b|  5000|   Employee|
# |    3|   c| 15000|             |    3|   c| 15000|    Manager|
# |    4|   d| 25000|             |    4|   d| 25000|    Manager|
# |    5|   e| 50000|             |    5|   e| 50000|    Manager|
# |    6|   f|  7000|             |    6|   f|  7000|   Employee|
# +-----+----+------+             +-----+----+------+-----------+

# MYSQL ---------------------------------------------------------------------------------------------------------------------------

# cur.execute("DROP TABLE IF EXISTS df_6;")
# cur.execute("CREATE TABLE df_6 (empid int, name varchar(100), salary int);")
# cur.execute("INSERT INTO df_6 VALUES \
#             (1, 'a', 10000), \
#             (2, 'b', 5000), \
#             (3, 'c', 15000), \
#             (4, 'd', 25000), \
#             (5, 'e', 50000), \
#             (6, 'f', 7000);")

# con.commit()

# cur.execute("""
#               select empid, name, salary,
#                 case 
#                   when salary > 10000 then 'Manager'
#                   else 'Employee'                  
#                 end as Designation
#               from df_6
#             """)
# mysql_print()

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#     (1, "a", 10000),
#     (2, "b", 5000),
#     (3, "c", 15000),
#     (4, "d", 25000),
#     (5, "e", 50000),
#     (6, "f", 7000),
# )
# schema = "empid int, name string, salary int"

# df = spark.createDataFrame(data=data, schema=schema)
# df.createOrReplaceTempView("df")

# df.withColumn("Designation", when(col("salary") > 10000, "Manager").otherwise("Employee")).show()

# =======================================================================================================================
# Scenario 5
# =======================================================================================================================

# +---+----+---+-------------+                  +---+----+---+---------------+------+
# | id|name|age|        email|                  | id|name|age|          email|salary|
# +---+----+---+-------------+                  +---+----+---+---------------+------+
# |  1| abc| 31|abc@gmail.com|                  | 11| jkl| 22|  abc@gmail.com|  1000|
# |  2| def| 23| defyahoo.com|                  | 12| vbn| 33|  vbn@yahoo.com|  3000|
# |  3| xyz| 26|xyz@gmail.com|                  | 13| wer| 27|            wer|  2000|
# |  4| qwe| 34| qwegmail.com|                  | 14| zxc| 30|        zxc.com|  2000|
# |  5| iop| 24|iop@gmail.com|                  | 15| lkj| 29|lkj@outlook.com|  2000|
# +---+----+---+-------------+                  +---+----+---+---------------+------+


#      =>>     +---+----+---+---------------+------+
#              | id|name|age|          email|salary|
#              +---+----+---+---------------+------+
#              |  1| abc| 31|  abc@gmail.com|  1000|
#              |  3| xyz| 26|  xyz@gmail.com|  1000|
#              |  5| iop| 24|  iop@gmail.com|  1000|
#              | 11| jkl| 22|  abc@gmail.com|  1000|
#              | 12| vbn| 33|  vbn@yahoo.com|  3000|
#              | 15| lkj| 29|lkj@outlook.com|  2000|
#              +---+----+---+---------------+------+


# MYSQL ---------------------------------------------------------------------------------------------------------------------------

# cur.execute("DROP TABLE IF EXISTS df_5;")
# cur.execute("CREATE TABLE df_5 (id int, name varchar(100), age int, email varchar(100));")
# cur.execute("INSERT INTO df_5 VALUES \
#             (1, 'abc', 31, 'abc@gmail.com'), \
#             (2, 'def', 23, 'yahoo.com'), \
#             (3, 'xyz', 26, 'xyz@gmail.com'), \
#             (4, 'qwe', 34, 'qwegmail.com'), \
#             (5, 'iop', 24, 'iop@gmail.com');")

# cur.execute("DROP TABLE IF EXISTS df_5_1;")
# cur.execute("CREATE TABLE df_5_1 (id int, name varchar(100), age int, email varchar(100), salary int);")
# cur.execute("INSERT INTO df_5_1 VALUES \
#             (11, 'jkl', 22, 'abc@gmail.com', 1000), \
#             (12, 'vbn', 33, 'vbn@yahoo.com', 3000), \
#             (13, 'wer', 27, 'wer', 2000), \
#             (14, 'zxc', 30, 'zxc.com', 2000), \
#             (15, 'lkj', 29, 'lkj@outlook.com', 2000);")

# con.commit()

# cur.execute("""
#             select id, name, age, email, salary from (
#               select id, name, age, email, SUBSTRING_INDEX(email, '@', -1) as splitter, 1000 as salary from df_5
#             ) e
#             where 
#               splitter IN ('gmail.com', 'yahoo.com', 'outlook.com')
#               AND email != splitter
              
#             UNION
            
#             select id, name, age, email, salary from (
#               select id, name, age, email, SUBSTRING_INDEX(email, '@', -1) as splitter, salary from df_5_1
#             ) e
#             where 
#               splitter IN ('gmail.com', 'yahoo.com', 'outlook.com')
#               AND email != splitter
#             """)

# mysql_print()

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#     (1, "abc", 31, "abc@gmail.com"),
#     (2, "def", 23, "defyahoo.com"),
#     (3, "xyz", 26, "xyz@gmail.com"),
#     (4, "qwe", 34, "gmail.com"),
#     (5, "iop", 24, "iop@gmail.com"),
#     (6, "pov", 28, "@"),
# )
# schema = "id int, name string, age int, email string"

# df1 = spark.createDataFrame(data=data, schema=schema)
# df1.createOrReplaceTempView("df1")

# data = (
#     (11, "jkl", 22, "abc@gmail.com", 1000),
#     (12, "vbn", 33, "vbn@yahoo.com", 3000),
#     (13, "wer", 27, "wer", 2000),
#     (14, "zxc", 30, "zxc.com", 2000),
#     (15, "lkj", 29, "lkj@outlook.com", 2000),
# )
# schema = "id int, name string, age int, email string, salary int"

# df2 = spark.createDataFrame(data=data, schema=schema)
# df2.createOrReplaceTempView("df2")

# df1.withColumn("splitter", element_at(split(col("email"), "@"), -1))\
#   .filter((col("splitter").isin("gmail.com", "yahoo.com", "outlook.com"))\
#      & (col('splitter') != col("email"))).withColumn("salary", lit(1000)).drop('splitter').union(
#        df2.withColumn("splitter", element_at(split(col("email"), "@"), -1))\
#         .filter((col("splitter").isin("gmail.com", "yahoo.com", "outlook.com"))\
#           & (col('splitter') != col("email"))).drop("splitter")
#      ).show()

# df1.withColumn("salary", lit(1000)).union(df2).withColumn("splitter", element_at(split(col("email"), "@"), -1))\
#   .filter((col("splitter").isin("gmail.com", "yahoo.com", "outlook.com"))\
#      & (col('splitter') != col("email"))).drop('splitter').show()

# =======================================================================================================================
# Scenario 4
# =======================================================================================================================

# +------+-----------+-------+
# |custid|   custname|address|     =>>     +------+-----------+--------+
# +------+-----------+-------+             |custid|   custname| address|
# |     1|   Mark Ray|     AB|             +------+-----------+--------+
# |     2|Peter Smith|     CD|             |     1|   Mark Ray|[EF, AB]|
# |     1|   Mark Ray|     EF|             |     2|Peter Smith|[CD, GH]|
# |     2|Peter Smith|     GH|             |     3|       Kate|    [IJ]|
# |     2|Peter Smith|     CD|             +------+-----------+--------+
# |     3|       Kate|     IJ|
# +------+-----------+-------+


# MYSQL ---------------------------------------------------------------------------------------------------------------------------

# cur.execute("DROP TABLE IF EXISTS df_4;")
# cur.execute("CREATE TABLE df_4 (custid int, custname varchar(100), address varchar(100));")
# cur.execute("INSERT INTO df_4 VALUES \
#               (1, 'Mark Ray', 'AB'), \
#               (2, 'Peter Smith', 'CD'), \
#               (1, 'Mark Ray', 'EF'), \
#               (2, 'Peter Smith', 'GH'), \
#               (2, 'Peter Smith', 'CD'), \
#               (3, 'Kate', 'IJ');")
# con.commit()

# cur.execute("""
#               select custid, custname, CONCAT('[', GROUP_CONCAT(address), ']') as address from 
#               (
#                 select distinct custid, custname, address from df_4
#               ) e
#               group by custid, custname
#             """)
# mysql_print()

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#     (1, "Mark Ray", "AB"),
#     (2, "Peter Smith", "CD"),
#     (1, "Mark Ray", "EF"),
#     (2, "Peter Smith", "GH"),
#     (2, "Peter Smith", "CD"),
#     (3, "Kate", "IJ"),
# )
# schema = "custid int, custname string, address string"

# df = spark.createDataFrame(data=data, schema=schema)
# df.createOrReplaceTempView("df")

# df.distinct().groupBy(col("custid"), col("custname")).agg(collect_list(col("address")).alias("address"))\
#   .orderBy('custid').show()

# =======================================================================================================================
# Scenario 3
# =======================================================================================================================

# +--------+----------+------+
# |sensorid| timestamp|values|     =>>     +--------+----------+------+
# +--------+----------+------+             |sensorid| timestamp|values|
# |    1111|2021-01-15|    10|             +--------+----------+------+
# |    1111|2021-01-16|    15|             |    1111|2021-01-15|     5|
# |    1111|2021-01-17|    30|             |    1111|2021-01-16|    15|
# |    1112|2021-01-15|    10|             |    1112|2021-01-15|    10|
# |    1112|2021-01-15|    20|             |    1112|2021-01-15|    10|
# |    1112|2021-01-15|    30|             +--------+----------+------+
# +--------+----------+------+


# MYSQL ---------------------------------------------------------------------------------------------------------------------------

# cur.execute("DROP TABLE IF EXISTS df_3;")
# cur.execute("CREATE TABLE df_3 (sensorid int, timestamp varchar(100), values_val int);")
# cur.execute("INSERT INTO df_3 VALUES \
#               (1111, '2021-01-15', 10), \
#               (1111, '2021-01-16', 15), \
#               (1111, '2021-01-17', 30), \
#               (1112, '2021-01-15', 10), \
#               (1112, '2021-01-15', 20), \
#               (1112, '2021-01-15', 30);")

# con.commit()

# cur.execute("""
#             select sensorid, timestamp, values_val_lead - values_val as values_needed from (
#               select *, LEAD(values_val) OVER (partition by sensorid order by STR_TO_DATE(timestamp, '%Y-%m-%d'))
#               as values_val_lead
#               from df_3
#             ) e 
#             where values_val_lead IS NOT NULL
#             """)
# mysql_print()

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#     (1111, "2021-01-15", 10),
#     (1111, "2021-01-16", 15),
#     (1111, "2021-01-17", 30),
#     (1112, "2021-01-15", 10),
#     (1112, "2021-01-15", 20),
#     (1112, "2021-01-15", 30),
# )
# schema = "sensorid int, timestamp string, values_val int"

# df = spark.createDataFrame(data=data, schema=schema)
# df.createOrReplaceTempView("df")

# df.withColumn("values_val_lead", lead("values_val").over(Window.partitionBy("sensorid").orderBy("timestamp")))\
#   .filter(col("values_val_lead").isNotNull())\
#   .select("sensorid", "timestamp", (col("values_val_lead") - col("values_val")).alias("values")).show()

# =======================================================================================================================
# Scenario 2
# =======================================================================================================================

# +-------+----------+----------+
# |orderid|statusdate|    status|     =>>     +-------+----------+----------+
# +-------+----------+----------+             |orderid|statusdate|    status|
# |      1|     1-Jan|   Ordered|             +-------+----------+----------+
# |      1|     2-Jan|dispatched|             |      1|     2-Jan|dispatched|
# |      1|     3-Jan|dispatched|             |      1|     3-Jan|dispatched|
# |      1|     4-Jan|   Shipped|             |      2|     2-Jan|dispatched|
# |      1|     5-Jan|   Shipped|             +-------+----------+----------+
# |      1|     6-Jan| Delivered|
# |      2|     1-Jan|   Ordered|
# |      2|     2-Jan|dispatched|
# |      2|     3-Jan|   shipped|
# +-------+----------+----------+

# MYSQL ---------------------------------------------------------------------------------------------------------------------------

# cur.execute("DROP TABLE IF EXISTS df_2;")
# cur.execute("CREATE TABLE df_2 (orderid int, statusdate varchar(100), status varchar(100));")
# cur.execute("INSERT INTO df_2 VALUES \
#               (1, '1-Jan', 'Ordered'), \
#               (1, '2-Jan', 'dispatched'), \
#               (1, '3-Jan', 'dispatched'), \
#               (1, '4-Jan', 'Shipped'), \
#               (1, '5-Jan', 'Shipped'), \
#               (1, '6-Jan', 'Delivered'), \
#               (2, '1-Jan', 'Ordered'), \
#               (2, '2-Jan', 'dispatched'), \
#               (2, '3-Jan', 'Shipped');")

# con.commit()

# cur.execute("""
#               select orderid, statusdate, status from df_2 where status = 'dispatched'
#               and orderid in (
#                 select orderid from df_2 where status = BINARY 'Shipped'
#               )
#             """)
# mysql_print()

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#     (1, "1-Jan", "Ordered"),
#     (1, "2-Jan", "dispatched"),
#     (1, "3-Jan", "dispatched"),
#     (1, "4-Jan", "Shipped"),
#     (1, "5-Jan", "Shipped"),
#     (1, "6-Jan", "Delivered"),
#     (2, '1-Jan', 'Ordered'),
#     (2, '2-Jan', 'dispatched'),
#     (2, '3-Jan', 'shipped')
 
# )
# schema = "orderid int, statusdate string, status string"

# df = spark.createDataFrame(data=data, schema=schema)
# df.createOrReplaceTempView("df")

# df.filter(col("status") == "dispatched")\
#   .filter(col("orderid").isin(*[row.orderid for row in df.filter(col("status") == "Ordered").select("orderid").collect()]))\
#   .select("orderid", "statusdate", "status").show()

# =======================================================================================================================
# Scenario 1
# =======================================================================================================================

# +--------+---------+--------+------+-------------------+------+
# |workerid|firstname|lastname|salary|        joiningdate|depart|
# +--------+---------+--------+------+-------------------+------+
# |     001|   Monika|   Arora|100000|2014-02-20 09:00:00|    HR|
# |     002| Niharika|   Verma|300000|2014-06-11 09:00:00| Admin|
# |     003|   Vishal| Singhal|300000|2014-02-20 09:00:00|    HR|
# |     004|  Amitabh|   Singh|500000|2014-02-20 09:00:00| Admin|
# |     005|    Vivek|   Bhati|500000|2014-06-11 09:00:00| Admin|
# +--------+---------+--------+------+-------------------+------+
#                            ||
# 						   ||
# +--------+---------+--------+------+-------------------+------+
# |workerid|firstname|lastname|salary|        joiningdate|depart|
# +--------+---------+--------+------+-------------------+------+
# |     002| Niharika|   Verma|300000|2014-06-11 09:00:00| Admin|
# |     003|   Vishal| Singhal|300000|2014-02-20 09:00:00|    HR|
# |     004|  Amitabh|   Singh|500000|2014-02-20 09:00:00| Admin|
# |     005|    Vivek|   Bhati|500000|2014-06-11 09:00:00| Admin|
# +--------+---------+--------+------+-------------------+------+

# MYSQL ---------------------------------------------------------------------------------------------------------------------------

# cur.execute("DROP TABLE IF EXISTS df_1;")
# cur.execute("CREATE TABLE df_1 (workerid int, firstname varchar(100), lastname varchar(100), salary int, joiningdate varchar(100), depart varchar(100));")
# cur.execute("INSERT INTO df_1 VALUES \
#             (1, 'Monika', 'Arora', 100000, '2014-02-20 09:00:00', 'HR'), \
#             (2, 'Niharika', 'Verma', 300000, '2014-06-11 09:00:00', 'Admin'), \
#             (3, 'Vishal', 'Singhal', 300000, '2014-02-20 09:00:00', 'HR'), \
#             (4, 'Amitabh', 'Singh', 500000, '2014-02-20 09:00:00', 'Admin'), \
#             (5, 'Vivek', 'Bhati', 500000, '2014-06-11 09:00:00', 'Admin'), \
#             (6, 'Joey', 'Swole', 500000, '2014-06-11 09:00:00', 'HR');") \

# con.commit()

# cur.execute("""
#             select workerid, firstname, lastname, salary, joiningdate, depart from
#             (
#               select *, COUNT(1) over (partition by salary) as count from df_1
#             ) e where count > 1
#             """)

# mysql_print()

# # SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#     (1, "Monika", "Arora", 100000, "2014-02-20 09:00:00", "HR"),
#     (2, "Niharika", "Verma", 300000, "2014-06-11 09:00:00", "Admin"),
#     (3, "Vishal", "Singhal", 300000, "2014-02-20 09:00:00", "HR"),
#     (4, "Amitabh", "Singh", 500000, "2014-02-20 09:00:00", "Admin"),
#     (5, "Vivek", "Bhati", 500000, "2014-06-11 09:00:00", "Admin")
# )
# schema = "workerid int, firstname string, lastname string, salary int, joiningdate string, depart string"

# df = spark.createDataFrame(data=data, schema=schema)
# df.createOrReplaceTempView("df")

# df.withColumn("count", count(lit(1)).over(Window.partitionBy("salary"))).where("count > 1")\
#   .select("workerid", "firstname", "lastname", "salary", "joiningdate", "depart").show()

# =======================================================================================================================
# Scenario 35 Q21
# =======================================================================================================================

# +---+---------+--------+--------+
# | id|   airway|     src|    dest|     =>>     +---------+--------+-----------+
# +---+---------+--------+--------+             |   airway|  Source|Destination|
# |  1|   Indigo|   India|  Bhutan|             +---------+--------+-----------+
# |  2| Air Asia|     Aus|   India|             |   Indigo|   India|   SriLanka|
# |  3|   Indigo|  Bhutan|   Nepal|             | Air Asia|     Aus|      Japan|
# |  4|spice jet|SriLanka|  Bhutan|             |spice jet|SriLanka|      Nepal|
# |  5|   Indigo|   Nepal|SriLanka|             +---------+--------+-----------+
# |  6| Air Asia|   India|   Japan|
# |  7|spice jet|  Bhutan|   Nepal|
# +---+---------+--------+--------+

# MYSQL ---------------------------------------------------------------------------------------------------------------------------

# cur.execute("DROP TABLE IF EXISTS flight;")
# cur.execute("CREATE TABLE flight (id int, airway varchar(100), src varchar(100), dest varchar(100));")
# cur.execute("""INSERT INTO flight VALUES
#     (1,	'Indigo', 'India', 'Bhutan' ),
#     (2,	'Air Asia', 'Aus', 'India'),
#     (3,	'Indigo', 'Bhutan', 'Nepal'),
#     (4,	'spice jet', 'SriLanka', 'Bhutan'),
#     (5,	'Indigo', 'Nepal', 'SriLanka'),
#     (6,	'Air Asia', 'India', 'Japan'),
#     (7,	'spice jet', 'Bhutan', 'Nepal');""")

# con.commit()

# cur.execute("""
#             WITH RECURSIVE FlightPath AS (
#     -- Anchor member: Start with the first flight for each airway
#     SELECT
#         id,
#         airway,
#         src,
#         dest,
#         src AS start_src,
#         dest AS final_dest
#     FROM
#         flight
#     WHERE
#         src NOT IN (SELECT dest FROM flight) -- Find starting points (sources not used as destinations)

#     UNION ALL

#     -- Recursive member: Join the next flight in the sequence
#     SELECT
#         f.id,
#         f.airway,
#         f.src,
#         f.dest,
#         fp.start_src,
#         f.dest AS final_dest
#     FROM
#         flight f
#     INNER JOIN
#         FlightPath fp ON f.airway = fp.airway AND f.src = fp.dest
# )
# SELECT
#     airway AS Flight,
#     start_src AS Source,
#     final_dest AS Destination
# FROM
#     FlightPath
# WHERE
#     final_dest NOT IN (SELECT src FROM flight) -- Filter to get the final destination
# ORDER BY
#     airway;
#             """)
# mysql_print()

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#     (1,	'Indigo', 'India', 'Bhutan' ),
#     (2,	'Air Asia', 'Aus', 'India'),
#     (3,	'Indigo', 'Bhutan', 'Nepal'),
#     (4,	'spice jet', 'SriLanka', 'Bhutan'),
#     (5,	'Indigo', 'Nepal', 'SriLanka'),
#     (6,	'Air Asia', 'India', 'Japan'),
#     (7,	'spice jet', 'Bhutan', 'Nepal')
# )
# schema = "id int, airway string, src string, dest string"

# df = spark.createDataFrame(data=data, schema=schema)
# df.createOrReplaceTempView("df")

# df.show()
# df.groupBy("airway").agg(collect_list('src').alias("Source"), collect_list('dest').alias("Destination"))\
#     .withColumn("Source1", array_except(col("Source"), col("Destination"))[0])\
#     .withColumn("Dest1", array_except(col("Destination"), col("Source"))[0])\
#     .drop("Source").drop("Destination")\
#     .withColumnRenamed("Source1", "Source")\
#     .withColumnRenamed("Dest1", "Destination")\
#     .show()

# =======================================================================================================================
# Scenario 35 Q1
# =======================================================================================================================

# +---+--------------------+
# | id|              splits|     =>>     +---+---------------+
# +---+--------------------+             | id|count_of_splits|
# |  1|         p1,p2,p3,p4|             +---+---------------+
# |  2|                  p1|             |  4|              7|
# |  3|               p1,p2|             +---+---------------+
# |  4|p1,p2,p3,p4,p5,p6,p7|
# +---+--------------------+

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#  (1,"p1,p2,p3,p4"),
#  (2,"p1"),
#  (3,"p1,p2"),
#  (4,"p1,p2,p3,p4,p5,p6,p7"),
# )
# schema = "id int, splits string"

# df = spark.createDataFrame(data=data, schema=schema)
# df.createOrReplaceTempView("df")

# df.show()
# maxsplitsdf = df.withColumn("count_of_splits", size(split(df.splits, ',')))

# maxsplitsdf.alias("a")\
#     .join(maxsplitsdf.select(max("count_of_splits").alias("Max")).alias("b"), col("count_of_splits") == col("b.Max"))\
#         .drop("splits", "max").show()

# =======================================================================================================================
# Scenario 35 Q4
# =======================================================================================================================

# +-------+----------------------------------------+     =>>     +-------+--------+---------+------+
# |stockid|predictedprice                          |             |stockid|BuyPrice|SellPrice|Profit|
# +-------+----------------------------------------+             +-------+--------+---------+------+
# |RIL    |[1000, 1005, 1090, 1200, 1000, 900, 890]|             |    RIL|    1000|     1200|   200|
# |HDFC   |[890, 940, 810, 730, 735, 960, 980]     |             |   HDFC|     730|      980|   250|
# |INFY   |[1001, 902, 1000, 990, 1230, 1100, 1200]|             |   INFY|     902|     1230|   328|
# +-------+----------------------------------------+             +-------+--------+---------+------+

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#     ("RIL", [1000,1005,1090,1200,1000,900,890]),
#     ("HDFC", [890,940,810,730,735,960,980]),
#     ("INFY", [1001,902,1000,990,1230,1100,1200]),
# )
# schema = "stockid string, predictedprice array<int>"

# df = spark.createDataFrame(data=data, schema=schema)
# df.createOrReplaceTempView("df")
# df.show(truncate=False)

# @udf(returnType=ArrayType(IntegerType()))
# def get_max_min_seq(list_arr):
    
#     if len(list_arr) < 2:
#         return []

#     max_diff = list_arr[1] - list_arr[0]
#     min_element = list_arr[0]
#     max_element = list_arr[1]
#     n_info = [max_diff, min_element, max_element]
#     # for i in range(len(list_arr)):
#     #     for j in range(i+1, len(list_arr)):
#     #         if list_arr[j] - list_arr[i] > max_diff:
#     #             max_diff = list_arr[j] - list_arr[i]
#     #             max_element = list_arr[i] if list_arr[i] > list_arr[j] else list_arr[j]
#     #             min_element = max_element - max_diff
    
#     # Main
#     for num in list_arr:
#         if num - min_element > max_diff:
#             max_diff = num - min_element
#             max_element = num
#             n_info = [max_diff, min_element, max_element]
        
#         # if ((num < min_element) & (num != list_arr[-1])):
#         if ( num < min_element ):
#             min_element = num
                
#     return n_info

# # df.withColumn("predictedprice", explode(col("predictedprice")))\
# #     .groupBy("stockid")\
# #     .agg(max("predictedprice").alias("SellPrice"), min("predictedprice").alias("BuyPrice"), \
# #         (max(col("predictedprice")) - min(col("predictedprice"))).alias("Profit")).show()

# # Ans
# ansdf = df.withColumn("max_min", get_max_min_seq(col("predictedprice")))
# ansdf.printSchema()

# ansdf\
#     .withColumn("BuyPrice", col("max_min")[1])\
#     .withColumn("SellPrice", col("max_min")[2])\
#     .withColumn("Profit", col("max_min")[0]).drop("max_min", "predictedprice").show()

# =======================================================================================================================
# Scenario 35 Q5
# =======================================================================================================================

# +-------+------------------------+---+     =>>     +--------------------+--------------------+---------------------+
# |name   |travel_location         |age|             |places_visited_indiv|      people_visited|no_of_people_visiting|
# +-------+------------------------+---+             +--------------------+--------------------+---------------------+
# |ravi   |pune,delhi,chennai,noida|32 |             |             chennai|[ravi, gautham, s...|                    3|
# |gautham|delhi,chennai           |30 |             |               delhi|[ravi, gautham, t...|                    3|
# |mary   |noida,pune              |35 |             |               noida|[ravi, mary, shan...|                    3|
# |thomas |delhi,pune              |31 |             |                pune|[ravi, mary, thomas]|                    3|
# |shankar|chennai,noida           |30 |             +--------------------+--------------------+---------------------+
# +-------+------------------------+---+
#                                   ___  ____  
#                                  / _ \|  _ \ 
#                                 | | | | |_) |
#                                 | |_| |  _ < 
#                                  \___/|_| \_\

# +-------+------------------------+---+
# |name   |travel_location         |age|
# +-------+------------------------+---+      =>>     +----+--------------------+---+
# |ravi   |pune,delhi,chennai,noida|32 |              |name|     travel_location|age|
# |gautham|delhi,chennai           |30 |              +----+--------------------+---+
# |mary   |noida,pune              |35 |              |ravi|pune,delhi,chenna...| 32|
# |thomas |delhi,pune              |31 |              +----+--------------------+---+
# |shankar|chennai,noida           |30 |
# +-------+------------------------+---+

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#     ("ravi", "pune,delhi,chennai,noida", 32),
#     ("gautham", "delhi,chennai", 30),
#     ("mary", "noida,pune", 35),
#     ("thomas", "delhi,pune", 31),
#     ("shankar", "chennai,noida", 30),
# )
# schema = "name string, travel_location string, age int"

# df = spark.createDataFrame(data=data, schema=schema)
# df.createOrReplaceTempView("df")
# df.show(truncate=False)

# no_of_cols_df = df.withColumn("no_of_places_visited", size(split(col("travel_location"), ",")))
# max_places_visited = no_of_cols_df.selectExpr("max(no_of_places_visited)").first()[0]

# no_of_cols_df.filter(max_places_visited == col("no_of_places_visited")).drop("no_of_places_visited").show()

# OR 

# df.withColumn("places_visited_indiv", explode(split(col("travel_location"), ",")))\
#     .groupBy(col("places_visited_indiv")).agg(collect_list("name").alias("people_visited"), size(collect_list("name")).alias("no_of_people_visiting"))\
#     .show()

# =======================================================================================================================
# Scenario 35 Q7 1
# =======================================================================================================================

# Read JSON sc_35_q7 -- Assuming

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# df = spark.read.format("json").options(multiline=True).load("./req_scenario_files/sc_35_q7.json")
# df.createOrReplaceTempView("df")
# df.show()

# df1 = df.withColumn("emp", explode("emp"))\
#     .select(col("emp.id").alias("id"), col("emp.name").alias("name"), col("emp.address").alias("address"))\
#     .withColumn("address", explode("address"))\
#     .withColumn("address_line_1", col("address.line1"))\
#     .withColumn("address_line_2", col("address.line2"))\
#     .drop("address")\
#     .na.fill({'address_line_1': '', 'address_line_2': ''})
# df1.show()
# df1.printSchema()

# =======================================================================================================================
# Scenario 35 Q7 2
# =======================================================================================================================

# +-----+-------+------+---------+     =>>     +-----+-------+------+---------+------------+
# |empid|empname|salary|managerid|             |empid|empname|salary|managerid|manager_name|
# +-----+-------+------+---------+             +-----+-------+------+---------+------------+
# |    1|    xyz| 10000|     NULL|             |    1|    xyz| 10000|     NULL|         N/A|
# |    2|    abc| 20000|        1|             |    2|    abc| 20000|        1|         xyz|
# |    3|   fgkb| 30000|        2|             |    3|   fgkb| 30000|        2|         abc|
# |    4|   gfkj| 50000|        2|             |    4|   gfkj| 50000|        2|         abc|
# +-----+-------+------+---------+             +-----+-------+------+---------+------------+

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#     (1, "xyz", 10000, None),
#     (2, "abc", 20000, 1),
#     (3, "fgkb", 30000, 2),
#     (4, "gfkj", 50000, 2),
# )
# schema = "empid int, empname string, salary int, managerid int"

# df = spark.createDataFrame(data=data, schema=schema)
# df.createOrReplaceTempView("df")
# df.show()

# df.alias("a").join(df.alias("b"), col("a.managerid") == col("b.empid"), "left")\
#     .withColumn("manager_name", col("b.empname"))\
#     .select("a.*", "manager_name")\
#     .na.fill({"manager_name": "N/A"})\
#     .show()

# =======================================================================================================================
# Scenario 35 Q11 2
# =======================================================================================================================

# filename = "./req_scenario_files/sc_35_q11.txt"
# fw = open("./req_scenario_files/sc_35_q11_v1.txt", "w")

# with open(filename) as file:
#     for line in file:
#         fw.write(line.rstrip()+"\n")
# fw.close()

# spark.read.format("csv").options(delimiter='|^|', header=True)\
#     .load("./req_scenario_files/sc_35_q11_v1.txt").show()

# =======================================================================================================================
# Scenario 35 Q13
# =======================================================================================================================

# +------+--------+------+----------+
# |emp_id|emp_name|salary|manager_id|
# +------+--------+------+----------+     =>>     +----------+------------+----------------------------+
# |    10|    Anil| 50000|        18|             |manager_id|manager_name|Average_Salary_Under_Manager|
# |    11|   Vikas| 75000|        16|             +----------+------------+----------------------------+
# |    12|   Nisha| 40000|        18|             |        16|      Rajesh|                       75000|
# |    13|   Nidhi| 60000|        17|             |        17|       Raman|                       60000|
# |    14|   Priya| 80000|        18|             |        18|     Santosh|                       53750|
# |    15|   Mohit| 45000|        18|             +----------+------------+----------------------------+
# |    16|  Rajesh| 90000|        16|
# |    17|   Raman| 55000|        16|
# |    18| Santosh| 65000|        17|
# +------+--------+------+----------+

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#     (10, "Anil", 50000, 18),
#     (11, "Vikas", 75000, 16),
#     (12, "Nisha", 40000, 18),
#     (13, "Nidhi", 60000, 17),
#     (14, "Priya", 80000, 18),
#     (15, "Mohit", 45000, 18),
#     (16, "Rajesh", 90000, 16),
#     (17, "Raman", 55000, 16),
#     (18, "Santosh", 65000, 17),
# )
# schema = "emp_id int, emp_name string, salary int, manager_id int"

# df = spark.createDataFrame(data=data, schema=schema)
# df.createOrReplaceTempView("df")
# df.show()

# managers_id_df = df.select(col("manager_id").alias("id")).distinct()
# managers_id_df.show()

# df.join(managers_id_df, df.emp_id == managers_id_df.id, "anti").groupBy("manager_id")\
#     .agg(avg("salary").alias("Average_Salary_Under_Manager")).alias("avgdf")\
#     .join(df, col("avgdf.manager_id") == df.emp_id )\
#     .selectExpr("emp_id as manager_id", "emp_name as manager_name", "cast(Average_Salary_Under_Manager as int) as Average_Salary_Under_Manager").show()

# =======================================================================================================================
# Scenario 35 Q14
# =======================================================================================================================

# +------+     =>>     +------+
# |random|             |random|
# +------+             +------+
# |     1|             | 00001|
# |    01|             | 00001|
# |   011|             | 00011|
# |  0111|             | 00111|
# | 01111|             | 01111|
# +------+             +------+

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#     ("1",),
#     ("01",),
#     ("011",),
#     ("0111",),
#     ("01111",),
# )
# schema = "random string"

# df = spark.createDataFrame(data=data, schema=schema)
# df.createOrReplaceTempView("df")
# df.show()

# df\
#     .withColumn("random", expr("concat( repeat( '0' , (5 - length(random))), random)"))\
#     .show()

# =======================================================================================================================
# Scenario 35 Q16
# =======================================================================================================================

# +----------+     =>>     +--------------+
# |    random|             |        random|
# +----------+             +--------------+
# |aabbccabca|             |a2b2c2a1b1c1a1|
# +----------+             +--------------+

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#     ("aabbccabca",),
# )
# schema = "random string"

# df = spark.createDataFrame(data=data, schema=schema)
# df.createOrReplaceTempView("df")
# df.show()

# @udf(returnType=StringType())
# def count_consecutive_characters(s):
#     result = ""
#     current_char = s[0]
#     count = 1
#     for char in s[1:]:
#         if char == current_char:
#             count += 1
#         else:
#             result += current_char + str(count)
#             current_char = char
#             count = 1
#     result += current_char + str(count)
#     return result

# df.withColumn("random", count_consecutive_characters(df.random)).show()

# =======================================================================================================================
# Scenario 35 Q17 3
# =======================================================================================================================

# +---+-----------+      =>>     +------------------------+
# | id|  team_name|              |matches                 |
# +---+-----------+              +------------------------+
# |  1|      India|              |India vs Australia      |
# |  2|  Australia|              |India vs England        |
# |  3|    England|              |India vs New Zealand    |
# |  4|New Zealand|              |Australia vs England    |
# +---+-----------+              |Australia vs New Zealand|
#                                |England vs New Zealand  |
#                                +------------------------+

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#     (1, "India"),
#     (2, "Australia"),
#     (3, "England"),
#     (4, "New Zealand"),
# )
# schema = "id int, team_name string"

# df = spark.createDataFrame(data=data, schema=schema)
# df.createOrReplaceTempView("df")
# df.show()

# df.alias("a").join(df.alias("b"), (col("a.id") < col("b.id")), "inner")\
#     .select(concat(col("a.team_name"), lit(" vs "), col("b.team_name")).alias("matches"))\
#     .select("matches")\
#     .show(truncate=False)

# def print_matchups(list1):
#     i = 0
#     j = 1
#     while i < j:
#         print(listMap[list1[i]] + " vs " + listMap[list1[j]])
#         if (j == (len(list1) - 1)) :
#             i += 1
#             if i == j:
#                 break
#             j = i + 1
#             continue
#         j += 1


# list1= ["ind", "aus", "eng", "nz"]
# listMap = {
#     "ind": "India",
#     "aus": "Australia",
#     "eng": "England",
#     "nz": "New Zealand"
# }
# print_matchups(list1)

# =======================================================================================================================
# Scenario 35 Q20
# =======================================================================================================================

# ('number',)     =>>     ('missing_number',)
# (1,)                    (2,)
# (3,)                    (4,)
# (5,)                    (7,)
# (6,)                    (9,)
# (8,)
# (10,)


# MYSQL ---------------------------------------------------------------------------------------------------------------------------

# cur.execute("DROP TABLE IF EXISTS Numbers;")
# cur.execute("CREATE TABLE Numbers (number INT NOT Null);")
# cur.execute("insert into Numbers  values (1),(3),(5),(6),(8),(10);")

# con.commit()

# cur.execute("""
#             select missing_number from (
#                 select *, (case when (number - cast(lagger as SIGNED)) = 2 then (lagger + 1) else -1 end ) as missing_number from
#                 ( select *, LAG(number) over (order by number) as lagger from Numbers ) e
#             ) f where missing_number <> -1
#             """)
# mysql_print()

# # Using recursive cte
# cur.execute(" select * from Numbers")
# mysql_print()
# cur.execute("""
#                 with RECURSIVE Realseries as (
#                     select min(number) as number from Numbers
                    
#                     UNION ALL
                    
#                     select number + 1
#                     from Realseries
#                     where number + 1 <= ( select max(number) from Numbers )
#                 )
                
#                 select number as missing_number from Realseries where
#                 number NOT IN ( select * from Numbers)
#             """)
# mysql_print()

# =======================================================================================================================
# Scenario 35 Q22
# =======================================================================================================================

# ('Id', 'dated', 'item')                             =>>     ('dated', 'item')
# (1, datetime.date(2020, 1, 1), 'apple')                     (datetime.date(2020, 1, 1), 'apple')
# (2, datetime.date(2020, 1, 1), 'apple')                     (datetime.date(2020, 1, 1), 'pear')
# (3, datetime.date(2020, 1, 1), 'pear')                      (datetime.date(2020, 1, 2), 'pear')
# (4, datetime.date(2020, 1, 1), 'pear')                      (datetime.date(2020, 1, 3), 'Banana')
# (5, datetime.date(2020, 1, 2), 'pear')
# (6, datetime.date(2020, 1, 2), 'pear')
# (7, datetime.date(2020, 1, 2), 'pear')
# (8, datetime.date(2020, 1, 2), 'orange')
# (9, datetime.date(2020, 1, 3), 'Banana')

# ------------------------------------------------------------------------------------------------------------------------

# ('Id', 'FName', 'LName', 'PhoneNumber', 'ManagerId', 'DepartmentId', 'Salary', 'HireDate')
# (1, 'James', 'Smith', '1234567890', None, 1, 13000, datetime.datetime(2002, 1, 1, 0, 0))
# (2, 'John', 'Johnson', '2468101214', 1, 3, 400, datetime.datetime(2005, 3, 23, 0, 0))
# (3, 'Michael', 'Williams', '1357911131', 1, 2, 16000, datetime.datetime(2009, 5, 12, 0, 0))
# (4, 'John', 'Smith', '1212121212', 2, 1, 500, datetime.datetime(2016, 7, 24, 0, 0))
# (5, 'James', 'Williams', '1234567891', None, 1, 5000, datetime.datetime(2012, 1, 1, 0, 0))
# (6, 'John', 'Williams', '2468101212', 3, 1, 3400, datetime.datetime(2015, 3, 23, 0, 0))
# (7, 'Smith', 'Williams', '1357911133', 4, 2, 6700, datetime.datetime(2019, 5, 12, 0, 0))
# (8, 'Michael', 'Smith', '1212121214', 2, 3, 1500, datetime.datetime(2006, 7, 24, 0, 0))
# (9, 'Michael', 'Johnson', '1357911135', 1, 2, 600, datetime.datetime(2009, 5, 12, 0, 0))
# (10, 'Johnathon', 'Smith', '1212121216', 2, 1, 2500, datetime.datetime(2020, 7, 24, 0, 0))


#      _ _   
#     | | |  
#     | | |  
#     | | |  
#   __| | |__
#   \ \_|_/ /
#    \ \ / / 
#     \ V /  
#      \_/   


# ('id', 'Full_Name', 'ManagerId', 'first_hire_date')
# (1, 'James Smith', 1, datetime.datetime(2002, 1, 1, 0, 0))
# (4, 'John Smith', 2, datetime.datetime(2002, 1, 1, 0, 0))
# (5, 'James Williams', 1, datetime.datetime(2002, 1, 1, 0, 0))
# (6, 'John Williams', 3, datetime.datetime(2002, 1, 1, 0, 0))
# (10, 'Johnathon Smith', 2, datetime.datetime(2002, 1, 1, 0, 0))
# (3, 'Michael Williams', 1, datetime.datetime(2009, 5, 12, 0, 0))        
# (7, 'Smith Williams', 4, datetime.datetime(2009, 5, 12, 0, 0))
# (9, 'Michael Johnson', 1, datetime.datetime(2009, 5, 12, 0, 0))
# (2, 'John Johnson', 1, datetime.datetime(2005, 3, 23, 0, 0))
# (8, 'Michael Smith', 2, datetime.datetime(2005, 3, 23, 0, 0))

# MYSQL ---------------------------------------------------------------------------------------------------------------------------

# cur.execute("DROP TABLE IF EXISTS Employees")
# cur.execute("DROP TABLE IF EXISTS Departments;")
# cur.execute("DROP TABLE IF EXISTS Items;")

# cur.execute("""
#             CREATE TABLE Departments (
#                 Id INT NOT NULL AUTO_INCREMENT,
#                 Name VARCHAR(25) NOT NULL,
#                 PRIMARY KEY(Id)
#             );
#             """)
# cur.execute("""
#             INSERT INTO Departments
#                 (Id, Name)
#             VALUES
#                 (1, 'HR'),
#                 (2, 'Sales'),
#                 (3, 'Tech')
#             ;
#             """)

# cur.execute("""
#             CREATE TABLE Items (
#                 Id INT NOT Null AUTO_INCREMENT,
#                 dated DATE NOT NULL,
#                 item VARCHAR(25) NOT NULL,
#                 PRIMARY KEY (Id)
#             );
#             """)
# cur.execute("""
#                 INSERT INTO Items 
#                     (dated, item)
#                 VALUES
#                     (STR_TO_DATE('01-01-2020','%m-%d-%Y'), 'apple'),
#                     (STR_TO_DATE('01-01-2020','%m-%d-%Y'), 'apple'),
#                     (STR_TO_DATE('01-01-2020','%m-%d-%Y'), 'pear'),
#                     (STR_TO_DATE('01-01-2020','%m-%d-%Y'), 'pear'),
#                     (STR_TO_DATE('01-02-2020','%m-%d-%Y'), 'pear'),
#                     (STR_TO_DATE('01-02-2020','%m-%d-%Y'), 'pear'),
#                     (STR_TO_DATE('01-02-2020','%m-%d-%Y'), 'pear'),
#                     (STR_TO_DATE('01-02-2020','%m-%d-%Y'), 'orange'),
#                     (STR_TO_DATE('01-03-2020', '%m-%d-%Y'), 'Banana')
#                 ;
#             """)

# cur.execute("""
#             CREATE TABLE Employees (
#                 Id INT NOT NULL AUTO_INCREMENT,
#                 FName VARCHAR(35) NOT NULL,
#                 LName VARCHAR(35) NOT NULL,
#                 PhoneNumber VARCHAR(11),
#                 ManagerId INT,
#                 DepartmentId INT NOT NULL,
#                 Salary INT NOT NULL,
#                 HireDate DATETIME NOT NULL,
#                 PRIMARY KEY(Id),
#                 FOREIGN KEY (ManagerId) REFERENCES Employees(Id),
#                 FOREIGN KEY (DepartmentId) REFERENCES Departments(Id)
#             );
#             """)
# cur.execute("""
#             INSERT INTO Employees
#                 (Id, FName, LName, PhoneNumber, ManagerId, DepartmentId, Salary, HireDate)
#             VALUES
#                 (1, 'James', 'Smith', 1234567890, NULL, 1, 13000, str_to_date('01-01-2002', '%d-%m-%Y')),
#                 (2, 'John', 'Johnson', 2468101214, '1', 3, 400, str_to_date('23-03-2005', '%d-%m-%Y')),
#                 (3, 'Michael', 'Williams', 1357911131, '1', 2, 16000, str_to_date('12-05-2009', '%d-%m-%Y')),
#                 (4, 'John', 'Smith', 1212121212, '2', 1, 500, str_to_date('24-07-2016', '%d-%m-%Y')),
#                 (5, 'James', 'Williams', 1234567891, NULL, 1, 5000, str_to_date('01-01-2012', '%d-%m-%Y')),
#                 (6, 'John', 'Williams', 2468101212, '3', 1, 3400, str_to_date('23-03-2015', '%d-%m-%Y')),
#                 (7, 'Smith', 'Williams', 1357911133, '4', 2, 6700, str_to_date('12-05-2019', '%d-%m-%Y')),
#                 (8, 'Michael', 'Smith', 1212121214, '2', 3, 1500, str_to_date('24-07-2006', '%d-%m-%Y')),
#                 (9, 'Michael', 'Johnson', 1357911135, '1', 2, 600, str_to_date('12-05-2009', '%d-%m-%Y')),
#                 (10, 'Johnathon', 'Smith', 1212121216, '2', 1, 2500, str_to_date('24-07-2020', '%d-%m-%Y'));
#             """)

# con.commit()

# cur.execute("""
#             select id, concat(Fname, ' ', Lname) as Full_Name, 
#                 case when ManagerId IS NULL then DepartmentId else ManagerId end as ManagerId,
#                 MIN(HireDate) over (partition by DepartmentId) as first_hire_date
#             from Employees
#             """)
# mysql_print()

# cur.execute("""
#             select dated, item from (
#                 select *, DENSE_RANK() over (partition by dated order by count desc) as ranker from (
#                     select dated, item, count(1) as count from Items group by item, dated
#                 ) e
#             ) f where ranker = 1
#             """)
# mysql_print()

# =======================================================================================================================
# Scenario 35 Q23
# =======================================================================================================================

# +---+-------+-----+      =>>     +------+
# | id|formula|value|              |result|
# +---+-------+-----+              +------+
# |  1|    1+4|   10|              |    50|
# |  2|    2-3|   30|              |   -20|
# |  3|    2+4|   50|              |    70|
# |  4|    2+1|   40|              |    40|
# +---+-------+-----+              +------+

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#     (1, "1+4", 10),
#     (2, "2-3", 30),
#     (3, "2+4", 50),
#     (4, "2+1", 40)
# )
# schema = "id int, formula string, value int"

# df = spark.createDataFrame(data=data, schema=schema)
# df.createOrReplaceTempView("df")
# df.show()

# import re
# @udf(returnType=IntegerType())
# def get_result(str1, ids_ref, vals_ref):
#     pattern = "(?<=\d)\s*([\+\-\*\/])\s*(?=\d)"
#     match = re.search(pattern, str1)
#     if match:
#         operator = match.group()
#         id1 = ids_ref.index(int(str1.split(operator)[0]))
#         val1 = vals_ref[id1]
#         id2 = ids_ref.index(int(str1.split(operator)[1]))
#         val2 = vals_ref[id2]
#         string_to_eval = str(val1) + str(operator) + str(val2)
#         return eval(string_to_eval)
#     else:
#         return None


# df.crossJoin(df.agg(collect_list("id").alias("id_ref"), collect_list("value").alias("val_ref")))\
#     .withColumn("result", get_result(df.formula, col("id_ref"), col("val_ref"))).select("result").show()

# # Without cross joining and storing the ids and values in a variable
# ids_ref = df.agg(collect_list("id").alias("id_ref"), collect_list("value").alias("val_ref")).first()[0]
# vals_ref = df.agg(collect_list("id").alias("id_ref"), collect_list("value").alias("val_ref")).first()[1]

# udf_curry=udf(lambda x: get_result(x, ids_ref, vals_ref), IntegerType())

# df.withColumn("result", udf_curry(df.formula)).select("result").show()

# =======================================================================================================================
# Scenario 20250311
# =======================================================================================================================

# +----------+----------+
# | sell_date|   product|      =>>     +----------+--------------------------------+---------+
# +----------+----------+              |sell_date |products                        |null_sell|
# |2020-05-30| Headphone|              +----------+--------------------------------+---------+
# |2020-06-01|    Pencil|              |2020-05-30|[Headphone, Basketball, T-Shirt]|3        |
# |2020-06-02|      Mask|              |2020-06-01|[Pencil, Book]                  |2        |
# |2020-05-30|Basketball|              |2020-06-02|[Mask, Mask]                    |2        |
# |2020-06-01|      Book|              +----------+--------------------------------+---------+
# |2020-06-02|      Mask|
# |2020-05-30|   T-Shirt|
# +----------+----------+

# MYSQL ---------------------------------------------------------------------------------------------------------------------------

# cur.execute("DROP TABLE IF EXISTS df;")
# cur.execute("CREATE TABLE df (sell_date varchar(100), product varchar(100));")
# cur.execute("INSERT INTO df VALUES \
#             ('2020-05-30','Headphone'),('2020-06-01','Pencil'),('2020-06-02','Mask'),('2020-05-30','Basketball'),('2020-06-01','Book'),('2020-06-02','Mask'),('2020-05-30','T-Shirt');")
# con.commit()

# cur.execute("""
#             select sell_date, JSON_ARRAYAGG(product) as products, count(1) as 'null_sell'
#             from df group by sell_date
#             order by null_sell desc
#             """)
# mysql_print()

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = [('2020-05-30','Headphone'),('2020-06-01','Pencil'),('2020-06-02','Mask'),('2020-05-30','Basketball'),('2020-06-01','Book'),('2020-06-02','Mask'),('2020-05-30','T-Shirt')]
# columns = ["sell_date",'product']

# df = spark.createDataFrame(data,schema=columns)
# df.show()

# df.groupBy("sell_date").agg(collect_list(df.product).alias("products"),\
#     count(lit(1)).alias("null_sell")).orderBy(col("null_sell").desc()).show(truncate=False)

# =======================================================================================================================
# Scenario 34 Q1
# =======================================================================================================================

# +-----------+---+      =>>     +-----------+---+
# |       name|sal|              |       name|sal|
# +-----------+---+              +-----------+---+
# |sree_ramesh|100|              |   mar_jany|200|
# | chiran_tan|200|              |  ram_krish|300|
# |  ram_krish|300|              |sree_ramesh|100|
# |  john_stan|400|              |  john_stan|400|
# |   mar_jany|200|              | chiran_tan|200|
# +-----------+---+              +-----------+---+


# MYSQL ---------------------------------------------------------------------------------------------------------------------------

# cur.execute("DROP TABLE IF EXISTS df;")
# cur.execute("CREATE TABLE df (name varchar(100), sal varchar(100));")
# cur.execute("""INSERT INTO df VALUES
#             ('sree_ramesh','100'),
#             ('chiran_tan','200'),
#             ('ram_krish','300'),
#             ('john_stan','400'),
#             ('mar_jany','200');""")

# con.commit()

# cur.execute(""" select name, sal from (
#                     select *, SUBSTRING_INDEX(name, '_', -1) as second_name from df
#                 ) e order by second_name
#             """)
# mysql_print()

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#     ('sree_ramesh','100'),
#     ('chiran_tan','200'),
#     ('ram_krish','300'),
#     ('john_stan','400'),
#     ('mar_jany','200'),
# )
# schema = "name string, sal string"

# df = spark.createDataFrame(data=data, schema=schema)
# df.createOrReplaceTempView("df")
# df.show()

# df.withColumn("second_name", split(col("name"), "_")[1]).orderBy(col("second_name"))\
#     .drop("second_name").show()

# =======================================================================================================================
# Scenario 34 Q5
# =======================================================================================================================

# +-----+-----+---+      =>>     +--------+---+----+
# |TeamA|TeamB|Won|              |teamname|won|lost|
# +-----+-----+---+              +--------+---+----+
# |    A|    D|  D|              |       D|  0|   1|
# |    B|    A|  A|              |       A|  1|   1|
# |    A|    D|  A|              +--------+---+----+
# +-----+-----+---+


# MYSQL ---------------------------------------------------------------------------------------------------------------------------

# cur.execute("DROP TABLE IF EXISTS df;")
# cur.execute("CREATE TABLE df (TeamA varchar(100), TeamB varchar(100), Won varchar(100));")
# cur.execute("""INSERT INTO df VALUES
#             ('A','D','D'),
#             ('B','A','A'),
#             ('A','D','A');""")

# con.commit()

# cur.execute(""" 
#             select teamname, sum(wonflag) DIV 1 as won, sum(lostflag) DIV 1 as lost
#             from (
#                 SELECT TeamA AS TeamName, 
#                     CASE WHEN TeamA = Won THEN 1 ELSE 0 END AS WonFlag,
#                     CASE WHEN TeamA != Won THEN 1 ELSE 0 END AS LostFlag
#                 FROM df
#                 UNION ALL
#                 SELECT TeamB AS TeamName,
#                     CASE WHEN TeamB = Won THEN 1 ELSE 0 END AS WonFlag,
#                     CASE WHEN TeamB != Won THEN 1 ELSE 0 END AS LostFlag
#                 FROM df
#             ) e
#             group by teamname  
#             """)
# mysql_print()

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#         ('A', 'D', 'D'),
#         ('B', 'A', 'A'),
#         ('A', 'D', 'A'),
# )
# schema = "TeamA string, TeamB string, Won string"

# df = spark.createDataFrame(data=data, schema=schema)
# df.createOrReplaceTempView("df")
# df.show()

# df.withColumn("teamname", when(col("TeamA") == col("Won"), col("TeamA")).otherwise(col("TeamB")))\
#     .withColumn("wonflag", when(col("teamname") == col("TeamA"), 1).otherwise(0))\
#     .withColumn("lostflag", when(col("teamname") == col("TeamB"), 1).otherwise(0))\
#     .groupBy("teamname")\
#     .agg(sum("wonflag").alias("won"), sum("lostflag").alias("lost"))\
#     .show()

# =======================================================================================================================
# Scenario 34 Q6
# =======================================================================================================================

# +------+--------+---------+     =>>     +------+--------+---------+
# |Emp Id|Emp Name|Dept Name|             |Emp_Id|Emp_Name|Dept_Name|
# +------+--------+---------+             +------+--------+---------+
# |   101|   Alice|    Sales|             |   101|   Alice|    Sales|
# |   102|     Bob|    Sales|             |   102|     Bob|    Sales|
# +------+--------+---------+             +------+--------+---------+

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# df = spark.read.format("csv").options(header=True).load("./req_scenario_files/sc_34_q6.csv")
# df.show()

# mod_cols = [ col(f'{c}').alias('_'.join(c.split(' '))) for c in df.columns ]
# print( mod_cols )

# df.select(mod_cols).show()

# =======================================================================================================================
# Scenario 34 Q7
# =======================================================================================================================

# +-----+------+     =>>     +-----+------+
# |range|number|             |range|number|
# +-----+------+             +-----+------+
# |   90|     2|             |   90|     2|
# |   60|     3|             |   80|     3|
# |   70|     5|             |   70|     8|
# |   80|     1|             |   60|    11|
# +-----+------+             +-----+------+

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#         (90, 2),
#         (60, 3),
#         (70, 5),
#         (80, 1),
# )
# schema = "range int, number int"

# df = spark.createDataFrame(data=data, schema=schema)
# df.createOrReplaceTempView("df")
# df.show()

# df.withColumn("number", sum("number").over(Window.orderBy(col("range").desc()))).show()

# =======================================================================================================================
# Scenario 34 Q8
# =======================================================================================================================

# my_list = ['abc', 'for', 'abc', 'like','geek1','nerdy',\
#     'xyz', 'love','questions','words', 'life']

# def get_group_list(list1):
#     new_list = []

#     for i in range(int(len(my_list) / 5) + 1):
#         new_list.append(list1[5*i : 5*(i+1)])
        
#     return new_list

# print(get_group_list(my_list))

# ---------------------------------------------------------------------------------------------------------------------------

# string1 = "sahil sahoo"
# string2 = ""
# flag = True
# for i in string1:
#     if i == ' ':
#         string2 += ' '
#         continue
#     if flag:
#         string2 += i.upper()
#     else:
#         string2 += i
#     flag = not flag

# print(string2)

# =======================================================================================================================
# Scenario 34 Q10
# =======================================================================================================================

# A1 = [1,2,3]
# A2 = [2,3,4]

# print(list(set(A1 + A2)))

# =======================================================================================================================
# Scenario 34 Q13
# =======================================================================================================================

# +---+-------+-----+
# | id|subject|marks|     =>>     +---+---+---+---+
# +---+-------+-----+             | id|Eng|Mat|Sci|
# |101|    Eng|   95|             +---+---+---+---+
# |101|    Sci|   80|             |101| 95| 95| 80|
# |101|    Mat|   95|             |102| 75| 90| 85|
# |102|    Eng|   75|             +---+---+---+---+
# |102|    Sci|   85|
# |102|    Mat|   90|
# +---+-------+-----+

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#         (101, "Eng", 95),
#         (101, "Sci", 80),
#         (101, "Mat", 95),
#         (102, "Eng", 75),
#         (102, "Sci", 85),
#         (102, "Mat", 90),
# )
# schema = "id int, subject string, marks int"

# df = spark.createDataFrame(data=data, schema=schema)
# df.createOrReplaceTempView("df")
# df.show()

# df.groupBy("id").pivot("subject").agg(first("marks")).show()

# =======================================================================================================================
# Scenario 34 Q14
# =======================================================================================================================

# mylist = [ 10,5,24,'Hi',90,12,'Hello' ]
# print( [ c for c in mylist if type(c) == int] )

# =======================================================================================================================
# Scenario 34 Q17
# =======================================================================================================================

# +-----+------------+---------+-------------+----------+   +-----+-------+------+--------+
# |empid|    fullname|managerid|dateofjoining|      city|   |empid|project|salary|variable|
# +-----+------------+---------+-------------+----------+   +-----+-------+------+--------+
# |  121|   John Snow|      321|   01/31/2014|   Toronto|   |  121|     P1|  8000|     500|
# |  321|Walter White|      986|   01/30/2015|California|   |  321|     P2| 10000|    1000|
# |  421|Kuldeep Rana|      876|   27/11/2016| New Delhi|   |  421|     P1| 12000|       0|
# +-----+------------+---------+-------------+----------+   +-----+-------+------+--------+

#                                             _ _   
#                                            | | |  
#                                            | | |  
#                                            | | |  
#                                          __| | |__
#                                          \ \_|_/ /
#                                           \ \ / / 
#                                            \ V /  
#                                             \_/   

#                              +------------+-----------+
#                              |    fullname|finalsalary|
#                              +------------+-----------+
#                              |   John Snow|       8500|
#                              |Walter White|      11000|
#                              |Kuldeep Rana|       8000|
#                              +------------+-----------+

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#         (121, "John Snow", 321, "01/31/2014", "Toronto"),
#         (321, "Walter White", 986, "01/30/2015", "California"),
#         (421, "Kuldeep Rana", 876, "27/11/2016", "New Delhi"),
# )
# schema = "empid int, fullname string, managerid int, dateofjoining string, city string"

# df1 = spark.createDataFrame(data=data, schema=schema)
# df1.show()

# data = (
#         (121, "P1", 8000, 500),
#         (321, "P2", 10000, 1000),
#         (421, "P1", 12000, 0),
# )
# schema = "empid int, project string, salary int, variable int"

# df2 = spark.createDataFrame(data=data, schema=schema)
# df2.show()

# udf2 = df2.withColumn("salary", when(df2.empid == 421, lit(8000)).otherwise(df2.salary))

# df1.join(udf2, df1.empid == udf2.empid)\
#     .withColumn("finalsalary", col("salary") + col("variable"))\
#     .select(df1.fullname, col("finalsalary"))\
#     .show()

# =======================================================================================================================
# Scenario 34 Q18
# =======================================================================================================================

# +---+--------------------+      =>>     +---+-------+
# |id |dep                 |              | id|    dep|
# +---+--------------------+              +---+-------+
# |1  |(IT, HR)            |              |  1|     IT|
# |2  |(MR, Sales, Finance)|              |  1|     HR|
# +---+--------------------+              |  2|     MR|
#                                         |  2|  Sales|
#                                         |  2|Finance|
#                                         +---+-------+

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = (
#         (1, "(IT, HR)"),
#         (2, "(MR, Sales, Finance)"),
# )
# schema = "id int, dep string"

# df = spark.createDataFrame(data=data, schema=schema)
# df.show(truncate=False)

# @udf(ArrayType(StringType()))
# def get_list(str1):
#     return [ c.strip() for c in str1[1:-1].split(",")] 

# df.withColumn("dep", get_list(df.dep)).withColumn("dep", explode(col("dep"))).show()

# =======================================================================================================================
# Scenario 34 Q19
# =======================================================================================================================

# 1.Read the csv and create a dataframe
# 2.Add a new column age_Check to df with condition age > 18 then true else false 
# 3.Create a table from dataframe and retrieve contents from it where gender is male

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# df = spark.read.format("csv").options(header=True).load("./req_scenario_files/sc_34_q19.csv")
# df.show(truncate=False)

# df.withColumn("age_check", when(df.Age>18, True).otherwise(False)).show()

# df.createOrReplaceTempView("df")

# spark.sql("""
#             select * from df where Gender = 'M'
#           """).show()

# =======================================================================================================================
# Scenario 34 Q20
# =======================================================================================================================

# 1.Read the csv and create a dataframe
# 2.Add a new column age_Check to df with condition age > 18 then true else false 
# 3.Create a table from dataframe and retrieve contents from it where gender is male

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# df = spark.read.format("csv").options(header=True).load("./req_scenario_files/sc_34_q19.csv")
# df.show(truncate=False)

# df.withColumn("age_check", when(df.Age>18, True).otherwise(False)).show()

# df.createOrReplaceTempView("df")

# spark.sql("""
#             select * from df where Gender = 'M'
#           """).show()

# =======================================================================================================================
# Scenario 20250312 109 
# =======================================================================================================================

# +----------+------------+
# |event_date|event_status|     =>>     +------------+----------+----------+
# +----------+------------+             |event_status|start_date|  end_date|
# |01-06-2020|         Won|             +------------+----------+----------+
# |02-06-2020|         Won|             |         Won|01-06-2020|03-06-2020|
# |03-06-2020|         Won|             |        Lost|04-06-2020|06-06-2020|
# |04-06-2020|        Lost|             |         Won|07-06-2020|07-06-2020|
# |05-06-2020|        Lost|             |        Lost|08-06-2020|08-06-2020|
# |06-06-2020|        Lost|             +------------+----------+----------+
# |07-06-2020|         Won|
# |08-06-2020|        Lost|
# +----------+------------+

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = [
#     ("01-06-2020", "Won"),
#     ("02-06-2020", "Won"),
#     ("03-06-2020", "Won"),
#     ("04-06-2020", "Lost"),
#     ("05-06-2020", "Lost"),
#     ("06-06-2020", "Lost"),
#     ("07-06-2020", "Won"),
#     ("08-06-2020", "Lost")
# ]

# schema = "event_date string, event_status string"

# df = spark.createDataFrame(data, schema)
# df.createOrReplaceTempView("events")
# df.show()

# df.withColumn("change_flag", \
#   when(col("event_status") != lag("event_status").over(Window.orderBy("event_date")), lit(1)).otherwise(lit(0)))\
#   .withColumn("event_group", sum(col("change_flag")).over(Window.orderBy("event_date")) )  \
#   .groupBy(col("event_group"), col("event_status")).agg(first("event_date").alias("start_date"), last("event_date").alias("end_date") )\
#     .drop(col("event_group")).show()

# One way to look at it is the diff is the number of of other event_status records inbetween
# window_base=Window.orderBy('event_date')
# df_t=df.withColumn("diff",
#                   dense_rank().over(window_base)-
#                   dense_rank().over(window_base.partitionBy("event_status")))\
#        .groupBy("event_status","diff").agg(min("event_date").alias("start_date")\
#                                    ,(max("event_date").alias("end_date")))\
#         .orderBy("start_date")\
#        .show()

# spark.sql("""
          
#           with CTE as (
#             select ( row_number() over (order by event_date) - row_number() over (partition by event_status order by event_date) ) as grouping,
#             event_date, event_status from events
#           )
          
#           select event_status, min(event_date) as start_date, max(event_date) as end_date
#           from CTE
#           group by grouping, event_status
#           """).show()

# =======================================================================================================================
# Scenario 20250312 111
# =======================================================================================================================

# +---+-------+      =>>     +---+-------+
# | id|student|              | id|student|
# +---+-------+              +---+-------+
# |  1|  Alice|              |  1|    Bob|
# |  2|    Bob|              |  2|  Alice|
# |  3|Charlie|              |  3|  David|
# |  4|  David|              |  4|Charlie|
# |  5|    Eve|              |  5|    Eve|
# +---+-------+              +---+-------+

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = [
#     (1, "Alice"),
#     (2, "Bob"),
#     (3, "Charlie"),
#     (4, "David"),
#     (5, "Eve")
# ]

# columns = ["id", "student"]

# df = spark.createDataFrame(data, columns)
# df.show()
# df.createOrReplaceTempView("df")

# df.withColumn("grouping", ((ceil(col("id")/lit(2)))) )\
#   .withColumn("leader", lead(col("student")).over(Window.partitionBy(col("grouping")).orderBy("id")))\
#   .withColumn("lagger", lag(col("student")).over(Window.partitionBy(col("grouping")).orderBy("id")))\
#   .withColumn("student", \
#     when((col("lagger").isNull() & col("leader").isNull()), col("student"))\
#     .when(col("leader").isNull(), col("lagger"))\
#     .otherwise(col("leader")))\
#   .select("id", "student")\
#   .show()

# slightly optimized one I guess
# df\
#   .withColumn("student", \
#     when((col("id")) % 2 == 0, lag(col("student")).over(Window.orderBy("id")))\
#     .when((col("id")) % 2 == 1, coalesce( lead(col("student")).over(Window.orderBy("id")), col("student") )))\
#   .show()

# spark.sql("""
#           select id,
#             case 
#               when (id % 2) = 1 then coalesce( lead(student) over (order by id), student)
#               when (id % 2) = 0 then lag(student) over (order by id)
#             end as student
#           from df
#           """).show()

# =======================================================================================================================
# Scenario 20250312 115
# =======================================================================================================================

# +-------+-----+--------+
# |from_id|to_id|duration|     =>>     +-------+-----+----------+--------------+
# +-------+-----+--------+             |from_id|to_id|call_count|total_duration|
# |     10|   20|      58|             +-------+-----+----------+--------------+
# |     20|   10|      12|             |     10|   30|         1|            20|
# |     10|   30|      20|             |     10|   20|         2|            70|
# |     30|   40|     100|             |     30|   40|         4|          1000|
# |     30|   40|     200|             +-------+-----+----------+--------------+
# |     30|   40|     200|
# |     40|   30|     500|
# +-------+-----+--------+

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = [
#     (10, 20, 58),
#     (20, 10, 12),
#     (10, 30, 20),
#     (30, 40, 100),
#     (30, 40, 200),
#     (30, 40, 200),
#     (40, 30, 500)
# ]

# columns = ["from_id", "to_id", "duration"]

# df = spark.createDataFrame(data, columns)
# df.createOrReplaceTempView("df")
# df.show()

# df.withColumn("maxId", when(df.from_id > df.to_id, df.from_id).otherwise(df.to_id))\
#   .withColumn("from_id", when(col("from_id") == col("maxId"), col("to_id")).otherwise(col("from_id")))\
#   .withColumn("to_id", when(col("from_id") == col("to_id"), col("maxId")).otherwise(col("to_id")))\
#   .groupBy(col("from_id"),col("to_id")).agg(count(lit(1)).alias("call_count"), sum(col("duration")).alias("total_duration"))\
#   .show()

# spark.sql("""
#             with CTE1 as (
#               select from_id + to_id as c, from_id, to_id, duration
#               from df
#             ),
#             CTE2 as (
#               select case
#                         when from_id > to_id then c - from_id
#                         else from_id end
#                       as from_id,
#                       case
#                         when from_id > to_id then c - to_id
#                         else to_id end
#                       as to_id,
#                       duration
#               from CTE1
#             )
            
#             select from_id, to_id, sum(duration) as total_duration, count(1) as call_count
#             from CTE2
#             group by from_id, to_id
#             order by from_id, to_id
#           """).show()

# Much simpler approach
# spark.sql("""
#           select 
#             LEAST(from_id, to_id) as person1,
#             GREATEST(from_id, to_id) as person2,
#             count(1) as total_count,
#             sum(duration) as total_duration
#           from df
#           group by person1, person2
#           """).show()

# =======================================================================================================================
# Scenario 20250312 117
# =======================================================================================================================

# +---------+-----------+        +-----------+---------+-------+-------+-------+
# |player_id|player_name|        |player_year|Wimbledon|Fr_open|US_open|Au_open|
# +---------+-----------+        +-----------+---------+-------+-------+-------+
# |        1|      Nadal|        |       2017|        2|      1|      1|      2|
# |        2|    Federer|        |       2018|        3|      1|      3|      2|
# |        3|      Novak|        |       2019|        3|      1|      1|      3|
# +---------+-----------+        +-----------+---------+-------+-------+-------+
#                                 _ _   
#                                | | |  
#                                | | |  
#                                | | |  
#                              __| | |__
#                              \ \_|_/ /
#                               \ \ / / 
#                                \ V /  
#                                 \_/   
								
#                 +---------+-----------+-----------------+
#                 |player_id|player_name|grand_slams_count|
#                 +---------+-----------+-----------------+
#                 |        1|      Nadal|                5|
#                 |        2|    Federer|                3|
#                 |        3|      Novak|                4|
#                 +---------+-----------+-----------------+

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# data = [
#     (1, "Nadal"),
#     (2, "Federer"),
#     (3, "Novak")
# ]
# columns = ["player_id", "player_name"]

# df1 = spark.createDataFrame(data, columns)
# df1.show()
# df1.createOrReplaceTempView("df1")

# data = [
#     (2017, 2, 1, 1, 2),
#     (2018, 3, 1, 3, 2),
#     (2019, 3, 1, 1, 3)
# ]
# columns = ["player_year", "Wimbledon", "Fr_open", "US_open", "Au_open"]

# df2 = spark.createDataFrame(data, columns)
# df2.show()
# df2.createOrReplaceTempView("df2")

# df1.join(df2, df1.player_id == df2.Wimbledon).union(
#   df1.join(df2, df1.player_id == df2.Fr_open)
# ).union(
#   df1.join(df2, df1.player_id == df2.US_open)
# ).union(
#   df1.join(df2, df1.player_id == df2.Au_open)
# ).groupBy("player_id","player_name").agg(count(lit(1)).alias("grand_slams_count"))\
# .orderBy("player_id").show()

# Alternative
# df2.unpivot("player_year", ["Wimbledon", "Fr_open", "US_open", "Au_open"], "var", "val")\
#   .groupBy(col("val")).agg(count(lit(1)).alias("grand_slams_count"))\
#   .join(df1, col("val") == df1.player_id).select("player_id", "player_name", "grand_slams_count")\
#   .orderBy("player_id").show()

# spark.sql("""
#             with 
#               wimbledonCTE as (
#                 select Wimbledon as title from df2
#               ),
#               fr_open_CTE as (
#                 select Fr_open as title from df2
#               ),
#               us_open_CTE as (
#                 select US_open as title from df2
#               ),
#               au_open_CTE as (
#                 select Au_open as title from df2
#               ),
#               clubbed_CTE as (
#                 select * from wimbledonCTE UNION ALL
#                 select * from fr_open_CTE UNION ALL
#                 select * from us_open_CTE UNION ALL
#                 select * from au_open_CTE
#               )
             
#             select title as player_id, player_name, grand_slams_count from df1 a
#             inner join(
#               select title, count(1) as grand_slams_count
#               from clubbed_CTE
#               group by title
#             ) b on a.player_id = b.title
#             order by player_id
            
#           """).show()

# spark.sql("""
#           with unpivot_cte as (
#             select *
#             from df2
#             unpivot( player_who_won FOR title IN (Wimbledon, Fr_open, US_open, Au_open))
#           ),
#           grouped_cte as (
#             select player_who_won as player_id, count(1) as grand_slams_count
#             from unpivot_cte
#             group by player_who_won
#           )
          
#           select a.player_id, b.player_name, a.grand_slams_count from grouped_cte a
#           inner join df1 b on a.player_id = b.player_id
#           order by a.player_id
#           """).show()

# =======================================================================================================================
# Scenario 20250313 118
# =======================================================================================================================

# +---+-----+------+---------+
# | ID| Name|Salary|ManagerID|     =>>     +-----+
# +---+-----+------+---------+             | Name|
# |  1| John|  6000|        4|             +-----+
# |  2|Kevin| 11000|        4|             |Kevin|
# |  3|  Bob|  8000|        5|             +-----+
# |  4|Laura|  9000|     NULL|
# |  5|Sarah| 10000|     NULL|
# +---+-----+------+---------+

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# schema = StructType([
#     StructField("ID", IntegerType(), True),
#     StructField("Name", StringType(), True),
#     StructField("Salary", IntegerType(), True),
#     StructField("ManagerID", IntegerType(), True)
# ])

# data = [
#     (1, "John", 6000, 4),
#     (2, "Kevin", 11000, 4),
#     (3, "Bob", 8000, 5),
#     (4, "Laura", 9000, None),
#     (5, "Sarah", 10000, None)
# ]

# df = spark.createDataFrame(data, schema)
# df.createOrReplaceTempView("df")
# df.show()

# manager_df = df.select("ManagerID").distinct()
# manager_df.show()

# df.alias("a").join(df.alias("b"), (col("a.Salary")>col("b.Salary")) & (col("a.id") != col("b.id")) & (col("a.ManagerId").isNotNull()))\
#   .join(manager_df, (col("b.ID") ==  manager_df.ManagerID)).select("a.Name").distinct().show()

# spark.sql("""
#           with CTE1 as (
#             select *, a.Salary as emp_sal, b.Salary as man_sal, a.Name as cust_name from df a 
#             inner join df b on
#             a.ManagerID = b.ID
#           )
          
#           select cust_name as Name
#           from CTE1
#           where emp_sal > man_sal
          
#           """).show()


# =======================================================================================================================
# Scenario 20250313 120
# =======================================================================================================================

# +-----------+-------------+-----------+------+
# |employee_id|employee_name| department|salary|     =>>     +-------------+-----------+------+------------------+
# +-----------+-------------+-----------+------+             |employee_name| department|salary|           avg_sal|
# |          1|        Alice|         HR| 60000|             +-------------+-----------+------+------------------+
# |          2|          Bob|         HR| 50000|             |         Hank|Engineering| 98000| 93666.66666666667|
# |          3|      Charlie|    Finance| 70000|             |        Alice|         HR| 60000|51666.666666666664|
# |          4|        David|    Finance| 75000|             |        David|    Finance| 75000| 70333.33333333333|
# |          5|          Eve|Engineering| 90000|             +-------------+-----------+------+------------------+
# |          6|        Frank|Engineering| 93000|
# |          7|        Grace|         HR| 45000|
# |          8|         Hank|Engineering| 98000|
# |          9|          Ivy|    Finance| 66000|
# +-----------+-------------+-----------+------+


# SPARK ---------------------------------------------------------------------------------------------------------------------------

# schema = StructType([
#     StructField("employee_id", IntegerType(), True),
#     StructField("employee_name", StringType(), True),
#     StructField("department", StringType(), True),
#     StructField("salary", IntegerType(), True)
# ])

# data = [
#     (1, "Alice", "HR", 60000),
#     (2, "Bob", "HR", 50000),
#     (3, "Charlie", "Finance", 70000),
#     (4, "David", "Finance", 75000),
#     (5, "Eve", "Engineering", 90000),
#     (6, "Frank", "Engineering", 93000),
#     (7, "Grace", "HR", 45000),
#     (8, "Hank", "Engineering", 98000),
#     (9, "Ivy", "Finance", 66000)
# ]

# df = spark.createDataFrame(data, schema)
# df.createOrReplaceTempView("df")
# df.show()

# avg_sal_df = df.groupBy("department").agg(avg("salary").alias("avg_sal"))
# avg_sal_df.show()

# joindf = df.alias("a").join(avg_sal_df.alias("b"), (col("a.salary") > col("b.avg_sal")) & ( col("a.department") == col("b.department")) )
# joindf.show()

# df.alias("a").join(avg_sal_df.alias("b"), (col("a.salary") > col("b.avg_sal")) & ( col("a.department") == col("b.department")) )\
#   .select(col("a.employee_name"), col("a.department"), col("a.salary"), col("b.avg_sal")).show()

# import time
# time.sleep(3000)

# spark.sql("""
#           with CTE as (
#             select *, avg(salary) over (partition by department) as avg_salary
#             from df
#           )
          
#           select employee_name, department, salary, avg_salary
#           from CTE
#           where salary > avg_salary
               
#           """).show()

# =======================================================================================================================
# HackerRank - 15 Days of Learning SQL
# =======================================================================================================================

# +---------+--------+			   +---------------+-------------+---------+-----+
# |hacker_id|    name|             |submission_date|submission_id|hacker_id|score|
# +---------+--------+             +---------------+-------------+---------+-----+
# |       79|    Rose|             |     2016-03-01|           48|      650|    0|
# |      433|  Angela|             |     2016-03-01|          119|     3162|    0|
# |      463|   Frank|             |     2016-03-01|          141|     4413|    0|
# |      533| Patrick|             |     2016-03-01|          203|     5478|    0|
# |      597|    Lisa|             |     2016-03-01|          215|     5509|    0|
# |      650|Kimberly|             |     2016-03-01|          252|     5990|    0|
# |     1050|  Bonnie|             |     2016-03-01|          264|     7460|    0|
# |     1240| Michael|             |     2016-03-01|          348|     7865|    0|
# |     1433|    Todd|             |     2016-03-01|          395|     7897|    0|
# |     2345|     Joe|             |     2016-03-01|          452|     7978|    0|
# |     2697|    Earl|             |     2016-03-01|          460|     8150|    0|
# |     2764|  Robert|             |     2016-03-01|          485|     9630|    0|
# |     2820|     Amy|             |     2016-03-01|          522|    11209|    0|
# |     2873|  Pamela|             |     2016-03-01|          798|    12371|    0|
# |     3018|   Maria|             |     2016-03-01|          807|    12423|    0|
# |     3124|     Joe|             |     2016-03-01|          908|    19773|    0|
# |     3162|   Linda|             |     2016-03-01|          971|    19963|    0|
# |     3178| Melissa|             |     2016-03-01|          998|    20811|    0|
# |     3222|   Carol|             |     2016-03-01|         1119|    20888|    0|
# |     3374|   Paula|             |     2016-03-01|         1123|    21372|    0|
# +---------+--------+             +---------------+-------------+---------+-----+
#                                  only showing top 20 rows

#                          _ _   
#                         | | |  
#                         | | |  
#                         | | |  
#                       __| | |__
#                       \ \_|_/ /
#                        \ \ / / 
#                         \ V /  
#                          \_/   

#   +---------------+---------+---------+---------+        
# 	|submission_date|consistor|hacker_id|     name|		
# 	+---------------+---------+---------+---------+		
# 	|     2016-03-01|      112|    81314|   Denise|		
# 	|     2016-03-02|       59|    39091|     Ruby|		
# 	|     2016-03-03|       51|    18105|      Roy|		
# 	|     2016-03-04|       49|      533|  Patrick|		
# 	|     2016-03-05|       49|     7891|Stephanie|		
# 	|     2016-03-06|       49|    84307|   Evelyn|		
# 	|     2016-03-07|       35|    80682|  Deborah|		
# 	|     2016-03-08|       35|    10985|  Timothy|		
# 	|     2016-03-09|       35|    31221|    Susan|		
# 	|     2016-03-10|       35|    43192|    Bobby|		
# 	|     2016-03-11|       35|     3178|  Melissa|		
# 	|     2016-03-12|       35|    54967|  Kenneth|		
# 	|     2016-03-13|       35|    30061|    Julia|		
# 	|     2016-03-14|       35|    32353|     Rose|		
# 	|     2016-03-15|       35|    27789|    Helen|		
# 	+---------------+---------+---------+---------+		


# MYSQL ---------------------------------------------------------------------------------------------------------------------------

# cur.execute("DROP TABLE IF EXISTS submissions;")
# cur.execute("""CREATE TABLE submissions (
#     submission_date DATE,
#     submission_id INT,
#     hacker_id INT,
#     score INT
# );""")

# cur.execute("""
#             INSERT INTO submissions (submission_date, submission_id, hacker_id, score) VALUES ('2016-03-01', 48, 650, 0), ('2016-03-01', 119, 3162, 0), ('2016-03-01', 141, 4413, 0), ('2016-03-01', 203, 5478, 0), ('2016-03-01', 215, 5509, 0), ('2016-03-01', 252, 5990, 0), ('2016-03-01', 264, 7460, 0), ('2016-03-01', 348, 7865, 0), ('2016-03-01', 395, 7897, 0), ('2016-03-01', 452, 7978, 0), ('2016-03-01', 460, 8150, 0), ('2016-03-01', 485, 9630, 0), ('2016-03-01', 522, 11209, 0), ('2016-03-01', 798, 12371, 0), ('2016-03-01', 807, 12423, 0), ('2016-03-01', 908, 19773, 0), ('2016-03-01', 971, 19963, 0), ('2016-03-01', 998, 20811, 0), ('2016-03-01', 1119, 20888, 0), ('2016-03-01', 1123, 21372, 0), ('2016-03-01', 1172, 22165, 0), ('2016-03-01', 1236, 22917, 0), ('2016-03-01', 1352, 22949, 0), ('2016-03-01', 1374, 24095, 0), ('2016-03-01', 1380, 24576, 0), ('2016-03-01', 1385, 26093, 0), ('2016-03-01', 1410, 26468, 0), ('2016-03-01', 1625, 27064, 0), ('2016-03-01', 1648, 30082, 0), ('2016-03-01', 1666, 32455, 0), ('2016-03-01', 1667, 33323, 0), ('2016-03-01', 1706, 33863, 0), ('2016-03-01', 1712, 34234, 0), ('2016-03-01', 1736, 34369, 0), ('2016-03-01', 1749, 36594, 0), ('2016-03-01', 1760, 37997, 0), ('2016-03-01', 1786, 38962, 0), ('2016-03-01', 1871, 41057, 0), ('2016-03-01', 1898, 42973, 0), ('2016-03-01', 1906, 44791, 0), ('2016-03-01', 2023, 48490, 0), ('2016-03-01', 2072, 49340, 0), ('2016-03-01', 2172, 51132, 0), ('2016-03-01', 2178, 51548, 0), ('2016-03-01', 2316, 53342, 0), ('2016-03-01', 2350, 54113, 0), ('2016-03-01', 2470, 54408, 0), ('2016-03-01', 2520, 55374, 0), ('2016-03-01', 2521, 56707, 0), ('2016-03-01', 2624, 81338, 85), ('2016-03-01', 2676, 83509, 95), ('2016-03-01', 2686, 81314, 10), ('2016-03-01', 2823, 26955, 35), ('2016-03-01', 2947, 91573, 55), ('2016-03-01', 3231, 26170, 10), ('2016-03-01', 3235, 89164, 65), ('2016-03-01', 3266, 92239, 20), ('2016-03-01', 3394, 67815, 40), ('2016-03-01', 3459, 59792, 10), ('2016-03-01', 3483, 56909, 95), ('2016-03-01', 3498, 
# 5026, 50), ('2016-03-01', 3507, 80744, 0), ('2016-03-01', 3517, 84441, 90), ('2016-03-01', 3518, 70115, 15), ('2016-03-01', 3560, 89737, 95), ('2016-03-01', 3565, 18050, 0), ('2016-03-01', 3580, 53295, 75), ('2016-03-01', 3584, 19516, 95), ('2016-03-01', 3588, 11587, 20), ('2016-03-01', 3595, 42225, 15), ('2016-03-01', 3603, 64790, 70), ('2016-03-01', 3682, 37492, 40), ('2016-03-01', 3688, 25226, 70), ('2016-03-01', 3706, 95648, 15), ('2016-03-01', 3784, 83913, 65), ('2016-03-01', 3786, 83968, 100), ('2016-03-01', 3845, 54045, 75), ('2016-03-01', 3891, 22750, 100), ('2016-03-01', 3939, 39091, 0), ('2016-03-01', 3941, 98981, 65), ('2016-03-01', 4005, 16014, 15), ('2016-03-01', 4009, 94251, 15), ('2016-03-01', 4016, 62640, 30), ('2016-03-01', 4081, 31247, 85), ('2016-03-01', 4133, 97530, 100), ('2016-03-01', 4184, 66648, 20), ('2016-03-01', 4270, 79278, 35), ('2016-03-01', 4303, 92654, 15), ('2016-03-01', 4451, 8878, 55), ('2016-03-01', 4523, 2697, 100), ('2016-03-01', 4533, 34294, 65), ('2016-03-01', 4575, 22467, 70), ('2016-03-01', 4598, 3124, 70), ('2016-03-01', 4624, 73695, 30), ('2016-03-01', 4651, 21743, 5), ('2016-03-01', 4683, 95335, 60), ('2016-03-01', 4748, 83371, 40), ('2016-03-01', 4798, 81314, 80), ('2016-03-01', 4921, 58141, 90), ('2016-03-01', 4952, 75233, 35), ('2016-03-01', 5003, 433, 25), ('2016-03-01', 5006, 77217, 75), ('2016-03-01', 5137, 43192, 100), ('2016-03-01', 5270, 78993, 60), ('2016-03-01', 5284, 81314, 35), ('2016-03-01', 5320, 53072, 25), ('2016-03-01', 5336, 6030, 70), ('2016-03-01', 5386, 79136, 25), ('2016-03-01', 5406, 57527, 55), ('2016-03-01', 5408, 31263, 15), ('2016-03-01', 5640, 41618, 20), ('2016-03-01', 5698, 22780, 45), ('2016-03-01', 5712, 88484, 30), ('2016-03-01', 5848, 63800, 60), ('2016-03-02', 5851, 650, 0), ('2016-03-02', 5970, 3162, 0), ('2016-03-02', 6171, 4413, 0), ('2016-03-02', 6191, 5478, 0), ('2016-03-02', 6395, 5509, 0), ('2016-03-02', 6464, 5990, 0), ('2016-03-02', 6559, 7460, 0), ('2016-03-02', 6588, 7865, 0), 
# ('2016-03-02', 6606, 7897, 0), ('2016-03-02', 6608, 7978, 0), ('2016-03-02', 6619, 8150, 0), ('2016-03-02', 6637, 9630, 0), ('2016-03-02', 6642, 11209, 0), ('2016-03-02', 6696, 12371, 0), ('2016-03-02', 6739, 12423, 0), ('2016-03-02', 6784, 19773, 0), ('2016-03-02', 6793, 19963, 0), ('2016-03-02', 6807, 20811, 0), ('2016-03-02', 6843, 20888, 0), ('2016-03-02', 6857, 21372, 0), ('2016-03-02', 6879, 22165, 0), ('2016-03-02', 6914, 22917, 0), ('2016-03-02', 6944, 22949, 0), ('2016-03-02', 6951, 24095, 0), ('2016-03-02', 7000, 24576, 0), ('2016-03-02', 7061, 26093, 0), ('2016-03-02', 7125, 26468, 0), ('2016-03-02', 7155, 27064, 0), ('2016-03-02', 7171, 30082, 0), ('2016-03-02', 7241, 32455, 0), ('2016-03-02', 7244, 33323, 0), ('2016-03-02', 7287, 33863, 0), ('2016-03-02', 7360, 34234, 0), ('2016-03-02', 7423, 34369, 0), ('2016-03-02', 7514, 36594, 0), ('2016-03-02', 7606, 37997, 0), ('2016-03-02', 7607, 38962, 0), 
# ('2016-03-02', 7756, 41057, 0), ('2016-03-02', 7787, 42973, 0), ('2016-03-02', 7902, 44791, 0), ('2016-03-02', 7906, 48490, 0), ('2016-03-02', 7924, 49340, 0), ('2016-03-02', 7989, 51132, 0), ('2016-03-02', 8097, 51548, 0), ('2016-03-02', 8151, 53342, 0), ('2016-03-02', 8311, 54113, 0), ('2016-03-02', 8413, 54408, 0), ('2016-03-02', 8437, 55374, 0), ('2016-03-02', 8440, 56707, 0), ('2016-03-02', 8491, 56978, 0), ('2016-03-02', 8579, 59818, 0), ('2016-03-02', 8604, 60355, 0), ('2016-03-02', 8622, 62333, 0), ('2016-03-02', 8656, 67479, 0), ('2016-03-02', 8677, 69799, 0), ('2016-03-02', 8773, 70302, 0), ('2016-03-02', 8829, 71848, 0), ('2016-03-02', 8842, 73849, 0), ('2016-03-02', 8901, 58932, 65), ('2016-03-02', 8944, 86429, 55), ('2016-03-02', 8972, 90959, 65), ('2016-03-02', 9068, 87230, 25), ('2016-03-02', 9092, 34840, 75), ('2016-03-02', 9122, 51726, 10), ('2016-03-02', 9228, 89780, 0), ('2016-03-02', 9267, 67735, 25), ('2016-03-02', 9277, 85501, 40), ('2016-03-02', 9368, 59761, 65), ('2016-03-02', 9389, 78408, 35), ('2016-03-02', 9403, 89781, 80), ('2016-03-02', 9406, 79101, 30), ('2016-03-02', 9408, 11092, 35), ('2016-03-02', 9419, 94083, 45), ('2016-03-02', 9472, 77184, 80), ('2016-03-02', 9503, 80394, 40), 
# ('2016-03-02', 9587, 11753, 90), ('2016-03-02', 9705, 97336, 10), ('2016-03-02', 9789, 1050, 85), ('2016-03-02', 9814, 50467, 60), ('2016-03-02', 9932, 83376, 55), ('2016-03-02', 9986, 69030, 10), ('2016-03-02', 9988, 95354, 75), ('2016-03-02', 10033, 60516, 65), ('2016-03-02', 10039, 81598, 15), ('2016-03-02', 10146, 66648, 95), ('2016-03-02', 10162, 62640, 85), ('2016-03-02', 10165, 98981, 0), ('2016-03-02', 10256, 49116, 70), ('2016-03-02', 10325, 99789, 
# 60), ('2016-03-02', 10345, 89781, 25), ('2016-03-02', 10352, 73967, 30), ('2016-03-02', 10506, 51134, 20), ('2016-03-02', 10519, 99789, 90), ('2016-03-02', 10524, 21973, 50), ('2016-03-02', 10526, 87230, 5), ('2016-03-02', 10586, 68071, 10), ('2016-03-02', 10596, 83913, 45), ('2016-03-02', 10620, 78002, 0), ('2016-03-02', 10653, 39091, 0), ('2016-03-02', 10669, 73967, 40), ('2016-03-02', 10784, 12303, 20), ('2016-03-02', 10814, 20033, 30), ('2016-03-02', 10860, 31822, 80), ('2016-03-02', 10866, 39091, 25), ('2016-03-02', 10887, 29719, 100), ('2016-03-02', 10902, 5333, 0), ('2016-03-02', 10915, 36691, 5), ('2016-03-02', 11001, 10068, 10), ('2016-03-02', 11048, 48592, 65), ('2016-03-02', 11082, 87555, 45), ('2016-03-02', 11292, 18941, 35), ('2016-03-02', 11373, 
# 36786, 55), ('2016-03-02', 11376, 21334, 60), ('2016-03-02', 11468, 98981, 35), ('2016-03-02', 11527, 20435, 90), ('2016-03-02', 11546, 8878, 60), ('2016-03-02', 11551, 95648, 10), ('2016-03-02', 11649, 98727, 75), ('2016-03-02', 11687, 73740, 0), ('2016-03-02', 11763, 87802, 10), ('2016-03-02', 11796, 32349, 40), ('2016-03-02', 11806, 66648, 30), ('2016-03-02', 11852, 533, 85), ('2016-03-02', 11859, 97530, 35), ('2016-03-02', 11880, 15225, 0), ('2016-03-02', 11890, 40093, 45), ('2016-03-02', 11901, 60516, 0), ('2016-03-02', 11942, 98981, 65), ('2016-03-02', 11960, 49008, 85), ('2016-03-02', 11994, 73115, 60), ('2016-03-02', 12002, 29047, 70), ('2016-03-02', 12014, 57448, 10), ('2016-03-02', 12033, 53295, 45), ('2016-03-02', 12059, 77749, 0), ('2016-03-02', 12151, 72783, 95), ('2016-03-02', 12211, 70115, 95), ('2016-03-02', 12304, 21973, 15), ('2016-03-02', 12318, 16932, 95), ('2016-03-02', 12422, 69030, 45), ('2016-03-02', 12454, 78408, 25), ('2016-03-02', 12472, 41558, 80), ('2016-03-02', 12476, 77490, 60), ('2016-03-02', 12477, 59446, 50), ('2016-03-02', 12503, 30845, 80), ('2016-03-02', 12513, 2764, 5), ('2016-03-02', 12523, 74021, 55), ('2016-03-02', 12537, 46328, 0), ('2016-03-02', 12602, 37187, 40), ('2016-03-02', 12679, 99169, 85), ('2016-03-02', 12776, 61280, 15), ('2016-03-02', 12856, 40147, 45), ('2016-03-02', 12875, 78205, 55), ('2016-03-02', 12883, 22013, 45), ('2016-03-02', 12908, 47174, 5), ('2016-03-02', 12920, 66014, 45), ('2016-03-02', 13066, 39091, 55), ('2016-03-02', 13133, 39857, 60), ('2016-03-03', 13148, 650, 0), ('2016-03-03', 13184, 3162, 0), ('2016-03-03', 13187, 4413, 0), ('2016-03-03', 13211, 5478, 0), ('2016-03-03', 13229, 5509, 0), ('2016-03-03', 13289, 5990, 0), ('2016-03-03', 13349, 7460, 0), ('2016-03-03', 13486, 7865, 0), ('2016-03-03', 13524, 7897, 0), ('2016-03-03', 13647, 7978, 0), ('2016-03-03', 13676, 8150, 0), ('2016-03-03', 13737, 9630, 0), ('2016-03-03', 13751, 11209, 0), ('2016-03-03', 13800, 12371, 0), ('2016-03-03', 13889, 
# 12423, 0), ('2016-03-03', 13905, 19773, 0), ('2016-03-03', 13918, 19963, 0), ('2016-03-03', 13952, 20811, 0), ('2016-03-03', 14164, 20888, 0), ('2016-03-03', 14186, 21372, 0), ('2016-03-03', 14245, 22165, 0), ('2016-03-03', 14308, 22917, 0), ('2016-03-03', 14387, 22949, 0), ('2016-03-03', 14391, 24095, 0), 
# ('2016-03-03', 14517, 24576, 0), ('2016-03-03', 14560, 26093, 0), ('2016-03-03', 14637, 26468, 0), ('2016-03-03', 14654, 27064, 0), ('2016-03-03', 14742, 
# 30082, 0), ('2016-03-03', 14749, 32455, 0), ('2016-03-03', 14760, 33323, 0), ('2016-03-03', 14813, 33863, 0), ('2016-03-03', 14821, 34234, 0), ('2016-03-03', 14914, 34369, 0), ('2016-03-03', 14961, 36594, 0), ('2016-03-03', 14965, 37997, 0), ('2016-03-03', 15048, 38962, 0), ('2016-03-03', 15329, 41057, 0), 
# ('2016-03-03', 15427, 42973, 0), ('2016-03-03', 15558, 44791, 0), ('2016-03-03', 15589, 48490, 0), ('2016-03-03', 15627, 49340, 0), ('2016-03-03', 15748, 
# 51132, 0), ('2016-03-03', 15763, 51548, 0), ('2016-03-03', 15839, 53342, 0), ('2016-03-03', 15913, 54113, 0), ('2016-03-03', 16025, 54408, 0), ('2016-03-03', 16051, 55374, 0), ('2016-03-03', 16223, 56707, 0), ('2016-03-03', 16248, 56978, 0), ('2016-03-03', 16249, 59818, 0), ('2016-03-03', 16322, 60355, 0), 
# ('2016-03-03', 16327, 62333, 0), ('2016-03-03', 16368, 67479, 0), ('2016-03-03', 16459, 69799, 0), ('2016-03-03', 16505, 70302, 0), ('2016-03-03', 16616, 
# 71848, 0), ('2016-03-03', 16680, 73849, 0), ('2016-03-03', 16794, 76080, 0), ('2016-03-03', 17028, 2697, 25), ('2016-03-03', 17081, 34840, 100), ('2016-03-03', 17188, 50467, 65), ('2016-03-03', 17346, 49116, 95), ('2016-03-03', 17382, 65113, 20), ('2016-03-03', 17385, 46518, 40), ('2016-03-03', 17392, 91573, 95), ('2016-03-03', 17423, 24725, 65), ('2016-03-03', 17480, 24725, 10), ('2016-03-03', 17598, 10985, 5), ('2016-03-03', 17661, 97336, 90), ('2016-03-03', 17726, 15039, 10), ('2016-03-03', 17801, 33142, 90), ('2016-03-03', 17817, 74861, 55), ('2016-03-03', 17830, 18105, 15), ('2016-03-03', 17839, 20594, 20), ('2016-03-03', 17959, 67735, 10), ('2016-03-03', 17967, 81598, 50), ('2016-03-03', 17970, 32540, 15), ('2016-03-03', 18051, 79278, 80), ('2016-03-03', 18157, 16014, 35), ('2016-03-03', 18197, 53808, 10), ('2016-03-03', 18363, 69706, 0), ('2016-03-03', 18389, 91573, 30), ('2016-03-03', 18482, 89991, 40), ('2016-03-03', 18522, 55343, 20), ('2016-03-03', 18583, 53295, 90), ('2016-03-03', 18697, 90401, 55), ('2016-03-03', 18819, 70287, 75), ('2016-03-03', 18834, 78002, 0), ('2016-03-03', 18864, 80682, 40), ('2016-03-03', 18995, 78408, 85), ('2016-03-03', 19012, 46870, 90), ('2016-03-03', 19039, 12852, 10), ('2016-03-03', 19056, 29719, 50), ('2016-03-03', 19283, 74568, 15), ('2016-03-03', 19291, 56909, 60), ('2016-03-03', 19440, 21657, 40), ('2016-03-03', 19448, 21743, 70), ('2016-03-03', 19501, 42368, 100), ('2016-03-03', 19564, 31247, 50), ('2016-03-03', 19569, 43604, 30), ('2016-03-03', 19578, 72237, 55), ('2016-03-03', 19668, 17482, 100), ('2016-03-03', 19705, 89164, 50), ('2016-03-03', 19758, 75908, 50), ('2016-03-03', 19835, 50910, 20), ('2016-03-03', 19911, 86429, 20), ('2016-03-03', 19952, 8878, 75), ('2016-03-03', 20007, 18105, 60), ('2016-03-03', 20073, 83263, 15), ('2016-03-03', 20130, 25398, 90), ('2016-03-03', 20295, 73740, 95), ('2016-03-03', 20298, 86065, 70), ('2016-03-03', 20337, 79480, 0), ('2016-03-03', 20388, 87555, 15), ('2016-03-03', 20464, 10068, 55), ('2016-03-03', 20486, 59761, 50), ('2016-03-03', 20567, 95958, 30), ('2016-03-03', 20590, 31822, 10), ('2016-03-03', 20609, 16932, 60), ('2016-03-03', 20620, 12707, 50), ('2016-03-03', 20664, 82956, 45), ('2016-03-03', 20784, 59761, 60), ('2016-03-03', 20945, 95647, 75), ('2016-03-03', 21185, 75889, 45), ('2016-03-03', 21209, 45630, 65), ('2016-03-03', 21210, 80682, 0), ('2016-03-04', 21226, 650, 0), ('2016-03-04', 21229, 3162, 0), ('2016-03-04', 21445, 4413, 0), ('2016-03-04', 21482, 5478, 0), ('2016-03-04', 21492, 5509, 0), ('2016-03-04', 21497, 5990, 0), ('2016-03-04', 21526, 7460, 0), ('2016-03-04', 21703, 7865, 0), ('2016-03-04', 21756, 7897, 0), ('2016-03-04', 21781, 7978, 0), ('2016-03-04', 21812, 8150, 0), ('2016-03-04', 21973, 9630, 0), ('2016-03-04', 22008, 11209, 0), ('2016-03-04', 22035, 12371, 0), ('2016-03-04', 22148, 12423, 0), ('2016-03-04', 22150, 19773, 0), ('2016-03-04', 22169, 19963, 0), ('2016-03-04', 22212, 20811, 0), ('2016-03-04', 22313, 20888, 0), ('2016-03-04', 22407, 21372, 0), ('2016-03-04', 22456, 22165, 0), ('2016-03-04', 
# 22474, 22917, 0), ('2016-03-04', 22485, 22949, 0), ('2016-03-04', 22554, 24095, 0), ('2016-03-04', 22588, 24576, 0), ('2016-03-04', 22645, 26093, 0), ('2016-03-04', 22650, 26468, 0), ('2016-03-04', 22743, 27064, 0), ('2016-03-04', 22745, 30082, 0), ('2016-03-04', 22792, 32455, 0), ('2016-03-04', 22811, 33323, 0), ('2016-03-04', 22833, 33863, 0), ('2016-03-04', 22873, 34234, 0), ('2016-03-04', 23098, 34369, 0), ('2016-03-04', 23142, 36594, 0), ('2016-03-04', 
# 23211, 37997, 0), ('2016-03-04', 23282, 38962, 0), ('2016-03-04', 23316, 41057, 0), ('2016-03-04', 23365, 42973, 0), ('2016-03-04', 23369, 44791, 0), ('2016-03-04', 23476, 48490, 0), ('2016-03-04', 23501, 49340, 0), ('2016-03-04', 23508, 51132, 0), ('2016-03-04', 23527, 51548, 0), ('2016-03-04', 23528, 53342, 0), ('2016-03-04', 23541, 54113, 0), ('2016-03-04', 23544, 54408, 0), ('2016-03-04', 23596, 55374, 0), ('2016-03-04', 23671, 56707, 0), ('2016-03-04', 
# 23676, 56978, 0), ('2016-03-04', 23682, 64609, 45), ('2016-03-04', 23732, 13923, 15), ('2016-03-04', 23834, 51572, 100), ('2016-03-04', 23869, 40816, 40), ('2016-03-04', 23927, 49116, 70), ('2016-03-04', 23932, 75635, 75), ('2016-03-04', 23993, 41336, 35), ('2016-03-04', 24066, 24725, 30), ('2016-03-04', 24071, 36654, 70), ('2016-03-04', 24098, 95183, 15), ('2016-03-04', 24102, 78408, 50), ('2016-03-04', 24166, 31151, 20), ('2016-03-04', 24198, 89737, 0), ('2016-03-04', 24243, 89780, 5), ('2016-03-04', 24253, 15039, 5), ('2016-03-04', 24267, 7336, 80), ('2016-03-04', 24283, 13733, 95), ('2016-03-04', 24413, 59446, 45), ('2016-03-04', 24503, 41457, 65), ('2016-03-04', 24585, 533, 0), ('2016-03-04', 24834, 1240, 60), ('2016-03-04', 24996, 16932, 70), ('2016-03-04', 25007, 80094, 35), ('2016-03-04', 25011, 77217, 80), ('2016-03-04', 25154, 61793, 85), ('2016-03-04', 25156, 69660, 55), ('2016-03-04', 25285, 31263, 
# 20), ('2016-03-04', 25301, 30061, 60), ('2016-03-04', 25312, 77217, 15), ('2016-03-04', 25408, 47174, 70), ('2016-03-04', 25444, 21152, 15), ('2016-03-04', 25476, 73716, 80), ('2016-03-04', 25552, 19516, 80), ('2016-03-04', 25593, 53548, 10), ('2016-03-04', 25735, 21334, 70), ('2016-03-04', 25744, 90612, 0), ('2016-03-04', 25755, 29719, 95), ('2016-03-04', 25781, 69928, 5), ('2016-03-04', 25799, 93664, 50), ('2016-03-04', 25830, 72721, 100), ('2016-03-04', 25906, 37492, 25), ('2016-03-04', 25939, 16257, 100), ('2016-03-04', 25972, 62640, 40), ('2016-03-04', 26020, 80580, 85), ('2016-03-04', 26023, 86845, 35), ('2016-03-04', 26126, 84307, 65), ('2016-03-04', 26133, 70287, 40), ('2016-03-04', 26146, 90531, 20), ('2016-03-04', 26147, 39831, 60), ('2016-03-04', 26202, 11092, 20), ('2016-03-04', 26645, 19904, 40), ('2016-03-04', 26741, 42573, 25), ('2016-03-04', 26781, 15225, 10), ('2016-03-04', 26786, 50910, 10), ('2016-03-04', 26795, 79136, 90), ('2016-03-04', 26818, 7891, 0), ('2016-03-04', 26839, 81314, 25), ('2016-03-04', 26850, 59943, 85), ('2016-03-04', 26908, 28201, 80), ('2016-03-04', 26958, 80744, 95), ('2016-03-04', 26967, 533, 15), ('2016-03-04', 27030, 93361, 10), ('2016-03-04', 27073, 14737, 35), ('2016-03-04', 27106, 85006, 10), ('2016-03-04', 27128, 36562, 55), ('2016-03-04', 27149, 40093, 85), ('2016-03-04', 27262, 50467, 20), ('2016-03-04', 27314, 69706, 45), ('2016-03-04', 27334, 30845, 65), ('2016-03-04', 27403, 73374, 75), ('2016-03-04', 27552, 66014, 30), ('2016-03-04', 27566, 63715, 85), ('2016-03-04', 27627, 12707, 55), ('2016-03-04', 27673, 54807, 25), ('2016-03-04', 27726, 82956, 60), ('2016-03-04', 27727, 42368, 75), ('2016-03-04', 27822, 47258, 75), ('2016-03-04', 27889, 72783, 95), ('2016-03-04', 27906, 78408, 5), ('2016-03-04', 27955, 80682, 0), ('2016-03-04', 27972, 81511, 90), ('2016-03-04', 27990, 14737, 25), ('2016-03-04', 28008, 72783, 90), ('2016-03-04', 28018, 24420, 80), ('2016-03-04', 28040, 95648, 20), ('2016-03-04', 28042, 19540, 60), ('2016-03-04', 28043, 25226, 90), ('2016-03-04', 28066, 10985, 85), ('2016-03-04', 28120, 44598, 50), ('2016-03-04', 28178, 30845, 35), ('2016-03-04', 
# 28189, 44397, 30), ('2016-03-04', 28215, 6508, 90), ('2016-03-05', 28276, 650, 0), ('2016-03-05', 28277, 3162, 0), ('2016-03-05', 28308, 4413, 0), ('2016-03-05', 28368, 5478, 0), ('2016-03-05', 28404, 5509, 0), ('2016-03-05', 28444, 5990, 0), ('2016-03-05', 28471, 7460, 0), ('2016-03-05', 28493, 7865, 0), ('2016-03-05', 28496, 7897, 0), ('2016-03-05', 28526, 7978, 0), ('2016-03-05', 28627, 8150, 0), ('2016-03-05', 28652, 9630, 0), ('2016-03-05', 28772, 11209, 0), ('2016-03-05', 28790, 12371, 0), ('2016-03-05', 28792, 12423, 0), ('2016-03-05', 28795, 19773, 0), ('2016-03-05', 28919, 19963, 0), ('2016-03-05', 28938, 20811, 0), ('2016-03-05', 29096, 20888, 0), ('2016-03-05', 29100, 21372, 0), ('2016-03-05', 29117, 22165, 0), ('2016-03-05', 29180, 22917, 0), ('2016-03-05', 29230, 22949, 0), ('2016-03-05', 29301, 24095, 0), ('2016-03-05', 29376, 24576, 0), ('2016-03-05', 29400, 26093, 0), ('2016-03-05', 29414, 26468, 0), ('2016-03-05', 29419, 27064, 0), ('2016-03-05', 29490, 30082, 0), ('2016-03-05', 29548, 32455, 0), ('2016-03-05', 29581, 33323, 0), ('2016-03-05', 29608, 33863, 0), ('2016-03-05', 29629, 34234, 0), ('2016-03-05', 29759, 34369, 0), ('2016-03-05', 29785, 36594, 0), ('2016-03-05', 29804, 37997, 0), ('2016-03-05', 29829, 38962, 0), ('2016-03-05', 29834, 41057, 0), ('2016-03-05', 29889, 42973, 0), ('2016-03-05', 29905, 44791, 0), ('2016-03-05', 29940, 48490, 0), ('2016-03-05', 29944, 49340, 0), ('2016-03-05', 29992, 51132, 0), ('2016-03-05', 29993, 51548, 0), ('2016-03-05', 29997, 53342, 0), ('2016-03-05', 30120, 54113, 0), ('2016-03-05', 30125, 54408, 0), ('2016-03-05', 30128, 55374, 0), ('2016-03-05', 30150, 56707, 0), ('2016-03-05', 30289, 56978, 0), ('2016-03-05', 30311, 59818, 0), ('2016-03-05', 30313, 60355, 0), ('2016-03-05', 30340, 62333, 0), ('2016-03-05', 30440, 67479, 0), ('2016-03-05', 30443, 69799, 0), ('2016-03-05', 30490, 70302, 0), ('2016-03-05', 30544, 71848, 0), ('2016-03-05', 30654, 73849, 0), ('2016-03-05', 30680, 76080, 0), ('2016-03-05', 30718, 77963, 0), ('2016-03-05', 30832, 79449, 0), ('2016-03-05', 30871, 80214, 0), ('2016-03-05', 30910, 83245, 0), ('2016-03-05', 31033, 83772, 0), ('2016-03-05', 31107, 86195, 0), ('2016-03-05', 31118, 86284, 0), ('2016-03-05', 31152, 88706, 0), ('2016-03-05', 31206, 40093, 55), ('2016-03-05', 31302, 90612, 50), ('2016-03-05', 31328, 7891, 10), ('2016-03-05', 31372, 68071, 75), ('2016-03-05', 31398, 40093, 50), ('2016-03-05', 31401, 20574, 85), ('2016-03-05', 31414, 39091, 70), ('2016-03-05', 31420, 16932, 55), ('2016-03-05', 31496, 53808, 20), ('2016-03-05', 31550, 44690, 0), ('2016-03-05', 31588, 1050, 75), ('2016-03-05', 31637, 73426, 20), ('2016-03-05', 31703, 86065, 30), ('2016-03-05', 31761, 14113, 5), ('2016-03-05', 31807, 67735, 30), ('2016-03-05', 31874, 80648, 10), ('2016-03-05', 31935, 77490, 60), ('2016-03-05', 32094, 50503, 5), ('2016-03-05', 32104, 46518, 20), ('2016-03-05', 32207, 13224, 10), ('2016-03-05', 32214, 73115, 50), ('2016-03-05', 32217, 13391, 25), ('2016-03-05', 32267, 15054, 75), ('2016-03-05', 32325, 44214, 35), ('2016-03-05', 32342, 41558, 60), ('2016-03-05', 32429, 597, 60), ('2016-03-05', 32464, 83643, 85), ('2016-03-05', 32521, 99169, 55), ('2016-03-05', 32550, 83643, 100), ('2016-03-05', 32564, 79, 60), ('2016-03-05', 32570, 54045, 35), ('2016-03-05', 32583, 81186, 45), ('2016-03-05', 32590, 57572, 70), ('2016-03-05', 32658, 97530, 50), ('2016-03-05', 32761, 41336, 30), ('2016-03-05', 32826, 83371, 90), ('2016-03-05', 32835, 90612, 30), ('2016-03-05', 32852, 89814, 5), ('2016-03-05', 32875, 20574, 25), ('2016-03-05', 32985, 91573, 50), ('2016-03-05', 32986, 31822, 55), ('2016-03-05', 32996, 31822, 20), ('2016-03-05', 33079, 43604, 85), ('2016-03-05', 33143, 30845, 20), ('2016-03-05', 33159, 16700, 45), ('2016-03-05', 33162, 40816, 50), ('2016-03-05', 33169, 19904, 70), ('2016-03-05', 33317, 39441, 10), ('2016-03-05', 33343, 50874, 100), ('2016-03-05', 33362, 57572, 65), ('2016-03-05', 33433, 32710, 15), ('2016-03-05', 33437, 75635, 
# 30), ('2016-03-05', 33517, 7891, 5), ('2016-03-05', 33538, 88484, 65), ('2016-03-05', 33551, 92654, 85), ('2016-03-05', 33556, 66702, 75), ('2016-03-05', 
# 33570, 40816, 55), ('2016-03-05', 33576, 5327, 90), ('2016-03-05', 33684, 60517, 25), ('2016-03-05', 33708, 20033, 50), ('2016-03-05', 33765, 49116, 95), 
# ('2016-03-05', 33939, 5026, 30), ('2016-03-05', 33952, 71152, 55), ('2016-03-05', 33967, 62640, 50), ('2016-03-05', 33993, 93361, 10), ('2016-03-05', 34134, 35492, 25), ('2016-03-05', 34145, 68071, 20), ('2016-03-05', 34148, 26701, 60), ('2016-03-05', 34150, 34840, 95), ('2016-03-05', 34164, 48592, 65), ('2016-03-05', 34227, 73967, 30), ('2016-03-05', 34282, 34794, 15), ('2016-03-05', 34293, 73374, 40), ('2016-03-05', 34388, 81314, 15), ('2016-03-05', 34389, 79480, 90), ('2016-03-05', 34410, 83376, 75), ('2016-03-05', 34419, 36691, 95), ('2016-03-05', 34425, 73716, 60), ('2016-03-05', 34558, 44690, 0), ('2016-03-05', 34657, 6259, 40), ('2016-03-05', 34683, 11753, 5), ('2016-03-05', 34854, 6508, 20), ('2016-03-05', 34984, 56107, 50), ('2016-03-05', 35070, 3124, 40), ('2016-03-05', 35167, 11753, 45), ('2016-03-05', 35184, 13733, 80), ('2016-03-05', 35195, 99789, 45), ('2016-03-05', 35221, 50910, 70), ('2016-03-06', 35252, 650, 0), ('2016-03-06', 35293, 3162, 0), ('2016-03-06', 35300, 4413, 0), ('2016-03-06', 35310, 5478, 0), ('2016-03-06', 35341, 5509, 0), ('2016-03-06', 35370, 5990, 0), ('2016-03-06', 35376, 7460, 0), ('2016-03-06', 35429, 7865, 0), ('2016-03-06', 35497, 7897, 0), ('2016-03-06', 35530, 7978, 0), ('2016-03-06', 35569, 8150, 0), ('2016-03-06', 35740, 9630, 0), ('2016-03-06', 35744, 11209, 0), ('2016-03-06', 35787, 12371, 0), ('2016-03-06', 35878, 12423, 0), ('2016-03-06', 35937, 19773, 0), ('2016-03-06', 35990, 19963, 0), ('2016-03-06', 36080, 20811, 0), ('2016-03-06', 36152, 20888, 0), ('2016-03-06', 36181, 21372, 0), ('2016-03-06', 36187, 22165, 0), ('2016-03-06', 36279, 22917, 0), ('2016-03-06', 36317, 22949, 0), ('2016-03-06', 36349, 24095, 0), ('2016-03-06', 36494, 24576, 0), ('2016-03-06', 36561, 26093, 0), ('2016-03-06', 36707, 26468, 0), ('2016-03-06', 36736, 27064, 0), ('2016-03-06', 36783, 30082, 0), ('2016-03-06', 36821, 32455, 0), ('2016-03-06', 36852, 33323, 0), ('2016-03-06', 36890, 33863, 0), ('2016-03-06', 37032, 34234, 0), ('2016-03-06', 37120, 34369, 0), ('2016-03-06', 37134, 36594, 0), ('2016-03-06', 37164, 37997, 0), ('2016-03-06', 37220, 38962, 0), ('2016-03-06', 37223, 41057, 0), ('2016-03-06', 37231, 42973, 0), ('2016-03-06', 37269, 44791, 0), ('2016-03-06', 37315, 48490, 0), ('2016-03-06', 37540, 49340, 0), ('2016-03-06', 37581, 51132, 0), ('2016-03-06', 37615, 51548, 0), ('2016-03-06', 37629, 53342, 0), ('2016-03-06', 37670, 54113, 0), ('2016-03-06', 37678, 54408, 0), ('2016-03-06', 37692, 55374, 0), ('2016-03-06', 37721, 56707, 0), ('2016-03-06', 37799, 56978, 0), ('2016-03-06', 37804, 59818, 0), ('2016-03-06', 37838, 60355, 0), ('2016-03-06', 37848, 62333, 0), ('2016-03-06', 37885, 67479, 0), ('2016-03-06', 37948, 69799, 0), ('2016-03-06', 38011, 70302, 0), ('2016-03-06', 38029, 71848, 0), ('2016-03-06', 38051, 73849, 0), ('2016-03-06', 38057, 76080, 0), ('2016-03-06', 38075, 84307, 25), ('2016-03-06', 38088, 43604, 90), ('2016-03-06', 38139, 95934, 95), ('2016-03-06', 38175, 90959, 100), ('2016-03-06', 38186, 95335, 100), ('2016-03-06', 38215, 5327, 65), ('2016-03-06', 38231, 93764, 
# 95), ('2016-03-06', 38234, 93494, 35), ('2016-03-06', 38243, 3222, 0), ('2016-03-06', 38315, 41618, 0), ('2016-03-06', 38320, 66627, 55), ('2016-03-06', 38332, 27789, 80), ('2016-03-06', 38394, 72783, 5), ('2016-03-06', 38407, 75908, 80), ('2016-03-06', 38416, 57572, 95), ('2016-03-06', 38601, 94083, 25), ('2016-03-06', 38605, 8894, 60), ('2016-03-06', 38651, 47258, 100), ('2016-03-06', 38764, 8894, 100), ('2016-03-06', 38786, 54967, 20), ('2016-03-06', 38789, 85948, 40), ('2016-03-06', 38823, 3018, 30), ('2016-03-06', 38858, 75635, 85), ('2016-03-06', 38941, 13733, 40), ('2016-03-06', 38954, 84307, 20), ('2016-03-06', 39010, 2345, 100), ('2016-03-06', 39045, 84254, 80), ('2016-03-06', 39062, 20594, 80), ('2016-03-06', 39068, 16700, 90), ('2016-03-06', 39079, 
# 29445, 20), ('2016-03-06', 39106, 73426, 0), ('2016-03-06', 39115, 20435, 75), ('2016-03-06', 39123, 42115, 90), ('2016-03-06', 39124, 75233, 95), ('2016-03-06', 39170, 83669, 30), ('2016-03-06', 39194, 15039, 100), ('2016-03-06', 39347, 72783, 35), ('2016-03-06', 39413, 84307, 80), ('2016-03-06', 39441, 15999, 60), ('2016-03-06', 39468, 81064, 100), ('2016-03-06', 39500, 87277, 75), ('2016-03-06', 39545, 19736, 40), ('2016-03-06', 39551, 18317, 75), ('2016-03-06', 39564, 98981, 0), ('2016-03-06', 39599, 58141, 30), ('2016-03-06', 39622, 68435, 100), ('2016-03-06', 39623, 50503, 40), ('2016-03-06', 39745, 69101, 0), ('2016-03-06', 39786, 84307, 90), ('2016-03-06', 39836, 15225, 65), ('2016-03-06', 40009, 10629, 20), ('2016-03-06', 40034, 36786, 40), ('2016-03-06', 40061, 94104, 85), ('2016-03-06', 40063, 15498, 30), ('2016-03-06', 40168, 24725, 45), ('2016-03-06', 40191, 86065, 35), ('2016-03-06', 40248, 68071, 85), ('2016-03-06', 40280, 23794, 20), ('2016-03-06', 40358, 22013, 5), ('2016-03-06', 40488, 10985, 0), ('2016-03-06', 40506, 74021, 85), ('2016-03-06', 40567, 40816, 85), ('2016-03-06', 40608, 31618, 90), ('2016-03-06', 40631, 18050, 5), ('2016-03-06', 40674, 78143, 5), ('2016-03-06', 40706, 597, 65), ('2016-03-06', 40710, 27725, 85), ('2016-03-06', 40839, 90030, 75), ('2016-03-06', 40899, 89737, 60), ('2016-03-06', 40907, 40816, 55), ('2016-03-06', 40951, 75635, 65), ('2016-03-06', 40970, 37492, 15), ('2016-03-06', 41012, 46870, 70), ('2016-03-06', 41041, 75635, 30), ('2016-03-06', 41137, 73374, 90), ('2016-03-06', 41296, 15158, 40), ('2016-03-06', 41374, 62325, 85), ('2016-03-06', 41496, 15225, 60), ('2016-03-06', 41508, 94104, 55), ('2016-03-06', 41524, 
# 51775, 85), ('2016-03-06', 41551, 6508, 90), ('2016-03-06', 41677, 85948, 35), ('2016-03-06', 41754, 70287, 25), ('2016-03-06', 41801, 8878, 35), ('2016-03-06', 41808, 33245, 80), ('2016-03-06', 41809, 24725, 55), ('2016-03-06', 41820, 14826, 25), ('2016-03-06', 41827, 94083, 75), ('2016-03-06', 41859, 19761, 60), ('2016-03-06', 41959, 68435, 95), ('2016-03-06', 41966, 31151, 100), ('2016-03-06', 42002, 79278, 75), ('2016-03-06', 42027, 59761, 80), ('2016-03-06', 42091, 65875, 40), ('2016-03-06', 42115, 21743, 100), ('2016-03-06', 42150, 46870, 80), ('2016-03-07', 42153, 650, 0), ('2016-03-07', 42296, 3162, 0), ('2016-03-07', 42341, 4413, 0), ('2016-03-07', 42365, 5478, 0), ('2016-03-07', 42390, 5509, 0), ('2016-03-07', 42481, 5990, 0), ('2016-03-07', 42484, 7460, 0), ('2016-03-07', 42500, 7865, 0), ('2016-03-07', 42545, 7897, 0), ('2016-03-07', 42600, 7978, 0), ('2016-03-07', 42652, 8150, 0), ('2016-03-07', 42726, 9630, 0), ('2016-03-07', 42772, 11209, 0), ('2016-03-07', 42840, 12371, 0), ('2016-03-07', 42851, 12423, 0), ('2016-03-07', 42925, 19773, 0), ('2016-03-07', 42948, 19963, 0), ('2016-03-07', 43014, 20811, 0), ('2016-03-07', 43021, 20888, 0), ('2016-03-07', 43050, 21372, 0), ('2016-03-07', 43107, 22165, 
# 0), ('2016-03-07', 43124, 22917, 0), ('2016-03-07', 43194, 22949, 0), ('2016-03-07', 43208, 24095, 0), ('2016-03-07', 43292, 24576, 0), ('2016-03-07', 43374, 26093, 0), ('2016-03-07', 43396, 26468, 0), ('2016-03-07', 43504, 27064, 0), ('2016-03-07', 43554, 30082, 0), ('2016-03-07', 43619, 32455, 0), ('2016-03-07', 43624, 33323, 0), ('2016-03-07', 43627, 33863, 0), ('2016-03-07', 43630, 34234, 0), ('2016-03-07', 43634, 34369, 0), ('2016-03-07', 43710, 36594, 
# 0), ('2016-03-07', 43740, 39857, 85), ('2016-03-07', 43759, 64823, 100), ('2016-03-07', 43787, 73740, 75), ('2016-03-07', 43805, 57824, 70), ('2016-03-07', 43939, 98835, 10), ('2016-03-07', 43953, 13391, 85), ('2016-03-07', 44003, 18105, 80), ('2016-03-07', 44068, 80682, 50), ('2016-03-07', 44073, 64790, 70), ('2016-03-07', 44081, 54899, 60), ('2016-03-07', 44193, 39434, 30), ('2016-03-07', 44196, 64823, 60), ('2016-03-07', 44208, 21219, 75), ('2016-03-07', 
# 44307, 80682, 5), ('2016-03-07', 44322, 80682, 10), ('2016-03-07', 44354, 36654, 25), ('2016-03-07', 44534, 51775, 85), ('2016-03-07', 44580, 94083, 85), 
# ('2016-03-07', 44588, 90030, 25), ('2016-03-07', 44723, 77749, 90), ('2016-03-07', 44773, 95354, 70), ('2016-03-07', 44786, 55343, 15), ('2016-03-07', 44820, 73716, 10), ('2016-03-07', 44876, 81242, 90), ('2016-03-07', 44944, 14113, 5), ('2016-03-07', 44950, 39831, 0), ('2016-03-07', 44962, 87555, 90), ('2016-03-07', 44977, 62640, 30), ('2016-03-07', 44990, 88484, 0), ('2016-03-07', 45042, 44217, 35), ('2016-03-07', 45098, 83371, 15), ('2016-03-07', 45144, 14826, 35), ('2016-03-07', 45276, 99789, 35), ('2016-03-07', 45369, 99169, 55), ('2016-03-07', 45482, 81186, 30), ('2016-03-07', 45516, 68845, 0), ('2016-03-07', 45614, 69149, 50), ('2016-03-07', 45655, 80682, 5), ('2016-03-07', 45688, 9198, 35), ('2016-03-07', 45708, 53940, 30), ('2016-03-07', 45766, 3018, 
# 20), ('2016-03-07', 45794, 30061, 90), ('2016-03-07', 45865, 34294, 50), ('2016-03-07', 45891, 2820, 40), ('2016-03-07', 45899, 98780, 80), ('2016-03-07', 45950, 84640, 50), ('2016-03-07', 45951, 20435, 50), ('2016-03-07', 46042, 54807, 60), ('2016-03-07', 46069, 62078, 25), ('2016-03-07', 46115, 31247, 90), ('2016-03-07', 46163, 31221, 0), ('2016-03-07', 46169, 16747, 10), ('2016-03-07', 46253, 80902, 55), ('2016-03-07', 46305, 53940, 45), ('2016-03-07', 46335, 70689, 50), ('2016-03-07', 46372, 42672, 75), ('2016-03-07', 46398, 89991, 60), ('2016-03-07', 46412, 14737, 65), ('2016-03-07', 46424, 56107, 60), ('2016-03-07', 46458, 1240, 95), ('2016-03-07', 46566, 78993, 45), ('2016-03-07', 46569, 61010, 75), ('2016-03-07', 46576, 73716, 85), ('2016-03-07', 46606, 533, 55), ('2016-03-07', 46673, 79480, 70), ('2016-03-07', 46711, 7891, 50), ('2016-03-07', 46809, 30073, 65), ('2016-03-07', 46811, 41558, 85), ('2016-03-07', 46832, 99149, 20), ('2016-03-07', 46956, 30061, 20), ('2016-03-07', 47361, 98727, 80), ('2016-03-07', 47458, 95647, 70), ('2016-03-07', 47515, 6775, 20), ('2016-03-07', 47520, 62078, 85), ('2016-03-08', 47557, 650, 0), ('2016-03-08', 47585, 3162, 0), ('2016-03-08', 47676, 4413, 0), ('2016-03-08', 47706, 5478, 0), ('2016-03-08', 47733, 5509, 0), ('2016-03-08', 47870, 5990, 0), ('2016-03-08', 47892, 7460, 0), ('2016-03-08', 47908, 7865, 0), ('2016-03-08', 47968, 7897, 0), ('2016-03-08', 47976, 7978, 0), ('2016-03-08', 48048, 8150, 0), ('2016-03-08', 48051, 9630, 0), ('2016-03-08', 48152, 11209, 0), ('2016-03-08', 48159, 12371, 0), ('2016-03-08', 48241, 12423, 0), ('2016-03-08', 48257, 19773, 0), ('2016-03-08', 48476, 19963, 0), ('2016-03-08', 48524, 20811, 0), ('2016-03-08', 48591, 20888, 0), ('2016-03-08', 48679, 21372, 0), ('2016-03-08', 48791, 22165, 0), ('2016-03-08', 48822, 22917, 0), ('2016-03-08', 
# 48863, 22949, 0), ('2016-03-08', 48877, 24095, 0), ('2016-03-08', 48897, 24576, 0), ('2016-03-08', 48914, 26093, 0), ('2016-03-08', 48928, 26468, 0), ('2016-03-08', 49029, 27064, 0), ('2016-03-08', 49069, 30082, 0), ('2016-03-08', 49132, 32455, 0), ('2016-03-08', 49189, 33323, 0), ('2016-03-08', 49210, 33863, 0), ('2016-03-08', 49234, 34234, 0), ('2016-03-08', 49277, 34369, 0), ('2016-03-08', 49297, 36594, 0), ('2016-03-08', 49393, 37997, 0), ('2016-03-08', 
# 49485, 38962, 0), ('2016-03-08', 49522, 41057, 0), ('2016-03-08', 49567, 42973, 0), ('2016-03-08', 49592, 44791, 0), ('2016-03-08', 49629, 48490, 0), ('2016-03-08', 49778, 49340, 0), ('2016-03-08', 49938, 51132, 0), ('2016-03-08', 49960, 51548, 0), ('2016-03-08', 49965, 53342, 0), ('2016-03-08', 50010, 54113, 0), ('2016-03-08', 50029, 54408, 0), ('2016-03-08', 50060, 55374, 0), ('2016-03-08', 50062, 56707, 0), ('2016-03-08', 50081, 56978, 0), ('2016-03-08', 
# 50145, 59818, 0), ('2016-03-08', 50186, 60355, 0), ('2016-03-08', 50288, 62333, 0), ('2016-03-08', 50310, 67479, 0), ('2016-03-08', 50329, 69799, 0), ('2016-03-08', 50603, 70302, 0), ('2016-03-08', 50747, 71848, 0), ('2016-03-08', 50767, 73849, 0), ('2016-03-08', 50955, 76080, 0), ('2016-03-08', 50973, 77963, 0), ('2016-03-08', 50977, 79449, 0), ('2016-03-08', 51061, 80214, 0), ('2016-03-08', 51093, 83245, 0), ('2016-03-08', 51181, 83772, 0), ('2016-03-08', 
# 51244, 86195, 0), ('2016-03-08', 51328, 86284, 0), ('2016-03-08', 51447, 88706, 0), ('2016-03-08', 51448, 89638, 0), ('2016-03-08', 51463, 90236, 0), ('2016-03-08', 51544, 89781, 70), ('2016-03-08', 51586, 46518, 15), ('2016-03-08', 51599, 90959, 45), ('2016-03-08', 51614, 54899, 30), ('2016-03-08', 51626, 
# 32710, 30), ('2016-03-08', 51685, 16530, 55), ('2016-03-08', 51858, 81492, 50), ('2016-03-08', 51915, 91095, 65), ('2016-03-08', 52067, 3374, 80), ('2016-03-08', 52154, 16014, 10), ('2016-03-08', 52287, 42368, 70), ('2016-03-08', 52292, 10985, 45), ('2016-03-08', 52391, 84640, 40), ('2016-03-08', 52432, 2873, 55), ('2016-03-08', 52473, 89737, 25), ('2016-03-08', 52511, 55343, 60), ('2016-03-08', 52518, 27725, 5), ('2016-03-08', 52528, 16234, 55), ('2016-03-08', 52537, 39857, 95), ('2016-03-08', 52556, 57527, 70), ('2016-03-08', 52647, 13901, 35), ('2016-03-08', 52676, 31822, 50), ('2016-03-08', 52686, 20604, 
# 5), ('2016-03-08', 52696, 45630, 100), ('2016-03-08', 52800, 50503, 85), ('2016-03-08', 52802, 95928, 80), ('2016-03-08', 52810, 83371, 60), ('2016-03-08', 52908, 42573, 85), ('2016-03-08', 52916, 54180, 95), ('2016-03-08', 52985, 83509, 30), ('2016-03-08', 53059, 99149, 35), ('2016-03-08', 53155, 61816, 50), ('2016-03-08', 53247, 55050, 40), ('2016-03-08', 53265, 11092, 65), ('2016-03-08', 53297, 73695, 50), ('2016-03-08', 53302, 86429, 60), ('2016-03-08', 
# 53323, 22750, 0), ('2016-03-08', 53388, 39091, 60), ('2016-03-08', 53424, 49008, 55), ('2016-03-08', 53426, 18003, 15), ('2016-03-08', 53441, 22780, 55), 
# ('2016-03-08', 53515, 43604, 90), ('2016-03-08', 53533, 81186, 80), ('2016-03-08', 53779, 98981, 0), ('2016-03-08', 53835, 80902, 5), ('2016-03-08', 53932, 77490, 25), ('2016-03-08', 53945, 54180, 55), ('2016-03-08', 53952, 6030, 60), ('2016-03-08', 54019, 44690, 80), ('2016-03-08', 54093, 62325, 25), ('2016-03-08', 54139, 85948, 25), ('2016-03-08', 54177, 19552, 60), ('2016-03-08', 54281, 10985, 90), ('2016-03-08', 54326, 40266, 85), ('2016-03-08', 54329, 21657, 50), ('2016-03-08', 54344, 84254, 100), ('2016-03-08', 54425, 74763, 20), ('2016-03-08', 54571, 77184, 25), ('2016-03-08', 54591, 66648, 55), ('2016-03-08', 54642, 94251, 30), ('2016-03-08', 54651, 18497, 90), ('2016-03-08', 54666, 73470, 30), ('2016-03-08', 54784, 7891, 25), ('2016-03-08', 54789, 1240, 55), ('2016-03-08', 54918, 9643, 95), ('2016-03-08', 54956, 73716, 25), ('2016-03-08', 54973, 69660, 85), ('2016-03-08', 55110, 18105, 85), ('2016-03-08', 55121, 68566, 80), ('2016-03-08', 55137, 18105, 20), ('2016-03-08', 55185, 3018, 40), ('2016-03-08', 55219, 14737, 100), ('2016-03-08', 55223, 83669, 
# 10), ('2016-03-08', 55308, 44397, 35), ('2016-03-08', 55311, 14113, 65), ('2016-03-08', 55353, 74186, 60), ('2016-03-08', 55387, 87230, 25), ('2016-03-08', 55529, 80648, 30), ('2016-03-08', 55575, 23101, 65), ('2016-03-08', 55841, 44690, 100), ('2016-03-08', 55846, 50503, 0), ('2016-03-08', 55857, 2697, 10), ('2016-03-08', 55937, 50467, 10), ('2016-03-09', 55967, 650, 0), ('2016-03-09', 56000, 3162, 0), ('2016-03-09', 56082, 4413, 0), ('2016-03-09', 56095, 5478, 0), ('2016-03-09', 56104, 5509, 0), ('2016-03-09', 56148, 5990, 0), ('2016-03-09', 56149, 7460, 0), ('2016-03-09', 56186, 7865, 0), ('2016-03-09', 56190, 7897, 0), ('2016-03-09', 56251, 7978, 0), ('2016-03-09', 56294, 8150, 0), ('2016-03-09', 56602, 9630, 0), ('2016-03-09', 56629, 11209, 0), ('2016-03-09', 56696, 12371, 0), ('2016-03-09', 56752, 12423, 0), ('2016-03-09', 56908, 19773, 0), ('2016-03-09', 57039, 19963, 0), ('2016-03-09', 57064, 20811, 0), ('2016-03-09', 57067, 20888, 0), ('2016-03-09', 57095, 21372, 0), ('2016-03-09', 57126, 22165, 0), ('2016-03-09', 57263, 22917, 0), ('2016-03-09', 57283, 22949, 0), ('2016-03-09', 57329, 24095, 0), ('2016-03-09', 57330, 24576, 0), ('2016-03-09', 57331, 26093, 0), ('2016-03-09', 57350, 26468, 0), ('2016-03-09', 57362, 27064, 0), ('2016-03-09', 57396, 30082, 0), ('2016-03-09', 57563, 32455, 0), ('2016-03-09', 57626, 33323, 0), ('2016-03-09', 57631, 33863, 0), ('2016-03-09', 57663, 34234, 0), ('2016-03-09', 57684, 34369, 0), ('2016-03-09', 57759, 36594, 0), ('2016-03-09', 57782, 37997, 0), ('2016-03-09', 57821, 38962, 0), ('2016-03-09', 57827, 41057, 0), ('2016-03-09', 57873, 42973, 0), ('2016-03-09', 57877, 44791, 0), ('2016-03-09', 57897, 48490, 0), ('2016-03-09', 57910, 49340, 0), ('2016-03-09', 57972, 51132, 0), ('2016-03-09', 58034, 51548, 0), ('2016-03-09', 58107, 53342, 0), ('2016-03-09', 58182, 54113, 0), ('2016-03-09', 58184, 54408, 0), ('2016-03-09', 58194, 55374, 0), ('2016-03-09', 58199, 56707, 0), ('2016-03-09', 58212, 56978, 0), ('2016-03-09', 58218, 59818, 0), ('2016-03-09', 58231, 60355, 0), ('2016-03-09', 58343, 62333, 0), ('2016-03-09', 58362, 67479, 0), ('2016-03-09', 58438, 69799, 0), ('2016-03-09', 58488, 70302, 0), ('2016-03-09', 58528, 71848, 0), ('2016-03-09', 58543, 73849, 0), ('2016-03-09', 58618, 76080, 0), ('2016-03-09', 58660, 77963, 0), ('2016-03-09', 58736, 79449, 0), ('2016-03-09', 58792, 80214, 0), ('2016-03-09', 59053, 83245, 0), ('2016-03-09', 59064, 83772, 0), ('2016-03-09', 59100, 86195, 0), ('2016-03-09', 59144, 86284, 0), ('2016-03-09', 59263, 88706, 0), ('2016-03-09', 59312, 89638, 0), ('2016-03-09', 59370, 90236, 0), ('2016-03-09', 59376, 91640, 0), ('2016-03-09', 59397, 91744, 0), ('2016-03-09', 59398, 92783, 0), ('2016-03-09', 59439, 92840, 0), ('2016-03-09', 59628, 73716, 80), ('2016-03-09', 59681, 62078, 30), ('2016-03-09', 59783, 21334, 100), ('2016-03-09', 59821, 51872, 65), ('2016-03-09', 59867, 40093, 45), ('2016-03-09', 
# 59935, 53072, 60), ('2016-03-09', 59953, 15225, 75), ('2016-03-09', 60027, 75635, 100), ('2016-03-09', 60100, 46977, 90), ('2016-03-09', 60110, 89310, 60), ('2016-03-09', 60191, 5026, 100), ('2016-03-09', 60283, 6944, 95), ('2016-03-09', 60289, 60516, 25), ('2016-03-09', 60341, 31247, 30), ('2016-03-09', 60392, 21743, 0), ('2016-03-09', 60442, 21866, 10), ('2016-03-09', 60457, 83376, 70), ('2016-03-09', 60526, 20594, 60), ('2016-03-09', 60595, 33782, 95), ('2016-03-09', 60661, 81492, 75), ('2016-03-09', 60711, 3374, 100), ('2016-03-09', 60729, 31221, 15), ('2016-03-09', 60784, 10985, 90), ('2016-03-09', 60892, 95648, 90), ('2016-03-09', 60980, 22780, 30), ('2016-03-09', 61018, 57572, 80), ('2016-03-09', 61098, 41558, 5), ('2016-03-09', 61171, 12852, 15), ('2016-03-09', 61232, 77217, 80), ('2016-03-09', 61244, 74486, 95), ('2016-03-09', 61257, 18941, 70), ('2016-03-09', 61287, 32353, 75), ('2016-03-09', 61312, 463, 10), ('2016-03-09', 61367, 23101, 55), ('2016-03-09', 61442, 84254, 65), ('2016-03-09', 61466, 33142, 45), ('2016-03-09', 61467, 89164, 80), ('2016-03-09', 61470, 13391, 70), ('2016-03-09', 61581, 20574, 50), ('2016-03-09', 61803, 29451, 90), ('2016-03-09', 61894, 433, 60), ('2016-03-09', 61955, 59761, 
# 25), ('2016-03-09', 61971, 58485, 85), ('2016-03-09', 61995, 31221, 95), ('2016-03-09', 62027, 29445, 35), ('2016-03-09', 62028, 74658, 80), ('2016-03-09', 62065, 97336, 0), ('2016-03-09', 62157, 16234, 10), ('2016-03-09', 62280, 78002, 40), ('2016-03-09', 62410, 40816, 10), ('2016-03-09', 62427, 41618, 40), ('2016-03-09', 62458, 87230, 40), ('2016-03-09', 62459, 80178, 10), ('2016-03-09', 62568, 31221, 45), ('2016-03-09', 62615, 15071, 40), ('2016-03-09', 62621, 34840, 10), ('2016-03-09', 62642, 93664, 100), ('2016-03-09', 62805, 99617, 40), ('2016-03-09', 62842, 21866, 70), ('2016-03-09', 62961, 73374, 55), ('2016-03-09', 63060, 62078, 20), ('2016-03-09', 63085, 81474, 20), ('2016-03-09', 63091, 46082, 80), ('2016-03-09', 63093, 79658, 100), ('2016-03-09', 63139, 65716, 20), ('2016-03-09', 63161, 42368, 25), ('2016-03-09', 63162, 18003, 5), ('2016-03-09', 63243, 22744, 30), ('2016-03-09', 63264, 46518, 30), ('2016-03-09', 63279, 81186, 5), ('2016-03-09', 63455, 81598, 10), ('2016-03-09', 63619, 95648, 95), ('2016-03-09', 63639, 62078, 10), ('2016-03-09', 63657, 18497, 35), ('2016-03-09', 63699, 58891, 95), ('2016-03-09', 63728, 18050, 0), ('2016-03-09', 63773, 70689, 30), ('2016-03-09', 63798, 44397, 80), ('2016-03-09', 63907, 22744, 85), ('2016-03-09', 63936, 19708, 90), ('2016-03-09', 63939, 15498, 65), ('2016-03-09', 63944, 39831, 90), ('2016-03-09', 63968, 95648, 10), ('2016-03-09', 63982, 32920, 50), ('2016-03-09', 64066, 83968, 70), ('2016-03-09', 64071, 50467, 95), ('2016-03-09', 64162, 61045, 20), ('2016-03-09', 64321, 41457, 10), ('2016-03-09', 64351, 63715, 80), ('2016-03-10', 64369, 650, 0), ('2016-03-10', 64392, 3162, 0), ('2016-03-10', 64438, 4413, 0), ('2016-03-10', 64444, 5478, 0), ('2016-03-10', 64477, 5509, 0), ('2016-03-10', 64501, 5990, 0), ('2016-03-10', 64540, 7460, 0), ('2016-03-10', 64556, 7865, 0), ('2016-03-10', 64570, 7897, 0), ('2016-03-10', 64593, 7978, 0), ('2016-03-10', 64600, 8150, 0), ('2016-03-10', 64704, 9630, 0), ('2016-03-10', 64751, 11209, 0), ('2016-03-10', 64830, 12371, 0), ('2016-03-10', 64852, 12423, 0), ('2016-03-10', 64865, 19773, 0), ('2016-03-10', 64867, 19963, 0), ('2016-03-10', 64971, 20811, 0), ('2016-03-10', 64988, 20888, 0), ('2016-03-10', 65041, 21372, 0), ('2016-03-10', 65060, 22165, 0), ('2016-03-10', 65143, 22917, 
# 0), ('2016-03-10', 65316, 22949, 0), ('2016-03-10', 65461, 24095, 0), ('2016-03-10', 65572, 24576, 0), ('2016-03-10', 65580, 26093, 0), ('2016-03-10', 65667, 26468, 0), ('2016-03-10', 65739, 27064, 0), ('2016-03-10', 65740, 30082, 0), ('2016-03-10', 65745, 32455, 0), ('2016-03-10', 65902, 33323, 0), ('2016-03-10', 65914, 33863, 0), ('2016-03-10', 65921, 34234, 0), ('2016-03-10', 65932, 34369, 0), ('2016-03-10', 65974, 36594, 0), ('2016-03-10', 66015, 37997, 
# 0), ('2016-03-10', 66064, 38962, 0), ('2016-03-10', 66080, 41057, 0), ('2016-03-10', 66090, 42973, 0), ('2016-03-10', 66135, 44791, 0), ('2016-03-10', 66136, 48490, 0), ('2016-03-10', 66207, 49340, 0), ('2016-03-10', 66241, 51132, 0), ('2016-03-10', 66297, 51548, 0), ('2016-03-10', 66303, 53342, 0), ('2016-03-10', 66383, 54113, 0), ('2016-03-10', 66389, 54408, 0), ('2016-03-10', 66417, 55374, 0), ('2016-03-10', 66419, 56707, 0), ('2016-03-10', 66437, 56978, 
# 0), ('2016-03-10', 66454, 59818, 0), ('2016-03-10', 66494, 60355, 0), ('2016-03-10', 66539, 62333, 0), ('2016-03-10', 66542, 67479, 0), ('2016-03-10', 66616, 69799, 0), ('2016-03-10', 66682, 70302, 0), ('2016-03-10', 66683, 71848, 0), ('2016-03-10', 66812, 73849, 0), ('2016-03-10', 66851, 76080, 0), ('2016-03-10', 66887, 77963, 0), ('2016-03-10', 66935, 79449, 0), ('2016-03-10', 67026, 80214, 0), ('2016-03-10', 67120, 83245, 0), ('2016-03-10', 67121, 87802, 
# 0), ('2016-03-10', 67147, 10068, 85), ('2016-03-10', 67161, 7336, 90), ('2016-03-10', 67186, 2820, 20), ('2016-03-10', 67280, 64823, 35), ('2016-03-10', 67310, 69030, 95), ('2016-03-10', 67357, 46977, 0), ('2016-03-10', 67374, 83987, 0), ('2016-03-10', 67409, 1433, 85), ('2016-03-10', 67426, 70115, 15), ('2016-03-10', 67482, 86845, 50), ('2016-03-10', 67586, 16530, 35), ('2016-03-10', 67603, 75908, 30), ('2016-03-10', 67642, 19540, 80), ('2016-03-10', 67702, 40266, 70), ('2016-03-10', 67718, 72237, 20), ('2016-03-10', 67890, 21973, 70), ('2016-03-10', 67894, 54899, 45), ('2016-03-10', 67936, 24725, 35), ('2016-03-10', 67987, 54807, 20), ('2016-03-10', 68018, 2697, 70), ('2016-03-10', 68023, 51572, 50), ('2016-03-10', 68034, 50385, 80), ('2016-03-10', 68145, 93764, 55), ('2016-03-10', 68147, 22013, 70), ('2016-03-10', 68226, 64716, 95), ('2016-03-10', 68233, 75019, 80), ('2016-03-10', 68313, 94671, 90), ('2016-03-10', 68315, 75635, 40), ('2016-03-10', 68401, 19552, 60), ('2016-03-10', 68452, 66648, 15), ('2016-03-10', 68454, 47174, 75), ('2016-03-10', 68473, 75908, 70), ('2016-03-10', 68478, 43192, 15), ('2016-03-10', 68480, 81064, 90), ('2016-03-10', 68483, 43192, 70), ('2016-03-10', 68604, 6259, 75), ('2016-03-10', 68663, 54967, 5), ('2016-03-10', 68693, 15039, 85), ('2016-03-10', 68741, 66648, 25), ('2016-03-10', 68850, 95934, 75), ('2016-03-10', 68853, 30845, 70), ('2016-03-10', 68870, 20574, 40), ('2016-03-10', 68982, 27050, 20), ('2016-03-10', 69044, 51572, 25), ('2016-03-10', 69049, 80648, 55), ('2016-03-10', 69051, 8894, 65), ('2016-03-10', 69112, 41708, 55), ('2016-03-10', 69129, 21219, 60), ('2016-03-11', 69174, 650, 0), ('2016-03-11', 69253, 3162, 0), ('2016-03-11', 69255, 4413, 0), ('2016-03-11', 69315, 5478, 0), ('2016-03-11', 69332, 5509, 0), ('2016-03-11', 69389, 5990, 0), ('2016-03-11', 69410, 7460, 0), ('2016-03-11', 69511, 7865, 0), ('2016-03-11', 69516, 7897, 0), ('2016-03-11', 69553, 7978, 0), ('2016-03-11', 69567, 8150, 0), ('2016-03-11', 69590, 9630, 0), ('2016-03-11', 69614, 11209, 0), ('2016-03-11', 69622, 12371, 0), ('2016-03-11', 69636, 12423, 0), ('2016-03-11', 69664, 19773, 0), ('2016-03-11', 69703, 19963, 0), ('2016-03-11', 69836, 20811, 0), ('2016-03-11', 69847, 20888, 0), ('2016-03-11', 69866, 21372, 0), ('2016-03-11', 69942, 22165, 0), ('2016-03-11', 70012, 22917, 0), ('2016-03-11', 70026, 22949, 0), ('2016-03-11', 70103, 24095, 0), ('2016-03-11', 70114, 24576, 0), ('2016-03-11', 70163, 26093, 0), ('2016-03-11', 70241, 26468, 0), ('2016-03-11', 70271, 27064, 0), ('2016-03-11', 70359, 30082, 0), ('2016-03-11', 70373, 32455, 0), ('2016-03-11', 70404, 33323, 0), ('2016-03-11', 70513, 33863, 0), ('2016-03-11', 70549, 34234, 0), ('2016-03-11', 70641, 34369, 0), ('2016-03-11', 70649, 36594, 0), ('2016-03-11', 70871, 37997, 0), ('2016-03-11', 70880, 38962, 0), ('2016-03-11', 70893, 54967, 60), ('2016-03-11', 70909, 91095, 80), ('2016-03-11', 70929, 74486, 25), ('2016-03-11', 70940, 6259, 75), ('2016-03-11', 70944, 56909, 35), ('2016-03-11', 70994, 84307, 95), ('2016-03-11', 71040, 97530, 70), ('2016-03-11', 71067, 90531, 40), ('2016-03-11', 71115, 21219, 5), ('2016-03-11', 71118, 23101, 80), ('2016-03-11', 71130, 23177, 25), ('2016-03-11', 71141, 60517, 15), ('2016-03-11', 71146, 37187, 0), ('2016-03-11', 71228, 81064, 35), ('2016-03-11', 71311, 66702, 80), ('2016-03-11', 71340, 62078, 55), ('2016-03-11', 71345, 98727, 95), ('2016-03-11', 71357, 74763, 85), ('2016-03-11', 71360, 47559, 35), ('2016-03-11', 71363, 68845, 75), ('2016-03-11', 71368, 94671, 70), ('2016-03-11', 71432, 30073, 65), ('2016-03-11', 71499, 66014, 95), ('2016-03-11', 71523, 14737, 10), ('2016-03-11', 71577, 75233, 65), ('2016-03-11', 71624, 47559, 100), ('2016-03-11', 71645, 91095, 45), ('2016-03-11', 71681, 50874, 40), ('2016-03-11', 71695, 9643, 50), ('2016-03-11', 71699, 65113, 55), ('2016-03-11', 71702, 61280, 15), ('2016-03-11', 71721, 86429, 20), ('2016-03-11', 71777, 70115, 65), ('2016-03-11', 71798, 93764, 15), ('2016-03-11', 71863, 44690, 5), ('2016-03-11', 71907, 71152, 85), ('2016-03-11', 71925, 77184, 95), ('2016-03-11', 72032, 92239, 85), ('2016-03-11', 72046, 39434, 10), ('2016-03-11', 72126, 73716, 15), ('2016-03-11', 72146, 91573, 10), ('2016-03-11', 72244, 41708, 100), ('2016-03-11', 72303, 39434, 5), ('2016-03-11', 72316, 47174, 60), ('2016-03-11', 72340, 50385, 55), ('2016-03-11', 72342, 65716, 40), ('2016-03-11', 72381, 59761, 5), ('2016-03-11', 72445, 40827, 0), ('2016-03-11', 72488, 12707, 100), ('2016-03-11', 72500, 98727, 15), ('2016-03-11', 72520, 8878, 65), ('2016-03-11', 72563, 92239, 75), ('2016-03-11', 72574, 3178, 85), ('2016-03-11', 72687, 2764, 90), ('2016-03-11', 72694, 83968, 85), ('2016-03-11', 72729, 22510, 45), ('2016-03-11', 72781, 6508, 85), ('2016-03-11', 72782, 80902, 50), ('2016-03-11', 72863, 31221, 100), ('2016-03-11', 73080, 10629, 45), ('2016-03-11', 73112, 94671, 70), ('2016-03-11', 73146, 95934, 30), ('2016-03-11', 73252, 60516, 60), ('2016-03-11', 73302, 44214, 90), ('2016-03-11', 73374, 97336, 85), ('2016-03-11', 73386, 59792, 20), ('2016-03-11', 73410, 12852, 10), ('2016-03-11', 73569, 61045, 100), ('2016-03-11', 73570, 99169, 90), ('2016-03-11', 73595, 44690, 100), ('2016-03-11', 73618, 41708, 55), ('2016-03-11', 73635, 3178, 90), ('2016-03-11', 73748, 54045, 15), ('2016-03-11', 73780, 60516, 90), ('2016-03-11', 73794, 87277, 25), ('2016-03-11', 73869, 86173, 30), ('2016-03-11', 73988, 16363, 40), ('2016-03-11', 74055, 18497, 90), ('2016-03-11', 74182, 63715, 100), ('2016-03-11', 74214, 25398, 
# 60), ('2016-03-11', 74302, 13901, 40), ('2016-03-11', 74368, 78143, 20), ('2016-03-11', 74398, 95647, 70), ('2016-03-11', 74408, 64790, 40), ('2016-03-11', 74425, 24725, 80), ('2016-03-11', 74451, 79658, 5), ('2016-03-11', 74517, 15054, 20), ('2016-03-11', 74567, 64609, 55), ('2016-03-11', 74591, 13901, 75), ('2016-03-11', 74642, 6340, 60), ('2016-03-11', 74745, 34794, 95), ('2016-03-12', 74780, 650, 0), ('2016-03-12', 74792, 3162, 0), ('2016-03-12', 74810, 
# 4413, 0), ('2016-03-12', 74969, 5478, 0), ('2016-03-12', 75010, 5509, 0), ('2016-03-12', 75067, 5990, 0), ('2016-03-12', 75109, 7460, 0), ('2016-03-12', 75135, 7865, 0), ('2016-03-12', 75155, 7897, 0), ('2016-03-12', 75308, 7978, 0), ('2016-03-12', 75368, 8150, 0), ('2016-03-12', 75437, 9630, 0), ('2016-03-12', 75453, 11209, 0), ('2016-03-12', 75502, 12371, 0), ('2016-03-12', 75541, 12423, 0), ('2016-03-12', 75546, 19773, 0), ('2016-03-12', 75579, 19963, 0), ('2016-03-12', 75638, 20811, 0), ('2016-03-12', 75643, 20888, 0), ('2016-03-12', 75646, 21372, 0), ('2016-03-12', 75653, 22165, 0), ('2016-03-12', 75709, 22917, 0), ('2016-03-12', 75742, 22949, 0), ('2016-03-12', 75773, 24095, 0), ('2016-03-12', 75815, 24576, 0), ('2016-03-12', 76061, 26093, 0), ('2016-03-12', 76076, 26468, 0), ('2016-03-12', 76123, 27064, 0), ('2016-03-12', 76153, 30082, 0), ('2016-03-12', 76193, 32455, 0), ('2016-03-12', 76312, 33323, 0), ('2016-03-12', 76361, 33863, 0), ('2016-03-12', 76381, 34234, 0), ('2016-03-12', 76402, 34369, 0), ('2016-03-12', 76455, 36594, 0), ('2016-03-12', 76473, 37997, 0), ('2016-03-12', 76486, 38962, 0), ('2016-03-12', 76515, 41057, 0), ('2016-03-12', 76544, 42973, 0), ('2016-03-12', 76564, 44791, 0), ('2016-03-12', 76632, 48490, 0), ('2016-03-12', 76635, 49340, 0), ('2016-03-12', 76668, 51132, 0), ('2016-03-12', 76727, 51548, 0), ('2016-03-12', 76765, 53342, 0), ('2016-03-12', 76852, 54113, 0), ('2016-03-12', 76858, 54408, 0), ('2016-03-12', 76859, 55374, 0), ('2016-03-12', 76874, 56707, 0), ('2016-03-12', 76894, 56978, 0), ('2016-03-12', 77014, 59818, 0), ('2016-03-12', 77133, 60355, 0), ('2016-03-12', 77136, 62333, 0), ('2016-03-12', 77265, 67479, 0), ('2016-03-12', 77297, 69799, 0), ('2016-03-12', 77336, 70302, 0), ('2016-03-12', 77436, 71848, 0), ('2016-03-12', 77470, 98835, 45), ('2016-03-12', 77528, 3124, 80), ('2016-03-12', 77573, 75908, 50), ('2016-03-12', 77675, 70115, 95), ('2016-03-12', 77785, 35116, 85), ('2016-03-12', 77798, 83643, 30), ('2016-03-12', 77803, 19552, 50), ('2016-03-12', 77809, 98727, 0), ('2016-03-12', 77855, 68435, 0), ('2016-03-12', 77929, 96017, 70), ('2016-03-12', 77985, 73716, 45), ('2016-03-12', 78081, 36786, 25), ('2016-03-12', 78083, 75019, 95), ('2016-03-12', 78150, 54967, 0), ('2016-03-12', 78287, 88642, 60), ('2016-03-12', 78298, 50467, 55), ('2016-03-12', 78303, 13901, 70), ('2016-03-12', 78326, 86429, 15), ('2016-03-12', 78398, 61045, 50), ('2016-03-12', 78402, 83968, 75), ('2016-03-12', 78473, 97530, 75), ('2016-03-12', 78621, 64790, 40), ('2016-03-12', 78684, 93764, 15), ('2016-03-12', 78782, 29047, 85), ('2016-03-12', 78805, 18497, 55), ('2016-03-12', 78811, 18497, 55), ('2016-03-12', 79011, 65554, 10), ('2016-03-12', 79090, 54967, 0), ('2016-03-12', 79225, 83376, 20), ('2016-03-12', 79442, 93308, 0), ('2016-03-12', 79621, 79278, 45), ('2016-03-12', 79624, 75019, 15), ('2016-03-12', 80062, 61793, 0), ('2016-03-12', 80068, 93361, 70), ('2016-03-12', 80082, 23101, 75), ('2016-03-12', 80122, 16747, 55), ('2016-03-12', 80172, 533, 75), ('2016-03-12', 80175, 73470, 75), ('2016-03-12', 80206, 18105, 35), ('2016-03-12', 80253, 58932, 95), ('2016-03-12', 80293, 93664, 35), ('2016-03-12', 80324, 61816, 85), ('2016-03-12', 80329, 54967, 15), ('2016-03-12', 80347, 48592, 80), ('2016-03-12', 80407, 6340, 15), ('2016-03-12', 80429, 77184, 55), ('2016-03-12', 80496, 61045, 65), ('2016-03-12', 80498, 79658, 25), ('2016-03-12', 80503, 37187, 100), ('2016-03-12', 80598, 64823, 45), ('2016-03-12', 80628, 98727, 40), ('2016-03-12', 80737, 83376, 85), 
# ('2016-03-12', 80807, 80394, 5), ('2016-03-12', 80910, 51572, 70), ('2016-03-12', 80943, 46082, 35), ('2016-03-12', 80958, 50874, 55), ('2016-03-12', 81022, 10068, 90), ('2016-03-12', 81128, 50874, 55), ('2016-03-12', 81132, 10068, 100), ('2016-03-13', 81311, 650, 0), ('2016-03-13', 81320, 3162, 0), ('2016-03-13', 81382, 4413, 0), ('2016-03-13', 81447, 5478, 0), ('2016-03-13', 81458, 5509, 0), ('2016-03-13', 81480, 5990, 0), ('2016-03-13', 81521, 7460, 0), ('2016-03-13', 81611, 7865, 0), ('2016-03-13', 81622, 7897, 0), ('2016-03-13', 81644, 7978, 0), ('2016-03-13', 81760, 8150, 0), ('2016-03-13', 81805, 9630, 0), ('2016-03-13', 81815, 11209, 0), ('2016-03-13', 81842, 12371, 0), ('2016-03-13', 81884, 12423, 0), ('2016-03-13', 81912, 19773, 0), ('2016-03-13', 81921, 19963, 0), ('2016-03-13', 81923, 20811, 0), ('2016-03-13', 82005, 20888, 0), ('2016-03-13', 82051, 21372, 0), ('2016-03-13', 82057, 22165, 0), ('2016-03-13', 82109, 22917, 0), ('2016-03-13', 82215, 22949, 0), ('2016-03-13', 82357, 24095, 0), ('2016-03-13', 82358, 24576, 0), ('2016-03-13', 82493, 26093, 0), ('2016-03-13', 82510, 26468, 0), ('2016-03-13', 82537, 27064, 0), ('2016-03-13', 82612, 30082, 0), ('2016-03-13', 82669, 32455, 0), ('2016-03-13', 82674, 33323, 0), ('2016-03-13', 82811, 33863, 0), ('2016-03-13', 82820, 34234, 0), ('2016-03-13', 82894, 34369, 0), ('2016-03-13', 82975, 36594, 0), ('2016-03-13', 83024, 37997, 0), ('2016-03-13', 83027, 38962, 0), ('2016-03-13', 83032, 41057, 0), ('2016-03-13', 83049, 42973, 0), ('2016-03-13', 83070, 44791, 0), ('2016-03-13', 83095, 48490, 0), ('2016-03-13', 83120, 49340, 0), ('2016-03-13', 83152, 51132, 0), ('2016-03-13', 83166, 51548, 0), ('2016-03-13', 83180, 53342, 0), ('2016-03-13', 83203, 54113, 0), ('2016-03-13', 83266, 54408, 0), ('2016-03-13', 83317, 40816, 40), ('2016-03-13', 83377, 21334, 40), ('2016-03-13', 83463, 47258, 65), ('2016-03-13', 83603, 1240, 70), ('2016-03-13', 83646, 68071, 75), ('2016-03-13', 83653, 81242, 15), ('2016-03-13', 83710, 36654, 20), ('2016-03-13', 83730, 48743, 90), ('2016-03-13', 83735, 26955, 75), ('2016-03-13', 83793, 81242, 70), ('2016-03-13', 83796, 22780, 65), ('2016-03-13', 83807, 86065, 70), ('2016-03-13', 83851, 54967, 0), ('2016-03-13', 83874, 3178, 80), ('2016-03-13', 83910, 10940, 55), ('2016-03-13', 84069, 44914, 65), ('2016-03-13', 84081, 66648, 100), ('2016-03-13', 84092, 81492, 95), ('2016-03-13', 84107, 53940, 15), ('2016-03-13', 84318, 53940, 45), ('2016-03-13', 84390, 73967, 10), ('2016-03-13', 84425, 27725, 90), ('2016-03-13', 84560, 30073, 100), ('2016-03-13', 84689, 30061, 0), ('2016-03-13', 84698, 21152, 60), ('2016-03-13', 84720, 22942, 95), ('2016-03-13', 84820, 78002, 10), ('2016-03-13', 84841, 89457, 80), ('2016-03-13', 84850, 463, 15), ('2016-03-13', 84893, 30061, 65), ('2016-03-13', 84902, 90401, 5), ('2016-03-13', 84974, 94104, 20), ('2016-03-13', 84980, 78408, 25), ('2016-03-13', 84983, 22510, 15), ('2016-03-13', 85020, 89310, 95), ('2016-03-13', 85106, 95934, 10), ('2016-03-13', 85140, 84254, 20), ('2016-03-13', 85147, 89457, 0), ('2016-03-13', 85168, 19761, 45), ('2016-03-13', 85175, 95958, 60), ('2016-03-13', 85230, 57824, 20), ('2016-03-13', 85255, 92239, 70), ('2016-03-13', 85270, 64790, 90), ('2016-03-13', 85295, 18105, 65), ('2016-03-13', 85301, 60517, 85), ('2016-03-13', 85370, 95648, 5), ('2016-03-13', 85376, 32710, 85), ('2016-03-14', 85386, 650, 0), ('2016-03-14', 85477, 3162, 0), ('2016-03-14', 85486, 4413, 0), ('2016-03-14', 85534, 5478, 0), ('2016-03-14', 85619, 5509, 0), ('2016-03-14', 85642, 5990, 0), ('2016-03-14', 85722, 7460, 0), ('2016-03-14', 86025, 7865, 0), ('2016-03-14', 86178, 7897, 0), ('2016-03-14', 86240, 7978, 0), ('2016-03-14', 86258, 8150, 0), ('2016-03-14', 86444, 9630, 0), ('2016-03-14', 86506, 11209, 0), ('2016-03-14', 86528, 12371, 0), ('2016-03-14', 86774, 12423, 0), ('2016-03-14', 86838, 19773, 0), ('2016-03-14', 86884, 19963, 0), ('2016-03-14', 86893, 20811, 0), ('2016-03-14', 86981, 20888, 0), ('2016-03-14', 87149, 21372, 0), ('2016-03-14', 87249, 22165, 0), ('2016-03-14', 87254, 22917, 0), ('2016-03-14', 87294, 22949, 0), ('2016-03-14', 87315, 24095, 0), ('2016-03-14', 87408, 24576, 0), ('2016-03-14', 87440, 26093, 0), ('2016-03-14', 87505, 26468, 0), ('2016-03-14', 87511, 27064, 0), ('2016-03-14', 87581, 30082, 0), ('2016-03-14', 87637, 32455, 0), ('2016-03-14', 87639, 33323, 0), ('2016-03-14', 87675, 33863, 0), ('2016-03-14', 87713, 34234, 0), ('2016-03-14', 87812, 34369, 0), ('2016-03-14', 87888, 36594, 0), ('2016-03-14', 87915, 37997, 0), ('2016-03-14', 87916, 38962, 0), ('2016-03-14', 87926, 41057, 0), ('2016-03-14', 88064, 42973, 0), ('2016-03-14', 88069, 44791, 0), ('2016-03-14', 88105, 48490, 0), ('2016-03-14', 88176, 49340, 0), ('2016-03-14', 88188, 51132, 0), ('2016-03-14', 88303, 51548, 0), ('2016-03-14', 88310, 53342, 0), ('2016-03-14', 88328, 54113, 0), ('2016-03-14', 88340, 54408, 0), ('2016-03-14', 88393, 55374, 0), ('2016-03-14', 88448, 56707, 0), ('2016-03-14', 88528, 56978, 0), ('2016-03-14', 88540, 59818, 0), ('2016-03-14', 88546, 60355, 0), ('2016-03-14', 88581, 62333, 0), ('2016-03-14', 88602, 67479, 0), ('2016-03-14', 88644, 69799, 0), ('2016-03-14', 88846, 70302, 0), ('2016-03-14', 88918, 71848, 0), ('2016-03-14', 88993, 73849, 0), ('2016-03-14', 89071, 76080, 0), ('2016-03-14', 89118, 77963, 0), ('2016-03-14', 89160, 79449, 0), ('2016-03-14', 89190, 80214, 0), ('2016-03-14', 89212, 83245, 0), ('2016-03-14', 89245, 83772, 0), ('2016-03-14', 89306, 86195, 0), ('2016-03-14', 89322, 86284, 0), ('2016-03-14', 89412, 88706, 0), ('2016-03-14', 89441, 89638, 0), ('2016-03-14', 89488, 90236, 0), ('2016-03-14', 89491, 91640, 0), ('2016-03-14', 89567, 91744, 0), ('2016-03-14', 89604, 92783, 0), ('2016-03-14', 89670, 92840, 0), ('2016-03-14', 89674, 93433, 0), ('2016-03-14', 89758, 27789, 60), ('2016-03-14', 89764, 
# 74861, 95), ('2016-03-14', 89765, 6508, 50), ('2016-03-14', 89768, 23794, 90), ('2016-03-14', 89784, 13923, 30), ('2016-03-14', 89850, 3124, 10), ('2016-03-14', 90036, 73426, 100), ('2016-03-14', 90066, 32353, 5), ('2016-03-14', 90096, 54967, 60), ('2016-03-14', 90109, 58485, 75), ('2016-03-14', 90144, 32920, 15), ('2016-03-14', 90178, 94083, 90), ('2016-03-14', 90216, 45630, 100), ('2016-03-14', 90224, 23755, 25), ('2016-03-14', 90230, 68435, 50), ('2016-03-14', 90302, 53072, 15), ('2016-03-14', 90304, 79101, 20), ('2016-03-14', 90307, 15158, 65), ('2016-03-14', 90323, 58141, 50), ('2016-03-14', 90445, 53940, 70), ('2016-03-14', 90636, 90612, 5), ('2016-03-14', 90691, 39831, 20), ('2016-03-14', 90702, 65716, 65), ('2016-03-14', 90775, 78205, 20), ('2016-03-14', 90800, 56909, 40), ('2016-03-14', 90959, 24420, 15), ('2016-03-14', 91020, 94083, 45), ('2016-03-14', 91034, 80682, 100), ('2016-03-14', 91036, 59446, 
# 35), ('2016-03-14', 91076, 44052, 55), ('2016-03-14', 91278, 14113, 5), ('2016-03-14', 91296, 3374, 60), ('2016-03-14', 91300, 74861, 15), ('2016-03-14', 
# 91308, 94251, 60), ('2016-03-14', 91449, 76035, 70), ('2016-03-14', 91452, 74021, 35), ('2016-03-14', 91453, 99617, 25), ('2016-03-14', 91557, 32353, 15), ('2016-03-14', 91664, 74021, 85), ('2016-03-14', 91681, 73695, 100), ('2016-03-14', 91724, 47258, 95), ('2016-03-14', 91736, 33142, 60), ('2016-03-14', 91738, 46870, 80), ('2016-03-14', 91904, 13923, 90), ('2016-03-14', 91909, 18892, 70), ('2016-03-14', 91927, 10144, 55), ('2016-03-14', 91939, 50385, 85), 
# ('2016-03-14', 91964, 22750, 85), ('2016-03-14', 92090, 54045, 85), ('2016-03-14', 92157, 1240, 100), ('2016-03-14', 92286, 30933, 80), ('2016-03-14', 92306, 34294, 20), ('2016-03-14', 92340, 597, 65), ('2016-03-14', 92392, 31247, 70), ('2016-03-14', 92417, 74763, 10), ('2016-03-14', 92475, 55050, 90), ('2016-03-14', 92559, 74861, 95), ('2016-03-14', 92567, 10068, 85), ('2016-03-14', 92605, 40816, 55), ('2016-03-14', 92642, 24420, 5), ('2016-03-14', 92740, 42368, 90), ('2016-03-14', 92752, 31618, 30), ('2016-03-14', 92844, 3018, 35), ('2016-03-14', 92892, 87802, 70), ('2016-03-14', 92893, 57572, 95), ('2016-03-14', 92914, 36562, 60), ('2016-03-14', 92923, 58891, 15), ('2016-03-14', 92950, 31454, 80), ('2016-03-14', 92964, 34294, 60), ('2016-03-14', 93010, 86429, 10), ('2016-03-14', 93038, 47258, 20), ('2016-03-14', 93129, 35116, 55), ('2016-03-14', 93142, 44217, 80), ('2016-03-14', 93177, 32353, 20), ('2016-03-14', 93264, 32710, 90), ('2016-03-14', 93281, 18199, 20), ('2016-03-14', 93318, 65716, 10), ('2016-03-14', 93329, 41618, 40), ('2016-03-14', 93378, 61816, 90), ('2016-03-14', 93506, 86173, 25), ('2016-03-14', 93518, 463, 35), ('2016-03-14', 93560, 80094, 100), ('2016-03-14', 93609, 79136, 15), ('2016-03-15', 93657, 650, 0), ('2016-03-15', 93753, 3162, 0), ('2016-03-15', 93780, 4413, 0), ('2016-03-15', 93943, 5478, 0), ('2016-03-15', 93963, 5509, 0), ('2016-03-15', 93992, 5990, 0), ('2016-03-15', 94006, 7460, 0), ('2016-03-15', 94038, 7865, 0), ('2016-03-15', 94050, 7897, 0), ('2016-03-15', 94056, 7978, 0), ('2016-03-15', 94108, 8150, 0), ('2016-03-15', 94137, 9630, 0), ('2016-03-15', 94339, 11209, 0), ('2016-03-15', 94357, 12371, 0), ('2016-03-15', 94359, 12423, 0), ('2016-03-15', 94461, 19773, 0), ('2016-03-15', 94465, 19963, 0), ('2016-03-15', 94484, 20811, 0), ('2016-03-15', 94507, 20888, 0), ('2016-03-15', 
# 94791, 21372, 0), ('2016-03-15', 94810, 22165, 0), ('2016-03-15', 94824, 22917, 0), ('2016-03-15', 94893, 22949, 0), ('2016-03-15', 94921, 24095, 0), ('2016-03-15', 94953, 24576, 0), ('2016-03-15', 95011, 26093, 0), ('2016-03-15', 95089, 26468, 0), ('2016-03-15', 95144, 27064, 0), ('2016-03-15', 95200, 30082, 0), ('2016-03-15', 95232, 32455, 0), ('2016-03-15', 95467, 33323, 0), ('2016-03-15', 95690, 33863, 0), ('2016-03-15', 95800, 34234, 0), ('2016-03-15', 
# 95818, 34369, 0), ('2016-03-15', 95848, 36594, 0), ('2016-03-15', 95870, 37997, 0), ('2016-03-15', 95950, 38962, 0), ('2016-03-15', 95951, 41057, 0), ('2016-03-15', 95999, 42973, 0), ('2016-03-15', 96157, 44791, 0), ('2016-03-15', 96199, 48490, 0), ('2016-03-15', 96242, 49340, 0), ('2016-03-15', 96333, 51132, 0), ('2016-03-15', 96360, 51548, 0), ('2016-03-15', 96372, 53342, 0), ('2016-03-15', 96437, 54113, 0), ('2016-03-15', 96439, 54408, 0), ('2016-03-15', 
# 96441, 55374, 0), ('2016-03-15', 96444, 56707, 0), ('2016-03-15', 96484, 56978, 0), ('2016-03-15', 96577, 59818, 0), ('2016-03-15', 96588, 60355, 0), ('2016-03-15', 96611, 62333, 0), ('2016-03-15', 96612, 67479, 0), ('2016-03-15', 96652, 69799, 0), ('2016-03-15', 96757, 70302, 0), ('2016-03-15', 96775, 71848, 0), ('2016-03-15', 96805, 73849, 0), ('2016-03-15', 96865, 76080, 0), ('2016-03-15', 96904, 77963, 0), ('2016-03-15', 96913, 79449, 0), ('2016-03-15', 
# 96970, 80214, 0), ('2016-03-15', 96977, 83245, 0), ('2016-03-15', 96979, 83772, 0), ('2016-03-15', 97002, 86195, 0), ('2016-03-15', 97044, 86284, 0), ('2016-03-15', 97061, 88706, 0), ('2016-03-15', 97298, 89638, 0), ('2016-03-15', 97437, 90236, 0), ('2016-03-15', 97545, 91640, 0), ('2016-03-15', 97559, 91744, 0), ('2016-03-15', 97637, 92783, 0), ('2016-03-15', 97727, 92840, 0), ('2016-03-15', 97793, 72237, 75), ('2016-03-15', 97864, 8871, 50), ('2016-03-15', 97877, 31822, 25), ('2016-03-15', 97907, 90401, 35), ('2016-03-15', 97911, 39857, 0), ('2016-03-15', 97912, 15498, 25), ('2016-03-15', 97938, 41336, 40), ('2016-03-15', 98019, 61280, 40), ('2016-03-15', 98107, 27789, 75), ('2016-03-15', 98112, 23794, 50), ('2016-03-15', 98167, 80648, 35), ('2016-03-15', 98182, 41618, 85), ('2016-03-15', 98279, 77184, 10), ('2016-03-15', 98281, 71152, 15), ('2016-03-15', 98345, 98835, 65), ('2016-03-15', 98362, 79101, 100), 
# ('2016-03-15', 98395, 91573, 70), ('2016-03-15', 98545, 15158, 95), ('2016-03-15', 98635, 19708, 15), ('2016-03-15', 98648, 12856, 25), ('2016-03-15', 98729, 75908, 45), ('2016-03-15', 98803, 72237, 50), ('2016-03-15', 98813, 65875, 40), ('2016-03-15', 98816, 90531, 100), ('2016-03-15', 98859, 68071, 60), ('2016-03-15', 98861, 53808, 40), ('2016-03-15', 98959, 40093, 0), ('2016-03-15', 99025, 80648, 100), ('2016-03-15', 99043, 27789, 0), ('2016-03-15', 99068, 433, 70), ('2016-03-15', 99110, 87277, 35), ('2016-03-15', 99159, 25398, 70), ('2016-03-15', 99161, 19761, 0), ('2016-03-15', 99198, 59446, 90), ('2016-03-15', 99199, 22744, 30), ('2016-03-15', 99295, 37187, 90), ('2016-03-15', 99315, 95648, 10), ('2016-03-15', 99511, 96104, 100), ('2016-03-15', 99578, 39831, 0), ('2016-03-15', 99598, 7336, 30), ('2016-03-15', 99600, 19516, 75), ('2016-03-15', 99634, 26023, 0), ('2016-03-15', 99741, 41558, 100), ('2016-03-15', 99769, 87555, 5), ('2016-03-15', 99825, 57448, 5), ('2016-03-15', 99926, 87802, 100), ('2016-03-15', 99951, 53295, 45);
#             """)

# cur.execute("DROP TABLE IF EXISTS hackers;")
# cur.execute("""CREATE TABLE hackers (
#                 hacker_id INT,
#                 name VARCHAR(50)
#             );""")

# cur.execute("""
#             INSERT INTO hackers (hacker_id, name) VALUES (79, 'Rose'), (433, 'Angela'), (463, 'Frank'), (533, 'Patrick'), (597, 'Lisa'), (650, 'Kimberly'), (1050, 'Bonnie'), (1240, 'Michael'), (1433, 'Todd'), (2345, 'Joe'), (2697, 'Earl'), (2764, 'Robert'), (2820, 'Amy'), (2873, 'Pamela'), (3018, 'Maria'), (3124, 'Joe'), (3162, 'Linda'), (3178, 'Melissa'), (3222, 'Carol'), (3374, 'Paula'), (4413, 'Marilyn'), (5026, 'Jennifer'), (5327, 'Harry'), (5333, 'David'), (5478, 'Julia'), (5509, 'Kevin'), (5990, 'Paul'), (6030, 'James'), (6259, 'Kelly'), (6322, 'Robin'), (6340, 'Ralph'), (6508, 'Gloria'), (6775, 'Victor'), (6944, 'David'), (7336, 'Joyce'), (7460, 'Donna'), (7865, 'Michelle'), (7891, 'Stephanie'), (7897, 'Gerald'), (7978, 'Walter'), (8150, 'Christina'), (8871, 'Brandon'), (8878, 'Elizabeth'), (8894, 'Joseph'), (9198, 'Lawrence'), (9630, 'Marilyn'), (9643, 'Lori'), (10068, 'Matthew'), (10144, 'Jesse'), (10629, 'John'), (10940, 'Martha'), (10985, 'Timothy'), (11092, 'Christine'), (11209, 'Anthony'), (11587, 'Paula'), (11753, 'Kimberly'), (12303, 'Louise'), (12371, 'Martin'), (12423, 'Paul'), (12707, 'Antonio'), (12765, 'Jacqueline'), (12852, 'Diana'), (12856, 'John'), (13224, 'Dorothy'), (13391, 'Evelyn'), (13733, 'Phillip'), (13901, 'Evelyn'), (13923, 'Debra'), (14113, 'David'), (14737, 'Willie'), (14826, 'Brandon'), (15039, 'Ann'), (15054, 'Emily'), (15071, 'Dorothy'), (15158, 'Jonathan'), (15225, 'Dorothy'), (15486, 'Marilyn'), (15498, 'Norma'), (15999, 'Nancy'), (16014, 'Andrew'), (16234, 'Keith'), (16257, 'Benjamin'), 
# (16363, 'Charles'), (16530, 'Alan'), (16700, 'Tammy'), (16747, 'Anna'), (16932, 'James'), (17482, 'Robin'), (18003, 'Jean'), (18050, 'Andrew'), (18105, 'Roy'), (18199, 'Diana'), (18317, 'Christina'), (18497, 'Jesse'), (18892, 'Joyce'), (18941, 'Patricia'), (19131, 'Gregory'), (19516, 'Brian'), (19540, 'Christine'), (19552, 'Lillian'), (19708, 'Aaron'), (19736, 'Dorothy'), (19761, 'Christopher'), (19773, 'Bobby'), (19904, 'Bobby'), (19963, 'Gerald'), (20033, 
# 'Carol'), (20435, 'Jeremy'), (20574, 'Clarence'), (20594, 'Wayne'), (20604, 'Carolyn'), (20811, 'Margaret'), (20857, 'Andrew'), (20888, 'Albert'), (21152, 'Judy'), (21219, 'Arthur'), (21334, 'Cynthia'), (21372, 'Jerry'), (21657, 'Thomas'), (21743, 'Elizabeth'), (21866, 'Justin'), (21973, 'Albert'), (22013, 
# 'James'), (22165, 'Stephen'), (22467, 'Alan'), (22510, 'Joshua'), (22744, 'Norma'), (22750, 'Mildred'), (22780, 'Melissa'), (22917, 'Paul'), (22942, 'Gerald'), (22949, 'Ronald'), (23101, 'Sandra'), (23177, 'Helen'), (23755, 'Larry'), (23794, 'Alan'), (24095, 'Paul'), (24420, 'Chris'), (24576, 'Steven'), (24725, 'Jennifer'), (25226, 'Bonnie'), (25398, 'Shirley'), (26023, 'Jeffrey'), (26093, 'Janet'), (26170, 'Albert'), (26468, 'Charles'), (26601, 'Kelly'), (26701, 'Bobby'), (26955, 'Elizabeth'), (27050, 'Keith'), (27064, 'Jose'), (27725, 'Ann'), (27789, 'Helen'), (28201, 'Jason'), (29047, 'Gerald'), (29445, 'Carlos'), (29451, 'Ryan'), (29719, 'Ashley'), (30061, 'Julia'), (30073, 'Harry'), (30082, 'Sean'), (30845, 'Julia'), (30933, 'Marilyn'), (31151, 'Cheryl'), (31221, 'Susan'), (31247, 'Judith'), (31263, 'Ruth'), (31454, 'Jane'), (31618, 'Sara'), (31822, 'Denise'), (32349, 'Jason'), (32353, 'Rose'), (32455, 'Susan'), (32540, 'Irene'), (32687, 'Jonathan'), (32710, 'Shawn'), (32920, 'Julia'), (33142, 'Linda'), (33245, 'Melissa'), (33323, 'Dennis'), (33782, 'Jeremy'), (33863, 'Patrick'), (34234, 'Jennifer'), (34294, 'Lillian'), (34369, 'Charles'), (34506, 'Philip'), (34794, 'Jimmy'), (34840, 'Doris'), (35116, 'Craig'), (35492, 'Walter'), (35606, 'Wayne'), (36058, 'Katherine'), (36562, 'Mark'), (36594, 'Barbara'), (36654, 'Mark'), (36691, 'Joe'), (36786, 'Maria'), (37187, 'John'), (37492, 'Brian'), (37997, 'Kimberly'), (38419, 'Bonnie'), (38522, 'Terry'), (38962, 'Brian'), (39091, 'Ruby'), (39313, 'Wayne'), (39434, 'Rebecca'), (39441, 'Joyce'), (39831, 'Douglas'), (39857, 'Philip'), (40093, 'Lori'), (40147, 'Benjamin'), (40266, 'Dennis'), (40816, 'Sara'), (40827, 'Douglas'), (41057, 'Dennis'), (41336, 'Ernest'), (41457, 'Clarence'), (41558, 'Diana'), (41618, 'Steve'), (41708, 'Amy'), (42115, 'Adam'), (42225, 'Douglas'), 
# (42368, 'Scott'), (42573, 'Samuel'), (42672, 'Louis'), (42973, 'Jason'), (43192, 'Bobby'), (43604, 'Janet'), (44052, 'Clarence'), (44214, 'Dorothy'), (44217, 'Sharon'), (44397, 'Brandon'), (44598, 'Timothy'), (44690, 'Christina'), (44791, 'Barbara'), (44914, 'Jose'), (45630, 'Kelly'), (46082, 'Paul'), (46328, 'Clarence'), (46518, 'Lillian'), (46870, 'Christine'), (46977, 'Russell'), (47174, 'Marie'), (47258, 'Richard'), (47559, 'Kenneth'), (48490, 'Judy'), (48592, 'Arthur'), (48743, 'Lori'), (49008, 'Scott'), (49044, 'Brian'), (49116, 'Larry'), (49340, 'Karen'), (50385, 'Steve'), (50467, 'Teresa'), (50503, 'Nicholas'), (50616, 'Robin'), (50874, 'Bruce'), (50910, 'Harry'), (51132, 'Harold'), (51134, 'Richard'), (51548, 'Bobby'), (51572, 'Deborah'), (51726, 'Jeffrey'), (51775, 'Bobby'), (51872, 'Rose'), (53072, 'Douglas'), (53295, 'Brian'), (53342, 'Carolyn'), (53548, 'Denise'), (53808, 'Janet'), (53940, 'Kathy'), (54045, 'Catherine'), (54113, 'Paula'), (54180, 'Sara'), (54408, 'Thomas'), (54807, 'Daniel'), (54899, 'Amy'), (54967, 'Kenneth'), (55050, 'Jerry'), (55343, 'Randy'), (55374, 'Teresa'), (56107, 'Kelly'), (56707, 'Jose'), (56812, 'Beverly'), (56909, 'Arthur'), (56978, 'Melissa'), (57448, 'Earl'), (57527, 'Ryan'), (57572, 'Margaret'), (57824, 'Diana'), (58141, 'Nicholas'), (58485, 'Debra'), (58891, 'David'), (58932, 'Nicole'), (59446, 'Kevin'), (59761, 'Rachel'), (59792, 'Janet'), (59818, 'Virginia'), (59943, 'Philip'), (60355, 'Shirley'), (60516, 'Martin'), (60517, 'Martha'), (61010, 'Rachel'), (61045, 'Brian'), (61280, 'Philip'), (61793, 'Mark'), (61816, 'Kenneth'), (62078, 'Lillian'), (62110, 'Lawrence'), (62325, 'Marie'), (62333, 'Earl'), (62640, 'Brenda'), (63107, 'Sean'), (63715, 'Donald'), (63800, 'Anna'), (64609, 'Frances'), (64716, 'Mark'), (64790, 'Dorothy'), (64823, 'Bruce'), (65072, 'Stephanie'), (65113, 'Lawrence'), (65554, 'Randy'), (65716, 'Sarah'), (65875, 'Carolyn'), (66014, 'Anna'), (66627, 'Craig'), (66648, 'Virginia'), (66702, 'Nicholas'), (67479, 'Roy'), (67735, 'Janice'), (67815, 'Douglas'), (68071, 'Charles'), (68435, 'Thomas'), (68566, 'Karen'), (68845, 'Harry'), (69030, 'Carl'), (69101, 'Stephen'), (69149, 'Elizabeth'), (69660, 'Shirley'), (69706, 'Matthew'), (69799, 'Paula'), (69928, 'Chris'), (70115, 'Stephen'), (70287, 'Gloria'), (70302, 'George'), (70689, 'Joan'), (71152, 'Paula'), (71848, 'Frank'), (72237, 'Brandon'), (72721, 'Michelle'), (72783, 'Dennis'), (73115, 'Maria'), (73374, 'Doris'), (73426, 'Edward'), (73470, 'Paul'), (73695, 'Julie'), (73716, 'Bobby'), (73740, 'Julie'), (73849, 'Eugene'), (73967, 'Ruby'), (74021, 'Russell'), 
# (74186, 'Jeremy'), (74486, 'Frances'), (74568, 'Ralph'), (74658, 'Linda'), (74763, 'Jessica'), (74861, 'Fred'), (75019, 'Catherine'), (75233, 'Pamela'), (75635, 'Eric'), (75889, 'Jeremy'), (75908, 'Rebecca'), (76035, 'John'), (76080, 'Barbara'), (77184, 'Susan'), (77217, 'Sarah'), (77490, 'Kathryn'), (77749, 'Sarah'), (77963, 'Michelle'), (78002, 'Emily'), (78143, 'Diana'), (78205, 'Jose'), (78408, 'Mildred'), (78666, 'Theresa'), (78993, 'Jeremy'), (79101, 'Beverly'), (79136, 'Jennifer'), (79278, 'Phyllis'), (79449, 'Kathryn'), (79480, 'Roy'), (79658, 'Tina'), (80094, 'Anne'), (80178, 'Carolyn'), (80214, 'Nicholas'), (80394, 'Nicholas'), (80580, 'Ralph'), (80648, 'Michael'), (80682, 'Deborah'), (80744, 'Alan'), (80902, 'Julia'), (81064, 'Albert'), (81186, 'Brenda'), (81242, 'Frances'), (81314, 'Denise'), (81338, 'Mark'), (81474, 'Bonnie'), (81492, 'Ralph'), (81511, 'Howard'), (81598, 'Roy'), (81751, 'Roy'), (82956, 'Christina'), (83245, 'Steve'), (83263, 'Johnny'), (83371, 'Cynthia'), (83376, 'Walter'), (83509, 'Sharon'), (83643, 'Earl'), (83669, 'Alan'), (83772, 'Judy'), (83913, 'Matthew'), (83968, 'Julie'), (83987, 'Jerry'), (84254, 'Diane'), (84307, 'Evelyn'), (84441, 'Dennis'), (84640, 'Douglas'), (85006, 'Martha'), (85501, 'Beverly'), (85948, 'Mark'), (86065, 'Samuel'), (86173, 'Janet'), (86195, 'Craig'), (86284, 'Howard'), (86429, 'Kathleen'), (86742, 'Norma'), (86845, 'Wayne'), (87230, 'Phyllis'), (87277, 'Jimmy'), (87555, 'Jerry'), (87802, 'Gregory'), (88484, 'Jean'), (88642, 'Anna'), (88706, 'Alan'), (89164, 'Steve'), (89310, 'Bruce'), (89457, 'Douglas'), (89638, 'Antonio'), (89737, 'Jeremy'), (89780, 'Willie'), (89781, 'Jeffrey'), (89814, 'Jane'), (89988, 
# 'Larry'), (89991, 'Katherine'), (90030, 'Martin'), (90236, 'Jesse'), (90401, 'Shawn'), (90531, 'Jack'), (90612, 'Edward'), (90750, 'Joyce'), (90959, 'Christina'), (91095, 'Doris'), (91573, 'Cynthia'), (91640, 'Debra'), (91744, 'Harold'), (92239, 'Shirley'), (92654, 'Joyce'), (92783, 'Justin'), (92840, 'Harold'), (93308, 'Amy'), (93361, 'Louis'), (93433, 'Tina'), (93494, 'Laura'), (93664, 'Keith'), (93764, 'Dennis'), (94083, 'Lillian'), (94104, 'Patrick'), (94251, 'Adam'), (94671, 'Clarence'), (95183, 'Victor'), (95335, 'Lawrence'), (95354, 'Nicholas'), (95647, 'George'), (95648, 'Charles'), (95682, 'Christine'), (95928, 'Russell'), (95934, 'Christine'), (95958, 'Linda'), (96017, 'Carlos'), (96104, 'Emily'), (96821, 'Angela'), (97336, 'Lawrence'), (97530, 'Amy'), (98727, 'Carol'), (98780, 'Nancy'), (98835, 'Gary'), (98981, 'Rose'), (99149, 'Timothy'), (99169, 'Nancy'), (99617, 'Mary'), (99789, 'Joshua');
#             """)

# con.commit()

# cur.execute("""
#             WITH CTE2 as (
#                 select *, row_number() over (partition by submission_date, hacker_id order by hacker_id) as submit_flag from submissions
#             ),
#             CTE3 as (
#                 select *, row_number() over (partition by submission_date order by submit_flag desc, hacker_id) as maxxer from CTE2
#             ),
#             CTE4 as (
#                 select *, dense_rank() over (partition by hacker_id order by submission_date) as ranker,
#                 row_number() over (partition by submission_date, hacker_id) as duplicate_val
#                 from submissions
#             ),
#             cte_start_date as (
#                 select min(submission_date) from submissions
#             ),
#             cte_unique_submitters as (
#                 select submission_date, consistors
#                 from (
#                     select submission_date, sum(consistor) over (partition by submission_date) DIV 1 as consistors
#                     from (
#                         select *, case when datediff(submission_date, (select * from cte_start_date)) + 1 = ranker then 1 else 0 end consistor from CTE4 where duplicate_val = 1 order by submission_date
#                     )  e
#                 ) f
#                 group by submission_date, consistors
#             ),
#             CTE6 as (
#                 select a.submission_date, consistors, hacker_id from CTE3 a inner join cte_unique_submitters b on a.submission_date = b.submission_date where maxxer = 1
#             )
#             select submission_date, consistors, a.hacker_id, b.name from CTE6 a inner join hackers b on a.hacker_id = b.hacker_id order by submission_date
#             """)

# mysql_print()

# SPARK ---------------------------------------------------------------------------------------------------------------------------

# hackers_df = ( spark.read
#   .format("jdbc")
#   .option("driver", "com.mysql.cj.jdbc.Driver")
#   .option("url", "jdbc:mysql://localhost")
#   .option("dbtable", "scenarios.hackers")
#   .option("user", "root")
#   .option("password", "pass")
#   .load()
# )

# hackers_df.show()

# submissions_df = ( spark.read
#   .format("jdbc")
#   .option("driver", "com.mysql.cj.jdbc.Driver")
#   .option("url", "jdbc:mysql://localhost")
#   .option("dbtable", "scenarios.submissions")
#   .option("user", "root")
#   .option("password", "pass")
#   .load()
# )

# submissions_df.show()

# maxSubPerDay_df = submissions_df.withColumn("ranker" , \
#     row_number().over(Window.partitionBy(col("submission_date"), col("hacker_id")).orderBy("hacker_id")))\
#     .withColumn("ranker", row_number().over(Window.partitionBy(col("submission_date")).orderBy(col("ranker").desc(), col("hacker_id")))).filter(col("ranker")==lit(1))\
#     .drop(col("ranker"), col("score"), col("submission_id"))


# # maxSubPerDay_df.show()

# start_date = submissions_df.agg(min("submission_date").alias("start_date"))

# submissions_df = submissions_df.crossJoin(start_date)

# uniqueTillDate_df =  submissions_df\
#     .withColumn("duplicate_value", row_number().over(Window.partitionBy(col("submission_date"), col("hacker_id")).orderBy("hacker_id")))\
#     .filter(col("duplicate_value") == lit(1))\
#     .withColumn("maxxer", dense_rank().over(Window.partitionBy(col("hacker_id")).orderBy(col("submission_date"))))\
#     .withColumn("maxxer", 
#         when(
#             col("maxxer") == (date_diff(col("submission_date"), col("start_date"))) + 1,
#             lit(1)
#         ).otherwise(lit(0)))\
#     .groupBy(col("submission_date"))\
#     .agg(sum(col("maxxer")).alias("consistor"))
            
# # uniqueTillDate_df.show()

# joined_df = maxSubPerDay_df.join(uniqueTillDate_df, ["submission_date"])
# joined_df = joined_df.join(hackers_df, ["hacker_id"]).select("submission_date", "consistor", "hacker_id", "name").orderBy("submission_date")
# joined_df.show()

# ---------------------------------------------------------------------------------------------------------------------------
# Sample DataFrames
# df_a = spark.createDataFrame([(1, None), (2, 'None')], ['reqid', 'mastermodelid'])
# df_b = spark.createDataFrame([(2,), (3,), (4,)], ['modelid'])

# # Creating a window spec for generating sequence numbers
# windowSpec = Window.orderBy('reqid')

# # Generating the next sequence of mastermodelid for df_a
# df_a = df_a.withColumn(
#     'mastermodelid',
#      expr("concat('mstc', repeat('0' , 8 - length( cast((row_number() over (order by reqid) + 10) as string) )), row_number() over (order by reqid) + 10 )")
# )

# # Show the result
# df_a.show()
# input("Wadup")

# =======================================================================================================================

# ('Team_1', 'Team_2', 'Winner')             =>>     ('team', 'matchesPlayed', 'wins', 'losses')
# ('India', 'SL', 'India')                           ('India', 2, 2, 0)
# ('SL', 'Aus', 'Aus')                               ('SL', 2, 0, 2)
# ('SA', 'Eng', 'Eng')                               ('SA', 1, 0, 1)
# ('Eng', 'NZ', 'NZ')                                ('Eng', 2, 1, 1)
# ('Aus', 'India', 'India')                          ('Aus', 2, 1, 1)
# 			                                             ('NZ', 1, 1, 0)

# MYSQL ---------------------------------------------------------------------------------------------------------------------------

# cur.execute("DROP TABLE IF EXISTS MatchResults;")
# cur.execute("""CREATE TABLE MatchResults (
#     Team_1 VARCHAR(50),
#     Team_2 VARCHAR(50),
#     Winner VARCHAR(50)
# );""")
# cur.execute("""INSERT INTO MatchResults (Team_1, Team_2, Winner) VALUES
# ('India', 'SL', 'India'),
# ('SL', 'Aus', 'Aus'),
# ('SA', 'Eng', 'Eng'),
# ('Eng', 'NZ', 'NZ'),
# ('Aus', 'India', 'India');""")

# con.commit()

# cur.execute("""
#             with cte1 as (
#               select Team_1, count(1) from MatchResults group by Team_1
#             ),
#             cte2 as (
#               select Team_2, count(1) from MatchResults group by Team_2
#             ),
#             cte3 as (
#               select * from cte1 union all select * from cte2
#             ),
#             wins as (
#               select Winner as team, count(1) as wins from MatchResults group by Winner
#             ),
#             matches_played as (
#               select Team_1 as team, count(1) as matchesPlayed from cte3 group by Team_1
#             )
            
#             select * from MatchResults
            
#             """)
# mysql_print()

# =======================================================================================================================

# ('order_id', 'customer_id', 'order_date', 'order_amount')     =>>     (datetime.date(2022, 1, 1), 0, 3)
# (1, 100, datetime.date(2022, 1, 1), Decimal('2000.00'))               (datetime.date(2022, 1, 2), 1, 2)
# (2, 200, datetime.date(2022, 1, 1), Decimal('2500.00'))               (datetime.date(2022, 1, 3), 2, 1)
# (3, 300, datetime.date(2022, 1, 1), Decimal('2100.00'))
# (4, 100, datetime.date(2022, 1, 2), Decimal('2000.00'))
# (5, 400, datetime.date(2022, 1, 2), Decimal('2200.00'))
# (6, 500, datetime.date(2022, 1, 2), Decimal('2700.00'))
# (7, 100, datetime.date(2022, 1, 3), Decimal('3000.00'))
# (8, 400, datetime.date(2022, 1, 3), Decimal('1000.00'))
# (9, 600, datetime.date(2022, 1, 3), Decimal('3000.00'))

# MYSQL -----------------------------------------------------------------------------------------------------------------

# cur.execute("DROP TABLE IF EXISTS orders;")
# cur.execute("""
#             CREATE TABLE orders (
#     order_id INT PRIMARY KEY,
#     customer_id INT,
#     order_date DATE,
#     order_amount DECIMAL(10, 2)
# );
#             """)
# cur.execute("""
#             INSERT INTO orders (order_id, customer_id, order_date, order_amount) VALUES
# (1, 100, '2022-01-01', 2000.00),
# (2, 200, '2022-01-01', 2500.00),
# (3, 300, '2022-01-01', 2100.00),
# (4, 100, '2022-01-02', 2000.00),
# (5, 400, '2022-01-02', 2200.00),
# (6, 500, '2022-01-02', 2700.00),
# (7, 100, '2022-01-03', 3000.00),
# (8, 400, '2022-01-03', 1000.00),
# (9, 600, '2022-01-03', 3000.00);
#             """)

# con.commit()

# cur.execute("""
#             with cte1 as (
#               select *, row_number() over (partition by customer_id) as lagger
#             from orders
#             ),
#             repeats as (
#               select order_date, count(1) as repeats from cte1 where lagger <> 1 group by order_date
#             ),
#             new_custs as (
#               select order_date, count(1) as new_customers from cte1 where lagger = 1 group by order_date
#             ),
#             distinct_dates as (
#               select distinct(order_date) as order_date from orders
#             )
#             select dd.order_date, coalesce(repeats, 0) as repeats, coalesce(new_customers, 0) as new_customers from distinct_dates dd
#             left join repeats a on a.order_date = dd.order_date
#             left join new_custs b on b.order_date = dd.order_date
#             """)
# mysql_print()

# =======================================================================================================================
# Scenario Template
# =======================================================================================================================

# +----------+----------+                                       
# | sell_date|   product|            ==>>            +----------+--------------------+---------+
# +----------+----------+                            | sell_date|            products|null_sell|


# SPARK ---------------------------------------------------------------------------------------------------------------------------

schema = StructType([
    StructField("Source", StringType(), nullable=False),
    StructField("Destination", StringType(), nullable=False),
    StructField("Distance", IntegerType(), nullable=False)
])

# Create the data
data = [
    ("Mumbai", "Pune", 150),
    ("Pune", "Mumbai", 150),
    ("Mumbai", "Pune", 150),
    ("Delhi", "Agra", 200),
    ("Agra", "Delhi", 200),
    ("Delhi", "Jaipur", 250),
    ("Jaipur", "Delhi", 250)
]

# Create the DataFrame
df = spark.createDataFrame(data, schema=schema)

# Show the DataFrame
df.show()

df.withColumn("pseudoSource", when(df.Destination > df.Source, df.Source).otherwise(df.Destination))\
  .withColumn("pseudoDest", when(df.Destination > df.Source, df.Destination).otherwise(df.Source))\
  .groupBy(col("pseudoSource"), col("pseudoDest")).agg(count(lit(1)).alias("Total_Trips"), sum(df.Distance).alias("Total_Distance"))\
  .selectExpr("pseudoSource as Source", "pseudoDest as Destination", "Total_Trips", "Total_Distance")\
  .show()
  
# df1=df.select('Source','Distance')
# df2=df.select('Destination','Distance')
# dff=df1.unionAll(df2)
# dff.show()
# res=dff.groupby('Source').agg(count('*').alias('total_trip'),sum('Distance').alias('Total_dist'))
# res=res.withColumnRenamed('Source','Source1')
# fin=res.join(df,res['Source1']==df['Source'],'inner').select('Source1','Destination','total_trip','Total_dist')
# fin.dropDuplicates(['total_trip']).show()
