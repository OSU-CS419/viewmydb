
import backend

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
cur = backend.connectdb("test1", "postgres", "cs419db")
if cur == -1:
  print "error connecting; please check dbname, username, password"
else:
  print "successfully connected"

  # get all table names
  tablenames = backend.gettables(cur)
  print tablenames

  # get all table rows
  rows = backend.allrows(cur, tablenames[0])
  print rows

