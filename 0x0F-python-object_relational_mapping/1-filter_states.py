#!/usr/bin/python3
"""
Python scripte to list items from MySQL
"""

import MySQLdb

from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    for rows in c.fetchall():
        if rows[1][0] == 'N':
            print(rows)

    c.close()
    db.close()