#!/usr/bin/python3
'''Script that lists all states with name starting N.'''

from unicodedata import name
import MySQLdb
import sys


if __name__ == '__main__':
    mysql_username = sys.argv[1]
    mysql_passwd = sys.argv[2]
    mysql_db = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(
        host='localhost',
        user=mysql_username,
        passwd=mysql_passwd,
        port=3306,
        db=mysql_db)
    cursor = conn.cursor()
    num_rows = cursor.execute(
        'SELECT * FROM states\
        WHERE states.name LIKE "{}"\
            ORDER BY states.id'.format(state_name))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
