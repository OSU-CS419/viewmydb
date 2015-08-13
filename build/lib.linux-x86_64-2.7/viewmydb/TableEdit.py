#!/usr/bin/python

import urwid
import mainview

"""
NOTES
-----
This module builds the widget to show the edit view for the table.

"""

class EditTableInfo:
  def __init__(self):
    self.rename_name = ""
    self.add_field = ""
    self.add_query_string = ""
    self.add_current = 0

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

  text_1 = urwid.Text([u"Rename table: ", tablename])
  text_error = urwid.AttrWrap( urwid.Text(u""), 'body')

  #rename edit input field
  table_rename_edit = urwid.Edit(u"New name: ", "")
  urwid.connect_signal(table_rename_edit, 'change', edit_change_event)
  table_rename_edit = urwid.AttrWrap(table_rename_edit, 'main_sel', 'main_self')

  #rename button
  table_rename_btn = urwid.AttrWrap( urwid.Button(u"Rename", rename_btn_press), 'btnf', 'btn')

  #---------------------------------------------------------------------------------
  #setting up the add a row view
  col_names = user_info.db_obj.getcolnames(user_info.db_conn, tablename)
  col_length = len(col_names)

  #clear out and start creating query string
  edit_info.add_query_string = ""
  edit_info.add_query_string += 'INSERT INTO ' + tablename + ' VALUES ('
  
  add_error = urwid.AttrWrap( urwid.Text(u""), 'main_sel')
  add_text_1 = urwid.Text(u"Use the below form to add a row of data to the table.\nIf you leave the entry blank, it will default to NULL.\nIf you have a table with an auto-incrementing column, you can type 'DEFAULT' and it will resort to the default value.\nNote that default will also work for other columns with default values set up.")

  field_text = urwid.Text(["Now adding data for field: ", str(edit_info.add_current + 1), " / ", str(col_length)])

  def edit_change_event(self, text):
    edit_info.add_field = text

  def try_again(button):
    main_body.original_widget = show_table_edit(frame, body, main_body, user_info, tablename)

  def next_field(button):
    frame.footer = urwid.AttrWrap( urwid.Text(""), 'body')

    field_copy = edit_info.add_field.upper()

    if edit_info.add_field == "":
      edit_info.add_query_string += "NULL"
    elif edit_info.add_field.isdigit() or field_copy == "DEFAULT":
      edit_info.add_query_string += edit_info.add_field
    else:
      edit_info.add_query_string += "'" + edit_info.add_field + "'"
    
    edit_info.add_current += 1

    if edit_info.add_current < col_length:
      #not done, need to load another form
      next_form()
    else:
      #input is done, can run query
      add_row()

  field_input_text = urwid.Edit(["Field->", col_names[edit_info.add_current], ": "])
  urwid.connect_signal(field_input_text, 'change', edit_change_event)
  field_input = urwid.AttrWrap(field_input_text, 'main_sel', 'main_self')

  #check to see if table only has one field, then next button becomes add button
  if edit_info.add_current < col_length:
    #next button
    next_field_btn = urwid.AttrWrap( urwid.Button(u"Next", next_field), 'btnf','btn')
  else:      
    #next button
    next_field_btn = urwid.AttrWrap( urwid.Button(u"Add", next_field), 'btnf','btn')

  next_field_btn = urwid.WidgetPlaceholder(next_field_btn)

  def add_row():
    edit_info.add_query_string += ');'

    #run insert query
    query_status = user_info.db_obj.runquery(user_info.db_conn, edit_info.add_query_string, False)

    if query_status['success']:
      #query was successful, show success message and change view
      frame.footer = urwid.AttrWrap( urwid.Text(u" Row added successfully"), 'header')      
      
      #redirect to show this page again
      main_body.original_widget = show_table_edit(frame, body, main_body, user_info, tablename)
    else:
      #query failed, show error message
      add_error.original_widget = urwid.AttrWrap( urwid.Text(["Query Failed.\nQUERY: ", edit_info.add_query_string, "\n\n", query_status['data']]), 'error')

      #show try again button
      next_field_btn.original_widget = urwid.AttrWrap( urwid.Button("Try Again", try_again), 'btnf', 'btn')
    
  def next_form():
    #clear form
    field_input_text.set_edit_text(u"")

    #show current number to edit
    field_text.set_text(["Now adding data for field: ", str(edit_info.add_current + 1), " / ", str(col_length)])

    #show current field name
    field_input_text.set_caption(["Field->", col_names[edit_info.add_current], ": "])

    #keep processing data
    edit_info.add_query_string += ', '

    if edit_info.add_current == col_length - 1:
      #this is the last attribute to add, replace next button with add button
      next_field_btn.original_widget = urwid.AttrWrap( urwid.Button("Add", next_field), 'btnf', 'btn')

  #----------------------------------------------------------------------------

  add_box = urwid.Pile([
    add_error,
    blank,
    field_text,
    blank,
    urwid.Padding(field_input, right=5),
    blank,
    urwid.Padding(next_field_btn, left=5, width=13)
  ])

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
      add_text_1,
      blank,
      urwid.LineBox(add_box)
    ]), left=5, right=5))

  return edit_body
