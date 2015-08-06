#!/usr/bin/python

import urwid

"""
NOTES
-----
This module builds the widget to show the structure information for a database.

"""

def show_db_structure(user_info):
  #build out the table that shows the db structure stats
  #get db info
  db_info = user_info.db_obj.getdbinfo(user_info.db_conn, user_info.db_name)
  
  #get table names and size
  db_tableinfo = user_info.db_obj.getdb_tableinfo(user_info.db_conn)

  #building out list of table name text widgets
  table_names_list = []
  for x in db_tableinfo:
    table_names_list.append(urwid.Text(x[0]))
  
  #building out list of table size text widgets
  table_sizes_list = []
  for x in db_tableinfo:
    table_sizes_list.append(urwid.Text(x[1]))


  #widgets for the database info table
  db_name_col = urwid.LineBox( 
      urwid.Text(db_info[0])
    , title="DB Name", rline=' ', trcorner=u'\u2500', brcorner=u'\u2500')
  encoding_col = urwid.LineBox( 
      urwid.Text(db_info[1])
    , title="Encoding", rline=' ', trcorner=u'\u2500', brcorner=u'\u2500')
  collation_col = urwid.LineBox( 
      urwid.Text(db_info[2])
    , title="Encoding")

  #widgets for the database tables info table
  table_names = urwid.LineBox( urwid.Pile(table_names_list)
    , title="Name", rline=' ', trcorner=u'\u2500', brcorner=u'\u2500')
  table_sizes = urwid.LineBox( urwid.Pile(table_sizes_list)
    , title="Size")

  #main widget for view
  structure_view = urwid.Padding( urwid.Pile( [
    urwid.Text(u"Database Info:"),
    urwid.Columns([
        db_name_col,
        encoding_col,
        collation_col
      ]),
    urwid.Divider(),
    urwid.Text(u"DB Tables:"),
    urwid.Columns([
        table_names,
        table_sizes
      ])
    ])
  , left=2, right=2)

  structure_view = urwid.WidgetPlaceholder(structure_view)

  #return the widget created that holds all the structure data
  return structure_view
