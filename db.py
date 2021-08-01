# create database:
# mysql> CREATE DATABASE todos;
# 
# create table:
# mysql> CREATE TABLE todolist (id INT NOT NULL, name VARCHAR(100) NOT NULL, status INT NOT NULL DEFAULT 0, PRIMARY KEY (id)) ENGINE=InnoDB DEFAULT CHARSET=utf8;

from logging import error
import MySQLdb as mdb
from MySQLdb.cursors import DictCursor
import sys

# private constants
__db_host = 'localhost'
__db_user = 'root'
__db_pswd = '654321'
__db_name = 'todos'
__connection = None

# public constants
table_name = "todolist"

def ping_db():
  try:
    con = mdb.connect(__db_host, __db_user, __db_pswd, __db_name)
    # con.cursorclass = DictCursor
    cur = con.cursor()
    cur.execute("SELECT VERSION()")
    ver = cur.fetchone()
    print("Database version : %s " % ver)
  except mdb.Error as e:
    print("Error %d: %s" % (e.args[0], e.args[1]))
    sys.exit(1) # means there was some issue / error / problem and that is why the program is exiting.
  finally:    
    if con:    
        con.close()


def init_db():
  global __connection
  __connection = mdb.connect(
    host=__db_host, 
    user=__db_user, 
    passwd=__db_pswd, 
    db=__db_name, 
    port=3306
  )


def get_connection():
  global __connection
  if __connection is None:
    init_db()
  __connection.cursorclass = DictCursor
  return __connection


def get_cursor():
  global __connection
  if __connection is None:
    init_db()
  return __connection.cursor(DictCursor)


def close_db():
  global __connection
  if __connection is not None:
    try:
      __connection.close()
    except mdb.Error as error:
      print(error)
    finally:
      __connection = None

