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

class Psql:
  # takes database name, username, password
  # returns psycopg2 cursor object on success, -1 on failure
  def connectdb(self, db, un, pw):
    try:
      conn = psycopg2.connect(database=db, user=un, password=pw)
      #conn = psycopg2.connect(database="test1", user="postgres", password="cs419db")
      return conn
    except psycopg2.OperationalError:
      return -1

  # takes psycopg2 cursor object
  # returns list of table names on success, -1 on failure
  def gettables(self, conn):
    cur = conn.cursor()
    try:
      cur.execute("""SELECT DISTINCT table_name FROM information_schema.tables 
      WHERE table_schema='public' AND table_type='BASE TABLE' ORDER BY table_name;""")
      data = cur.fetchall()
      #print data
      names = []
      for table in data:
        names.append(table[0])
      cur.close()
      return names
    except:
      cur.close()
      return -1

  # takes psycopg2 cursor object
  # returns list of row data on success, -1 on failure
  def allrows(self, conn, name):
    cur = conn.cursor()
    SQL = "SELECT * FROM " + name + ";"
    try:
      cur.execute(SQL)
      data = cur.fetchall()
      rows = []
      for index, row in enumerate(data):
        newrow = []
#        newrow.append(index)
        for element in row:
          newrow.append(element)
        rows.append(newrow)
      cur.close()
      return rows
    except:
      cur.close()
      return -1

  # takes psycopg2 cursor object
  # returns list of all column names on success, -1 on failure
  def getcolnames(self, conn, table):
    cur = conn.cursor()
    try:
      SQL = "SELECT column_name FROM information_schema.columns WHERE table_name = " + "'" + table + "';"
      cur.execute(SQL)
      data = cur.fetchall()
      columns = []
#      columns.append("Index")
      for column in data:
        columns.append(column[0])
      cur.close()
      return columns
    except:
      cur.close()
      return -1

  # takes psycopg2 cursor object and text string of query to run
  # returns 1 on success and error message on failure
  def runquery(self, conn, text, select):
    cur = conn.cursor()
    try:
      cur.execute(text)
      conn.commit()
      if select:
        data = cur.fetchall()
      else:
        data = ""
      cur.close()
      return {'success':True, 'data':data}
    except psycopg2.Error as e:
      conn.commit()
      cur.close()
      return {'success':False, 'data':e.pgerror}

  def getdbinfo(self, conn, name):
    cur = conn.cursor()
    try:
      cur.execute("""SELECT d.datname AS "Name",
          pg_catalog.pg_encoding_to_char(d.encoding) AS "Encoding",
          d.datcollate AS "Collate"
        FROM pg_catalog.pg_database d
        WHERE datname=(%s);""", (name,))
      data = cur.fetchall()
      cur.close()
      return data[0]
    except:
      cur.close()
      return -1

  def getdb_tableinfo(self, conn):
    cur = conn.cursor()
    try:
      cur.execute("""SELECT relname AS "Table",
          pg_size_pretty(pg_total_relation_size(relid)) AS "Size"
        FROM pg_catalog.pg_statio_user_tables
        ORDER BY pg_total_relation_size(relid) DESC;""")
      data = cur.fetchall()
      cur.close()
      return data
    except:
      cur.close()
      return -1

  def gettableinfo(self, conn, tablename):
    cur = conn.cursor()
    try:
      cur.execute("""SELECT column_name, data_type, character_maximum_length, is_nullable, column_default
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE table_name=(%s);""", (tablename,))
      data = cur.fetchall()
      cur.close()
      return data
    except:
      cur.close()
      return -1

  def truncate_table(self, conn, tablename):
    cur = conn.cursor()
    try:
      SQL = "TRUNCATE " + str(tablename)
      cur.execute(SQL)
      conn.commit()
      cur.close()
      return 1
    except psycopg2.Error as e:
      conn.commit()
      cur.close()
      return e.pgerror

  def drop_table(self, conn, tablename):
    cur = conn.cursor()
    try:
        SQL = "DROP TABLE " + str(tablename)
        cur.execute(SQL)
        conn.commit()
        cur.close()
        return 1
    except psycopg2.Error as e:
      conn.commit()
      cur.close()
      return e.pgerror

  def rename_table(self, conn, tablename, newname):
    cur = conn.cursor()
    try:
        SQL = "ALTER TABLE " + str(tablename) + " RENAME TO " + str(newname)
        cur.execute(SQL)
        conn.commit()
        cur.close()
        return 1
    except psycopg2.Error as e:
      conn.commit()
      cur.close()
      return e.pgerror
