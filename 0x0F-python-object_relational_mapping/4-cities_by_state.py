#!/usr/bin/python3
'''Script lists all cities fro database'''
import MySQLdb
from sys import argv

if __name__ == '__main__':
    conn = MySQLdb.connect(user=argv[1],
                           passwd=argv[2],
                           host='localhost',
                           port=3306,
                           db=argv[3])
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cities ORDER BY id')
    for row in cursor.fetchall():
        print(row)
