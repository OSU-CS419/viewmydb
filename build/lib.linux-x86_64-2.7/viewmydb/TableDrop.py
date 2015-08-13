#!/usr/bin/python

import urwid
import mainview

"""
NOTES
-----
This module builds a widget with a warning message for dropping a table

"""

def show_table_drop(frame, body, user_info, tablefunction, tablebutton):
  blank = urwid.Divider()

  def yes_drop(button):
    #execute the drop query
    status = user_info.db_obj.drop_table(user_info.db_conn, tablebutton.get_label())

    if status == 1:
      #show success message in frame footer
      frame.footer = urwid.AttrWrap( urwid.Text([u" Table ",tablebutton.get_label() , " successfully dropped"]), 'header')

      #redirect to main view
      mainview.show_main_view(frame, body, user_info)
    else:
      text_error.original_widget = urwid.AttrWrap( urwid.Text(status), 'error')

  def no_drop(button):
    #redirect to table view
    tablefunction(tablebutton)

  text_1 = urwid.Text(u"WARNING!!!!!\nDropping a table permanently deletes this table and all its data from the database.")
  text_2 = urwid.Text([u"Do you wish to proceed with dropping table ", tablebutton.get_label(), "?"])
  text_error = urwid.AttrWrap( urwid.Text(u""), 'body')

  table_drop_yes = urwid.AttrWrap( urwid.Button(u"Yes", yes_drop), 'btnf', 'btn')
  table_drop_no = urwid.AttrWrap( urwid.Button(u"No", no_drop), 'btnf', 'btn')

  drop_table = urwid.WidgetPlaceholder( urwid.Padding(
    urwid.Pile([
      blank,
      text_error,
      text_1,
      text_2,
      blank,
      urwid.Columns([
        ('fixed', 6, table_drop_no),
        ('fixed', 5, urwid.Text(u"     ")),
        ('fixed', 7, table_drop_yes)
      ]),
    ]), left=5, right=5))

  return drop_table
