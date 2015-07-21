#!/usr/bin/python

import urwid
import urwid.curses_display

"""
NOTES
-----
These are the possible colors we can use:
black, dark red, dark green, brown, dark blue, dark magenta, dark cyan, light gray



"""


def exit_loop(key):
  if key in ('q', 'Q'):
    raise urwid.ExitMainLoop()

def main():
  text_header = (u" Welcome to our CS419 project! q or Q exits the program.")
  text_leftcol1_1 = (u"Database:")
  text_leftcol1_2 = (u"Test DB")
  text_leftcol2_1 = (u"Tables:")
  text_leftcol2_2 = (u"Table 1")
  text_leftcol2_3 = (u"Table 2")
  text_leftcol2_4 = (u"Table 3")
  text_leftcol2_5 = (u"Table 4")
  text_leftcol2_6 = (u"Table 5")
  text_leftcol2_7 = (u"Table 6")
  text_maintop = (u"This is the top section of the main body")
  text_mainbody = (u" This is the main body section")
  text_instructions = (u"This program allows you to connect to a PostgreSQL or MySQL database and then perform operations on that databse. The program is written in python and is an ncurses based command line tool.")
  
  #this creates blank as a simple divider widget to add a line of space
  blank = urwid.Divider()

  #Signal handler for the left side buttons
  def leftcol_btn_press(button):
      frame.footer = urwid.AttrWrap(urwid.Text(
          [u" Pressed: ", button.get_label()]), 'header')

  #creating left column widget
  left_column = urwid.AttrWrap( urwid.Padding (urwid.Pile([
          blank,
          urwid.Text(text_leftcol1_1, align='center'),
          urwid.AttrWrap( urwid.Button(text_leftcol1_2, leftcol_btn_press), 'btn', 'btnf'),
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


  listbox_content = [
    blank,
    urwid.Padding(urwid.Text(text_instructions), left=2, right=2),
    blank,
    urwid.Columns([
      ('fixed', 17, left_column),
      urwid.AttrWrap( urwid.Padding( urwid.Pile([
            urwid.AttrWrap( urwid.Text(text_maintop), 'topmenu'),
            urwid.AttrWrap( urwid.Divider("-"), 'topmenu'),
            blank,
            urwid.Text(text_mainbody),
            urwid.Text(u" It can keep going down"),
            urwid.Text(u" ... ... ... ... ... ... ... ... ... ... ..."),
            urwid.Text(u" ... ... ... ... ... ... ... ... ... ... ..."),
            urwid.Text(u" ... ... ... ... ... ... ... ... ... ... ..."),
            urwid.Text(u" ... ... ... ... ... ... ... ... ... ... ..."),
            urwid.Text(u" ... ... ... ... ... ... ... ... ... ... ..."),
            urwid.Text(u" ... ... ... ... ... ... ... ... ... ... ..."),
            urwid.Text(u" ... ... ... ... ... ... ... ... ... ... ..."),
            urwid.Text(u" ... ... ... ... ... ... ... ... ... ... ..."),
            urwid.Text(u" ... ... ... ... ... ... ... ... ... ... ..."),
            urwid.Text(u" ... ... ... ... ... ... ... ... ... ... ..."),
            urwid.Text(u" ... ... ... ... ... ... ... ... ... ... ..."),
            urwid.Text(u" ... ... ... ... ... ... ... ... ... ... ..."),
            urwid.Text(u" ... ... ... ... ... ... ... ... ... ... ...")
          ])
        , left=0, right=1)
      , 'body')
    ])
  ]

  frame_header = urwid.AttrWrap(urwid.Text(text_header), 'header')
  listbox = urwid.ListBox(urwid.SimpleListWalker(listbox_content))
  frame = urwid.Frame(urwid.AttrWrap(listbox, 'bg'), header=frame_header)

  palette = [
      ('header', 'light gray', 'dark red'),
      ('topmenu', 'light gray', 'dark blue'),
      ('leftside', 'light gray', 'dark cyan'),
      ('body', 'black', 'light gray'),
      ('bg', 'black', 'light gray'),
      ('btn','light gray','dark cyan'),
      ('btnf','light gray','dark blue')
  ]

  loop = urwid.MainLoop(frame, palette, unhandled_input=exit_loop, screen=urwid.curses_display.Screen())

  loop.run()

if __name__ == '__main__':
  main()
