from setuptools import setup

setup(
  name='viewmydb',
  version='0.1.0',
  description='Python terminal GUI for MySQL and PostgreSQL DBs.',
  url='http://github.com/OSU-CS419/viewmydb',
  author="reformingpanda, davidtadams",
  author_email="adams.t.david@gmail.com",
  license='MIT',
  packages=['viewmydb'],
  install_requires=[
      'urwid',
      'psycopg2',
      'MySQL-python'
    ],
  keywords=['mysql', 'postgresql', 'urwid', 'ncurses', 'curses'],
  zip_safe=False
)