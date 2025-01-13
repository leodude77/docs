# Welcome to week 8

## Day 1
* Date - 20250111
* Video - 15 hive deep dive hive vs sql
<iframe width="560" height="315" src="https://www.youtube.com/embed/PyZ1Gu8Pxk4?si=82CDyBJmrH-XWKqb" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Sqoop import all tables
Importing all tables present in the same database
=== "Example"
    ```
    sqoop import-all-tables --connect jdbc.. --username root --password cloudera --warehouse-dir /user/cloudera/alltab --exclude-tables tab1,tab2 -m 1
    ```
=== "Try it out"
    ```sql
    hadoop dfsadmin -safemode leave

    mysql -uroot -pcloudera

    create database if not exists alltabdb;
    use alltabdb;
    drop table if exists city1;
    create table city1(id int,name varchar(100),city varchar(100));
    insert into city1 values(1,'sai','chennai');
    insert into city1 values(2,'ravi','hyderabad');
    insert into city1 values(3,'rani','chennai');
    insert into city1 values(4,'vasu','bangalore');

    select * from city1;

    drop table if exists city2;
    create table city2(id int,name varchar(100),city varchar(100));
    insert into city2 values(1,'sai','Delhi');
    insert into city2 values(2,'ravi','Mumbai');

    select * from city2;

    drop table if exists city3;
    create table city3(id int,name varchar(100),city varchar(100));
    insert into city3 values(1,'sai','Kochi');
    insert into city3 values(2,'ravi','Pajk');

    select * from city3;
    exit;

    sqoop import-all-tables --connect jdbc:mysql://localhost/alltabdb --username root --password cloudera --warehouse-dir /user/cloudera/alltab --exclude-tables city1 -m 1
    ```
Seems like internally it runs seperate jobs for each table
![sqoop](../../assets/big_data/Week%208/sqoop_import_all.jpg "sqoop-import-all")

* https://sqoop.apache.org/docs/1.4.0-incubating/SqoopUserGuide.html#id1766722

### Hive intro
#### Hive diagram
![hive-intro](../../assets/big_data/Week%208/hive_diag.jpg "hive-intro")

#### Children of Hive (Tools/Services built on hive)
* Snowflake
* AWS Athena
* AWS Redshift
* Azure Synapse
* Google big query

#### SQL VS HQL

##### ETL
```sql
mysql -uroot -pcloudera

drop database example;
create database example;
use example;
create table tab1(id int, name varchar(100));
insert into tab1 values(1,'name1');
insert into tab1 values(2,'name2');
select * from tab1;
exit;

sqoop import --connect jdbc:mysql://localhost/example --username root --password cloudera --delete-target-dir --target-dir /user/cloudera/example -m 1 --table tab1 --as-parquetfile

hadoop fs -ls /user/cloudera/example
mkdir /home/cloudera/example
hadoop fs -get /user/cloudera/example/01bbbca6-3fbd-4be0-8be1-44de284752aa.parquet /home/cloudera/example
cd /home/cloudera/example
mv 01bbbca6-3fbd-4be0-8be1-44de284752aa.parquet data.parquet

mysql -uroot -pcloudera
use example;
truncate table tab1;
load data local infile '/home/cloudera/example/data.parquet' into table tab1;
select * from tab1;
exit;
```

## Day 2
* Date - 20250112
* Video - 16

### Sqoop fetch-size
By default sqoop imports records in batches of 1000, can have custom value depending on the usecase and resources available, used for performance tuning. (No one value fits all - trial & error)

### Hive
* Hive uses mapreduce engine when certain operations are performed
* Hive has a separate directory in hdfs which is `/user/hive/warehouse` any objects created without specifying location(for a table) land here
* For example, once a table is created within a db the directory would be shown as - `/user/hive/warehouse/db_name.db/table_name`
* DML operations run MR jobs
![insert-hive](../../assets/big_data/Week%208/insert_into_hive_yarn_job.jpg "insert-hive")
* Hive and hdfs dir are interlinked, if changes are done in hdfs, hive reflects the said changes and vice versa
* `describle formatted table_name` can be used to get info including location

#### Hive Handson (Basic insert)

=== "Shortened"
    ```sql title="hive"
    create database odb;
    use odb;

    create table  otab(id int);
    insert into otab values(1000);
    select * from otab;
    ```
    ```sql title="hdfs"
    hadoop   fs   -cat  /user/hive/warehouse/odb.db/otab/000000_0
    ```

=== "Try it out"

    ```sql
    hadoop dfsadmin -safemode leave

    --Hive
    drop database odb cascade;
    create database odb;
    use odb;

    create table  otab(id int);
    insert into otab values(1000);
    select * from otab;

    quit;

    hadoop   fs   -ls   /user/hive/warehouse/
    hadoop   fs   -ls   /user/hive/warehouse/odb.db
    hadoop   fs   -ls   /user/hive/warehouse/odb.db/otab
    hadoop   fs   -cat  /user/hive/warehouse/odb.db/otab/000000_0
    ```


#### Hive Handson (No location specified)
=== "Shortened"
    ```sql title="hive"
    create table ztab(id int,name string,amt int) row format delimited fields terminated by ',';

    load data local inpath '/home/cloudera/zfile' into table ztab;
    ```

    ```sql title="hdfs"
    hadoop    fs   -ls    /user/hive/warehouse/zdb.db/ztab
    ```

    Alt: One liner for hive
    ```sql
    hive -e "drop database if exists odb cascade; create database if not exists odb; use odb; create table if not exists otab(id int); insert into otab values(2000); select * from otab;"
    ```

=== "Try it out"
    ```sql
    hadoop dfsadmin -safemode leave

    cd
    echo 1,zeyo,40 > zfile
    echo 2,ravi,70 >> zfile
    echo 3,rani,70 >> zfile

    --Hive
    drop database if exists zdb cascade;
    create database if not exists zdb;
    use zdb;

    create table ztab(id int,name string,amt int) row format delimited fields terminated by ',';
    load data local inpath '/home/cloudera/zfile' into table ztab;

    select * from ztab;
    select * from ztab where id>1;

    quit;

    hadoop    fs   -ls    /user/hive/warehouse/zdb.db/ztab
    ```

#### Hive Handson (Specifying location)

=== "Shortened"
    ```sql
    hadoop  fs   -mkdir  /user/cloudera/ddir
    hadoop  fs   -put   /home/cloudera/zfile  /user/cloudera/ddir

    create table ltab(id int,name string,amt int) row format delimited fields terminated by ',' location '/user/cloudera/ddir';
    ```

    Alt: One liner for hive
    ```sql
    hive -e "drop database if exists ldb cascade; create database if not exists ldb; use ldb; create table ltab(id int,name string,amt int) row format delimited fields terminated by ',' location '/user/cloudera/ddir';select * from ltab;select * from ltab where id > 1;"
    ```

=== "Try it out"
    ```sql
    hadoop dfsadmin -safemode leave

    cd
    echo 1,zeyo,40 > zfile
    echo 2,ravi,70 >> zfile
    echo 3,rani,70 >> zfile

    --Hive
    drop database if exists ldb cascade;
    exit;

    hadoop  fs   -mkdir  /user/cloudera/ddir
    hadoop  fs   -put   /home/cloudera/zfile  /user/cloudera/ddir/

    --Hive
    create database ldb;
    use ldb;

    create table ltab(id int,name string,amt int) row format delimited fields terminated by ',' location '/user/cloudera/ddir';

    select * from ltab;
    select * from ltab where id > 1;

    describe formatted ltab;
    ```

### Task
* Execute above handson

### Extra notes
* Multiple tables can have same location specified during hive table creation
* Performance tuning for sqoop
    * https://medium.com/swlh/performance-tuning-apache-sqoop-512242a58df5
    * https://community.cloudera.com/t5/Community-Articles/SQOOP-Performance-tuning/ta-p/248260
