#!/usr/bin/python
import psqlDB

"""
NOTES
-----
This script is for testing purposes.  It connects to the database and
gets all tables and rows or a specific table so we don't have to 
run the whole program to test

"""

# ------------------------------------------------
# tests
# ------------------------------------------------
#connectdb w/ dbname, username, pass
cur = psqlDB.connectdb("postgres", "postgres", "cs419db")
tablenames = psqlDB.gettables(cur)
cols = psqlDB.getcolnames(cur, tablenames[0])
rows = psqlDB.allrows(cur, tablenames[0])

