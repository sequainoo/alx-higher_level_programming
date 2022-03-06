#!/usr/bin/python3
'''Script that lists all states with name starting N.'''

import MySQLdb
import sys


if __name__ == '__main__':
    mysql_username = sys.argv[1]
    mysql_passwd = sys.argv[2]
    mysql_db = sys.argv[3]

    conn = MySQLdb.connect(
        host='localhost',
        user=mysql_username,
        passwd=mysql_passwd,
        port=3306,
        db=mysql_db)
    cursor = conn.cursor()
    num_rows = cursor.execute(
        'SELECT * FROM states\
        WHERE regexp_like(states.name, "^N") ORDER BY states.id')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
