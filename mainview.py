#!/usr/bin/python

import urwid
import DBstructure
import DBcreatetable
import runsql
import tablestructure

"""
NOTES
-----
These are the possible colors we can use:
black, dark red, dark green, brown, dark blue, dark magenta, dark cyan, light gray

This is the code that sets up and displays the main dashboard view for the program

"""


def show_main_view(frame, body, user_info):
  # the way it is currently, this code block would need to be in every file
  # to determine which db to import
  if user_info.mysql == True and user_info.psql == False:
    import mysqlDB as sqlDB
  elif user_info.psql == True and user_info.mysql == False:
    import psqlDB as sqlDB

  blank = urwid.Divider()

  text_instructions = (u"This program allows you to connect to a PostgreSQL or MySQL database and then perform operations on that databse. The program is written in python and is an ncurses based command line tool. Anything within < > brackets is a selectable button. If the tables do not look right, please make the console window wider.")

  #--------------------------------------------------------------------
  #This creates the widget for the top most bar

  #Signal Handler for the Run SQL button
  def run_sql(button):
    #run the code that generates the run sql input view
    main_body.original_widget = runsql.show_runsql(main_body, user_info)

    frame.footer = urwid.AttrWrap(urwid.Text(
      [u" Pressed: ", button.get_label()]), 'header')

  #Creating the widget that holds the top bar information
  selected = urwid.Text([u" Selected Database: ", user_info.db_name])
  top_bar = urwid.Columns([
    urwid.AttrWrap( selected, 'topmenu'),
    ('fixed', 15, urwid.AttrWrap( urwid.Padding( urwid.Button(
          u"Run SQL", run_sql), 
        right=4), 
      'btnf', 'btn'))
  ])
  #END~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


  #--------------------------------------------------------------------
  #This creates the left column widget
  text_leftcol1_1 = (u"Database:")
  text_leftcol2_1 = (u"Tables:")

  #signal handler for left column database button
  def leftcol_btn_press_db(button):
    main_body.original_widget = DBstructure.show_db_structure(user_info)
    frame.footer = urwid.AttrWrap(urwid.Text(
      [u" Pressed: ", button.get_label()]), 'header')
    selected.set_text([u" Selected Database: ", button.get_label()])

  #signal handler for left column widget buttons
  def leftcol_btn_press_table(button):
    main_body.original_widget = tablestructure.showTables(sqlDB.getcolnames(user_info.db_conn, button.get_label()), sqlDB.allrows(user_info.db_conn, button.get_label()))
    frame.footer = urwid.AttrWrap(urwid.Text(
      [u" Pressed: ", button.get_label()]), 'header')
    selected.set_text([u" Selected Table: ", button.get_label()])

  #store database name that user is connected to
  db_name = user_info.db_name

  #store the table names
  db_tables = sqlDB.gettables(user_info.db_conn)

  #create the table button widgets
  table_buttons = urwid.Pile(
    [urwid.AttrWrap( urwid.Button(txt, leftcol_btn_press_table), 'btn', 'btnf') for txt in db_tables ])

  #creating variable for database button widget
  db_button = urwid.AttrWrap( urwid.Button(db_name, leftcol_btn_press_db), 'btn', 'btnf')

  #left column widget variable build
  left_column = urwid.AttrWrap( urwid.Padding (urwid.Pile([
          blank,
          urwid.Text(text_leftcol1_1, align='center'),
          db_button,
          urwid.Divider("="),
          blank,
          urwid.Text(text_leftcol2_1, align='center'),
          table_buttons,
          blank
        ])
      , left=1, right=2)
    , 'leftside')
  #END~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


  #--------------------------------------------------------------------
  #This will be the tool bar top widget of the main body
  def db_structure_btn_press(button):
    #replace main body with structure data table
    main_body.original_widget = DBstructure.show_db_structure(user_info)

  def db_createtable_btn_press(button):
    #create a table in the database, if error message, show error
    main_body.original_widget = DBcreatetable.show_db_createtable(main_body, user_info)

  text_maintop = u" This is the top section of the main body"
  db_structure_button = urwid.AttrWrap( urwid.Button(u"Structure", db_structure_btn_press), 'btnf', 'btn')
  db_createtable_button = urwid.AttrWrap( urwid.Button(u"Create Table", db_createtable_btn_press), 'btnf', 'btn')

  main_top = urwid.Padding( urwid.Columns([
      ('fixed', 13, db_structure_button),
      ('fixed', 3, urwid.Text(u"  ")),
      ('fixed', 16, db_createtable_button)
    ])
  , left=2, right=2)
  #END~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


  #--------------------------------------------------------------------
  #This will be the main body widget
  #default view upon first render of screen is database-show structure
  main_body = DBstructure.show_db_structure(user_info)
  #END~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


  #--------------------------------------------------------------------
  #This is creating the listbox that makes up the body of the main frame
  #This listbox is the main body of the UI
  listbox_content = [
    blank,
    #instructions section
    urwid.Padding(urwid.Text(text_instructions), left=2, right=2),
    blank,
    urwid.AttrWrap( urwid.Divider(), 'topmenu'),
    #top most bar
    top_bar,
    urwid.AttrWrap( urwid.Divider(), 'topmenu'),
    #the 2 columns holding the left and right side of main body
    urwid.Columns([
      #left column menu
      ('fixed', 17, left_column),
      #right column tool bar and main body
      urwid.AttrWrap( urwid.Padding( urwid.Pile([
            #tool bar menu
            urwid.AttrWrap( urwid.Divider("-"), 'topmenu'),
            urwid.AttrWrap( main_top, 'topmenu'),
            urwid.AttrWrap( urwid.Divider("-"), 'topmenu'),
            blank,
            #main body
            main_body
          ])
        , left=0, right=0)
      , 'body')
    ])
  ]
  #END~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  
  #this is the widget that acts as the body of the frame and is a ListBox
  listbox = urwid.ListBox(urwid.SimpleListWalker(listbox_content))
  listbox = urwid.AttrWrap(listbox, 'bg')

  #this substitutes in the old body for this new listbox body
  body.original_widget = listbox

