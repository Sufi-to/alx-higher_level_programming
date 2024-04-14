#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    no_funny_bidnes = sys.argv[4]
    cur.execute("""SELECT cities.name * FROM
                 cities INNER JOIN states ON states.id=cities.states_id
                 WHERE states.name=%s""", (no_funny_bidnes, ))
    query_rows = cur.fetchall()
    list_cities = list(row[0] for row in query_rows)
    print(*list_cities, sep=", ")
    cur.close()
    conn.close()
