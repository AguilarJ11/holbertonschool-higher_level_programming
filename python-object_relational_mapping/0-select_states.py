#!/usr/bin/python3
"""
Write a script that lists all states from the database
"""
import MySQLdb
import sys


def get_all_states():

    try:
        db = MySQLdb.connect(host='localhost',
                             port=3306,
                             user=sys.argv[1],
                             passwd=sys.argv[2],
                             db=sys.argv[3])
        cur = db.cursor(named_tuple=True)
        cur.execute("SELECT * FROM states ORDER BY states.id ASC")
        rows = cur.fetchall()
        for row in rows:
            print(row)

        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print(e)
