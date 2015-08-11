#!/usr/bin/python

import urwid

"""
NOTES
-----
This module builds the widget to show the structure information for a table.

"""

def show_table_structure(user_info, tablename):
  #build out the table that shows the table structure information
  #get table info
  table_info = user_info.db_obj.gettableinfo(user_info.db_conn, tablename)

  #building out list of column names
  table_col_names = []
  for x in table_info:
    table_col_names.append(urwid.Text(x[0]))

  #building out list of data types
  table_data_type = []
  for x in table_info:
    table_data_type.append(urwid.Text(x[1]))

  #building out list of character lengths
  table_char_length = []
  for x in table_info:
    if x[2] == None:
      table_char_length.append(urwid.Text(u" "))
    else:
      table_char_length.append(urwid.Text(str(x[2])))

  #building out list of null
  table_null = []
  for x in table_info:
    if x[3] == None:  
      table_null.append(urwid.Text(u" "))
    else:
      table_null.append(urwid.Text(x[3]))

  #building out list of default values
  table_default = []
  for x in table_info:
    if x[4] == None:  
      table_default.append(urwid.Text(u" "))
    else:
      table_default.append(urwid.Text(x[4]))

  #widgets for the table info table
  col_names = urwid.LineBox( urwid.Pile(table_col_names)
    , title="Name", rline=' ', trcorner=u'\u2500', brcorner=u'\u2500')
  datatypes = urwid.LineBox( urwid.Pile(table_data_type)
    , title="Type", rline=' ', trcorner=u'\u2500', brcorner=u'\u2500')
  charlengths = urwid.LineBox( urwid.Pile(table_char_length)
    , title="Length", rline=' ', trcorner=u'\u2500', brcorner=u'\u2500')
  nulls =urwid.LineBox( urwid.Pile(table_null)
    , title="Is Null", rline=' ', trcorner=u'\u2500', brcorner=u'\u2500')
  defaults = urwid.LineBox( urwid.Pile(table_default)
    , title="Default")

  text_1 = urwid.Text(u"Here is the table structure information. If the table does not look alligned, then please make your terminal wider.")

  #main widget for view
  structure_view = urwid.Padding( urwid.Pile( [
    urwid.Divider(),
    text_1,
    urwid.Divider(),
    urwid.Text([u"Structure for table: ", tablename]),
    urwid.Divider(),
    urwid.Columns([
        col_names,
        datatypes,
        charlengths,
        nulls,
        defaults
      ])
    ])
  , left=2, right=2)

  structure_view = urwid.WidgetPlaceholder(structure_view)

  #return the widget created that holds all the structure data
  return structure_view
