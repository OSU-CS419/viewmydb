#!/usr/bin/python

import urwid
import urwid.curses_display

#import whatever file the widget you need to test is in
import DBcreatetable
import tablestructure
import connect

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
  
  #TEST WIDGET GOES HERE-----------------------------------
#  test_widget = tablestructure.showTables([('row1', 'row1', 'row1'), ('row2', 'row2', 'row2'), ('row3', 'row3', 'row3')], ['name1', 'name2', 'name3'])
#  test_widget = DBcreatetable.show_db_createtable("test", "test")
  test_widget= tablestructure.showTables(connect.cols, connect.rows)	# method to dynamically show all table rows
  test_widget = urwid.Filler(test_widget)

  #create loop variable and then call urwid event loop
  loop = urwid.MainLoop(test_widget, palette, unhandled_input=unhandled_input, screen=urwid.curses_display.Screen())
  loop.run()


if __name__ == '__main__':
  main()
