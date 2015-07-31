#!/usr/bin/python

import urwid
import urwid.curses_display

#import whatever file the widget you need to test is in
import DBcreatetable


"""
NOTES
-----
This is just a file to help with the development process.

You can build widgets and without having to run the whole program to test them out,
you can just call the function that creates them here and run this file to see what
they look like. 

"""


#This is the color palette used for the program. the format is "name, foreground, background"
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


#This function handles all input that isn't directly handled by a widget. This is
#what allows the user to exit the program.
def unhandled_input(key):
  if key == 'q':
    raise urwid.ExitMainLoop()


#Main function to start the program
def main():
  #test widget goes here
  test_widget = DBcreatetable.show_db_createtable()

  #create loop variable and then call urwid event loop
  loop = urwid.MainLoop(test_widget, palette, unhandled_input=unhandled_input, screen=urwid.curses_display.Screen())
  loop.run()


if __name__ == '__main__':
  main()
