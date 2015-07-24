#!/usr/bin/python

import urwid
import urwid.curses_display
import backend

"""
NOTES
-----
These are the possible colors we can use:
black, dark red, dark green, brown, dark blue, dark magenta, dark cyan, light gray

I'm creating this file to try and put all of the urwid code back into 1 file
instead of separating it out like I previously did. I started to run into some
problems that were being caused by separating the files out, so I wanted to go
back to having it all in one file and working and then try and separate it out.

I'm aiming to follow the structure of the example program bigtext.py in this file



"""

class UserDBInfo:
  def __init__(self):
    self.db_uname = ""
    self.db_name = ""
    self.db_pw = ""
    self.psql = False
    self.mysql = False


#global variables
user_info = UserDBInfo()
blank = urwid.Divider()

class MainDisplay:
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

  def setup_view(self):
    #setup of login view
    text_mainbody_1 = urwid.Text(u"First, please use the below radio buttons to select either a MySQL or PostgreSQL database to connect to.")
    text_mainbody_2 = urwid.Text(u"Now, please enter in the database name and password below in order to connect to the database.")

    #signal handler for 
    def db_connect(button):
      #ADD LATER: check DB connection and show error if not working
      #Call a DB connect function here
      #if error, let user enter in data again and show error
      user_info.db_conn = backend.connectdb(user_info.db_name, user_info.db_uname, user_info.db_pw)

      #build out and show the main app view on the screen
      self.show_main_view()

      #print vars(self.body)
      #print vars(user_info)
      #self.body.original_widget = urwid.Filler(urwid.Text(u"new body"))
      
      #show connect button being pressed in frame footer
      frame.footer = urwid.AttrWrap(urwid.Text(
        [u" Pressed: ", button.get_label()]), 'header')
      
    #signal handler for radio buttons
    def radio_change(self, state):
      if self.label == "MySQL":
        if state == True:
          user_info.mysql = True
          user_info.psql = False
      elif self.label == "PostgreSQL":
        if state == True:
          user_info.psql = True
          user_info.mysql = False

    #signal handler for text input
    def edit_change_event(self, text):
      if self.caption == u"Database name: ":
        user_info.db_name = text
      elif self.caption == u"Database password: ":
        user_info.db_pw = text
      elif self.caption == u"Username: ":
        user_info.db_uname = text

    #setting up radio elements for MySQL or PostgreSQL choice
    radio_list = []
    mysql_radio = urwid.AttrWrap( urwid.RadioButton(radio_list, u"MySQL", False, on_state_change=radio_change), 'main_sel', 'main_self')
    psql_radio = urwid.AttrWrap( urwid.RadioButton(radio_list, u"PostgreSQL", False, on_state_change=radio_change), 'main_sel', 'main_self')

    #setting up the edit input widgets for database name and password
    db_uname_edit = urwid.Edit(u"Username: ", "")
    urwid.connect_signal(db_uname_edit, 'change', edit_change_event)
    db_uname_edit = urwid.AttrWrap(db_uname_edit, 'main_sel', 'main_self')

    db_name_edit = urwid.Edit(u"Database name: ", "")
    urwid.connect_signal(db_name_edit, 'change', edit_change_event)
    db_name_edit = urwid.AttrWrap(db_name_edit, 'main_sel', 'main_self')

    db_pw_edit = urwid.Edit(u"Database password: ", "")
    urwid.connect_signal(db_pw_edit, 'change', edit_change_event)
    db_pw_edit = urwid.AttrWrap(db_pw_edit, 'main_sel', 'main_self')

    #connect button
    db_connect_btn = urwid.AttrWrap( urwid.Button(u"Connect", db_connect), 'main_sel', 'main_self')

    #This is the pile widget that holds all of the main body widgets
    self.body = urwid.WidgetPlaceholder( urwid.Filler( urwid.Padding(      
        urwid.Pile([text_mainbody_1,
          blank, 
          urwid.Padding( urwid.Pile([mysql_radio, psql_radio]), width=14, left=5),
          blank,
          text_mainbody_2,
          blank,
          urwid.Padding( urwid.Pile([db_uname_edit, db_name_edit, db_pw_edit]), left=5, width=45),
          blank,
          urwid.Padding(db_connect_btn, left=5, width=11)
        ]), left=5, right=5),
      valign='top', top=3))
    
    self.body = urwid.AttrWrap(self.body, 'bg')

    #Setting up frame
    frame_header = urwid.Padding( urwid.Text(u"Welcome to our CS419 project! 'q' exits the pogram. Use up and down arrow to navigate."), left=1, right=1)
    frame_header = urwid.AttrWrap(frame_header, 'header')
    frame = urwid.Frame(body=self.body, header=frame_header)

    return frame


  def show_main_view(self):
    text_instructions = (u"This program allows you to connect to a PostgreSQL or MySQL database and then perform operations on that databse. The program is written in python and is an ncurses based command line tool.")

    #--------------------------------------------------------------------
    #This creates the widget for the top most bar

    #Signal Handler for the Run SQL button
    def run_sql(button):
      self.view.footer = urwid.AttrWrap(urwid.Text(
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

    #signal handler for left column widget buttons
    def leftcol_btn_press(button):
      self.view.footer = urwid.AttrWrap(urwid.Text(
        [u" Pressed: ", button.get_label()]), 'header')
      selected.set_text([u" Selected Entity: ", button.get_label()])

    #store database name that user is connected to
    db_name = user_info.db_name

    #store the table names
    db_tables = backend.gettables(user_info.db_conn)

    #create the table button widgets
    table_buttons = urwid.Pile(
      [urwid.AttrWrap( urwid.Button(txt, leftcol_btn_press), 'btn', 'btnf') for txt in db_tables ])

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
            table_buttons,
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
    main_body = urwid.Text(u"This is where the main body will be")
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
    
    #this is the widget that acts as the body of the frame and is a ListBox
    listbox = urwid.ListBox(urwid.SimpleListWalker(listbox_content))
    listbox = urwid.AttrWrap(listbox, 'bg')

    #this substitutes in the old body for this new listbox body
    self.body.original_widget = listbox


  def main(self):
    self.view = self.setup_view()
    self.loop = urwid.MainLoop(self.view, self.palette, unhandled_input=self.unhandled_input, screen=urwid.curses_display.Screen())
    self.loop.run()


  def unhandled_input(self, key):
    if key == 'q':
      raise urwid.ExitMainLoop()
      #print vars(self.body)
      #self.body.original_widget = urwid.Filler(urwid.Text(u"new body"))


def main():
  MainDisplay().main()


if __name__ == '__main__':
  main()

