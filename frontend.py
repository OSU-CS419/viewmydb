#!/usr/bin/python

import urwid

"""
NOTES
-----
These are the possible colors we can use:
black, dark red, dark green, brown, dark blue, dark magenta, dark cyan, light gray

This file exists to organize some of the front end code

The UI can be separated into components (components of widgets that we created)
This file aims to organize that better




"""

#Instruction text
text_instructions = (u"This program allows you to connect to a PostgreSQL or MySQL database and then perform operations on that databse. The program is written in python and is an ncurses based command line tool.")

#This is the color palette for the UI
palette = [
  ('header', 'light gray', 'dark red'),
  ('topmenu', 'light gray', 'dark blue'),
  ('leftside', 'light gray', 'dark cyan'),
  ('body', 'black', 'light gray'),
  ('bg', 'black', 'light gray'),
  ('btn','light gray','dark cyan'),
  ('btnf','light gray','dark blue'),
  ('main_sel', 'black', 'light gray'),
  ('main_self', 'light gray', 'black'),
  ('selected', 'light gray', 'dark red')
]

#blank is used as a generic divider widget
blank = urwid.Divider()


#--------------------------------------------------------------------
#This creates the widget for the top most bar

#Signal Handler for the Run SQL button
def run_sql(button):
  frame.footer = urwid.AttrWrap(urwid.Text(
    [u" Pressed: ", button.get_label()]), 'header')

#Creating the widget that holds the top bar information
selected = urwid.Text(u" Selected Entity:")
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

db_name = (u"")

text_leftcol2_2 = (u"")
text_leftcol2_3 = (u"")
text_leftcol2_4 = (u"")
text_leftcol2_5 = (u"")
text_leftcol2_6 = (u"")
text_leftcol2_7 = (u"")

#signal handler for left column widget buttons
def leftcol_btn_press(button):
  frame.footer = urwid.AttrWrap(urwid.Text(
    [u" Pressed: ", button.get_label()]), 'header')
  selected.set_text([u" Selected Entity: ", button.get_label()])

#Function to build the DB button based off of DB name given
def build_db_btn(db_name):
  db_button = urwid.AttrWrap( urwid.Button(db_name, leftcol_btn_press), 'btn', 'btnf')
  return db_button

#creating variable for database button widget
db_button = urwid.AttrWrap( urwid.Button(db_name, leftcol_btn_press), 'btn', 'btnf')

#left column widget variable build
left_column = urwid.AttrWrap( urwid.Padding (urwid.Pile([
        blank,
        urwid.Text(text_leftcol1_1, align='center'),
        db_button,
        urwid.Divider("="),
        blank,
        urwid.Text(text_leftcol2_1, align='center'),
        

        urwid.AttrWrap( urwid.Button(text_leftcol2_2, leftcol_btn_press), 'btn', 'btnf'),
        urwid.AttrWrap( urwid.Button(text_leftcol2_3, leftcol_btn_press), 'btn', 'btnf'),
        urwid.AttrWrap( urwid.Button(text_leftcol2_4, leftcol_btn_press), 'btn', 'btnf'),
        urwid.AttrWrap( urwid.Button(text_leftcol2_5, leftcol_btn_press), 'btn', 'btnf'),
        urwid.AttrWrap( urwid.Button(text_leftcol2_6, leftcol_btn_press), 'btn', 'btnf'),
        urwid.AttrWrap( urwid.Button(text_leftcol2_7, leftcol_btn_press), 'btn', 'btnf'),
        blank
      ])
    , left=1, right=2)
  , 'leftside')
#END~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#--------------------------------------------------------------------
#This will be the tool bar top widget of the main body
text_maintop = u" This is the top section of the main body"
#END~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#--------------------------------------------------------------------
#This will be the main body widget
text_mainbody_1 = urwid.Text(u"First, please use the below radio buttons to select either a MySQL or PostgreSQL database to connect to.")
text_mainbody_2 = urwid.Text(u"Now, please enter in the database name and password below in order to connect to the database.")

#signal handler for 
def db_connect(button):
  frame.footer = urwid.AttrWrap(urwid.Text(
    [u" Pressed: ", button.get_label()]), 'header')
  #print vars(main_body)
  #main_body.original_widget = urwid.Text(u"Testing")
  #main_body = urwid.Text(u"Testing")
  #print vars(main_body)
  #frame.body = urwid.Filler( urwid.Text(u"Testing"))


#signal handler for radio buttons
def radio_change():
  test1 = 2

#signal handler for text input




# def leftcol_btn_press(button):
#   frame.footer = urwid.AttrWrap(urwid.Text(
#     [u" Pressed: ", button.get_label()]), 'header')
#   selected.set_text([u" Selected Entity: ", button.get_label()])


#setting up radio elements for MySQL or PostgreSQL choice
radio_list = []
mysql_radio = urwid.AttrWrap( urwid.RadioButton(radio_list, u"MySQL"), 'main_sel', 'main_self')
psql_radio = urwid.AttrWrap( urwid.RadioButton(radio_list, u"PostgreSQL"), 'main_sel', 'main_self')

#setting up the edit input widgets for database name and password
db_name_edit = urwid.AttrWrap( urwid.Edit(u"Database name: ", ""), 'main_sel', 'main_self')
db_pw_edit = urwid.AttrWrap( urwid.Edit(u"Database password: ", ""), 'main_sel', 'main_self')

#connect button
db_connect_btn = urwid.AttrWrap( urwid.Button(u"Connect", db_connect), 'main_sel', 'main_self')

#This is the pile widget that holds all of the main body widgets
main_body = urwid.Padding( 
  urwid.Pile([text_mainbody_1,
    blank, 
    urwid.Padding( urwid.Pile([mysql_radio, psql_radio]), width=14, left=5),
    blank,
    text_mainbody_2,
    blank,
    urwid.Padding( urwid.Pile([db_name_edit, db_pw_edit]), left=5, width=45),
    blank,
    urwid.Padding(db_connect_btn, left=5, width=11)
  ]), left=1, right=2)
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
          urwid.AttrWrap( urwid.Divider("-"), 'topmenu'),
          #tool bar menu
          urwid.AttrWrap( urwid.Text(text_maintop), 'topmenu'),
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


#--------------------------------------------------------------------
#Creating the frame widget with header and body
#The frame is the most top level widget that is passed to the MainLoop()
text_header = (u" Welcome to our CS419 project! q or Q exits the program.")

#this is the widget for the frame header
frame_header = urwid.AttrWrap(urwid.Text(text_header), 'header')

#this is the widget that acts as the body of the frame and is a ListBox
listbox = urwid.ListBox(urwid.SimpleListWalker(listbox_content))

#setting the listbox focus to start focus on db name button
listbox.set_focus(6)

#Creating the frame widget
frame = urwid.Frame(urwid.AttrWrap(listbox, 'bg'), header=frame_header)
#END~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



