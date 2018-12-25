#!/usr/bin/env python

# Udacity Full Stack Web Developer Nanodegree
# Project: Log Analysis
# Date: 25 December, 2018
# Created by Varun Joshi (joshvarun@gmail.com)

import psycopg2

# Database name
DBNAME = "news"

# Query Types
POPULAR_ARTICLES = "popular_articles"
POPULAR_AUTHORS = "popular_authors"
ERROR_RATES = "error_rates"

# Query 1: What are the most popular three articles of all time?
query_popular_articles = "SELECT * FROM article_view LIMIT 3;"

# Query 2: Who are the most popular article authors of all time?
query_popular_authors = """SELECT name, SUM(views) AS views FROM article_view
GROUP BY name ORDER BY views DESC;"""

# Query 3: On which days did more than 1% of requests lead to errors?
query_error_days = "SELECT * FROM error_view WHERE \"Error Rate\" > 1;"


# Execute query & return results
def get_results(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


# Print Results
def print_results(results, source):
    if source == POPULAR_ARTICLES:
        print ("\n1. The 3 most popular articles of all time are:\n\n")
        for result in results['results']:
            print (
                '\"' + str(result[0]) + '\"' + ' by ' + str(result[1]) +
                ' -> ' + str(result[2]) + ' views'
                )

    elif source == POPULAR_AUTHORS:
        print ("\n2. The most popular authors are:\n\n")
        for result in results['results']:
            print (str(result[0]) + ' -> ' + str(result[1]) + ' views')

    elif source == ERROR_RATES:
        print ("""\n3. Days on which more than 1% of requests led to
        an error:\n\n""")
        for result in results['results']:
            print (str(result[0]) + ' -> ' + str(result[1]) + ' %')

# Store Results of query
popular_articles_result = dict()
popular_authors_result = dict()
error_rates_result = dict()

# Get Results of the query
popular_articles_result['results'] = get_results(query_popular_articles)
popular_authors_result['results'] = get_results(query_popular_authors)
error_rates_result['results'] = get_results(query_error_days)

# Print results to command line
print_results(popular_articles_result, POPULAR_ARTICLES)
print_results(popular_authors_result, POPULAR_AUTHORS)
print_results(error_rates_result, ERROR_RATES)
