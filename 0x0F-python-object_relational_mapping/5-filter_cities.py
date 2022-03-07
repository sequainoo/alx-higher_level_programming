#!/usr/bin/python3
'''Script queries cities of a given state.

Pass state to it as argument and would retrieve all
Associated cities.
'''
import MySQLdb
from sys import argv

if __name__ == '__main__':
    conn = MySQLdb.connect(user=argv[1],
                           passwd=argv[2],
                           host='localhost',
                           port=3306,
                           db=argv[3])
    cursor = conn.cursor()
    sql = 'SELECT cities.name\
           FROM cities JOIN states\
           ON cities.state_id = states.id\
           WHERE states.name LIKE %s\
           ORDER BY cities.id'
    cursor.execute(sql, (argv[4],))
    rows = cursor.fetchall()
    length = len(rows)
    i = 0
    for row in rows:
        if i + 1 == length:
            print(row[0], end='')
        else:
            print(row[0], end=', ')
        i += 1
    print()
