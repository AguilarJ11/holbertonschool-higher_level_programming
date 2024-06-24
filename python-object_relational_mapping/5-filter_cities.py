#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists all cities of that state
"""
import MySQLdb
import sys


def get_all_cities():

    try:
        db = MySQLdb.connect(host='localhost',
                             port=3306,
                             user=sys.argv[1],
                             passwd=sys.argv[2],
                             db=sys.argv[3])
        cur = db.cursor()
        state_name = sys.argv[4]
        query = """
                SELECT cities.name
                FROM cities
                LEFT JOIN states ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY id ASC
                """
        cur.execute(query, (state_name,))
        rows = cur.fetchall()
        for row in rows:
            print(row)

        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print(e)


if __name__ == '__main__':
    get_all_cities()
