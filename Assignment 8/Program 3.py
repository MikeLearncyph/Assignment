import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='minhvu07f',
    autocommit=True
)
from geopy import distance
mycursor = mydb.cursor()
code1 = input("Enter the code for the first airport: ")
code2 = input("Enter the code for the second airport: ")
sql = (f'Select latitude_deg, longitude_deg from airport where airport.ident IN (%s, %s)')
mycursor.execute(sql, (code1, code2))
result = mycursor.fetchall()

if len(result) == 2:
    print(f"{distance.distance(result[0], result[1]).km:.2f} km")