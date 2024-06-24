#!/usr/bin/python3
"""
takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys


def get_all_states():
    
    usr = sys.argv[1]
    psw = sys.argv[2]
    dbase = sys.argv[3]
    try:
        db = MySQLdb.connect(host='localhost',
                             port=3306,
                             user=usr,
                             passwd=psw,
                             db=dbase)
        cur = db.cursor()
        arg = sys.argv[4]
        query = 'SELECT * \
                    FROM states \
                    WHERE name = %s \
                    ORDER BY id ASC'
        cur.execute(query, (arg,))
        rows = cur.fetchall()
        for row in rows:
            print(row)

        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print(e)


if __name__ == '__main__':
    get_all_states()
