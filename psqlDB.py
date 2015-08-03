#!/usr/bin/python

import psycopg2

"""
NOTES
-----
psycopg returns tuples, which are hard to work with as they're unchangable,
so they're converted into lists before they're returned.
EDIT: the reason I first turned them into lists was that I was getting results
like [('dbname1', ), ('dbname1', )]
with an extra space afte the first element so I repackaged into lists to get
rid of this empty item.
Turns out this is just how python prints single element tuples. There's
actually nothing there. I think I still like lists better anyway.

psycopg documentation says:
Never, never, NEVER use Python string concatenation (+) or string parameters
interpolation (%) to pass variables to a SQL query string.
Not even at gunpoint.

I couldn't seem to make it work without concatenating a string for the query
to execute. I can investigate that further later on, but for now I just wanted
it to work.
"""

# takes database name, username, password
# returns psycopg2 cursor object on success, -1 on failure
def connectdb(db, un, pw):
  try:
    conn = psycopg2.connect(database=db, user=un, password=pw)
    cur = conn.cursor()
    return cur
  except psycopg2.OperationalError:
    return -1

# takes psycopg2 cursor object
# returns list of table names on success, -1 on failure
def gettables(cur):
  try:
    cur.execute("""SELECT table_name FROM information_schema.tables 
    WHERE table_schema='public' AND table_type='BASE TABLE' ORDER BY table_name;""")
    data = cur.fetchall()
    #print data
    names = []
    for table in data:
      names.append(table[0])
    return names
  except:
    return -1

# takes psycopg2 cursor object
# returns list of row data on success, -1 on failure
def allrows(cur, name):
  SQL = "SELECT * FROM " + name + ";"
  try:
    cur.execute(SQL)
    data = cur.fetchall()
    rows = []
    for row in data:
      rows.append(row)
    return rows
  except:
    return -1

# takes psycopg2 cursor object
# returns list of all column names on success, -1 on failure
def getcolnames(cur, table):
  try:
    SQL = "SELECT column_name FROM information_schema.columns WHERE table_name = " + "'" + table + "';"
    cur.execute(SQL)
    data = cur.fetchall()
    columns = []
    for column in data:
      columns.append(column[0])
    return columns
  except:
    return -1;
