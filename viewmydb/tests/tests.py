#!/usr/bin/python

import unittest

"""
NOTES
-----
Moving test in backend.py to a separate file containing tests
When the module backend.py was being implemented, it would run the
tests since they aren't in a function or anything, so that's why 
I'm moving them here.

can just run 'python tests.py' to run this file

"""

# add your credentials to credentials.py in order to run tests
import credentials as creds


class LoginCreds:
  def __init__(self):
    self.uname = ""
    self.dbname = ""
    self.pw = ""

class TestDB(unittest.TestCase):

  def setUp(self):
    login = LoginCreds()
    
    postgres = True #make True for psql and False for mysql

    if postgres:
      # print "\n\n****************POSTGRES*****************"
      from viewmydb import psqlDB
      self.db = psqlDB.Psql()
      login.uname = creds.psqluname
      login.dbname = creds.psqldbname 
      login.pw = creds.psqlpass
    else:
      # print "\n\n******************MYSQL******************"
      from viewmydb import mysqlDB
      self.db = mysqlDB.MYsql()
      login.uname = creds.mysqluname
      login.dbname = creds.mysqldbname
      login.pw = creds.mysqlpass    

    self.conn = self.db.connectdb(login.dbname, login.uname, login.pw)
    self.tablenames = self.db.gettables(self.conn)

  def tearDown(self):
    if self.conn != -1:
      self.conn.close()
  
# ------------------------------------------------
# tests
# ------------------------------------------------
  def test_connect_db(self):
    self.assertNotEqual(self.conn, -1, "Could not connect to DB")

  def test_tablenames(self):
    self.assertNotEqual(self.tablenames, -1, "Could not get table names")

  def test_columnnames(self):
    self.assertNotEqual(self.db.getcolnames(self.conn, self.tablenames[0]), -1, "Could not get column names")

  def test_tablerows(self):
    self.assertNotEqual(self.db.allrows(self.conn, self.tablenames[0]), -1, "Could not get table rows")

  def test_runquery(self):
    data = self.db.runquery(self.conn, "select * from moretest;", True)
    self.assertTrue(data['success'], "Could not run query")
  
  def test_dbinfo(self):
    self.assertNotEqual(self.db.getdbinfo(self.conn, "test1"), -1, "Could not get db info")

  def test_dbtableinfo(self):
    self.assertNotEqual(self.db.getdb_tableinfo(self.conn), -1, "Could not get db table info")

  def test_tableinfo(self):
    self.assertNotEqual(self.db.gettableinfo(self.conn, "cats"), -1, "Could not get table info")

if __name__ == '__main__':
  unittest.main()
