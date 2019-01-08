#! /usr/bin/env python
import psycopg2
DBNAME = "news"

question1 = "1. What are the most popular three articles of all time?"
query1 = """
        select title, count(*) as cnt
        from articles,log
        where log.path=CONCAT('/article/',articles.slug)
        group by articles.title
        order by cnt DESC
        limit 3;
"""

question2 = "2. Who are the most popular article authors of all time?"
query2 = """
       select name, count(*) as cnt
        from log, articles, authors
        where log.path = '/article/' || articles.slug AND articles.author = authors.id
        group by name
        order by count(*) DESC;
"""

question3 = "3. On which days did more than 1% of requests lead to errors?"
query3 = """
    WITH error_rate AS (
        select date(time),round(100.0*sum(case log.status
            when '200 OK'  then 0 else 1 end)/count(log.status),3) as error
    from log
    group by date(time)
    order by error desc)
    select * from error_rate where error > 1;
"""


def connect_to_database():
    try:
        db = psycopg2.connect(database=DBNAME)
        cursor = db.cursor()
    except psycopg2.Error as e:
        print("Failed to connect to the database.")
        exit(1)
    else:
        return cursor


def query_db(cur, query):
    try:
        cur.execute(query)
    except psycopg2.Error as e:
        print('Failed to run' + query)
    results = cur.fetchall()
    return results


def print_results(results):
    for result in results:
        print('\t' + str(result[0]) + ' - ' + str(result[1]) + ' views')


def print_question(question):
    print("\n")
    print(question)
    print('================================================================\n')


def get_top3__articles(cur):
    print_question(question1)
    res1 = query_db(cur, query1)
    print_results(res1)


def get_top_authors(cur):
    print_question(question2)
    res2 = query_db(cur, query2)
    print_results(res2)


def get_days_with_errors(cur):
    print_question(question3)
    res3 = query_db(cur, query3)
    print_results(res3)


if __name__ == "__main__":
    cur = connect_to_database()
    if cur:
        get_top3__articles(cur)
        get_top_authors(cur)
        get_days_with_errors(cur)
        cur.close()
