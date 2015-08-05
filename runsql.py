#!/usr/bin/python

import urwid


"""
NOTES
-----
This module builds the widget to allow the user to enter in their own SQL query

This module will also run the sql query and show a success message if it works

"""


def show_runsql(main_body, user_info):
  #used to easily insert a blank line widget
  blank = urwid.Divider()

  query_text = ""

  #signal handler for text input, stores input information from user
  def edit_change_event(self, text):
    query_text = text


  #signal handler for the run button
  def run_btn_press(button):
    #ADD ERROR HANDLING!!!!!!!!!!!!!!!!!!!!!!!!!!
    #error handling to make sure the sql query works
    #if no error, then show success message and sql query

    #text_error.set_text(u"No error, query ran successfully!")
    #text_error.set_attr_map({None:'topmenu'})
    #text_error.original_widget.set_text(u" No error, query ran successfully!")
    #size = (5,)
    #text_error.render(size)
    user_info.db_conn.runquery()

    print "TeST"

    try:
      user_info.db_conn.execute(query_text)
      text_error.original_widget = urwid.AttrWrap( urwid.Text(u" No error, query ran successfully"), 'topmenu')
    except psycopg2.Error as e:
      query_error = u"There was an error"
      #query_error = e.pgerror
      text_error.original_widget = urwid.AttrWrap( urwid.Text(query_error), 'error')
      print e

 

  #variables to hold text to show user for login view
  text_1 = urwid.Text(u"Enter a SQL query to run below:")
  text_2 = urwid.Text(u"(The edit box supports multiple lines when you press enter)")

  text_error = urwid.AttrMap( urwid.Text(u""), 'body')

  #setting up the edit input widgets for database name and password
  sql_edit = urwid.Edit(caption="", edit_text="", multiline=True)
  urwid.connect_signal(sql_edit, 'change', edit_change_event)
  sql_edit = urwid.AttrWrap(sql_edit, 'btnf', 'btn')

  #run button
  runsql_btn = urwid.AttrWrap( urwid.Button(u"Run", run_btn_press), 'btnf', 'btn')

  #This is the pile widget that holds all of the main body widgets
  runsql = urwid.WidgetPlaceholder(      
      urwid.Pile([
        urwid.Padding(text_error, left=5, width = 50),
        blank,
        urwid.Padding(text_1, left=2),
        urwid.Padding(text_2, left=2),
        urwid.Padding( sql_edit, left=2, width=60),
        blank,
        urwid.Padding(runsql_btn, left=10, width=11)
      ]))

  return runsql
