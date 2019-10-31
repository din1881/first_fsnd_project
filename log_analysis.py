# !/usr/bin/env python

# My Logs Analysis Project

import psycopg2

dbname = "news"

first_query = """SELECT * FROM art_views LIMIT 3;"""

second_query = """SELECT name, sum(art_views.views) AS views
                  FROM art_authors, art_views
                  WHERE art_authors.title = art_views.title
                  GROUP BY name ORDER BY views desc;"""

third_query = """SELECT err_logs.date,
                round(100.0*error_c/log_c,2) as percent FROM logs, err_logs
                WHERE logs.date = err_logs.date AND error_c > log_c/100;"""


def connect(query):
    # Connecting to database
    db = psycopg2.connect(database=dbname)
    cur = db.cursor()
    # Executing queries
    cur.execute(query)
    # Fetching results
    res = cur.fetchall()
    db.close()
    return res


def most_read_articles(query):
    res = connect(query)
    print('Most popular articles of all time:\n')
    for k in res:
        print('\t' + str(k[0]) + ' - ' + str(k[1]) + ' view')
    print('\n')


def most_famous_authors(query):
    res = connect(query)
    print('Most popular authors of all time:\n')
    for k in res:
        print('\t' + str(k[0]) + ' - ' + str(k[1]) + ' view')
    print('\n')


def err_percent(query):
    res = connect(query)
    print('The days where more than 1% of requests lead to error:\n')
    for k in res:
        print('\t' + str(k[0]) + ' - ' + str(k[1]) + ' %' + ' errors')
    print('\n')


if __name__ == '__main__':
    # executing the results
    most_readed_articles(first_query)
    most_famous_authors(second_query)
    err_percent(third_query)
