#!/usr/bin/python3
"""This module lists all cities from the database hbtn_0e_0_usa
script should take 3 arguments: mysql username, mysql password
and database name
script should connect to a MySQL server running on localhost at
port 3306
Results must be sorted in ascending order by cities.id"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name from cities\
                INNER JOIN states ON states.id = cities.state_id\
                ORDER BY cities.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
