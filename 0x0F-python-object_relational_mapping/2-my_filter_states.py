#!/usr/bin/python3
'''Script that lists all states with name starting N.'''

from sqlite3 import connect
from unicodedata import name
import MySQLdb
import sys


if __name__ == '__main__':
    mysql_username = sys.argv[1]
    mysql_passwd = sys.argv[2]
    mysql_db = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(host='localhost',
                           user=mysql_username,
                           passwd=mysql_passwd,
                           port=3306,
                           db=mysql_db)
    cursor = conn.cursor()
    cursor.execute('SELECT *\
                    FROM states\
                    WHERE states.name LIKE "{:s}"\
                    ORDER BY states.id'.format(state_name))
    for row in cursor.fetchall():
        if row[1] == state_name:
            print(row)
    cursor.close()
    conn.close()
