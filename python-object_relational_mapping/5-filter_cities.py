import sys
import MySQLdb

if len(sys.argv) != 5:
    print("Usage: python script.py host port user password database state_name")
    sys.exit(1)

host = sys.argv[1]
port = int(sys.argv[2])
user = sys.argv[3]
password = sys.argv[4]
database = sys.argv[5]
state_name = sys.argv[6]

try:
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
    else:
        print("No cities found for the state: {}".format(state_name))

except MySQLdb.Error as e:
    print("Error: {}".format(e))

finally:
    # Close cursor and database connection
    if 'cur' in locals() and cur:
        cur.close()
    if 'db' in locals() and db:
        db.close()
