
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

# takes a Python list object and builds a table of urwid widgets to show it
def show_table(table):
  for index, row in enumerate(table):
    print str(index) + ": "
    for index, element in enumerate(row):
      print str(index) + ":" + str(element)

#connectdb w/ dbname, username, pass
cur = psqlDB.connectdb("postgres", "postgres", "cs419db")
if cur == -1:
  print "error connecting; please check dbname, username, password"
else:
  print "successfully connected"

  # get all table names
  tablenames = psqlDB.gettables(cur)
  print tablenames

  # get all column names
  cols = psqlDB.getcolnames(cur, tablenames[0])
  print cols

  # get all table rows
  rows = psqlDB.allrows(cur, tablenames[0])
  print rows

