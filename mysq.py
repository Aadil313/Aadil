# mysql> select * from peoples;
# +------+-----------+----------+------+--------+---------+
# | id   | firstname | lastname | age  | gender | address |
# +------+-----------+----------+------+--------+---------+
# |   51 | aadil     | mny      |   25 | male   | kollam  |
# |   50 | suhail    | knply    |   24 | male   | kollam  |
# |   54 | remold    | klmsry   |   23 | male   | aluva   |
# |   55 | luslin    | vypin    |   22 | male   | kochi   |
# +------+-----------+----------+------+--------+---------+
# 4 rows in set (0.00 sec)

# mysql> select id,age from peoples;
# +------+------+
# | id   | age  |
# +------+------+
# |   51 |   25 |
# |   50 |   24 |
# |   54 |   23 |
# |   55 |   22 |
# +------+------+
# 4 rows in set (0.00 sec)

# mysql> select * from peoples where id=51;
# +------+-----------+----------+------+--------+---------+
# | id   | firstname | lastname | age  | gender | address |
# +------+-----------+----------+------+--------+---------+
# |   51 | aadil     | mny      |   25 | male   | kollam  |
# +------+-----------+----------+------+--------+---------+
# 1 row in set (0.00 sec)

# mysql> select distinct firstname from peoples;
# +-----------+
# | firstname |
# +-----------+
# | aadil     |
# | suhail    |
# | remold    |
# | luslin    |
# +-----------+
# 4 rows in set (0.00 sec)

# mysql> select * from peoples order by address asc;
# +------+-----------+----------+------+--------+---------+
# | id   | firstname | lastname | age  | gender | address |
# +------+-----------+----------+------+--------+---------+
# |   54 | remold    | klmsry   |   23 | male   | aluva   |
# |   55 | luslin    | vypin    |   22 | male   | kochi   |
# |   51 | aadil     | mny      |   25 | male   | kollam  |
# |   50 | suhail    | knply    |   24 | male   | kollam  |
# +------+-----------+----------+------+--------+---------+
# 4 rows in set (0.00 sec)

# mysql> select * from peoples order by address dsc;
# ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'dsc' at line 1
# mysql> select * from peoples order by address desc;
# +------+-----------+----------+------+--------+---------+
# | id   | firstname | lastname | age  | gender | address |
# +------+-----------+----------+------+--------+---------+
# |   51 | aadil     | mny      |   25 | male   | kollam  |
# |   50 | suhail    | knply    |   24 | male   | kollam  |
# |   55 | luslin    | vypin    |   22 | male   | kochi   |
# |   54 | remold    | klmsry   |   23 | male   | aluva   |
# +------+-----------+----------+------+--------+---------+
# 4 rows in set (0.00 sec)

# mysql> select * from peoples order by lastname desc;
# +------+-----------+----------+------+--------+---------+
# | id   | firstname | lastname | age  | gender | address |
# +------+-----------+----------+------+--------+---------+
# |   55 | luslin    | vypin    |   22 | male   | kochi   |
# |   51 | aadil     | mny      |   25 | male   | kollam  |
# |   50 | suhail    | knply    |   24 | male   | kollam  |
# |   54 | remold    | klmsry   |   23 | male   | aluva   |
# +------+-----------+----------+------+--------+---------+
# 4 rows in set (0.00 sec)

# mysql> select * from peoples order by lastname asc;
# +------+-----------+----------+------+--------+---------+
# | id   | firstname | lastname | age  | gender | address |
# +------+-----------+----------+------+--------+---------+
# |   54 | remold    | klmsry   |   23 | male   | aluva   |
# |   50 | suhail    | knply    |   24 | male   | kollam  |
# |   51 | aadil     | mny      |   25 | male   | kollam  |
# |   55 | luslin    | vypin    |   22 | male   | kochi   |
# +------+-----------+----------+------+--------+---------+
# 4 rows in set (0.00 sec)

# mysql> select * from peoples order by lastname,firstname asc;
# +------+-----------+----------+------+--------+---------+
# | id   | firstname | lastname | age  | gender | address |
# +------+-----------+----------+------+--------+---------+
# |   54 | remold    | klmsry   |   23 | male   | aluva   |
# |   50 | suhail    | knply    |   24 | male   | kollam  |
# |   51 | aadil     | mny      |   25 | male   | kollam  |
# |   55 | luslin    | vypin    |   22 | male   | kochi   |
# +------+-----------+----------+------+--------+---------+
# 4 rows in set (0.00 sec)

# mysql> select * from peoples order by firstname asc;
# +------+-----------+----------+------+--------+---------+
# | id   | firstname | lastname | age  | gender | address |
# +------+-----------+----------+------+--------+---------+
# |   51 | aadil     | mny      |   25 | male   | kollam  |
# |   55 | luslin    | vypin    |   22 | male   | kochi   |
# |   54 | remold    | klmsry   |   23 | male   | aluva   |
# |   50 | suhail    | knply    |   24 | male   | kollam  |
# +------+-----------+----------+------+--------+---------+
# 4 rows in set (0.00 sec)

# mysql> select firstname from peoples order by firstname asc;
# +-----------+
# | firstname |
# +-----------+
# | aadil     |
# | luslin    |
# | remold    |
# | suhail    |
# +-----------+
# 4 rows in set (0.00 sec)

# mysql> select firstname,lastname,age from peoples order by firstname asc;
# +-----------+----------+------+
# | firstname | lastname | age  |
# +-----------+----------+------+
# | aadil     | mny      |   25 |
# | luslin    | vypin    |   22 |
# | remold    | klmsry   |   23 |
# | suhail    | knply    |   24 |
# +-----------+----------+------+
# 4 rows in set (0.00 sec)

# mysql> select firstname,lastname,age from peoples order by firstname desc;
# +-----------+----------+------+
# | firstname | lastname | age  |
# +-----------+----------+------+
# | suhail    | knply    |   24 |
# | remold    | klmsry   |   23 |
# | luslin    | vypin    |   22 |
# | aadil     | mny      |   25 |
# +-----------+----------+------+
# 4 rows in set (0.00 sec)

# mysql> select count(age),firstname from peoples group by firstname;
# +------------+-----------+
# | count(age) | firstname |
# +------------+-----------+
# |          1 | aadil     |
# |          1 | luslin    |
# |          1 | remold    |
# |          1 | suhail    |
# +------------+-----------+
# 4 rows in set (0.00 sec)

# mysql> mysql> select count(*),firstname,age from peoples group by firstname;
# ERROR 1055 (42000): Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'organisation.peoples.age' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
# mysql> select count(*)firstname,age from peoples group by firstname;
# ERROR 1055 (42000): Expression #2 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'organisation.peoples.age' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
# mysql> select count(age),firstname from peoples group by firstname;
# +------------+-----------+
# | count(age) | firstname |
# +------------+-----------+
# |          1 | aadil     |
# |          1 | luslin    |
# |          1 | remold    |
# |          1 | suhail    |
# +------------+-----------+
# 4 rows in set (0.00 sec)

# mysql> select count(*),firstname from peoples group by firstname;
# +----------+-----------+
# | count(*) | firstname |
# +----------+-----------+
# |        1 | aadil     |
# |        1 | luslin    |
# |        1 | remold    |
# |        1 | suhail    |
# +----------+-----------+
# 4 rows in set (0.00 sec)

# mysql> select count(*),firstname from peoples group by lastname;
# ERROR 1055 (42000): Expression #2 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'organisation.peoples.firstname' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
# mysql> select count(*),lastname from peoples group by lastname;
# +----------+----------+
# | count(*) | lastname |
# +----------+----------+
# |        1 | klmsry   |
# |        1 | knply    |
# |        1 | mny      |
# |        1 | vypin    |
# +----------+----------+
# 4 rows in set (0.00 sec)

# mysql> select age,lastname from peoples group by lastname;
# ERROR 1055 (42000): Expression #1 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'organisation.peoples.age' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
# mysql> select age,lastname from peoples group by age,lastname;
# +------+----------+
# | age  | lastname |
# +------+----------+
# |   22 | vypin    |
# |   23 | klmsry   |
# |   24 | knply    |
# |   25 | mny      |
# +------+----------+
# 4 rows in set (0.00 sec)

# mysql> select count(*),lastname from peoples group by lastname;
# +----------+----------+
# | count(*) | lastname |
# +----------+----------+
# |        1 | klmsry   |
# |        1 | knply    |
# |        1 | mny      |
# |        1 | vypin    |
# +----------+----------+
# 4 rows in set (0.00 sec)

# mysql> select count(*),lastname,age from peoples group by lastname,age;
# +----------+----------+------+
# | count(*) | lastname | age  |
# +----------+----------+------+
# |        1 | klmsry   |   23 |
# |        1 | knply    |   24 |
# |        1 | mny      |   25 |
# |        1 | vypin    |   22 |
# +----------+----------+------+
