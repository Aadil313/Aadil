mysql> create table workers(worker_id int primary key,first_name varchar(20),last_name varchar(15),salary int,joining_date datetime,department varchar(20));
Query OK, 0 rows affected (0.35 sec)

mysql> create table bonus(worker_ref_id int,bonus_date datetime,bonus_amount int,foreign key(worker_ref_id
    -> )references workers(worker_id));
ERROR 1050 (42S01): Table 'bonus' already exists
mysql> create table bonus1(worker_ref_id int,bonus_date datetime,bonus_amount int,foreign key(worker_ref_id )references workers(worker_id));
Query OK, 0 rows affected (0.42 sec)

mysql> insert valuemysql> 
mysql> insert into wokers(1,"monika","arora",10000,"2014-02-20 09:00:00",HR);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '1,"monika","arora",10000,"2014-02-20 09:00:00",HR)' at line 1
mysql> insert into wokers(1,"monika","arora",10000,"2014-02-20 09:00:00","HR");
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '1,"monika","arora",10000,"2014-02-20 09:00:00","HR")' at line 1
mysql> insert into workers values(1,"monika","arora",10000,"2014-02-20 09:00:00","HR");
Query OK, 1 row affected (0.05 sec)

mysql> insert into workers values(1,"nitha","varma",20000,"2014-02-10 08:00:00","HR");
ERROR 1062 (23000): Duplicate entry '1' for key 'PRIMARY'
mysql> insert into workers values(2,"nitha","varma",20000,"2014-02-10 08:00:00","HR");
Query OK, 1 row affected (0.05 sec)

mysql> insert into workers values(3,"vishal","singh",30000,"2014-02-15 08:20:00","HR");
Query OK, 1 row affected (0.06 sec)

mysql> insert into workers values(4,"amith","sanjay",40000,"2014-03-25 06:20:00","HR");
Query OK, 1 row affected (0.06 sec)

mysql> insert into workers values(5,"arun","kumar",50000,"2014-03-15 06:24:00","admin");
Query OK, 1 row affected (0.05 sec)

mysql> insert into workers values(6,"anjana","bhatti",60000,"2014-04-15 06:50:00","admin");
Query OK, 1 row affected (0.05 sec)

mysql> insert into workers values(7,"anitha","kumari",70000,"2015-09-28 07:40:20","account");
Query OK, 1 row affected (0.05 sec)

mysql> insert into workers values(8,"rohith","mehra",80000,"2015-10-22 07:20:30","account");
Query OK, 1 row affected (0.05 sec)

mysql> select * from workers;
+-----------+------------+-----------+--------+---------------------+------------+
| worker_id | first_name | last_name | salary | joining_date        | department |
+-----------+------------+-----------+--------+---------------------+------------+
|         1 | monika     | arora     |  10000 | 2014-02-20 09:00:00 | HR         |
|         2 | nitha      | varma     |  20000 | 2014-02-10 08:00:00 | HR         |
|         3 | vishal     | singh     |  30000 | 2014-02-15 08:20:00 | HR         |
|         4 | amith      | sanjay    |  40000 | 2014-03-25 06:20:00 | HR         |
|         5 | arun       | kumar     |  50000 | 2014-03-15 06:24:00 | admin      |
|         6 | anjana     | bhatti    |  60000 | 2014-04-15 06:50:00 | admin      |
|         7 | anitha     | kumari    |  70000 | 2015-09-28 07:40:20 | account    |
|         8 | rohith     | mehra     |  80000 | 2015-10-22 07:20:30 | account    |
+-----------+------------+-----------+--------+---------------------+------------+
8 rows in set (0.00 sec)

mysql> insert into bonus1(1,"2016-05-25 07:00:00",5000);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '1,"2016-05-25 07:00:00",5000)' at line 1
mysql> insert into bonus1 values(1,"2016-05-25 07:00:00",5000);
Query OK, 1 row affected (0.05 sec)

mysql> insert into bonus1 values(2,"2016-05-22 07:30:30",4000);
Query OK, 1 row affected (0.05 sec)

mysql> insert into bonus1 values(3,"2016-04-29 08:40:30",3000);
Query OK, 1 row affected (0.05 sec)

mysql> insert into bonus1 values(4,"2016-10-31 08:15:30",6000);
Query OK, 1 row affected (0.05 sec)

mysql> insert into bonus1 values(5,"2016-12-30 07:50:40",7000);
Query OK, 1 row affected (0.06 sec)

mysql> select * from bonus1;
+---------------+---------------------+--------------+
| worker_ref_id | bonus_date          | bonus_amount |
+---------------+---------------------+--------------+
|             1 | 2016-05-25 07:00:00 |         5000 |
|             2 | 2016-05-22 07:30:30 |         4000 |
|             3 | 2016-04-29 08:40:30 |         3000 |
|             4 | 2016-10-31 08:15:30 |         6000 |
|             5 | 2016-12-30 07:50:40 |         7000 |
+---------------+---------------------+--------------+
5 rows in set (0.00 sec)

mysql> select first_name as WORKER_NAME from workers;
+-------------+
| WORKER_NAME |
+-------------+
| monika      |
| nitha       |
| vishal      |
| amith       |
| arun        |
| anjana      |
| anitha      |
| rohith      |
+-------------+
8 rows in set (0.00 sec)

mysql> select upper(first_name) from workers;
+-------------------+
| upper(first_name) |
+-------------------+
| MONIKA            |
| NITHA             |
| VISHAL            |
| AMITH             |
| ARUN              |
| ANJANA            |
| ANITHA            |
| ROHITH            |
+-------------------+
8 rows in set (0.01 sec)

mysql> select distinct department from workers;
+------------+
| department |
+------------+
| HR         |
| admin      |
| account    |
+------------+
3 rows in set (0.00 sec)

mysql> select substring(first_name 1,3) from workers;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '1,3) from workers' at line 1
mysql> select substring(first_name, 1,3) from workers;
+----------------------------+
| substring(first_name, 1,3) |
+----------------------------+
| mon                        |
| nit                        |
| vis                        |
| ami                        |
| aru                        |
| anj                        |
| ani                        |
| roh                        |
+----------------------------+
8 rows in set (0.00 sec)

mysql> select RTRIM(first_name) from workers;
+-------------------+
| RTRIM(first_name) |
+-------------------+
| monika            |
| nitha             |
| vishal            |
| amith             |
| arun              |
| anjana            |
| anitha            |
| rohith            |
+-------------------+
8 rows in set (0.00 sec)

mysql> select replace(first_name,"A","a") from workers;
+-----------------------------+
| replace(first_name,"A","a") |
+-----------------------------+
| monika                      |
| nitha                       |
| vishal                      |
| amith                       |
| arun                        |
| anjana                      |
| anitha                      |
| rohith                      |
+-----------------------------+
8 rows in set (0.00 sec)

mysql> select replace(first_name,"a","A") from workers;
+-----------------------------+
| replace(first_name,"a","A") |
+-----------------------------+
| monikA                      |
| nithA                       |
| vishAl                      |
| Amith                       |
| Arun                        |
| AnjAnA                      |
| AnithA                      |
| rohith                      |
+-----------------------------+
8 rows in set (0.00 sec)

mysql> select CONCAT(first_name," ",last_name) as COMPLETE_NAME workers;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'workers' at line 1
mysql> select CONCAT(first_name," ",last_name) as COMPLETE_NAME from workers;
+---------------+
| COMPLETE_NAME |
+---------------+
| monika arora  |
| nitha varma   |
| vishal singh  |
| amith sanjay  |
| arun kumar    |
| anjana bhatti |
| anitha kumari |
| rohith mehra  |
+---------------+
8 rows in set (0.00 sec)

mysql> select * from workers order by first_name asc;
+-----------+------------+-----------+--------+---------------------+------------+
| worker_id | first_name | last_name | salary | joining_date        | department |
+-----------+------------+-----------+--------+---------------------+------------+
|         4 | amith      | sanjay    |  40000 | 2014-03-25 06:20:00 | HR         |
|         7 | anitha     | kumari    |  70000 | 2015-09-28 07:40:20 | account    |
|         6 | anjana     | bhatti    |  60000 | 2014-04-15 06:50:00 | admin      |
|         5 | arun       | kumar     |  50000 | 2014-03-15 06:24:00 | admin      |
|         1 | monika     | arora     |  10000 | 2014-02-20 09:00:00 | HR         |
|         2 | nitha      | varma     |  20000 | 2014-02-10 08:00:00 | HR         |
|         8 | rohith     | mehra     |  80000 | 2015-10-22 07:20:30 | account    |
|         3 | vishal     | singh     |  30000 | 2014-02-15 08:20:00 | HR         |
+-----------+------------+-----------+--------+---------------------+------------+
8 rows in set (0.00 sec)

mysql> select * from worker where first_name in ("amith","anitha");
Empty set (0.00 sec)

mysql> select * from workers where first_name in ("amith","anitha");
+-----------+------------+-----------+--------+---------------------+------------+
| worker_id | first_name | last_name | salary | joining_date        | department |
+-----------+------------+-----------+--------+---------------------+------------+
|         4 | amith      | sanjay    |  40000 | 2014-03-25 06:20:00 | HR         |
|         7 | anitha     | kumari    |  70000 | 2015-09-28 07:40:20 | account    |
+-----------+------------+-----------+--------+---------------------+------------+
2 rows in set (0.00 sec)

mysql> 
