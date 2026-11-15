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
area = input("Enter the code for area of airport: ")
mycursor.execute(f'SELECT airport.type, COUNT(*) FROM airport where iso_Country = %s GROUP BY airport.type ORDER BY airport.type DESC', (area,))

result = mycursor.fetchall()
if result:
    for row in result:
        print("Airports type", row[0], "- Airport number", row[1])