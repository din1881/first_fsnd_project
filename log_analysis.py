
# My Logs Analysis Project

# Import postgresql library
import psycopg2

dbname = "news"

first_query = """SELECT * FROM artviews LIMIT 3;"""

second_query = """SELECT name, sum(artviews.views) AS views FROM artauthors, artviews WHERE artauthors.title = artviews.title GROUP BY name ORDER BY views desc;"""


third_query = """SELECT err_logs.date, round(100.0*error_c/log_c,2) as percent FROM logs, err_logs WHERE logs.date = err_logs.date AND error_c > log_c/100;"""


def connect(query):
    # Connecting to database
    db = psycopg2.connect(database=dbname)
    cur = db.cursor()
    # Executing queries
    cur.execute(query)
    # Fetching results
    res = cur.fetchall()
    db.close()
    return results

# Create Views for Question 2 and Question 3 as instructed on the README file.

# Question 1. What are the most popular three articles of all time?


def most_readed_articles(query):
    res = connect(query)
    print('The most popular articles of all time:\n')
    for k in res:
        print('\t' + str(k[0]) + ' - ' + str(k[1]) + ' view')
        print(" ")


# Question 2. Who are the most popular article authors of all time?

def most_famous_authors(query):
    res = connect(query)
    print('The most popular authors of all time:\n')
    for k in res:
        print('\t' + str(k[0]) + ' - ' + str(k[1]) + ' view')
        print(" ")


# Question 3. On which days did more than 1% of requests lead to errors?

def err_percent(query):
    res = connect(query)
    print('The days where more than 1% of requests lead to error:\n')
    for k in res:
        print('\t' + str(k[0]) + ' - ' + str(k[1]) + ' %' + ' errors')
        print(" ")

if __name__ == '__main__':
	# executing the results

    most_readed_articles(first_query)
    most_famous_authors(second_query)
    err_percent(third_query)
