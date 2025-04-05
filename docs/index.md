# Welcome to Docs

Feel free to contribute by opening a PR to this repository

Resources:

* For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Services in CDH VM
List services
```
service --status-all
```
Service names can be found by listing init.d dir
```
ll /etc/init.d/
```
Restarting a service
```
sudo service hadoop-yarn-resourcemanager restart
```

## Listing applications (Yarn)

Yarn WebUI - http://node_ip:8088/cluster
Job history - http://node_ip:19888/jobhistory
```
yarn application -list 
yarn application -kill application_1736085557915_0006
```

## Running Mysql 8.0 using docker
```
docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=pass -d -p 3306:3306 mysql:8.0
```
```
mysql -uroot -ppass -h127.0.0.1
mysql -uroot -ppass -hlocalhost --protocol=TCP
```
