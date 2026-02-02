import mysql.connector as connector
# print("MySQl Connector imported successfully")


# con=connector.connect(
#     host="localhost",
#     user="root",
#     password="Rajesh@2005",
#     database="python_sql_connection"
# )
# print("connection established successfully")

# mycursor=con.cursor()
# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#     print(x)
# created table named Customers
# mycursor.execute("CREATE TABLE Customers (name VARCHAR(255), address VARCHAR(255))")

# inserting details in customers table
# sql="INSERT INTO Customers (name,address) VALUES (%s,%s)"
# val=("Rajesh","Hyderabad")
# val=("Rajesh","Hyderabad")
# val=("Rajesh","Hyderabad")
# mycursor.execute(sql,val)
# con.commit()
# print(mycursor.rowcount,"record inserted")

#using class to store database

class DatabaseConnection:
    def __init__(self):
        self.con=connector.connect(
            host="localhost",
            user="root",
            password="Rajesh@2005",
            database="python_sql_connection"
        )
        cur=self.con.cursor()
        query="CREATE TABLE IF NOT EXISTS Students (id INT PRIMARY KEY, name VARCHAR(20),age INT)"
        cur.execute(query)
        print("Table 'Student' ensured to exist")

    def insert_student(self,id,name,age):
          sql="INSERT INTO Students(id,name,age) VALUES (%s,%s,%s)"
          val=[id,name,age]
          cur=self.con.cursor()
          cur.execute(sql,val)
          self.con.commit()
          print("Inserted Successfully")
    def insert_student1(self,id,name,age):
        sql1=f"INSERT INTO Students(id,name,age) VALUES ({id},'{name}',{age})"
        cur=self.con.cursor()
        cur.execute(sql1)
        self.con.commit()
        print("Inserted Successfully")

    def show_student(self):
         sql="SELECT * FROM Students"
         cur=self.con.cursor()
         cur.execute(sql)
         rows=cur.fetchall()
         for row in rows:
            print(row)
    def del_data(self):
        query="DELETE FROM Students WHERE name='Vikram'"
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
    def update_data(self):
        query1="UPDATE Students SET name='Rohith' WHERE name='Arjun'"
        cur=self.con.cursor()
        cur.execute(query1)
        self.con.commit()
      
db=DatabaseConnection()
# db.insert_student(1,"Rajesh",20)
# db.insert_student(2,"Vikram",77)
# db.insert_student(3,"Arjun",50)
# db.insert_student1(4,"Jay",30)
# db.insert_student1(5,"Srikar",19)
# db.del_data()
db.update_data()
db.show_student()