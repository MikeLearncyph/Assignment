import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='minhvu07f',
    autocommit=True
)

mycursor = mydb.cursor()
code = input("Enter ICAO Code to search for airports name and location: ")
mycursor.execute (f'SELECT airport.name, airport.municipality FROM airport where airport.ident = %s', (code,))

result = mycursor.fetchall()
if result:
    print("Airport Name: ", result[0][0])
    print("Municipality: ", result[0][1])