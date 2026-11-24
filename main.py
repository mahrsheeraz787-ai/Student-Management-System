from students import add_student, show_students, search_student


while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Student name: ")
        age = int(input("Student age: "))
        course = input("Student course: ")

        add_student(name, age, course)

    elif choice == "2":
        show_students()

    elif choice == "3":
        name = input("Enter student name: ")
        search_student(name)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")