#!/usr/bin/python

import urwid
import mainview

"""
NOTES
-----
This module builds the widget to allow the user to enter in their own SQL query

This module will also run the sql query and show a success message if it works

"""

class Qinfo:
  def __init__(self):
    self.query_text = None
    self.query_status = None

class Tracking:
  def __init__(self):
    self.start = 0
    self.end = 15

def show_runsql(frame, body, user_info):
  #used to easily insert a blank line widget
  blank = urwid.Divider()
  query_info = Qinfo()

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

  #do all of the work to show the select query
  def show_select_results(data, text):
    location = Tracking()
    row_length = len(data)
    col_length = len(data[0])
    widget_lists = splitTable(data)    # get a list of a list of widgets

    #clear out previous query text
    sql_edit.original_widget.set_edit_text(u"")

    #generates tables of 15 starting at a certain row
    def generate_table(start, end):
      columns = []          # empty columns list
      for i in range (0, col_length):    # for each column
        if widget_lists:        # if list not empty
          include_list = []     # list to hold just the widgets to make table out of
          for y in range(start, end):
            include_list.append(widget_lists[i][y])
          mypile = urwid.Pile(include_list) # make a Pile with the list of widgets
        else:
          mypile = urwid.Pile([     # a blank widget to fill up some space
          urwid.Text(u""),
        ])

        # make a linebox with the Pile and the columnname
        if i == col_length - 1:
          mylinebox = urwid.LineBox(mypile)
        else:
          mylinebox = urwid.LineBox((mypile), rline=' ', trcorner=u'\u2500', brcorner=u'\u2500')

        columns.append(mylinebox)     # append the linebox to the list of columns

      return urwid.Columns(columns)
    
    #signal handler for the more button
    def more_btn_press(button):
      if location.end < row_length - 15:
        #can still render a full set of 15 rows
        location.end += 15
        location.start += 15
        table.original_widget = generate_table(location.start, location.end)
        count.set_text([u"Viewing rows ", str(location.start + 1), " - ", str(location.end)])
      elif location.end < row_length:
        #last chuck of data to show
        location.start = location.end
        location.end = row_length
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

    select_text_1 = urwid.Text(["The results from the following SELECT query are below.", "\n\nQUERY: ", text])
    select_text_2 = urwid.Text([u"Total Rows: ", str(row_length)])
    count = urwid.Text([u"Viewing rows ", str(location.start + 1), " - ", str(location.end)])

    if row_length < 15:
      #render just the data available
      table = generate_table(0, row_length)

      #clear out more and less buttons
      more_btn.original_widget = urwid.Text(u"")
      less_btn.original_widget = urwid.Text(u"")
    else:
      table = urwid.WidgetPlaceholder(generate_table(location.start, location.end))

    #build out selection results view
    select_results.original_widget = urwid.Pile([
      select_text_1,
      blank,
      select_text_2,
      count,
      blank,
      table,
      blank,
      urwid.Columns([
        ('fixed', 8, less_btn),
        ('fixed', 3, urwid.Text(u"   ")),
        ('fixed', 8, more_btn)
      ])
    ])

  #signal handler for text input, stores input information from user
  def edit_change_event(self, text):
    query_info.query_text = text

  #signal handler for the run button
  def run_btn_press(button):
    #clear out any previous error messages
    text_error.original_widget = urwid.AttrWrap( urwid.Text(u""), 'body')

    #clear out any previous data results
    select_results.original_widget = urwid.Text(u"")

    if query_info.query_text != None:
      #convert string to all uppercase to search for select
      query_info.query_text = query_info.query_text.upper()

      #identify if query string is a select query
      select = False
      if 'SELECT' in query_info.query_text:
        select = True
      
      #run query
      query_info.query_status = user_info.db_obj.runquery(user_info.db_conn, query_info.query_text, select)

      if query_info.query_status['success'] == True:
        if select:
          if query_info.query_status['data']:
            #query was a select query and has data, show select data
            show_select_results(query_info.query_status['data'], query_info.query_text)
          else:
            text_error.original_widget = urwid.AttrWrap( urwid.Text([u" SELECT query did not return any data", "\n QUERY: ", query_info.query_text]), 'error')
        else:
          #show success message
          frame.footer = urwid.AttrWrap(urwid.Text(u" Query executed successfully"), 'header')
          
          #reload main view. this updates tables list if table was created
          mainview.show_main_view(frame, body, user_info)
      else:
        text_error.original_widget = urwid.AttrWrap( urwid.Text(query_info.query_status['data']), 'error')
    else:
      text_error.original_widget = urwid.AttrWrap( urwid.Text(u" You have enter in a query."), 'error')

  #variables to hold text to show user for login view
  text_1 = urwid.Text(u"Enter a SQL query to run below:")
  text_2 = urwid.Text(u"(The edit box supports multiple lines when you press enter)")

  text_error = urwid.AttrMap( urwid.Text(u""), 'body')

  #setting up the edit input widgets for database name and password
  sql_edit = urwid.Edit(caption="", edit_text="", multiline=True)
  urwid.connect_signal(sql_edit, 'change', edit_change_event)
  sql_edit = urwid.AttrWrap(sql_edit, 'btnf', 'btn')

  #run button
  runsql_btn = urwid.AttrWrap( urwid.Button(u"Run", run_btn_press), 'btnf', 'btn')

  #placeholder for any data results from SELECT query
  select_results = urwid.WidgetPlaceholder( urwid.Text(u""))

  #This is the pile widget that holds all of the main body widgets
  runsql = urwid.WidgetPlaceholder(      
      urwid.Pile([
        urwid.Padding(text_error, left=5, width = 50),
        blank,
        urwid.Padding(text_1, left=5),
        urwid.Padding(text_2, left=5),
        urwid.Padding(sql_edit, left=2, right=2),
        blank,
        urwid.Padding(runsql_btn, left=10, width=11),
        blank,
        urwid.Padding(select_results, left=2)
      ]))

  return runsql
