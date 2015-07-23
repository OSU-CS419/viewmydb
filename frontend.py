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

#This is a list of variables that are used to hold text for the UI
text_header = (u" Welcome to our CS419 project! q or Q exits the program.")
text_instructions = (u"This program allows you to connect to a PostgreSQL or MySQL database and then perform operations on that databse. The program is written in python and is an ncurses based command line tool.")
text_leftcol1_1 = (u"Database:")
db_name = (u"Test DB")
text_leftcol2_1 = (u"Tables:")

text_leftcol2_2 = (u"Table 1")
text_leftcol2_3 = (u"Table 2")
text_leftcol2_4 = (u"Table 3")
text_leftcol2_5 = (u"Table 4")
text_leftcol2_6 = (u"Table 5")
text_leftcol2_7 = (u"Table 6")

text_maintop = (u" This is the top section of the main body")
text_mainbody = (u" This is the main body section")


#This is the color palette for the UI
palette = [
  ('header', 'light gray', 'dark red'),
  ('topmenu', 'light gray', 'dark blue'),
  ('leftside', 'light gray', 'dark cyan'),
  ('body', 'black', 'light gray'),
  ('bg', 'black', 'light gray'),
  ('btn','light gray','dark cyan'),
  ('btnf','light gray','dark blue'),
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
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#--------------------------------------------------------------------
#This creates the left column widget

#signal handler for left column widget buttons
def leftcol_btn_press(button):
  frame.footer = urwid.AttrWrap(urwid.Text(
    [u" Pressed: ", button.get_label()]), 'header')
  selected.set_text([u" Selected Entity: ", button.get_label()])

#creating variable for database button
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
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


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
          urwid.Text(text_mainbody),
          urwid.Text(u" It can keep going down"),
        ])
      , left=0, right=0)
    , 'body')
  ])
]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#--------------------------------------------------------------------
#Creating the frame widget with header and body
#The frame is the most top level widget that is passed to the MainLoop()

#this is the widget for the frame header
frame_header = urwid.AttrWrap(urwid.Text(text_header), 'header')

#this is the widget that acts as the body of the frame and is a ListBox
listbox = urwid.ListBox(urwid.SimpleListWalker(listbox_content))

#setting the listbox focus to start focus on db name button
listbox.set_focus(6)

#Creating the frame widget
frame = urwid.Frame(urwid.AttrWrap(listbox, 'bg'), header=frame_header)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



