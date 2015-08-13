#!/usr/bin/python

import urwid
import mainview

"""
NOTES
-----
This module builds a widget with a warning message for truncating a table

"""

def show_table_trunc(frame, user_info, tablefunction, tablebutton):
  blank = urwid.Divider()

  def yes_trunc(button):
    #execute the truncate query
    status = user_info.db_obj.truncate_table(user_info.db_conn, tablebutton.get_label())

    if status == 1:
      #show success message in frame footer
      frame.footer = urwid.AttrWrap( urwid.Text([u" Table ",tablebutton.get_label() , " successfully truncated"]), 'header')

      #redirect to table view
      tablefunction(tablebutton)
    else:
      text_error.original_widget = urwid.AttrWrap( urwid.Text(status), 'error')

  def no_trunc(button):
    #redirect to table view
    tablefunction(tablebutton)

  text_1 = urwid.Text(u"WARNING!!!!!\nTruncating a table permanently deletes all data from this table.")
  text_2 = urwid.Text([u"Do you wish to proceed with truncating table ", tablebutton.get_label(), "?"])
  text_error = urwid.AttrWrap( urwid.Text(u""), 'body')

  table_trunc_yes = urwid.AttrWrap( urwid.Button(u"Yes", yes_trunc), 'btnf', 'btn')
  table_trunc_no = urwid.AttrWrap( urwid.Button(u"No", no_trunc), 'btnf', 'btn')

  trunc_table = urwid.WidgetPlaceholder( urwid.Padding(
    urwid.Pile([
      blank,
      text_error,
      text_1,
      text_2,
      blank,
      urwid.Columns([
        ('fixed', 6, table_trunc_no),
        ('fixed', 5, urwid.Text(u"     ")),
        ('fixed', 7, table_trunc_yes)
      ]),
    ]), left=5, right=5))

  return trunc_table
