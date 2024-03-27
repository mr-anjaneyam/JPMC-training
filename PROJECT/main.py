# A simple login management portal

user_logins = {"test":"1234"}
user_details = {"test":["name", "rollno", "email"]}

class UserMgmt:
    def createUser(self, uname, pword):
        user_logins[uname] = pword
        print("User {} created successfully!".format(uname))
    def userLogin(self, uname):
        if uname in user_logins:
            pword = input("Password: ")
            if user_logins[uname] == pword:
                print("Successfully logged in")
            else:
                print("Incorrect password")
        else:
            print("User not found. Please register before trying again!")
    def displayDetails(self, uname):
        if uname in user_details:
            print("Name: {}\nRollNo: {}\nEmail: {}".format(*user_details[uname]))
            # print(*user_details[uname])
        else:
            print("User not found")

    def updateDetails(self, name, uname, email, rollno):
        if uname in user_logins:
            user_details[uname] = [name, rollno, email]
            print("User details updated successfully!")
        else:
            print("User not found")

user = UserMgmt()
while True:
    print("\n*********************\n1. Create User\n2. Login\n3. Update Details\n4. Display Details\nAny other number to exit\n*********************\n")
    n = int(input("Enter choice: "))
    if n == 1:
        print("Enter user details")
        uname = input("Username: ")
        if uname not in user_logins:
            pword = input("Password: ")
            name = input("Name: ")
            email = input("Email: ")
            rollno = input("RollNo: ")
            user.createUser(uname, pword)
            user.updateDetails(name, uname, email, rollno)
        else:
            print("User already exists!")
    elif n==2:
        print("Enter login details")
        uname = input("Username: ")
        user.userLogin(uname)
    elif n==3:
        uname = input("Username: ")
        pword = input("New Password: ")
        name = input("Name: ")
        email = input("Email: ")
        RollNo = input("RollNo: ")
        user_logins[uname] = pword
        user.updateDetails(name, uname, email, RollNo)
    elif n==4:
        uname = input("Username: ")
        user.displayDetails(uname)
    else:
        print("Hasta la Vista!\n")
        break
