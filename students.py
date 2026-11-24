students = []


def add_student(name, age, course):
    student = {
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    print("Student added successfully!")


def show_students():
    if not students:
        print("No students found.")
        return

    for student in students:
        print("\n----------------")
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Course:", student["course"])


def search_student(name):
    for student in students:
        if student["name"].lower() == name.lower():
            print("Student found:", student)
            return

    print("Student not found.")