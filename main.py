from weekassignment import AdmissionDB

def main():
    db=AdmissionDB()
    while True:
        print("1. Add Student")
        print("2. Apply for Admission")
        print("3. View Applications")
        print("4. Approve Application")
        print("5. Reject Application")
        print("6. Exit")
        choice=int(input("Enter a choice: "))
        if choice==1:
            name=input("Enter a name: ")
            email=input("Enter a email: ")
            phone_number=(input("Enter a phone number: "))
            city=input("Enter a city: ")
            db.add_students(name,email,phone_number,city)
        elif choice==2:
            student_id=int(input("Enter the student_id: "))
            course=input("Enter the course: ")
            marks=int(input("Enter the marks: "))
            db.apply_for_admission(student_id,course,marks)
        elif choice==3:
            db.view_all_applications()
        elif choice==4:
            application_id=int(input("Enter a application id: "))
            status="Approved"
            db.update_status(application_id,status)
        elif choice==5:
            application_id=int(input("Enter a appliaction id: "))
            status="Rejected"
            db.update_status(application_id,status)
        elif choice==6:
            db.close()
            break
        else:
            print("Invalid choice")
main()