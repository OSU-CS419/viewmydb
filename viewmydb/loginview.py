#!/usr/bin/python

import urwid
import mainview

"""
NOTES
-----
These are the possible colors we can use:
black, dark red, dark green, brown, dark blue, dark magenta, dark cyan, light gray

This is the code to create and run the login view for the program.
If a log in is successful, then the code here will initialize the code that will
create the main view for the program, with a connected DB.

"""


def create_main_view(user_info):
  #used to easily insert a blank line widget
  blank = urwid.Divider()

  #signal handler for the connect button
  def db_connect(button):
    if user_info.mysql == True:
      import mysqlDB as sqlDB	# for MySQL
      user_info.db_obj = sqlDB.MYsql()
    elif user_info.psql == True:
      import psqlDB as sqlDB	# for PostgreSQL
      user_info.db_obj = sqlDB.Psql()

    if (user_info.db_name and user_info.db_uname and user_info.db_pw):
      # connect to the db
      user_info.db_conn = user_info.db_obj.connectdb(user_info.db_name, user_info.db_uname, user_info.db_pw)

      # if connection error returned
      if user_info.db_conn == -1:
        db_error_box.original_widget = urwid.AttrMap( urwid.Text
        (u"Incorrect username, database name, or password. Please try again"),
        'error', 'error')

      # if good connection returned
      else:
        #build out and show the main app view on the screen
        mainview.show_main_view(frame, body, user_info)

    else:
      db_error_box.original_widget = urwid.AttrMap( urwid.Text
        (u"Please enter your username, database name, and password"),
        'error', 'error')

  #signal handler for radio buttons, stores input information from user
  def radio_change(self, state):
    if self.label == "MySQL":
      if state == True:
        user_info.mysql = True
        user_info.psql = False
    elif self.label == "PostgreSQL":
      if state == True:
        user_info.psql = True
        user_info.mysql = False

  #signal handler for text input, stores input information from user
  def edit_change_event(self, text):
    if self.caption == u"Database name: ":
      user_info.db_name = text
    elif self.caption == u"Database password: ":
      user_info.db_pw = text
    elif self.caption == u"Username: ":
      user_info.db_uname = text

  #variables to hold text to show user for login view
  text_mainbody_1 = urwid.Text(u"First, please use the below radio buttons to select either a MySQL or PostgreSQL database to connect to.")
  text_mainbody_2 = urwid.Text(u"Now, please enter in the database name and password below in order to connect to the database.")  

  #setting up radio elements for MySQL or PostgreSQL choice
  radio_list = []
  user_info.psql = True		# default to PostgreSQL
  user_info.mysql = False
  mysql_radio = urwid.AttrWrap( urwid.RadioButton(radio_list, u"MySQL", False, on_state_change=radio_change), 'main_sel', 'main_self')
  psql_radio = urwid.AttrWrap( urwid.RadioButton(radio_list, u"PostgreSQL", True, on_state_change=radio_change), 'main_sel', 'main_self')

  #setting up the edit input widgets for database name and password
  db_uname_edit = urwid.Edit(u"Username: ", "")
  urwid.connect_signal(db_uname_edit, 'change', edit_change_event)
  db_uname_edit = urwid.AttrWrap(db_uname_edit, 'main_sel', 'main_self')

  db_name_edit = urwid.Edit(u"Database name: ", "")
  urwid.connect_signal(db_name_edit, 'change', edit_change_event)
  db_name_edit = urwid.AttrWrap(db_name_edit, 'main_sel', 'main_self')

  db_pw_edit = urwid.Edit(u"Database password: ", "", mask=u"*")
  urwid.connect_signal(db_pw_edit, 'change', edit_change_event)
  db_pw_edit = urwid.AttrWrap(db_pw_edit, 'main_sel', 'main_self')

  #connect button
  db_connect_btn = urwid.AttrWrap( urwid.Button(u"Connect", db_connect), 'main_sel', 'main_self')

  #error box
  db_error_box = urwid.AttrMap( urwid.Text(u""), 'main_sel')

  #This is the pile widget that holds all of the main body widgets
  body = urwid.WidgetPlaceholder( urwid.Filler( urwid.Padding(      
      urwid.Pile([
        text_mainbody_1,
        blank, 
        urwid.Padding( urwid.Pile([psql_radio, mysql_radio]), width=14, left=5),
        blank,
        text_mainbody_2,
        blank,
        urwid.Padding( urwid.Pile([db_uname_edit, db_name_edit, db_pw_edit]), left=5, width=45),
        blank,
        urwid.Padding(db_connect_btn, left=5, width=11),
	blank,
	urwid.Padding(db_error_box, left=5, width=50)
      ]), left=5, right=5),
    valign='top', top=3))
  
  #adding color styling to the body widget
  body = urwid.AttrWrap(body, 'bg')

  #Setting up frame
  frame_header = urwid.Padding( urwid.Text(u"Welcome to our CS419 project! 'q' exits the pogram. Use up and down arrow to navigate."), left=1, right=1)
  frame_header = urwid.AttrWrap(frame_header, 'header')
  frame = urwid.Frame(body=body, header=frame_header)

  #return the frame all set up with body widget
  return frame
