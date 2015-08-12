#!/usr/bin/python

import urwid
import mainview
import TableAdd
import TableDelete


"""
NOTES
-----
This module builds the widget to show the edit view for the table.

"""

class EditTableInfo:
  def __init__(self):
    self.rename_name = ""

def show_table_edit(frame, body, main_body, user_info, tablename):
  blank = urwid.Divider()

  edit_info = EditTableInfo()

  def rename_btn_press(button):
    #make sure new name has been entered in
    if edit_info.rename_name == "":
      #show error for blank entry
      text_error.original_widget = urwid.AttrWrap( urwid.Text(u"Enter in a table name."), 'error')
    else:
      #sql function to rename table
      status = user_info.db_obj.rename_table(user_info.db_conn, tablename, edit_info.rename_name)

      if status == 1:
        #show success message in frame footer
        frame.footer = urwid.AttrWrap( urwid.Text([u" Table ", tablename, " renamed to ", edit_info.rename_name]), 'header')

        #redirect to main view to reload new table name
        mainview.show_main_view(frame, body, user_info)
      else:
        #show error message
        text_error.original_widget = urwid.AttrWrap( urwid.Text(status), 'error')

    
  #signal handler for rename table input field
  def edit_change_event(self, text):
    edit_info.rename_name = text

  def add_btn_press(button):
    edit_body.original_widget = TableAdd.show_add_view(frame, edit_body, user_info, tablename)

  def delete_btn_press(button):
    edit_body.original_widget = TableDelete.show_delete_view(frame, edit_body, user_info, tablename)

  text_1 = urwid.Text([u"Rename table: ", tablename])
  text_error = urwid.AttrWrap( urwid.Text(u""), 'body')

  #rename edit input field
  table_rename_edit = urwid.Edit(u"New name: ", "")
  urwid.connect_signal(table_rename_edit, 'change', edit_change_event)
  table_rename_edit = urwid.AttrWrap(table_rename_edit, 'main_sel', 'main_self')

  #rename button
  table_rename_btn = urwid.AttrWrap( urwid.Button(u"Rename", rename_btn_press), 'btnf', 'btn')

  text_2 = urwid.Text(u"Use the below buttons to either add or delete data from the table")
  #add a row button
  add_row_btn = urwid.AttrWrap( urwid.Button(u"Add a row", add_btn_press), 'btnf', 'btn')  
  #delete a row button
  delete_row_btn = urwid.AttrWrap( urwid.Button(u"Delete a row", delete_btn_press), 'btnf', 'btn')

  edit_body = urwid.WidgetPlaceholder( urwid.Padding(
    urwid.Pile([
      blank,
      text_error,
      text_1,
      table_rename_edit,
      blank,
      urwid.Padding(table_rename_btn, left=5, width=10),
      blank,
      blank,
      text_2,
      blank,
      urwid.Columns([
        urwid.Padding(add_row_btn, width=13),
        urwid.Padding(delete_row_btn, width=16)
      ])
    ]), left=5, right=5))

  return edit_body

