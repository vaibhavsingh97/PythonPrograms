# Create a Python application that manages a set of users who join the
# system with a login name and a password. Once established, existing
# users can return as long as theyremember their login and password. New
# users cannot create an entry with  someone else's login name.
database = {}


def showmenu():
    while(True):
        print("**Python Login Application**")
        print("1. Login\n2. Signup\n3. Exit")
        choice = input("Enter Choice:")
        if choice == 1:
            olduser()
        elif choice == 2:
            newuser()
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


if __name__ == '__main__':
    showmenu()
