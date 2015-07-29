#!/usr/bin/python

import urwid
import urwid.curses_display
import loginview


"""
NOTES
-----
These are the possible colors we can use:
black, dark red, dark green, brown, dark blue, dark magenta, dark cyan, light gray

This file is an attempt to remove the object oriented approach of having the 
screen implementation be in a class. I don't think it makes much sense to use
classes here as we aren't dealing with objects.
So, I'm trying to make it a functional programming approach.

"""

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

def unhandled_input(key):
  if key == 'q':
    raise urwid.ExitMainLoop()

def main():
  login_widget = loginview.create_main_view()
  loop = urwid.MainLoop(login_widget, palette, unhandled_input=unhandled_input, screen=urwid.curses_display.Screen())
  loop.run()

if __name__ == '__main__':
  main()
