#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Database connection parameters
    host = "localhost"
    port = 3306
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the database
    db = MySQLdb.connect(host=host, port=port, user=user, passwd=password, db=database)

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute the SQL query to select states starting with 'N'
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    # Fetch all the rows
    rows = cur.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()

