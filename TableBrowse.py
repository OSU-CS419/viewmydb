#!/usr/bin/python

import urwid

"""
NOTES
-----
This module dynamically builds a table to show all the rows in a
table including column names.

"""

class Tracking:
  def __init__(self):
    self.start = 0
    self.end = 15
  

# reorganizes row list for a column-oriented view, e.g.
# returns a list of widget lists
def splitTable(allrows):
  cols = []
  if allrows:
    # for each column
    for i in range(0, len(allrows[0])):
      col = [] # start a blank column
      # for each row, add to a column
      for index, row in enumerate(allrows):
        col.append(urwid.Text(str(row[i]))) # add a text cell w/ the row's value from the current column
      cols.append(col)  # add the column to the list of columns

  return cols

# creates a widget consisting of a table of all data in the rows
# with column headers
# takes a list of column names and a list of (list)rows

#def showTables(colnames, rowdata):
def showTables(colnames, rowdata, tablefunction, tablebutton, tablename, user_info):
  location = Tracking()
  rows_length = len(rowdata)            # amount of total rows in data
  widget_lists = splitTable(rowdata)    # get a list of a list of widgets

  #generates tables of 15 starting at a certain row
  def generate_table(start, end):
    columns = []					# empty columns list
    for i in range (0, len(colnames)):		# for each column
      if widget_lists:				# if list not empty
        include_list = []     # list to hold just the widgets to make table out of
        for y in range(start, end):
          include_list.append(widget_lists[i][y])
        mypile = urwid.Pile(include_list)	# make a Pile with the list of widgets
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


# builds the Delete buttons in the first column
################################################################################################################
    prepile = []
    for j in range (start, end):
      prepile.append(urwid.Button((u"Delete " + str(j)), row_delete_btn_press, rowdata[j]))

    newpile = urwid.Pile(prepile)
    newlinebox = urwid.LineBox(newpile, title="Delete", rline=' ', trcorner=u'\u2500', brcorner=u'\u2500')
    columns.insert(0, newlinebox)
################################################################################################################

    return urwid.Columns(columns)

# handles presses for the delete buttons
####################################################################
  def row_delete_btn_press(button, row):
    # delete the row
    query = "DELETE FROM " + tablename + " WHERE "
    for k, name in enumerate(colnames):
      if str(row[k]) != "None":
        if k != 0:
          query += " AND "
        query += name
        query += "='"
        query += (str(row[k]) + "'")

    print query
    #query_status = user_info.db_obj.runquery(user_info.db_conn, query_text, 0)
    # go back to the table view
    #tablefunction(tablebutton, tablename)
####################################################################

  #signal handler for the more button
  def more_btn_press(button):
    if location.end < rows_length - 15:
      #can still render a full set of 15 rows
      location.end += 15
      location.start += 15
      table.original_widget = generate_table(location.start, location.end)
      count.set_text([u"Viewing rows ", str(location.start + 1), " - ", str(location.end)])
    elif location.end < rows_length:
      #last chuck of data to show
      location.start = location.end
      location.end = rows_length
      table.original_widget = generate_table(location.start, location.end)
      count.set_text([u"Viewing rows ", str(location.start + 1), " - ", str(location.end)])

  #signal handler for the less button
  def less_btn_press(button):
    if location.start >= 15:
      location.end = location.start
      location.start = location.end - 15
      table.original_widget = generate_table(location.start, location.end)
      count.set_text([u"Viewing rows ", str(location.start + 1), " - ", str(location.end)])

  #more button to show more results
  #only show if results are greater than a certain amount
  more_btn = urwid.AttrWrap( urwid.Button(u"More", more_btn_press), 'btnf', 'btn')
  more_btn = urwid.Padding(more_btn, width=8)

  #less button to go back
  less_btn = urwid.AttrWrap( urwid.Button(u"Less", less_btn_press), 'btnf', 'btn')
  less_btn = urwid.Padding(less_btn, width=8)

  text_1 = urwid.Text(u"View table data below. If the columns or column names are not rendering correctly, then make your terminal wider. The table displays data in pages of 15 rows, click the more or less button to cycle through the data.")

  text_2 = urwid.Text([u"Total Rows: ", str(rows_length)])

  count = urwid.Text([u"Viewing rows ", str(location.start + 1), " - ", str(location.end)])

  if rows_length < 15:
    #render just the data available
    table = generate_table(0, rows_length)

    #clear out more and less buttons
    more_btn.original_widget = urwid.Text(u"")
    less_btn.original_widget = urwid.Text(u"")
  else:
    table = urwid.WidgetPlaceholder(generate_table(location.start, location.end))

  structure_view = urwid.WidgetPlaceholder( urwid.Padding( urwid.Pile([
      urwid.Divider(),
      text_1,
      urwid.Divider(),
      text_2,
      count,
      urwid.Divider(),
      table,
      urwid.Divider(),
      urwid.Columns([
        ('fixed', 8, less_btn),
        ('fixed', 3, urwid.Text(u"   ")),
        ('fixed', 8, more_btn)
      ])
    ]), left=2, right=2))

  #return the widget created that holds all the structure data
  return structure_view

