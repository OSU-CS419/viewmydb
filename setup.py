from setuptools import setup

def readme():
  with open('README.md') as f:
    return f.read()

setup(
  name='viewmydb',
  version='0.1.0',
  description='Python terminal GUI for MySQL and PostgreSQL DBs.',
  classifiers=[
    'Development Status :: 4 - Beta',
    'Environment :: Console :: Curses',
    'Programming Language :: Python :: 2.7',
    'Intended Audience :: Information Technology',
    'Natural Language :: English',
    'License :: OSI Approved :: MIT License',
    'Operating System :: Unix'
  ],
  keywords=['mysql', 'postgresql', 'urwid', 'ncurses', 'curses'],
  url='http://github.com/OSU-CS419/viewmydb',
  author="reformingpanda, davidtadams",
  author_email="adams.t.david@gmail.com",
  license='MIT',
  scripts=['bin/viewmydb'],
  packages=['viewmydb'],
  install_requires=[
      'urwid',
      'psycopg2',
      'MySQL-python'
    ],
  include_package_data=True,
  zip_safe=False
)