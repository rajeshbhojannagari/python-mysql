import mysql.connector as connector
print("MySQl Connector imported successfully")


con=connector.connect(
    host="localhost",
    user="root",
    password="Rajesh@2005",
    database="python_sql_connection"
)

print("connection established successfully")


