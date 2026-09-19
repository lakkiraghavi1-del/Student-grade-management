students = {}


def calculate_grade(marks):
    average = sum(marks) / len(marks)

    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def add_student():
    name = input("Enter student name: ")

    if name in students:
        print("Student already exists!")
        return

    marks = []

    print("Enter marks for 5 subjects:")

    for i in range(1, 6):
        while True:
            try:
                mark = float(input(f"Subject {i}: "))

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    average = sum(marks) / len(marks)
    grade = calculate_grade(marks)

    students[name] = {
        "marks": marks,
        "average": average,
        "grade": grade
    }

    print(f"\n{name} added successfully!")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")


def view_students():
    if not students:
        print("\nNo students available.")
        return

    print("\n========== STUDENT RECORDS ==========")

    for name, data in students.items():
        print(f"\nName: {name}")
        print(f"Marks: {data['marks']}")
        print(f"Average: {data['average']:.2f}")
        print(f"Grade: {data['grade']}")


def search_student():
    name = input("Enter student name to search: ")

    if name in students:
        data = students[name]

        print("\nStudent Found!")
        print(f"Name: {name}")
        print(f"Marks: {data['marks']}")
        print(f"Average: {data['average']:.2f}")
        print(f"Grade: {data['grade']}")
    else:
        print("Student not found.")


def delete_student():
    name = input("Enter student name to delete: ")

    if name in students:
        del students[name]
        print("Student deleted successfully!")
    else:
        print("Student not found.")
      
while True:
    print("\n========== STUDENT GRADE MANAGER ==========")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank you for using Student Grade Manager!")
        break

    else:
        print("Invalid choice. Please try again.")

