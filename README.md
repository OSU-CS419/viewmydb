#viewmydb
####An Ncurses Based Database Frontend

Created for:<br>
#####CS419 Software Projects<br>
By:
#####Group 3 (David Adams, Adam Pedigo)<br>

Step 1: Install the program and dependencies<br>
  Execute install.sh with the command:<br>
  $  ./install.sh<br>

This script executes the following commands:<br>
sudo apt-get update<br>
sudo apt-get install python-dev<br>
sudo apt-get install postgresql libpq-dev<br>
sudo apt-get install mysql-server libmysqlclient-dev<br>
sudo apt-get install python-pip<br>
sudo pip install viewmydb<br>

This will install the program and all required dependencies.<br>
Development and testing were performed in Ubuntu 14.04 LTS, but other operating systems may be supported,<br>
provided that the required dependencies can be installed.<br>

Step 2: Set up databases (if not already setup)<br>
  MySQL:<br>
    $ mysql -uroot -p   // to execute the msyql shell<br>
    mysql> CREATE DATABASE [new database name]; // to create a database to work with<br><br>

  PostgreSQL:<br>
    $ sudo -u postgres -i  // to change to the postgres user role<br>
    postgres~$ createdb [new database name];   // to create a database to work with<br><br>
    
Step 3: Use the program<br>
  Start the program with the command:<br>
  $ viewmydb<br><br>
  
  Select your desired database type, MySQL or PostgreSQL<br>
  Enter your database name, username, and password (if any)<br>
  Click 'Connect'<br><br>
  
  Navigate tables using the buttons along the left side of the screen.<br>
  Navigate functions within tables using the buttons along the top of the screen.
