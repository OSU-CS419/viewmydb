#!/usr/bin/python
import mysqlDB as sqlDB
#import psqlDB as sqlDB
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
cur = sqlDB.connectdb("testdb", "root", "mypassword")
#cur = sqlDB.connectdb("postgres", "postgres", "cs419db")
if cur == -1:
  print "error connecting; please check dbname, username, password"
else:
  # get all table names
  tablenames = sqlDB.gettables(cur)
  print "All tables in selected DB"
  print tablenames

  # get all column names
  cols = sqlDB.getcolnames(cur, tablenames[1])
  print "All column names in first DB"
  print cols

  # get all table rows
  rows = sqlDB.allrows(cur, tablenames[1])
  print "All rows in first DB"
  print rows

  print "-------------------------------------------"
