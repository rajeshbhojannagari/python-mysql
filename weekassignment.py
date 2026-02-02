import mysql.connector as connector
from datetime import date
class AdmissionDB:
    def __init__(self):
        self.con=connector.connect(
            host='localhost',
            user='root',
            password='Rajesh@2005',
            database='new_db'
        )
        cur=self.con.cursor()
        query="""
        CREATE TABLE IF NOT EXISTS students(
        student_id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(50),
        email VARCHAR(50) UNIQUE,
        phone_number VARCHAR(20),
        city VARCHAR(50))"""
        query2="""
        CREATE TABLE IF NOT EXISTS applications(
        application_id INT PRIMARY KEY AUTO_INCREMENT,
        student_id INT,
        FOREIGN KEY(student_id) REFERENCES students(student_id),
        course VARCHAR(50),
        marks INT,
        status VARCHAR(15) DEFAULT 'pending',
        applied_date DATE)"""
        cur.execute(query)
        cur.execute(query2)
        print("Tables Created")
    def add_students(self,name,email,phone_number,city):
        query3="INSERT INTO students(name,email,phone_number,city) VALUES(%s,%s,%s,%s)"
        values=[name,email,phone_number,city]
        cur=self.con.cursor()
        cur.execute(query3,values)
        self.con.commit()
    def apply_for_admission(self,student_id,course,marks):
        query4="INSERT INTO applications(student_id,course,marks,status,applied_date) VALUES(%s,%s,%s,'pending',%s)"
        values1=[student_id,course,marks,date.today()]
        cur=self.con.cursor()
        cur.execute(query4,values1)
        self.con.commit()
    def view_all_applications(self):
        query5="""SELECT applications.application_id,students.name,applications.student_id,applications.course, 
        applications.marks,applications.status,applications.applied_date FROM applications INNER JOIN students on 
        applications.student_id=students.student_id"""
        cur=self.con.cursor()
        cur.execute(query5)
        rows=cur.fetchall()
        for x in rows:
            print(x)
    def update_status(self,application_id,status):
        query6="UPDATE applications SET status=%s WHERE application_id=%s"
        values=[status,application_id]
        cur=self.con.cursor()
        cur.execute(query6,values)
        self.con.commit()
    def close(self):
        self.con.close()
AdmissionDB()
