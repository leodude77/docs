# ======================================================================================
import os
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DateType, DoubleType, FloatType, \
    TimestampType
import sys

python_path = sys.executable
os.environ['PYSPARK_PYTHON'] = python_path
os.environ['HADOOP_HOME'] = r'C:\Code\docs\docs\big_data\spark\hadoop'
os.environ['JAVA_HOME'] = r'C:\Program Files\Java\jdk1.8.0_202'
######################################################

# os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages com.datastax.spark:spark-cassandra-connector_2.12:3.5.1 pyspark-shell'
# os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-avro_2.12:3.5.4 pyspark-shell'
# os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.4 pyspark-shell'


conf = SparkConf().setAppName("pyspark").setMaster("local[*]").set("spark.driver.host", "localhost").set(
    "spark.default.parallelism", "1")
sc = SparkContext(conf=conf)

spark = SparkSession.builder.getOrCreate()

##################🔴🔴🔴🔴🔴🔴 -> DONT TOUCH ABOVE CODE -- TYPE BELOW ####################################

# manual_schema = StructType([
#     StructField("id", IntegerType(), True),
#     StructField("tdate", StringType(), True),
#     StructField("amount", DoubleType(), True),
#     StructField("category", StringType(), True),
#     StructField("product", StringType(), True),
#     StructField("spendby", StringType(), True)
# ])


# df = spark.read.format("json").load("file4.json").write.mode("overwrite").bucketBy(10, "custno").format("csv").saveAsTable("csv_write_partition_bucketing")
# .write.mode("overwrite").options(path="./parquet_write_partition").partitionBy("state").save()

# df = df.withColumn('results', explode(df.results))

# manual_schema = "id INT, tdate STRING, amount DOUBLE, category STRING, product STRING, spendby STRING"
# data = [
#     (1, '05-26-2011', 200.0, 'Exercise Band', 'Weightlifting', 'credit'),
#     (2, '06-01-2011', 300.4, 'Exercise', 'Gymnastics Pro', 'cash'),
#     (3, '06-05-2011', 100.0, 'Gymnastics', 'Rings', 'credit'),
#     (4, '12-17-2011', 300.0, 'Team Sports', 'Field', 'cash'),
#     (5, '02-14-2011', 200.0, 'Gymnastics', "", 'cash'),
#     (6, '06-05-2011', 100.0, 'Exercise', 'Rings', 'credit'),
#     (7, '12-17-2011', 300.0, 'Team Sports', 'Field', 'cash'),
#     (8, '02-14-2011', 200.0, 'Gymnastics', "", 'cash')
# ]
# df = spark.createDataFrame(data, manual_schema).createTempView("checker")

# print (df.count())
# df.printSchema()
# df.show(truncate=False)

# resulting_df = df.select(df['amount'])
# resulting_df.show(truncate=False)

# result = spark.sql("""
#           select * from checker
#           """)

# result.show()
# print(result.rdd.getNumPartitions())

#--------------------------------------------------------------------------------------------------------------
# data = sc.textFile("usdata.csv")
# (data
#  .filter(lambda x: len(x) > 200)
#  .flatMap(lambda x: x.split(","))
#  .map(lambda x: ("zeyo " + x.replace("-", "")))
#  .saveAsTextFile("outputCheck.txt"))

# schema = "tno string, tdate string, amount double, category string, product string, mode string"
# data1 = spark.read.schema(schema).format("csv").load("dt.txt")
# data1.filter(data1.product.contains("Gymnastics")).write.mode("overwrite").save('outputParquet')
#
# spark.read.load("outputParquet").show()

#--------------------------------------------------------------------------------------------------------------

# from collections import namedtuple
# manCols = namedtuple("columns",["tno", "tdate", "amount", "category", "product", "mode"])
#
# sc.textFile("dt.txt").map(lambda x: x.split(",")).map(lambda x: manCols(x[0], x[1], x[2], x[3], x[4], x[5]))\
#     .filter(lambda x: "Gymnastics" in x.product).foreach(print)

#--------------------------------------------------------------------------------------------------------------
# listr = ["hadoop~hive~spark~sqoop"]
#
# rddr = sc.parallelize(listr)
#
# rddr.flatMap(lambda x: x.split("~")).map(lambda x: ("Tech->" + x.upper() + " Trainer->Sai")).foreach(print)

#--------------------------------------------------------------------------------------------------------------

# from collections import namedtuple
# manCols = namedtuple("columns",["tno", "tdate", "amount", "category", "product", "mode"])
# #
# sc.textFile("dt.txt").map(lambda x: x.split(",")).map(lambda x: manCols(x[0], x[1], x[2], x[3], x[4], x[5])) \
#     .filter(lambda x: "Gymnastics" in x.product).toDF().write.save("2025Parquetwrite")

# spark.read.load("2025Parquetwrite").show()

#--------------------------------------------------------------------------------------------------------------

# csvdf = spark.read.format("csv").option("header","true").load("usdata.csv")
# print()
# print("======== CSV DF==============")
# print()
# # csvdf.show()
#
# csvdf.createOrReplaceTempView("temp")
# spark.sql("select * from temp where age > 20").show()

#--------------------------------------------------------------------------------------------------------------
## SQL PRACTICE



#####SQL PRE CODE#####

data = [
    (0, "06-26-2011", 300.4, "Exercise", "GymnasticsPro", "cash"),
    (1, "05-26-2011", 200.0, "Exercise Band", "Weightlifting", "credit"),
    (2, "06-01-2011", 300.4, "Exercise", "Gymnastics Pro", "cash"),
    (3, "06-05-2011", 100.0, "Gymnastics", "Rings", "credit"),
    (4, "12-17-2011", 300.0, "Team Sports", "Field", "cash"),
    (5, "02-14-2011", 200.0, "Gymnastics", None, "cash"),
    (6, "06-05-2011", 100.0, "Exercise", "Rings", "credit"),
    (7, "12-17-2011", 300.0, "Team Sports", "Field", "cash"),
    (8, "02-14-2011", 200.0, "Gymnastics", None, "cash"),
    # (9, "06-12-2011", 200.0, "  Exercise   ", None, "credit")
]

df = spark.createDataFrame(data, ["id", "tdate", "amount", "category", "product", "spendby"])


# data2 = [
#     (4, "12-17-2011", 300.0, "Team Sports", "Field", "cash"),
#     (5, "02-14-2011", 200.0, "Gymnastics", None, "cash"),
#     (6, "02-14-2011", 200.0, "Winter", None, "cash"),
#     (7, "02-14-2011", 200.0, "Winter", None, "cash")
# ]
#
# df1 = spark.createDataFrame(data2, ["id", "tdate", "amount", "category", "product", "spendby"])
#
#
data4 = [
    (1, "raj"),
    (2, "ravi"),
    (3, "sai"),
    (5, "rani")
]

cust = spark.createDataFrame(data4, ["id", "name"])


data3 = [
    (1, "mouse"),
    (3, "mobile"),
    (7, "laptop")
]

prod = spark.createDataFrame(data3, ["id", "product"])

# df.show()
# df1.show()
# cust.show()
# prod.show()

# df.createOrReplaceTempView("df")
# df1.createOrReplaceTempView("df1")
# cust.createOrReplaceTempView("cust")
# prod.createOrReplaceTempView("prod")


# spark.sql("select id,tname from df").show()
# spark.sql("select * from df where category='Exercise'").show()
# spark.sql("select id,tdate,category,spendby from df where category='Exercise' and spendby='cash'").show()
# spark.sql("select id,tdate,category,spendby from df where category IN ('Exercise','Gymnastics')").show()
# spark.sql("select * from df where product LIKE '%Gymnastics%'").show()
# spark.sql("select * from df where category <> 'Exercise'").show()
# spark.sql("select * from df where category NOT IN ('Exercise','Gymnastics')").show()
# spark.sql("select * from df where product IS null").show()
# spark.sql("select * from df where product is not null").show()
# spark.sql("select max(id), min(id) from df").show()
# spark.sql("select count(1) from df").show()

# spark.sql("select *, case when spendby='cash' then 1 when spendby='somethingelse' then 2 else 0 end as status from df").show()
# spark.sql("select *, CONCAT(id,'-',category) as condata from df").show()
# spark.sql("select *, CONCAT_WS('-',id,category,product) as condata from df").show()
# spark.sql("select category, lower(category), upper(category) from df").show()
# spark.sql("select amount, CEIL(amount), ROUND(amount) from df").show()
# spark.sql("select product, COALESCE(product, 'NA') from df").show()
# spark.sql("select category, TRIM(category) from df").show()
# spark.sql("select distinct category,spendby from df").show()
# spark.sql("select category, substr(category, 0, 6) from df").show()
# spark.sql("select product, split(product, ' ')[1] from df").show()
# spark.sql("select product, split(product, ' ')[1] from df").show()

# spark.sql("select * from df union select * from df1").show()
# spark.sql("select category, spendby, sum(amount), count(1), max(amount) from (select * from df union select * from df1) group by spendby, category").show()

# spark.sql("select category, amount, ROW_NUMBER() OVER(partition by category order by amount desc) as row_number from df").show()
# spark.sql("select category, amount, lead(amount, 2, 'N/A') OVER(partition by category order by amount desc) from df").show()

# spark.sql("select category, count(1) from df group by category having count(1)>1").show()

# spark.sql("select a.id, name, product from cust a inner join prod b on a.id=b.id").show()
# spark.sql("select * from cust a full join prod b on a.id=b.id").show()
# spark.sql("select * from cust a left anti join prod b on a.id=b.id").show()

# import time
# time.sleep(300)

#--------------------------------------------------------------------------------------------------------------

# df.select("id","tdate").show()
# df.drop("id","tdate").show()
#
# df.filter("category='Exercise' and spendby='cash'").show()
# df.filter("category='Exercise' or spendby='cash'").show()
# df.filter("product LIKE '%Gymnastics%'").show()
# df.filter("category IN ('Exercise','Gymnastics')").show()
# df.filter("product IS NULL").show()
# df.filter("product IS NOT NULL").show()
#
# df.filter(" category <> 'Exercise' ").show()

# df.selectExpr("concat(product, '~zeyo')",
#               "upper(category)","cast(id as int)",
#               "split(tdate, '-')[2] as year",
#               "case when spendby='cash' then 0 else 1 end as status",
#               "to_date(tdate,'dd-mm-yyyy')",
#               "year(to_date(tdate,'dd-mm-yyyy')) as Year"
#               ).show()
#
# df.printSchema()

#--------------------------------------------------------------------------------------------------------------
# 20250301
# df.show()

# (df
    # .withColumn("id", expr("cast(id as int)"))
#     .withColumn("id", df.id.cast("string"))
#     .withColumn("amount", expr("amount+1000"))
#     .withColumn("category", expr("upper(category)"))
    # .withColumn("product", expr("concat(product, '~zeyo')"))
#     .withColumn("product", concat(df.product, lit('~zryo')))
    # .withColumn("tdate", expr("year(to_date(tdate, 'dd-mm-yyyy'))"))
#     .withColumn("tdate", year(to_date(df.tdate, "dd-mm-yyyy")))
#     .withColumn("status", expr("case when spendby == 'cash' then 1 else 0 end"))
    # .withColumn("status", when(df.spendby == 'cash', 1).otherwise(0))
#     .withColumnRenamed("tdate", "year")
#     .show()
# )

# cust.join(prod, ["id"], "inner").show()
# cust.join(prod, ["id"], "outer").show()
# cust.join(prod, ["id"], "left").show()
# cust.join(prod, ["id"], "right").show()
# cust.join(prod, cust.id == prod.id).select(cust.id).show()

# data5 = [
#     (1, "A"),
#     (2, "B"),
#     (3, "C"),
#     (4, "A")
# ]

# tab1 = spark.createDataFrame(data5, ["id", "name"])

# data6 = [
#     (1, "A"),
#     (2, "B"),
#     (4, "X"),
#     (5, "F")
# ]

# tab2 = spark.createDataFrame(data6, ["id", "name1"])

# (tab1.join(tab2, ["id"], "outer").withColumn("status", expr("case when name == name1 then null when name is null then 'New in target' when name1 is null then 'New in source' else 'Mismatch' end"))
#  .where("status is not null").select("id", "status")
#  .show())

#--------------------------------------------------------------------------------------------------------------
# 20250302

# data5 = [
#     (1, "S1"),
#     (2, "S2"),
#     (3, "S3"),
#     (5, "S4")
# ]

# tab1 = spark.createDataFrame(data5, ["id", "name"])

# data6 = [
#     (1, "Mouse"),
#     (3, "Mobile"),
#     (7, "Laptop")
# ]

# tab2 = spark.createDataFrame(data6, ["id1", "accessory"])

# (tab1.join(tab2, tab1.id == tab2.id1, "outer").withColumn("id", expr("case when id is null then id1 else id end"))
#  .show())

# tab1.join(tab2, tab1.id == tab2.id1, "outer").createOrReplaceTempView("tab3")
# spark.sql("update tab3 set id = id1 where id is null").show()

# -----------------------------------------------------------------------------------------------------------------
# data5 = [
#     ("A", "AA"),
#     ("B", "BB"),
#     ("C", "CC"),
#     ("AA", "AAA"),
#     ("BB", "BBB"),
#     ("CC", "CCC")
# ]

# tab1 = spark.createDataFrame(data5, ["child", "parent"])

# tab1.alias("df1").join(tab1.alias("df2"), col("df1.child") == col("df2.parent")).drop(col("df1.child")).show()

# -----------------------------------------------------------------------------------------------------------------
# data5 = [
#     (1, "Sai"),
#     (2, "Ravi"),
#     (3, "Ranni"),
#     (5, "Radhan")
# ]

# tab1 = spark.createDataFrame(data5, ["id", "name"])

# data6 = [
#     (1, "Mouse"),
#     (3, "Mobile"),
#     (7, "Laptop")
# ]

# tab2 = spark.createDataFrame(data6, ["id", "accessory"])

# (tab1.join(tab2, ["id"], "anti").show())

#--------------------------------------------------------------------------------------------------------------
# 20250308

# data5 = [
#     (1, "Sai"),
#     (2, "Ravi"),
#     (3, "Ranni"),
#     (5, "Radhan")
# ]

# tab1 = spark.createDataFrame(data5, ["id", "name"])

# data6 = [
#     (1, "Mouse"),
#     (3, "Mobile"),
#     (7, "Laptop")
# ]

# tab2 = spark.createDataFrame(data6, ["id", "accessory"])
# tab1.crossJoin(tab2).show()

# -----------------------------------------------------------------------------------------------------------------

# data = [
#     ('sai', 'chn', 1),
#     ('sai', 'hyd', 2),
#     ('sai', 'chn', 2),
#     ('sai', 'hyd', 1),
#     ('zeyo', 'chn', 2),
#     ('zeyo', 'hyd', 3),
#     ('zeyo', 'chn', 2),
#     ('zeyo', 'hyd', 1)

# ]

# # Create a DataFrame using the data and specifying the column names
# df = spark.createDataFrame(data, ["name", "city", "amount"]).coalesce(1)

# # Show the DataFrame
# df.show()

# print("======== SUM PER EACH NAME=========")
# aggdf1 = df.groupBy( "name" ).agg(  sum("amount").alias("total") )
# aggdf1.show()

# print("======== SUM AND COUNT PER EACH NAME=========")
# aggdf2 = df.groupBy("name").agg(

#                                     sum("amount").alias("total")  ,

#                                     count("amount").alias("cnt")

# )
# aggdf2.show()

# -----------------------------------------------------------------------------------------------------------------

# data = [
#     ('sai', 'chn', 1),
#     ('sai', 'hyd', 2),
#     ('sai', 'chn', 2),
#     ('sai', 'hyd', 1),
#     ('zeyo', 'chn', 2),
#     ('zeyo', 'hyd', 3),
#     ('zeyo', 'chn', 2),
#     ('zeyo', 'hyd', 1)
# ]

# Create a DataFrame using the data and specifying the column names
# df = spark.createDataFrame(data, ["name", "city", "amount"]).coalesce(1)

# Show the DataFrame
# df.show()

# print("======== SUM PER EACH NAME=========")
# aggdf1 = df.groupBy( "name" ).agg(  sum("amount").alias("total") )
# aggdf1.show()

# print("======== SUM AND COUNT PER EACH NAME=========")
# aggdf2 = df.groupBy("name").agg(
#     sum("amount").alias("total")  ,
#     count("amount").alias("cnt")
# )
# aggdf2.show()


# print("========== SUM  per each name and city=======")
# aggdf3 = df.groupBy( "name" , "city" ).agg(
#                                     sum("amount").alias("total") , 
#                                     count("amount").alias("cnt")
#                         )
# aggdf3.show()

# @udf
# def splitter(col):
#     return str(col)[1:-1]
    
# print("========== collect_list, group by 1 and 2 cols =======")
# df.groupBy(col("name")).agg(collect_list(df.amount)).show()
# df.groupBy(col("name"), df.city).agg( splitter(collect_list(df.amount)).alias("List") ).show()

#--------------------------------------------------------------------------------------------------------------
# 20250309

# from pyspark.sql.window import Window

# data = [
#         ("DEPT1", 1000),
#         ("DEPT1", 700),
#         ("DEPT1", 500),
#         ("DEPT2", 400),
#         ("DEPT2", 200),
#         ("DEPT3", 500),
#         ("DEPT3", 200)]

# columns = ["dept", "salary"]

# df = spark.createDataFrame(data, columns)

# df.show()

# ranker_window = Window.partitionBy("dept").orderBy(col("salary").desc())

# df.withColumn("ranker", dense_rank().over(ranker_window) )\
#     .where("ranker = 2").drop("ranker").show()

# --------------------------------------------------------------------------------------------------------------------------
# REVISION SPARK until now

# filerdd = sc.textFile("file1.txt")

# gymrdd = filerdd.filter(lambda x : 'Gymnastics' in x)

# print("====== FILTER GYMNASTICS=====")
# print()




# mapsplit = gymrdd.map( lambda x  :  x.split(",") )

# from collections import namedtuple

# columns = namedtuple('columns', ['txnno','txndate','custno','amount','category','product','city','state','spendby'])

# schemardd = mapsplit.map(lambda x : columns(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]))

# prodfilted = schemardd.filter(lambda x : 'Gymnastics' in x.product)

# prodfilted.foreach(print)


# schemadf = prodfilted.toDF()

# print()
# print("=====SCHEMA DF======")
# print()
# schemadf.show(5)



# csvdf = spark.read.format("csv").option("header","true").load("file3.txt")
# print()
# print("=====csvdf DF======")
# print()
# csvdf.show(5)



# jsondf = spark.read.format("json").load("file4.json").select('txnno','txndate','custno','amount','category','product','city','state','spendby')
# print()
# print("=====jsondf DF======")
# print()
# jsondf.show(5)



# parquetdf = spark.read.load("file5.parquet")
# print()
# print("=====parquetdf DF======")
# print()
# parquetdf.show(5)


# uniondf = schemadf.union(csvdf).union(jsondf).union(parquetdf)
# print()
# print("=====uniondf DF======")
# print()
# uniondf.show(5)



# procdf =(
#         uniondf.withColumn("txndate" , expr("split(txndate,'-')[2]"))
#                 .withColumnRenamed("txndate", "year")
#                 .withColumn("status",expr("case when spendby='cash' then 0 else 1 end"))
#                 .filter("txnno>50000")

# )

# print()
# print("=====procdf DF======")
# print()
# procdf.show(5)



# aggdf = procdf.groupBy("category").agg(sum("amount").alias("total"))

# print()
# print("=====aggdf DF======")
# print()
# aggdf.show()


# data4 = [
#         (1, "raj"),
#         (2, "ravi"),
#         (3, "sai"),
#         (5, "rani")
# ]

# cust = spark.createDataFrame(data4, ["id", "name"]).coalesce(1)
# cust.show()

# data3 = [
#         (1, "mouse"),
#         (3, "mobile"),
#         (7, "laptop")
# ]



# prod = spark.createDataFrame(data3, ["id", "product"]).coalesce(1)
# prod.show()



# inner = cust.join(prod, ["id"], "inner")
# print()
# print("======INNER=====")
# print()
# inner.show()


# left = cust.join(prod, ["id"], "left")
# print()
# print("======left=====")
# print()
# left.show()




# right = cust.join(prod, ["id"], "right")
# print()
# print("======right=====")
# print()
# right.show()


# full = cust.join(prod, ["id"], "full")
# print()
# print("======full=====")
# print()
# full.show()




# anti = cust.join(prod, ["id"], "left_anti")
# print()
# print("======anti=====")
# print()
# anti.show()



# cross = cust.crossJoin(prod)
# print()
# print("======cross=====")
# print()
# cross.show()



# from pyspark.sql.functions import *
# data = [
#         ("DEPT1", 1000),
#         ("DEPT1", 700),
#         ("DEPT1", 500),
#         ("DEPT2", 400),
#         ("DEPT2", 200),
#         ("DEPT3", 500),
#         ("DEPT3", 200)]

# columns = ["dept", "salary"]

# df = spark.createDataFrame(data, columns)

# df.show()


# ##🔴🔴🔴🔴🔴🔴 STEP 1 --- CREATE THE WINDOW

# from pyspark.sql.window import Window
# deptwindow = Window.partitionBy("dept").orderBy( col("salary").desc() )

# ##🔴🔴🔴🔴🔴🔴 STEP 2 --- APPLYING WITH WINDOW  ON DATAFRAME TO DENSE RANK

# drank = df.withColumn("drank" , dense_rank().over(deptwindow)       )
# drank.show()

# ##🔴🔴🔴🔴🔴🔴 STEP 3  -- FILTER RANK =2
# filrank = drank.filter(" drank = 2 ")
# filrank.show()

#--------------------------------------------------------------------------------------------------------------
# 20250315

# df = spark.read.format("csv").option("header","true").load("usdata.csv")
# df.show()

# fildf = df.filter("state='LA'")
# fildf.show()


# fildf.write.format("json").mode("overwrite").save("jsondata")
#  ## error   append   overwrite   ignore

# print("=====DATA WRITTEN=== GO AND CHECK=====")

# -------------------------------------------------------------------------------------------------------------
# jsondata = """

# {
#     "id": 1,
#     "trainer": "sai",
#     "zeyoAddress": {
#         "permanentAddress": "Hyderabad",
#         "temporaryAddress": "chennai"
#     }

# }
# """

# rdd = sc.parallelize([jsondata])

# df = spark.read.option("multiline","true").json(rdd)
# df.show()

# df.printSchema()

# flatdata = df.select(
#                         "id",
#                         "trainer",
#                         "zeyoAddress.permanentAddress",
#                         "zeyoAddress.temporaryAddress"
# )

# flatdata.show()
# flatdata.printSchema()

#--------------------------------------------------------------------------------------------------------------
# 20250316

# data="""
# {
#     "id": 1,
#     "trainer": "sai",
#     "zeyoAddress": {
#         "user": {
#             "permanentAddress": "hyderabad",
#             "temporaryAddress": "chennai"
#         }
#     }
# }
# """

# rdd = sc.parallelize([data])
# df = spark.read.option("multiline","true").json(rdd)

# df.show()
# df.printSchema()

# flatdata = df.select(
#                     "id",
#                     "trainer",
#                     "zeyoAddress.user.permanentAddress",
#                     "zeyoAddress.user.temporaryAddress",

# )

# flatdata.show()
# flatdata.printSchema()
# # --------------------------------------------------------------------------------------------------------------

# data="""
# {
# 	"id": "000",
# 	"type": "donut",
# 	"name": "Non cream",
# 	"image": {
# 		"url": "images/0001.jpg",
# 		"width": 200,
# 		"height": 200
# 	},
# 	"thumbnail": {
# 		"url": "images/thumbnails/0001.jpg",
# 		"width": 33,
# 		"height": 33
# 	}
# }
# """

# rdd = sc.parallelize([data])
# df = spark.read.option("multiline","true").json(rdd)

# df.show()
# df.printSchema()

# flatdata = df.selectExpr(
#                         "id",
#                         "image.height  as  i_height",
#                         "image.url   as  i_url",
#                         "image.width  as  i_width",
#                         "name",
#                         "thumbnail.height as  t_height",
#                         "thumbnail.url as  t_url",
#                         "thumbnail.width as  t_width",
#                         "type"
# )

# flatdata.show()
# flatdata.printSchema()

# # --------------------------------------------------------------------------------------------------------------

# data="""
# {
#     "id": 1,
#     "trainer": "sai",
#     "zeyoAddress": {
#             "permanentAddress": "hyderabad",
#             "temporaryAddress": "chennai"
#     }
# }
# """

# rdd = sc.parallelize([data])
# df = spark.read.option("multiline","true").json(rdd)

# df.show()
# df.printSchema()

# flatdata = df.select(
    
#                         "id",
#                         "trainer",
#                         "zeyoAddress.permanentAddress",
#                         "zeyoAddress.temporaryAddress"
#   )
# flatdata.show()
# flatdata.printSchema()

# withflat = (
#     df.withColumn( "permanentAddress" , expr("zeyoAddress.permanentAddress"))
#         .withColumn("temporaryAddress", expr("zeyoAddress.temporaryAddress"))
#         .drop("zeyoAddress")
# )

# withflat.show()
# withflat.printSchema()

# # --------------------------------------------------------------------------------------------------------------

# data="""
# {
#     "id": 1,
#     "trainer": "sai",
#     "zeyoAddress": {
#         "user": {
#             "permanentAddress": "hyderabad",
#             "temporaryAddress": "chennai"
#         }
#     }
# }
# """

# rdd = sc.parallelize([data])

# df = spark.read.option("multiline","true").json(rdd)

# df.show()
# df.printSchema()

# withflat = (
#         df.withColumn("permanentAddress", expr("zeyoAddress.user.permanentAddress"))
#         .withColumn("temporaryAddress", expr("zeyoAddress.user.temporaryAddress"))
#         .drop("zeyoAddress")
# )

# withflat.show()
# withflat.printSchema()

# # --------------------------------------------------------------------------------------------------------------

# data="""
# {
# 	"id": "000",
# 	"type": "donut",
# 	"name": "Non cream",
# 	"image": {
# 		"url": "images/0001.jpg",
# 		"width": 200,
# 		"height": 200
# 	},
# 	"thumbnail": {
# 		"url": "images/thumbnails/0001.jpg",
# 		"width": 33,
# 		"height": 33
# 	}
# }
# """

# rdd = sc.parallelize([data])

# df = spark.read.option("multiline","true").json(rdd)
# df.show()
# df.printSchema()

# withflat = (

#              df.withColumn( "i_height" , expr("image.height") )
#              .withColumn( "i_url" , expr("image.url") )
#              .withColumn( "i_width" , expr("image.width") )
#              .withColumn( "t_height" , expr("thumbnail.height") )
#              .withColumn( "t_url" , expr("thumbnail.url") )
#              .withColumn( "t_width" , expr("thumbnail.width") )
#              .drop("image","thumbnail")
# )

# withflat.show()
# withflat.printSchema()

#--------------------------------------------------------------------------------------------------------------
# 20250322
# data="""
# {
#     "id": 1,
#     "trainer": "sai",
#     "zeyoStudents": [
#         "Ankita",
#         "Ajay"
#     ],
#     "zeyoMentors": [
#         "M1",
#         "M2"
#     ]
# }
# """

# rdd = sc.parallelize([data])

# df = spark.read.option("multiline","true").json(rdd)

# df.show()
# df.printSchema()

# df.withColumn("zeyoStudents", explode("zeyoStudents")).withColumn("zeyoMentors", explode("zeyoMentors")).show()
# df.selectExpr("id", "trainer", "explode(zeyoStudents)", "explode(zeyoMentors)").show()

#--------------------------------------------------------------------------------------------------------------
# STRUCT INSIDE ARRAY

# data="""
# {
# 	"org": "zeyobron",
# 	"trainer": "zeyobron",
# 	"location": "Pune",
# 	"users": [{
# 			"userId": 1,
# 			"firstName": "Krish",
# 			"lastName": "Lee",
# 			"phoneNumber": 123456,
# 			"emailAddress": "krish.lee@learningcontainer.com"
# 		},
# 		{
# 			"userId": 2,
# 			"firstName": "racks",
# 			"lastName": "jacson",
# 			"phoneNumber": 123456,
# 			"emailAddress": "racks.jacson@learningcontainer.com"
# 		}
# 	]
# }
# """

# rdd = sc.parallelize([data])

# df = spark.read.option("multiline","true").json(rdd)

# df.show()
# df.printSchema()

# cols = df.withColumn("users", explode("users")).select("users.*").columns
# cols = [ f'users.{c} as {c}' for c in cols]
# print(cols)

# cols.extend(["org", "trainer", "location"])

# df.withColumn("users", explode("users")).selectExpr(cols).show()


#--------------------------------------------------------------------------------------------------------------
# FULL URL CODE

import urllib.request
import ssl

urldata = (

        urllib.request
        .urlopen("https://randomuser.me/api/0.8/?results=10",context=ssl._create_unverified_context())
        .read()
        .decode("utf-8")


)

print(urldata)

rdd = sc.parallelize([urldata])
df = spark.read.json(rdd)

df.show()
df.printSchema()

explodedf = df.withColumn("results",expr("explode(results)"))
explodedf.show()

explodedf.printSchema()

finalexplode =  explodedf.select(
        "nationality",
        "results.user.cell",
        "results.user.dob",
        "results.user.email",
        "results.user.gender",
        "results.user.location.city",
        "results.user.location.state",
        "results.user.location.street",
        "results.user.location.zip",
        "results.user.md5",
        "results.user.name.first",
        "results.user.name.last",
        "results.user.name.title",
        "results.user.password",
        "results.user.phone",
        "results.user.picture.large",
        "results.user.picture.medium",
        "results.user.picture.thumbnail",
        "results.user.registered",
        "results.user.salt",
        "results.user.sha1",
        "results.user.sha256",
        "results.user.username",
        "seed",
        "version"
)

finalexplode.show()
finalexplode.printSchema()
