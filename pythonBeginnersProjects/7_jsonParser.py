import json

FILE_NAME = "students.json"


def load_data():
    """Load student data from JSON file."""
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error: Unable to load data from students.json")
        return []


# Function to view all students
def view_students():
    """Display all student records."""
    students = load_data()
    if not students:
        print("No student records found.")
        return
    print("\n--- Student Records ---")
    for student in students:
        print(student)


# Function to search student by id
def search_student():
    """Search student by ID."""
    students = load_data()
    student_id = input("Enter student ID to search: ").strip()

    if not student_id.isdigit():
        print("Invalid input! Please enter a valid numeric ID.")
        return

    student_id = int(student_id)

    for student in students:
        if student["id"] == student_id:
            print("\n--- Student Found ---")
            print(student)
            return

    print(f"No student found with ID {student_id}.")


def filter_students():
    """Filter students based on CGPA or Age."""
    students = load_data()

    # Ask the user which field to filter by (cgpa or age)
    key = input("Enter key to filter by (cgpa/age): ").strip()

    if key not in ["cgpa", "age"]:
        print("Invalid key! You can only filter by 'cgpa' or 'age'.")
        return

    operator = input("Enter condition operator (>, <, >=, <=, ==): ").strip()

    # Ask the user to enter a value based on the key
    if key == "cgpa":
        value = float(input("Enter CGPA (e.g., 8.5): ").strip())  # Directly asking for a float
    elif key == "age":
        value = int(input("Enter age (integer): ").strip())  # Directly asking for an integer

    # Create an empty list to store filtered students
    filtered_students = []

    # Loop through all students and apply the condition
    for student in students:
        student_value = student[key]

        # Apply the filter condition
        if operator == ">" and student_value > value:
            filtered_students.append(student)
        elif operator == "<" and student_value < value:
            filtered_students.append(student)
        elif operator == ">=" and student_value >= value:
            filtered_students.append(student)
        elif operator == "<=" and student_value <= value:
            filtered_students.append(student)
        elif operator == "==" and student_value == value:
            filtered_students.append(student)

    # Print the filtered results
    if filtered_students:
        print(f"\n--- Students with {key} {operator} {value} ---")
        for student in filtered_students:
            print(student)
    else:
        print(f"No students found with {key} {operator} {value}.")


# Function to delete a student by ID
def delete_student():
    """Delete a student by ID."""
    students = load_data()
    student_id = int(input("Enter student ID to delete: ").strip())

    updated_students = []
    for s in students:
        if s["id"] != student_id:
            updated_students.append(s)

    if len(updated_students) == len(students):
        print("No student found with this ID.")
        return

    with open(FILE_NAME, "w") as f:
        json.dump(updated_students, f, indent=4)
    print(f"Student with ID {student_id} deleted successfully.")


# Function to handle user choices
def user_choice(choice):
    if choice == "1":
        view_students()
    elif choice == "2":
        search_student()
    elif choice == "3":
        filter_students()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting... Goodbye!")
        return
    else:
        print("Invalid choice! Try again.")


# Main CLI Menu
if __name__ == "__main__":
    while True:
        print("\nJSON Data Processor - Student Records")
        print("1. View all students")
        print("2. Search student by key-value pair")
        print("3. Filter students by condition")
        print("4. Delete a student")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()
        user_choice(choice)

        if choice == "5":
            break
