"""Create a simple name and employee number dictionary application. Have the user enter

a list of names and employee numbers. Your interface should allow a sorted output (sorted

by name) that displays employee names followed by their employee numbers"""

dict = {1: "a", 2: "c", 3: "b"}
while True:
    print "+++++Dictionary Application+++++"
    print "1. Enter employee name and employee number\n2. Display employee name and employee number\n3. Exit"
    choice = input("Enter your choice: ")
    if choice == 1:
        emp_number = input("Enter employee number: ")
        if dict.has_key(emp_number):
            print "Employee number already exist."
        else:
            emp_name = raw_input("Enter employee name: ")
            dict[emp_number] = emp_name
            print "Details entered successfully"
    elif choice == 2:
        print sorted(dict.items(), key=lambda x: x[1])
    else:
        exit(0)
