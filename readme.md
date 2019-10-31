# **LOG ANALYSIS PROJECT**

## Description
In this project, I'm building a internal reporting tool that will use information from a newspaper database to discover what kind of articles the site's readers like.

The reporting tool will be a python script program that uses psycopg2 module to connect to the database and to query the database to answer the following questions:

    1.What are the most popular three articles of all time?
    2.Who are the most popular article authors of all time?
    3.On which days did more than 1% of requests lead to errors?

## How  to run the program?
1. _First of all, it's adviced that you use a virtual machine. So Please downloadVagrant and VirtualBox to manage your Virtual machine. To bring up your virtual machine use `vagrant up` and `vagrantt ssh` to log in._
2. _Download Udacity's database from  [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) ._
3. _Use ```cd /vagrant``` to access your shared files._
4. _Use this command line to connect to the database and run the SQL statements in the file newsdata.sql ```psql -d news -f newsdata.sql```._
5. _Create the Views below._
6.  _Exit psql._
7.  _Execute the python file using the command ```python log_analysis.py ```._

## **CREATING VIEWS FOR Q2 AND Q3:**

### **Views for Question no. 2**

```
CREATE VIEW artauthors AS
SELECT title, name
FROM articles, authors
WHERE articles.author = authors.id;
```

```
CREATE VIEW artviews AS
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