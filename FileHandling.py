import csv
import os

students = {}

def add_student():
    """Add a new student with ID, name, age, and grades"""
    sid = input("Student ID Number: ").strip()

    if sid in students:
        print("That ID already exists!")
        return

    name = input("Enter name: ").strip()
    age = int(input("Enter age: "))

    grades_str = input("Enter student grades: ")
    grades = [int(g) for g in grades_str.split()]
    students[sid] = {"name": name, "age": age, "grades": grades}
    print(f"Student {name} added.")


def display_students():
    """Display all student information"""
    if not students:
        print("No students available.")
        return

    for sid, data in students.items():
        print(f"ID: {sid} | Name: {data['name']} | Age: {data['age']}")
        print(" Grades:", end=" ")
        for g in data['grades']:
            print(g, end=" ")
        print("\n---")

def update_student():
    """Update student info"""
    sid = input("Enter student ID to update: ").strip()
    if sid not in students:
        print("Student not found.")
        return

    name = input("New name (leave blank to keep): ").strip()
    age = input("New age (leave blank to keep): ").strip()
    grades_str = input("New grades (leave blank to keep): ").strip()  # <-- cleaned text

    if name:
        students[sid]["name"] = name
    if age:
        students[sid]["age"] = int(age)
    if grades_str:
        students[sid]["grades"] = [int(g) for g in grades_str.split()]
    print("Student updated.")

def delete_student():
    """Delete a student record"""
    sid = input("Enter student ID to delete: ").strip()
    if sid in students:
        del students[sid]
        print("Student deleted.")
    else:
        print("Student not found.")

def save_to_file():
    """Save students to a CSV file"""
    with open("students.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Age", "Grades"])
        for sid, data in students.items():
            writer.writerow([sid, data["name"], data["age"], ",".join(map(str, data["grades"]))])
    print("Data saved to students.csv")

def load_from_file():
    """Load students from a CSV file"""
    if not os.path.exists("students.csv"):
        print("No file found.")
        return
    with open("students.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            sid = row["ID"]
            name = row["Name"]
            age = int(row["Age"])
            grades = [int(x) for x in row["Grades"].split(",") if x]
            students[sid] = {"name": name, "age": age, "grades": grades}
    print("Data loaded from students.csv")

while True:
    print("===== Student Information System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Save to File")
    print("6. Load from File")
    print("7. Exit")

    choice = input("Enter your choice: ")


    if not choice.isdigit():
        print("Please enter a valid number.")
        continue

    choice = int(choice)

    if choice == 1:
        add_student()
    elif choice == 2:
        display_students()
    elif choice == 3:
        update_student()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        save_to_file()
    elif choice == 6:
        load_from_file()
    elif choice == 7:
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice, please select 1-7.")
