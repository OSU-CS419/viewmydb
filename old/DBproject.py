#!/usr/bin/python

import urwid
import urwid.curses_display
import frontend

"""
NOTES
-----
These are the possible colors we can use:
black, dark red, dark green, brown, dark blue, dark magenta, dark cyan, light gray

This file is the main file to run the program



"""


def exit_loop(key):
  if key in ('q', 'Q'):
    raise urwid.ExitMainLoop()

def main():
  loop = urwid.MainLoop(frontend.frame, frontend.palette, unhandled_input=exit_loop, screen=urwid.curses_display.Screen())

  loop.run()

if __name__ == '__main__':
  main()

