# **LOG ANALYSIS PROJECT**

## Description
In this project, I'm building a internal reporting tool that will use information from a newspaper database to discover what kind of articles the site's readers like.

The reporting tool will be a python script program that uses psycopg2 module to connect to the database and to query the database to answer the following questions:

    1.What are the most popular three articles of all time?
    2.Who are the most popular article authors of all time?
    3.On which days did more than 1% of requests lead to errors?

## How  to run the program?
1. _First you need to download [python 2](https://www.python.org/downloads/release/python-2716/) or [python 3](https://www.python.org/download/releases/3.0/)
2. _Second, it's adviced that you use a virtual machine. So Please download [Vagrant](https://www.vagrantup.com/) and [VirtualBox](virtualbox.org) to manage your Virtual machine._
3. _Download Udacity's preconfigured vagrant file from [here](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip)_ 
4. _To bring up your virtual machine use `vagrant up` and `vagrantt ssh` to log in from git bash in udacity's folder directory._
5. _Download Udacity's **news** database from  [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) ._
6. _Use ```cd /vagrant``` to access your shared files._
7. _Use this command line to connect to the database and run the SQL statements in the file newsdata.sql ```psql -d news -f newsdata.sql```._
8. _Create the Views below._
9. _Exit psql._
10. _Execute the python file using the command ```python log_analysis.py ```._

## **CREATE VIEWS FOR Q2 AND Q3:**

### **Views for Question no. 2**

```
CREATE VIEW art_authors AS
SELECT title, name
FROM articles, authors
WHERE articles.author = authors.id;
```

```
CREATE VIEW art_views AS
SELECT title, count(log.id) as views
FROM articles, log
WHERE log.path = CONCAT('/article/', articles.slug)
GROUP BY articles.title
ORDER BY views desc;
```

### **Views for Question no. 3**

```
CREATE VIEW logs AS
SELECT to_char(time,'DD-MON-YYYY') as Date, count(*) as log_c
FROM log
GROUP BY Date;
```

```
CREATE VIEW err_logs AS
SELECT to_char(time,'DD-MON-YYYY') as Date, count(*) as error_c
FROM log
WHERE STATUS = '404 NOT FOUND'
GROUP BY Date;
```