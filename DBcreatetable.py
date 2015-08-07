#!/usr/bin/python

import urwid
import mainview

"""
NOTES
-----
This module builds the widget to allow the user to create a table in a database.

"""

class CreateTableInfo:
  def __init__(self):
    self.count = None
    self.table_name = ""
    self.table_fields = None
    self.query_string = ""
    self.atr_name = ""
    self.atr_type = ""
    self.atr_null = False
    self.atr_primarykey = False
    self.atr_unique = False
    self.atr_none = True

def show_db_createtable(frame, body, main_body, user_info):
  #used to easily insert a blank line widget
  blank = urwid.Divider()

  #create class instance to hold table creation input
  table_info = CreateTableInfo()

  #signal handler for the create button
  def create_btn_press(button):
    #store number of fields in table_info
    table_info.table_fields = fields_num.value()

    #check for errors
    if table_info.table_fields == 0 or table_info.table_name == "":
      text_error.original_widget = urwid.AttrWrap( urwid.Text(u"Enter in both a name and number of fields."), 'error')
    elif table_info.table_fields > 20:
      text_error.original_widget = urwid.AttrWrap( urwid.Text(u"The max number of fields is 20"), 'error')
    else:
      #user input was correct, go to next view
      second_createtable(frame, body, main_body, user_info, table_info)  

  #signal handler for text input, stores input information from user
  def edit_change_event(self, text):
    table_info.table_name = text

  #variables to hold text to show user for login view
  text_error = urwid.AttrWrap( urwid.Text(u""), 'body')
  text_1 = urwid.Text(u"Create a table below:")
  text_2 = urwid.Text(u"(the number of fields must be less than 20...)")
  
  #setting up the edit input widgets for database name and password
  table_name_edit = urwid.Edit(u"Table Name: ", "")
  urwid.connect_signal(table_name_edit, 'change', edit_change_event)
  table_name_edit = urwid.AttrWrap(table_name_edit, 'main_sel', 'main_self')

  fields_num = urwid.IntEdit(u"Number of Table Fields: ")
  table_fields_edit = urwid.AttrWrap(fields_num, 'main_sel', 'main_self')

  #create button
  table_nextstep_btn = urwid.AttrWrap( urwid.Button(u"Next Step", create_btn_press), 'btnf', 'btn')

  #This is the pile widget that holds all of the main body widgets
  create_table = urwid.WidgetPlaceholder( urwid.Padding(      
      urwid.Pile([
        text_error,
        blank,
        text_1,
        blank, 
        urwid.Padding( urwid.Pile([table_name_edit, table_fields_edit]), left=5, width=45),
        blank,
        text_2,
        blank,
        urwid.Padding(table_nextstep_btn, left=5, width=13)
      ]), left=5, right=5))

  return create_table


def second_createtable(frame, body, main_body, user_info, table_info):
  blank = urwid.Divider()
  table_info.count = 0 #holds count on what attribute is being edited

  text_1 = urwid.Text([u"Creating Table: ", table_info.table_name])
  edit_num = urwid.Text([u"Now editing attribute number: ", str(table_info.count + 1), ' / ', str(table_info.table_fields)])

  #clear out query string first
  table_info.query_string = ""

  #start creating the query string
  table_info.query_string += 'CREATE TABLE ' + table_info.table_name + ' (\n'

  #error box
  error_box = urwid.AttrMap( urwid.Text(u""), 'main_sel')

  #signal handler for try again button
  def try_again(button):
    second_createtable(frame, body, main_body, user_info, table_info)

  #signal handler for the next attribute button
  def next_atr(button):
    if table_info.atr_name == "" or table_info.atr_type == "":
      error_box.original_widget = urwid.AttrWrap( urwid.Text(u"You must enter a name and type."), 'error')
    else:
      error_box.original_widget = urwid.AttrWrap( urwid.Text(u""), 'main_sel')

      table_info.query_string += table_info.atr_name + ' ' + table_info.atr_type

      if table_info.atr_null == True:
        table_info.query_string += ' NOT NULL'

      if table_info.atr_primarykey == True:
        table_info.query_string += ' PRIMARY KEY'

      if table_info.atr_unique == True:
        table_info.query_string += ' UNIQUE'

      #increment count to reflect new addition of data
      table_info.count += 1
      
      if table_info.count < table_info.table_fields:
        #call function to bring up next form
        next_form()
      else:
        #call function to execute create table query
        create_table()

  #next button
  atr_next_btn = urwid.AttrWrap( urwid.Button(u"Next", next_atr), 'main_sel', 'main_self')
  atr_next_btn = urwid.WidgetPlaceholder(atr_next_btn)

  #signal handler for edit field events
  def edit_change_event(self, text):
    if self.caption == "Name: ":
      table_info.atr_name = text
    elif self.caption == "Type: ":
      table_info.atr_type = text

  #widget for attribute name edit field
  atr_name_edit = urwid.Edit(u"Name: ", "")
  urwid.connect_signal(atr_name_edit, 'change', edit_change_event)
  atr_name_edit = urwid.AttrWrap(atr_name_edit, 'main_sel', 'main_self')

  #widget for type edit field
  atr_type_edit = urwid.Edit(u"Type: ", "")
  urwid.connect_signal(atr_type_edit, 'change', edit_change_event)
  atr_type_edit = urwid.AttrWrap(atr_type_edit, 'main_sel', 'main_self')  

  #signal handler for checkbox
  def checkbox_change(self, state):
    if state == True:
      table_info.atr_null = True
    else:
      table_info.atr_null = False

  #widget for null checkbox
  null_checkbox = urwid.CheckBox(u"Not Null", state=False, on_state_change=checkbox_change)
  null_checkbox = urwid.AttrWrap(null_checkbox, 'main_sel', 'main_self')

  #signal handler for radio buttons
  def radio_change(self, state):
    if self.label == "Primary Key":
      if state == True:
        table_info.atr_primarykey = True
        table_info.atr_unique = False
        table_info.atr_none = False
    elif self.label == "Unique":
      if state == True:
        table_info.atr_primarykey = False
        table_info.atr_unique = True
        table_info.atr_none = False
    elif self.label == "None":
      if state == True:
        table_info.atr_primarykey = False
        table_info.atr_unique = False
        table_info.atr_none = True

  #widgets for radio buttons
  radio_list = []
  primarykey_radio = urwid.AttrWrap( urwid.RadioButton(radio_list, u"Primary Key", False, on_state_change=radio_change), 'main_sel', 'main_self')
  unique_radio = urwid.AttrWrap( urwid.RadioButton(radio_list, u"Unique", False, on_state_change=radio_change), 'main_sel', 'main_self')
  none_radio = urwid.AttrWrap( urwid.RadioButton(radio_list, u"None", True, on_state_change=radio_change), 'main_sel', 'main_self')

  #create button placeholder
  table_create_btn = urwid.WidgetPlaceholder( urwid.Text(u""))

  #signal handler for create button
  def create_table():
    table_info.query_string += '\n);'
    
    #run query
    query_status = user_info.db_obj.runquery(user_info.db_conn, table_info.query_string)

    if query_status == 1:
      #query was successful, show success message and change view
      frame.footer = urwid.AttrWrap( urwid.Text(u" Table created successfully"), 'header')

      mainview.show_main_view(frame, body, user_info)
    else: 
      #query failed, show error message
      error_box.original_widget = urwid.AttrWrap( urwid.Text(
        [u"Query Failed. Select 'Try Again' below to re-enter attribute information, or 'Create Table' above to start over.\n\n", query_status, "\nQUERY:  ", table_info.query_string]), 'error')

      #if attributes = 1, next button will still be there
      if table_info.table_fields == 1:
        attribute_box.focus_position = 2  
        atr_next_btn.original_widget = urwid.AttrWrap( urwid.Text(u""), 'main_sel')
           
      #clear out create table button and make it try again button
      table_create_btn.original_widget = urwid.AttrWrap( urwid.Button(u"Try Again", try_again), 'main_sel', 'main_self')

  #controls the looping nature of the repetivie process of entering in data for attributes
  def next_form():
    #clear form
    atr_name_edit.set_edit_text(u"")
    atr_type_edit.set_edit_text(u"")
    null_checkbox.set_state(False)
    none_radio.set_state(True)

    #change focus to name input field
    attribute_box.focus_position = 2

    #change attribute count to show current attribute
    edit_num.set_text([u"Now editing attribute number: ", str(table_info.count + 1), ' / ', str(table_info.table_fields)])

    #keep processing data
    table_info.query_string += ',\n'

    if table_info.count == table_info.table_fields - 1:
      #this is the last attribute to edit
      #remove next button and replace with create button
      atr_next_btn.original_widget = urwid.AttrWrap( urwid.Text(u""), 'main_sel')
      table_create_btn.original_widget = urwid.AttrWrap( urwid.Button(u"Create", next_atr), 'main_sel', 'main_self')

  attribute_box = urwid.Pile([
    error_box,
    blank,
    atr_name_edit,
    blank,
    atr_type_edit,
    blank,
    null_checkbox,
    blank,
    primarykey_radio,
    unique_radio,
    none_radio,
    blank,
    urwid.Padding(atr_next_btn, left=15, width=10)
  ])

  create_attribute = urwid.WidgetPlaceholder( urwid.Padding(
    urwid.Pile([
      text_1,
      blank,
      edit_num,
      blank,
      urwid.LineBox(attribute_box),
      blank,
      urwid.Padding(table_create_btn, left=5, width=10)
    ]), left=5, right=5))

  main_body.original_widget = create_attribute
