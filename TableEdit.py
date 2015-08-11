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
    self.add_query_text = ""
    self.add_current = 1


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

  #signal handler for the add a row button, changes view to add row view
  def add_btn_press(button):
    col_names = user_info.db_obj.getcolnames(user_info.db_conn, tablename)
    col_length = len(col_names)

    add_error = urwid.Text(u"")
    add_text_1 = urwid.Text(u"Use the below form to add a row of data to the table.")

    field_text = urwid.Text(["Now adding data for field: ", str(edit_info.add_current), " / ", str(col_length)])

    def edit_change_event(self, text):
      edit_info.add_field = text


    def next_field(button):
      
      if edit_info.add_current < col_length:
        #not done, need to load another form
        next_form()
      else:
        #input is done, can run query
        add_row()



    field_input_text = urwid.Edit(["Field->", col_names[edit_info.add_current - 1], ": "])
    urwid.connect_signal(field_input_text, 'change', edit_change_event)
    field_input = urwid.AttrWrap(field_input_text, 'main_sel', 'main_self')

    

    #check to see if table only has one field, then next button becomes add button
    if edit_info.add_current < col_length:
      #next button
      next_field_btn = urwid.AttrWrap( urwid.Button(u"Next", next_field), 'btnf','btn')
    else:      
      #next button
      next_field_btn = urwid.AttrWrap( urwid.Button(u"Add", next_field), 'btnf','btn')

    #add button
    add_row_btn = urwid.AttrWrap( urwid.Button(u"Add", next_field), 'btnf','btn')



    def add_row():
      print "test"



    def next_form():
      print "test"




    #change the view to the add a row form
    edit_body.original_widget = urwid.Padding(
      urwid.Pile([
        blank,
        add_error,
        add_text_1,
        blank,
        field_text,
        blank,
        urwid.Padding(field_input, right=5),
        blank,
        urwid.Padding(next_field_btn, left=5, width=8)
      ]), left=5)









  def delete_btn_press(button):
    print "testdel"

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

