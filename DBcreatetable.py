#!/usr/bin/python

import urwid


"""
NOTES
-----
This module builds the widget to allow the user to create a table in a database.


"""

class CreateTableInfo:
  def __init__(self):
    self.table_name = ""
    self.table_fields = ""

def show_db_createtable(main_body, user_info):

  #used to easily insert a blank line widget
  blank = urwid.Divider()

  #create class instance to hold table creation input
  table_info = CreateTableInfo()


  #signal handler for the create button
  def create_btn_press(button):
    #ADD ERROR HANDLING!!!!!!!!!!!!!!!!!!!!!!!!!!
    #error handling to make sure number is less than a certain amount and is valid num
    #store number of fields in table_info
    table_info.table_fields = fields_num.value()

    #if no error, then call function to show second create table view
    second_createtable(main_body, user_info, table_info)


  #signal handler for text input, stores input information from user
  def edit_change_event(self, text):
    table_info.table_name = text


  #variables to hold text to show user for login view
  text_1 = urwid.Text(u"Create a table below:")
  text_2 = urwid.Text(u"(the number of fields must be less than 20...)")
  
  #setting up the edit input widgets for database name and password
  table_name_edit = urwid.Edit(u"Table Name: ", "")
  urwid.connect_signal(table_name_edit, 'change', edit_change_event)
  table_name_edit = urwid.AttrWrap(table_name_edit, 'main_sel', 'main_self')

  fields_num = urwid.IntEdit(u"Number of Table Fields: ")
  table_fields_edit = urwid.AttrWrap(fields_num, 'main_sel', 'main_self')

  #create button
  table_create_btn = urwid.AttrWrap( urwid.Button(u"Create", create_btn_press), 'btnf', 'btn')

  #This is the pile widget that holds all of the main body widgets
  create_table = urwid.WidgetPlaceholder( urwid.Padding(      
      urwid.Pile([
        text_1,
        blank, 
        urwid.Padding( urwid.Pile([table_name_edit, table_fields_edit]), left=5, width=45),
        blank,
        text_2,
        blank,
        urwid.Padding(table_create_btn, left=5, width=11)
      ]), left=5, right=5))

  return create_table


def second_createtable(main_body, user_info, table_info):
  blank = urwid.Divider()
  text_1 = urwid.Text([u"Creating Table: ", table_info.table_name])

  #build out second portion of UI to create a table

  #this is going to be very challenging to implement

  #edit_attribute = 

  #when this renders, you will be able to scroll down, but there's no way
  #to see it...probably not a good way to do it
  listbox_content = [
    blank,
    urwid.Padding(text_1, left=2),
    blank,
    blank,
    blank,
    blank,
    blank,
    blank,
    blank,
    blank,
    urwid.Padding(urwid.Text(u"Testing"), left=2)
  ]

  listbox = urwid.ListBox(urwid.SimpleListWalker(listbox_content))
  listbox = urwid.BoxAdapter(listbox, 5)

  main_body.original_widget = listbox

  

