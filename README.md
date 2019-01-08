Log-Analysis-Udacity-Project
=============

### Project Description
>To create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

#### Introduction

The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. The database includes three tables:

The authors table includes information about the authors of articles.
The articles table includes the articles themselves.
The log table includes one entry for each time a user has accessed the site.
  
#### Setting up the database:

  1. Load the data in local database using the command:
  
  ```
    psql -d news -f newsdata.sql
  ```
  2. Use `psql -d news` to connect to database.
  ```

#### To Run:

  Run logs.py using:
  ```
    $ python logs.py
  ```
