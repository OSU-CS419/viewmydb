
import psqlDB

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
cur = psqlDB.connectdb("postgres", "postgres", "cs419db")
if cur == -1:
  print "error connecting; please check dbname, username, password"
else:
  # get all table names
  tablenames = psqlDB.gettables(cur)
  print "All tables in selected DB"
  print tablenames

  # get all column names
  cols = psqlDB.getcolnames(cur, tablenames[0])
  print "All column names in first DB"
  print cols

  # get all table rows
  rows = psqlDB.allrows(cur, tablenames[0])
  print "All rows in first DB"
  print rows

