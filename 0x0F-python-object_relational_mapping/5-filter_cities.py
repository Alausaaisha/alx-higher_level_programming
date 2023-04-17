#!/usr/bin/python3
"""This module takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
script should take 4 arguments: mysql username, mysql password,
database name and state name.
script should connect to a MySQL server running on localhost at
port 3306
Results must be sorted in ascending order by cities.id"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    if len(argv) == 5:
        cur.execute("SELECT cities.name from cities\
                    INNER JOIN states ON states.id = cities.state_id\
                    WHERE states.name = %s ORDER BY cities.id ASC",
                    (argv[4], ))
        cities = []
        rows = cur.fetchall()
        for row in rows:
            for city in row:
                cities.append(city)
        if len(cities) != 0:
            for city in range(len(cities)):
                if city < len(cities) - 1:
                    print(cities[city], end=', ')
            print(cities[city])
        else:
            print('')
    cur.close()
    db.close()
