# Week 9


## Day 2
```
load data local inpath ( edge node )
load data inpath - (in cluster hdfs)

no extension = flat file

static partition (insert)-
table to table insertion, explicitly mentioning the partition name
insert into sitab partition(country='INDIA') select id,name,chk from helptab where country='IND';

dynamic partition (insert)-
insert into dyntab partition(country) select id,name,chk,country from helptab;
(Last col in select is the source for the partition to be created, in above case country)

sqoop incremental -
--incremental append --check-column id --last-value 0

sqoop job --create job_name -- import --connect

sqoop job --show job_name
```

## Revision
* PPT
https://docs.google.com/presentation/d/1JC_l79NxNI7Cl21gVblJ0EPJ3wuris3I/edit?usp=sharing&ouid=111124481208102386307&rtpof=true&sd=true
* Solution
https://drive.google.com/file/d/1lRNtimoCXViESC8WY9I3O9IwnVGN1b9K/view?usp=sharing