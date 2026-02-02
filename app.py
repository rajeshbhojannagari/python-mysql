from main1 import DatabaseConnection

def main():
    db=DatabaseConnection()
    while True:
        print('1.Insert data')
        print('2.Fetch data')
        print('3.Update data')
        print('4.Delete data')
        print('5.Exit')

        choice=int(input("Enter a choice: "))
        if choice==1:
            id=int(input("Enter a id number: "))
            name=input("Enter a name: ")
            age=int(input("Enter a age: "))
            db.insert_student(id,name,age)
        elif choice==2:
            db.show_student()
        elif choice==3:
            id=int(input("Enter a id to update: "))
            name=input("Enter a updated name: ")
            age=int(input("Enter updated age: "))
            db.update_data(id,name,age)
        elif choice==4:
            id=int(input("Enter the id which needed to delete: "))
            db.del_data(id)
        else:
            print("Exited")
            break
main()