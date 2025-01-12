# Welcome to week 8

## Day 2
* Date - 20250112
* Video - 14 serialized deep dive file formats parquet

### Sqoop fetch-size
By default sqoop imports records in batches of 1000, can have custom value depending on the usecase and resources available, used for performance tuning. (No one value fits all - trial & error)

### Hive Handson (Basic insert)
```
hadoop dfsadmin -safemode leave
```

hive
```
create database odb;
use odb;

create table  otab(id int);
insert into otab values(1000);
select * from otab;

quit;
```
```
hadoop   fs   -ls   /user/hive/warehouse/
hadoop   fs   -ls   /user/hive/warehouse/odb.db
hadoop   fs   -ls   /user/hive/warehouse/odb.db/otab
hadoop   fs   -cat  /user/hive/warehouse/odb.db/otab/000000_0
```


### Hive Handson (No location specified)
```
hadoop dfsadmin -safemode leave

cd
echo 1,zeyo,40 > zfile
echo 2,ravi,70 >> zfile
echo 3,rani,70 >> zfile
```
hive
```
drop database if exists zdb cascade;

create database if not exists zdb;
use zdb;

create table ztab(id int,name string,amt int) row format delimited fields terminated by ',';

load data local inpath '/home/cloudera/zfile' into table ztab;

select * from ztab;
select * from ztab where id>1;

quit;
```
```
hadoop    fs   -ls    /user/hive/warehouse/zdb.db/ztab
```
Alt: One liner for hive
```
hive -e "drop database if exists odb cascade; create database if not exists odb; use odb; create table if not exists otab(id int); insert into otab values(2000); select * from otab;"
```

### Hive Handson (Specifying location)

```
hadoop dfsadmin -safemode leave

cd
echo 1,zeyo,40 > zfile
echo 2,ravi,70 >> zfile
echo 3,rani,70 >> zfile

hadoop  fs   -mkdir  /user/cloudera/ddir
hadoop  fs   -put   /home/cloudera/zfile  /user/cloudera/ddir/
```

hive
```
drop database if exists ldb cascade;
create database if not exists ldb;
use ldb;

create table ltab(id int,name string,amt int) row format delimited fields terminated by ',' location '/user/cloudera/ddir';

select * from ltab;
select * from ltab where id > 1;
```

Alt: One liner for hive
```
hive -e "drop database if exists ldb cascade; create database if not exists ldb; use ldb; create table ltab(id int,name string,amt int) row format delimited fields terminated by ',' location '/user/cloudera/ddir';select * from ltab;select * from ltab where id > 1;"
```

### Task
* Execute above handson

### Extra notes
* Multiple tables can have same location specified during hive table creation
* Performance tuning for sqoop
    * https://medium.com/swlh/performance-tuning-apache-sqoop-512242a58df5
