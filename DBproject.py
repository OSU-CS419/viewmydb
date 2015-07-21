#!/usr/bin/python

import urwid
import urwid.curses_display

#black, dark red, dark green, brown, dark blue, dark magenta, dark cyan, light gray


def exit_loop(key):
	if key in ('q', 'Q'):
		raise urwid.ExitMainLoop()

def main():
	text_header = (u" Welcome to our CS419 project! q or Q exits the program.")
	text_leftcol1 = (u"Top of left column")
	text_leftcol2 = (u"This is the body of the left column")
	text_maintop = (u"This is the top section of the main body")
	text_mainbody = (u" This is the main body section")
	text_instructions = (u"This is an area that holds instructions")
	
	blank = urwid.Divider()
	listbox_content = [
		blank,
		urwid.Padding(urwid.Text(text_instructions), left=2, right=2),
		blank,
		urwid.Columns([
			('fixed', 15, 
				urwid.AttrWrap( urwid.Padding( urwid.Pile([
							urwid.Text(text_leftcol1),
							urwid.Divider("~"),
							urwid.Text(text_leftcol2)
						])
					, left=1, right=1)
				, 'leftside')
			),
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
	    ('leftside', 'black', 'dark cyan'),
	    ('body', '', 'black'),
	    ('bg', 'black', 'light gray')
	]

	loop = urwid.MainLoop(frame, palette, unhandled_input=exit_loop, screen=urwid.curses_display.Screen())

	loop.run()

if __name__ == '__main__':
	main()
