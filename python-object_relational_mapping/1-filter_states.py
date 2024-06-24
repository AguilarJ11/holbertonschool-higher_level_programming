#!/usr/bin/python3
"""
lists all states with a name starting with N (upper N) from the database
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
        cur = db.cursor()
        cur.execute("SELECT * \
                    FROM states \
                    WHERE name = LIKE 'N%'\
                    ORDER BY id ASC")
        rows = cur.fetchall()
        for row in rows:
            print(row)

        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print(e)


if __name__ == '__main__':
    get_all_states()
