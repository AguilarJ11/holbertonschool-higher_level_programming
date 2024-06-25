#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists all cities of that state
"""
import MySQLdb
import sys


def cities_from():

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
                ORDER BY states.id ASC
                """
        cur.execute(query, (state_name,))
        rows = cur.fetchall()
        for index, row in enumerate(rows):
            if index + 1 == len(rows):
                print(row[0], end="")
            else:
                print(f"{row[0]}, ", end="")
        print('\n')
        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print(e)


if __name__ == '__main__':
    cities_from()
