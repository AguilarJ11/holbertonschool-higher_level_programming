#!/usr/bin/python3

import MySQLdb
import sys


def get_all_states(username, password, database):

    try:
        db = MySQLdb.connect(host='localhost', user=username, passwd=password, db=database)
        cur = db.cursor()
        cur.execute("SELECT * FROM states ORDER BY ID")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print (e)

    cur.close()
    db.close()


if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Please enter only username, passowrd and database")
        sys.exit(1)
    
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    get_all_states(username, password, database)
