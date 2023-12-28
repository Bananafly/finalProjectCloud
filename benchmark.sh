#!/bin/bash

single_public= #hostname on single node, cant do because no AWS
manager_public= #hostname on manager node, cant do because no AWS


#single benchmark
sudo sysbench oltp_read_write --table-size=100000 --db-driver=mysql --mysql-db=sakila --mysql-user=test --mysql-password=test --mysql-host=${single_public} prepare
sudo sysbench oltp_read_write --table-size=100000 --db-driver=mysql --mysql-db=sakila --mysql-user=test --mysql-password=test --mysql-host=${single_public} run
sudo sysbench oltp_read_write --table-size=100000 --db-driver=mysql --mysql-db=sakila --mysql-user=test --mysql-password=test --mysql-host=${single_public} cleanup


#manager benchmark
sudo sysbench oltp_read_write --table-size=100000 --db-driver=mysql --mysql-db=sakila --mysql-user=test --mysql-password=test --mysql-host=${manager_public} --mysql_storage_engine=ndbcluster prepare
sudo sysbench oltp_read_write --table-size=100000 --db-driver=mysql --mysql-db=sakila --mysql-user=test --mysql-password=test --mysql-host=${manager_public} --mysql_storage_engine=ndbcluster run
sudo sysbench oltp_read_write --table-size=100000 --db-driver=mysql --mysql-db=sakila --mysql-user=test --mysql-password=test --mysql-host=${manager_public} --mysql_storage_engine=ndbcluster cleanup