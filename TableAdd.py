#!/usr/bin/python

import urwid

"""
NOTES
-----
This module builds the widget to add a row of data to a table

"""

class AddInfo:
  def __init__(self):
    self.add_field = ""
    self.add_query_text = ""
    self.add_current = 1


def show_add_view(frame, edit_body, user_info, tablename):
  blank = urwid.Divider()
  add_info = AddInfo()

  col_names = user_info.db_obj.getcolnames(user_info.db_conn, tablename)
  col_length = len(col_names)

  add_error = urwid.Text(u"")
  add_text_1 = urwid.Text(u"Use the below form to add a row of data to the table.")

  field_text = urwid.Text(["Now adding data for field: ", str(add_info.add_current), " / ", str(col_length)])

  def edit_change_event(self, text):
    add_info.add_field = text


  def next_field(button):
    if add_info.add_current < col_length:
      #not done, need to load another form
      next_form()
    else:
      #input is done, can run query
      add_row()



  field_input_text = urwid.Edit(["Field->", col_names[add_info.add_current - 1], ": "])
  urwid.connect_signal(field_input_text, 'change', edit_change_event)
  field_input = urwid.AttrWrap(field_input_text, 'main_sel', 'main_self')

  

  #check to see if table only has one field, then next button becomes add button
  if add_info.add_current < col_length:
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
  add_body = urwid.Padding(
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

  return add_body
