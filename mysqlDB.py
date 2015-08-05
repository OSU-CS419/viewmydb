#!/usr/bin/python

#import mysql module here

"""
NOTES
-----

This file can contain the functions for the mysql implementation part of the code.

What I was thinking might make sense is to have a module for psql and a separate
module for mysql. Since our interface/UI isn't going to change between the two,
we can make it so that the mysql and psql functions have the same names. Then,
we can create some sort of object that will refer to the appropriate mysql or 
psql code based off of what the user supplies. That way, we can then use 
that same object and function names within the code and it will just automatically
be pulling functions based off of either the mysql or psql functions. 

For instance,
have a class with all psql functions

class psql:
  def connectdb():
    #function code here

and a class with all the mysql functions

class mysql:
  def connectdb():
    #function code here

Then in the code we code do something like
if psql:
  db = psqlDB.psql()
elif mysql:
  db = mysqlDB.mysql()

Then, further down in the code you can just have 

db.connectdb()

in order to connect the database and that way you don't have to build out separate
code for mysql or psql and the only code that accounts for the difference is that 
if else if statement that instantiates the object based on what the user provided.



"""

def connectdb(db_name, db_uname, db_pw):
  return -1
