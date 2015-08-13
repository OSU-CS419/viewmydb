#!/usr/bin/python

# add your credentials to credentials.py
import credentials as creds

postgres = ""

postgres = True #comment this line for mysql, uncomment for psql

if postgres:
  print "\n\n****************POSTGRES*****************"
  import psqlDB
  db = psqlDB.Psql()
else:
  print "\n\n******************MYSQL******************"
  import mysqlDB
  db = mysqlDB.MYsql()

import tablestructure


"""
NOTES
-----
Moving test in backend.py to a separate file containing tests
When the module backend.py was being implemented, it would run the
tests since they aren't in a function or anything, so that's why 
I'm moving them here.

can just run 'python tests.py' to run this file

"""

# ------------------------------------------------
# tests
# ------------------------------------------------
#connectdb w/ dbname, username, pass
if postgres:
  conn = db.connectdb(creds.psqldbname, creds.psqluname, creds.psqlpass)
else:
  conn = db.connectdb(creds.mysqldbname, creds.mysqluname, creds.mysqlpass)

if conn == -1:
  print "error connecting; please check dbname, username, password"
else:
  #get all table names
  tablenames = db.gettables(conn)
  print "\nAll tables in selected DB"
  print tablenames

  # get all column names
  cols = db.getcolnames(conn, tablenames[0])
  print "\nAll column names in first DB"
  print cols

  # get all table rows
  rows = db.allrows(conn, tablenames[0])
  print "\nAll rows in first DB"
  print rows

  # testing run sql
#  data = db.runquery(conn, "select * from moretest;")
#  print "\nData from run sql query"
#  print data

  # get db info
  info = db.getdbinfo(conn, "testdb")
  print "\nDatabase info"
  print info

  # get db table info
  table_info = db.getdb_tableinfo(conn)
  print "\nDatabase table info"
  print table_info

  # get table info
  table_stat_info = db.gettableinfo(conn, 'cats')
  print "\nTable structure info"
  print table_stat_info

  print "-------------------------------------------"

conn.close()
