"""(a)Update the script in Question 1 so that a timestamp is also kept with the password

indicating date and time of last login. This interface should prompt for login and password

and indicate a successful or failed login as before, but if successful, it should update the last

login timestamp. If the login occurs within four hours of the last login, tell the user, "You

already logged in at: <last_login_timestamp>."

(b) Add an "administration" menu to include the following two menu options: (1) remove a

user and (2) display a list of all users in the system and their passwords

(c) The passwords are currently not encrypted. Add password-encryption if so desired"""
database = {"admin":1234}


def showmenu():
    while(True):
        print "**Python Login Application**"
        print "1. Login\n2. Signup\n3. Admin login \n4. Exit"
        choice = input("Enter Choice:")
        if choice == 1:
            olduser()
        elif choice == 2:
            newuser()
        elif choice==3:
            admin()
        else:
            exit(0)


def olduser():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if database.get(username) == password:
        print "Welcome ", username
    else:
        print "Incorrect credentials"


def newuser():
    while(True):
        username = input("Enter username: ")
        if(database.has_key(username)):
            print "username already exist, Please enter new username."
            continue
        else:
            break
    password = input("Enter password: ")
    database[username] = password


def admin():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if database.get(username) == password:
        print "Welcome ", username,"\n"
        while True:
            print "1.Remove user\n2.Display details of user"
            choice = input("Enter your choice: ")
            if choice==1:
                name=input("Enter username you want to delete:")
                del dict[name]
            else:
                print sorted(dict.items(), key=lambda x: x[1])
    else:
        print "Incorrect credentials\n"


if __name__ == '__main__':
    showmenu()
