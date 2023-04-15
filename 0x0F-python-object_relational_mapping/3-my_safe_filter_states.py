#!/usr/bin/python3
"""This module contains a script that takes in an argument
and displays all values in the states table of hbtn_0e_0_usa
where name matches the argument. must be safe from MySQL injections
script should take 4 arguments: mysql username, mysql password,
database name and state name searched
script should connect to a MySQL server running on localhost at
port 3306
must use format to create the SQL query with the user input
Results must be sorted in ascending order by states.id"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    if len(argv) == 5:
        cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                    (argv[4], ))
        rows = cur.fetchall()
        for row in rows:
            print(row)
    cur.close()
    db.close()
