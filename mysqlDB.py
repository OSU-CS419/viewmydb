#!/usr/bin/python

import MySQLdb

"""
NOTES
-----

This file contains the functions for the mysql implementation part of the code.

"""

# takes database name, username, password
# returns cursor object on success, -1 on failure
def connectdb(name, user, pw):
  try:
    conn = MySQLdb.connect(host="localhost",user=user, passwd=pw, db=name)
    cur = conn.cursor()
    cur.ourdbname = name	# for some reason, it needs the db name for the query
    return cur
  except:
    return -1

# takes cursor object
# returns list of table names on success, -1 on failure
def gettables(cur):
  try:
    sql ="""SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 
           'BASE TABLE' AND TABLE_SCHEMA = '""" + cur.ourdbname +  """';"""
    cur.execute(sql)
    data = cur.fetchall()
    #print data
    names = []
    for table in data:
      names.append(table[0])
    return names
  except:
    return -1
