#!/usr/bin/python

import MySQLdb

"""
NOTES
-----

This file contains the functions for the mysql implementation part of the code.

"""

class MYsql:
  # takes database name, username, password
  # returns cursor object on success, -1 on failure
  def connectdb(self, name, user, pw):
    try:
      conn = MySQLdb.connect(host="localhost",user=user, passwd=pw, db=name)
      conn.ourdbname = name	# for some reason, it needs the db name for the gettables query
      return conn
    except:
      return -1

  # takes cursor object
  # returns list of table names on success, -1 on failure
  def gettables(self, conn):
    cur = conn.cursor()
    try:
      SQL ="""SELECT DISTINCT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 
             'BASE TABLE' AND TABLE_SCHEMA = '""" + conn.ourdbname +  """';"""
      cur.execute(SQL)
      data = cur.fetchall()
      #print data
      names = []
      for table in data:
        names.append(table[0])
      cur.close()
      return names
    except:
      cur.close()
      return -1

  # takes cursor object
  # returns list of row data on success, -1 on failure
  def allrows(self, conn, name):
    cur = conn.cursor()
    SQL = "SELECT * FROM " + name + ";"
    try:
      cur.execute(SQL)
      data = cur.fetchall()
      rows = []
      for row in data:
        rows.append(row)
      cur.close()
      return rows
    except:
      cur.close()
      return -1

  # takes cursor object
  # returns list of all column names on success, -1 on failure
  def getcolnames(self, conn, table):
    cur = conn.cursor()
    try:
      SQL = """SELECT DISTINCT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='""" + table + """';"""
      cur.execute(SQL)
      data = cur.fetchall()
      columns = []
      for column in data:
        columns.append(column[0])
      cur.close()
      return columns
    except:
      cur.close()
      return -1

  # takes cursor object and text string of query to run
  # returns 1 on success and error message on failure
  def runquery(self, conn, text, select):
    cur = conn.cursor()
    try:
      cur.execute(text)
      conn.commit()
      if select:
        data = cur.fetchall()
      else:
        data = ""
      cur.close()
      return {'success':True, 'data':data}
    except MySQLdb.Error as e:
      f.close()
      conn.commit()
      cur.close()
      return {'success':False, 'data':e.pgerror}

  # gets information about the database
  def getdbinfo(self, conn, name):
    cur = conn.cursor()
    try:
      cur.execute("""SELECT schema_name AS "Name",
     default_character_set_name AS "Encoding",
     DEFAULT_COLLATION_NAME AS "Collate"
     FROM information_schema.SCHEMATA WHERE
     schema_name = (%s);""", (name,))
      data = cur.fetchall()
      cur.close()
      return data[0]
    except:
      cur.close()
      return -1

  # gets information about a table
  def getdb_tableinfo(self, conn):
    cur = conn.cursor()
    name = conn.ourdbname
    try:
      cur.execute("""SELECT table_name AS "Table", 
      round(((data_length + index_length) / 1024)) AS "Size" 
      FROM information_schema.TABLES 
      WHERE table_schema = (%s)
      ORDER BY (data_length + index_length) DESC;""", (name,))
      data = cur.fetchall()
      cur.close()

      # put it in a list instead of a tuple
      info = []
      row = []
      for table in data:
        # cast as a string
        size = str(table[1]) + " kB"
        name = str(table[0])
        row.append(name)	# append the name
        row.append(size)	# append the size
        info.append(row)	# append that row
        row = []		# empty the row

      return info
    except:
      cur.close()
      return -1
  
  # gets info about the table
  def gettableinfo(self, conn, tablename):
    cur = conn.cursor()
    try:
      cur.execute("""SELECT column_name, data_type, character_maximum_length, is_nullable, column_default
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE table_name=(%s);""", (tablename,))
      data = cur.fetchall()
      cur.close()
      return data
    except:
      cur.close()
      return -1

  # truncates a table
  def truncate_table(self, conn, tablename):
    cur = conn.cursor()
    try:
      SQL = "TRUNCATE " + str(tablename)
      cur.execute(SQL)
      conn.commit()
      cur.close()
      return 1
    except MySQLdb.Error as e:
      conn.commit()
      cur.close()
      return e.pgerror

  # drops a table
  def drop_table(self, conn, tablename):
    cur = conn.cursor()
    try:
        SQL = "DROP TABLE " + str(tablename)
        cur.execute(SQL)
        conn.commit()
        cur.close()
        return 1
    except MySQLdb.Error as e:
      conn.commit()
      cur.close()
      return e.pgerror

  # renames a table
  def rename_table(self, conn, tablename, newname):
    cur = conn.cursor()
    try:
        SQL = "ALTER TABLE " + str(tablename) + " RENAME TO " + str(newname)
        cur.execute(SQL)
        conn.commit()
        cur.close()
        return 1
    except MySQLdb.Error as e:
      conn.commit()
      cur.close()
      return e.pgerror
