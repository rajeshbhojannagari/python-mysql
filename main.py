import mysql.connector as connector
print("MySQl Connector imported successfully")


con=connector.connect(
    host="localhost",
    user="root",
    password="Rajesh@2005",
    database="python_sql_connection"
)
print("connection established successfully")

mycursor=con.cursor()
# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#     print(x)
# created table named Customers
# mycursor.execute("CREATE TABLE Customers (name VARCHAR(255), address VARCHAR(255))")

# inserting details in customers table

sql="INSERT INTO Customers (name,address) VALUES (%s,%s)"
val=("Rajesh","Hyderabad")
mycursor.execute(sql,val)
con.commit()
print(mycursor.rowcount,"record inserted")