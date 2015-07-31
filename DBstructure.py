#!/usr/bin/python

import urwid

"""
NOTES
-----
This module builds the widget to show the structure information for a database.

Note: as of right now, it just has harcoded text and doesn't actually pull data
from the database. This will need to be added.

"""

def show_db_structure(user_info):
  #build out the table that shows the db structure stats

  #Will have to fill all of this in with data received from db

  table_name_col = urwid.LineBox( urwid.Pile([
      urwid.Text(u"Table 1"),
      urwid.Text(u"Table 2"),
      urwid.Text(u"Table 3"),
      urwid.Text(u"Table 4"),
      urwid.Text(u"Table 5"),
      urwid.Text(u"Table 6"),
    ])
  , title="Table", rline=' ', trcorner=u'\u2500', brcorner=u'\u2500')

  records_col = urwid.LineBox( urwid.Pile([
      urwid.Text(u"Table 1"),
      urwid.Text(u"Table 2"),
      urwid.Text(u"Table 3"),
      urwid.Text(u"Table 4"),
      urwid.Text(u"Table 5"),
      urwid.Text(u"Table 6"),
    ])
  , title="Records", rline=' ', trcorner=u'\u2500', brcorner=u'\u2500')

  type_col = urwid.LineBox( urwid.Pile([
      urwid.Text(u"Table 1"),
      urwid.Text(u"Table 2"),
      urwid.Text(u"Table 3"),
      urwid.Text(u"Table 4"),
      urwid.Text(u"Table 5"),
      urwid.Text(u"Table 6"),
    ])
  , title="Type", rline=' ', trcorner=u'\u2500', brcorner=u'\u2500')

  collation_col = urwid.LineBox( urwid.Pile([
      urwid.Text(u"Table 1"),
      urwid.Text(u"Table 2"),
      urwid.Text(u"Table 3"),
      urwid.Text(u"Table 4"),
      urwid.Text(u"Table 5"),
      urwid.Text(u"Table 6"),
    ])
  , title="Collation", rline=' ', trcorner=u'\u2500', brcorner=u'\u2500')

  size_col = urwid.LineBox( urwid.Pile([
      urwid.Text(u"Table 1"),
      urwid.Text(u"Table 2"),
      urwid.Text(u"Table 3"),
      urwid.Text(u"Table 4"),
      urwid.Text(u"Table 5"),
      urwid.Text(u"Table 6"),
    ])
  , title="Size")


  #signal handler for the more button
  def more_btn_press(button):
    print "this is the more button"


  #more button to show more results
  #only show if results are greater than a certain amount
  more_btn = urwid.AttrWrap( urwid.Button(u"More", more_btn_press), 'btnf', 'btn')
  more_btn = urwid.Padding(more_btn, width=8)

  structure_view = urwid.Padding( urwid.Pile( [
    urwid.Columns([
      table_name_col,
      records_col,
      type_col,
      collation_col,
      size_col
    ]),
    more_btn])
  , left=2, right=2)

  structure_view = urwid.WidgetPlaceholder(structure_view)

  #return the widget created that holds all the structure data
  return structure_view
