def addstud():
    nm = input("Enter Name : ")
    cnt = input("Enter Contact : ")
    em = input("Enter Email : ")
    dpt = input("Enter Department : ")

    f = open("student.csv", "a")
    f.write(nm + "," + cnt + "," + em + "," + dpt + "\n")
    f.close()

    print("Student Added Successfully")
    menu()

def viewstud():
    print("\nStudent List\n")
    f = open("student.csv", "r")
    print(f.read())
    f.close()
    menu()

def menu():
    print("\n***** Student Management System *****")
    print("1. Add Student")
    print("2. View Student")
    print("3. Exit")

    op = input("Enter Your Choice : ")

    if op == "1":
        addstud()
    elif op == "2":
        viewstud()
    elif op == "3":
        print("Thank You")
    else:
        print("Invalid Choice")
        menu()

menu()
