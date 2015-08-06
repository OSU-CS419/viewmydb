#!/usr/bin/python

#toggle this to switch b/w psql and mysql
postgres = True

if postgres:
  import psqlDB
  db = psqlDB.Psql()
else:
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
#conn = db.connectdb("testdb", "root", "mypassword")
conn = db.connectdb("test1", "postgres", "cs419db")

if conn == -1:
  print "error connecting; please check dbname, username, password"
else:
  #get all table names
  tablenames = db.gettables(conn)
  print "All tables in selected DB"
  print tablenames

  # get all column names
  cols = db.getcolnames(conn, tablenames[1])
  print "All column names in first DB"
  print cols

  # get all table rows
  rows = db.allrows(conn, tablenames[1])
  print "All rows in first DB"
  print rows

  # get db info
  info = db.getdbinfo(conn, "test1")
  print info

  # get db table info
  table_info = db.getdb_tableinfo(conn)
  print table_info

  print "-------------------------------------------"

conn.close()
