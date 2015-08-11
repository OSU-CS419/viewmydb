#!/usr/bin/python

import urwid

"""
NOTES
-----
This module dynamically builds a table to show all the rows in a
table including column names.

"""

# reorganizes row list for a column-oriented view, e.g.
# returns a list of widget lists
def splitTable(allrows):
  cols = []
  if allrows:
    for i in range(0, len(allrows[0])):
      col = []
      for index, row in enumerate(allrows):
        col.append(urwid.Text(str(row[i])))
      cols.append(col)

  return cols

# creates a widget consisting of a table of all data in the rows
# with column headers
# takes a list of column names and a list of (list)rows
def showTables(colnames, rowdata):
  widget_lists = splitTable(rowdata)		# get a list of a list of widgets
  columns = []					# empty columns list
  for i in range (0, len(colnames)):		# for each column
    if widget_lists:				# if list not empty
      mypile = urwid.Pile(widget_lists[i])	# make a Pile with the list of widgets
    else:
      mypile = urwid.Pile([			# a blank widget to fill up some space
      urwid.Text(u""),
    ])

    # make a linebox with the Pile and the columnname
    if i == len(colnames) - 1:
      mylinebox = (urwid.LineBox((mypile), title=colnames[i]))
    else:
      mylinebox = (urwid.LineBox((mypile), title=colnames[i], rline=' ', trcorner=u'\u2500', brcorner=u'\u2500'))  

    columns.append(mylinebox)			# append the linebox to the list of columns

  #signal handler for the more button
  def more_btn_press(button):
    print "this is the more button"

  #more button to show more results
  #only show if results are greater than a certain amount
  more_btn = urwid.AttrWrap( urwid.Button(u"More", more_btn_press), 'btnf', 'btn')
  more_btn = urwid.Padding(more_btn, width=8)

  text_1 = urwid.Text(u"View table data below. If the columns or column names are not rendering correctly, then make your terminal wider.")

  structure_view = urwid.WidgetPlaceholder( urwid.Padding( urwid.Pile([
      urwid.Divider(),
      text_1,
      urwid.Divider(),
      urwid.Columns(columns),
      more_btn
    ]), left=2, right=2))

  #return the widget created that holds all the structure data
  return structure_view
