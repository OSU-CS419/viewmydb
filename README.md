viewmydb
===

###An Ncurses Based Database Frontend

Created for:

#####CS419 Software Projects

By:

#####Group 3 (David Adams, Adam Pedigo)



Step 1: Install the program and dependencies

Execute install.sh with the command

```sh
$  ./install.sh
```

This script executes the following commands:

    * sudo apt-get update
    * sudo apt-get install python-dev
    * sudo apt-get install postgresql libpq-dev
    * sudo apt-get install mysql-server libmysqlclient-dev
    * sudo apt-get install python-pip
    * sudo pip install viewmydb

This will install the program and all required dependencies.

Development and testing were performed in Ubuntu 14.04 LTS, but other operating systems may be supported, provided that the required dependencies can be installed.



Step 2: Set up databases (if not already setup)

MySQL:

```sh
$ mysql -uroot -p   // to execute the msyql shell
```
```sh
mysql> CREATE DATABASE [new database name]; // to create a database to work with
```

PostgreSQL:

```sh
$ sudo -u postgres -i  // to change to the postgres user role
```
```sh
postgres~$ createdb [new database name];   // to create a database to work with
```



Step 3: Use the program

Start the program with the command

```sh
$ viewmydb
```
  
Select your desired database type, MySQL or PostgreSQL

Enter your database name, username, and password (if any)

Click 'Connect'
  
Navigate tables using the buttons along the left side of the screen.
  
Navigate functions within tables using the buttons along the top of the screen.


#####Additional Support Available

See:

    docs/Getting-Started-Tuturial.pdf

and:

    docs/Install-Run-Dependencies.pdf

for more information.
