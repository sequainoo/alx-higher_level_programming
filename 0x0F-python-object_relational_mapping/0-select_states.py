#!/usr/bin/python3
'''Script that lists all states from hbtn_0e_0_usa.'''
import MySQLdb
import sys

mysql_username = sys.argv[1]
mysql_passwd = sys.argv[2]
mysql_db = sys.argv[3]

conn = MySQLdb.connect(
    host='localhost',
    user=mysql_username,
    passwd=mysql_passwd,
    db=mysql_db)
cursor = conn.cursor()

if __name__ == '__main__':
    num_rows = cursor.execute('SELECT * FROM states ORDER BY states.id')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
