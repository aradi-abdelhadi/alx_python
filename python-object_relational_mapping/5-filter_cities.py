#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities of that state
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check if the number of arguments is correct
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Database connection parameters
    host = "localhost"
    port = 3306
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the database
    db = MySQLdb.connect(host=host, port=port, user=user, passwd=password, db=database)

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute the SQL query
    query = """SELECT cities.name
               FROM cities
               JOIN states ON cities.state_id = states.id
               WHERE states.name = %s
               ORDER BY cities.id ASC"""
    cur.execute(query, (state_name,))

    # Fetch all the rows
    rows = cur.fetchall()

    # Display the results
    if rows:
        cities = ", ".join(row[0] for row in rows)
        print(cities)

    # Close cursor and database connection
    cur.close()
    db.close()

