#!/usr/bin/python

# comment out the one you don't want to use

import psqlDB as sqlDB
#import mysqlDB as sqlDB

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
cur = sqlDB.connectdb("postgres", "postgres", "cs419db")
tablenames = sqlDB.gettables(cur)
cols = sqlDB.getcolnames(cur, tablenames[0])
rows = sqlDB.allrows(cur, tablenames[0])
