import re

FILE_NAME = "students.txt"


def validate_email(email):
    """Validate email using regular expression."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None


def add_student():
    try:
        student_id = input("Enter Student ID: ").strip()

        if not student_id:
            raise ValueError("Student ID cannot be empty.")

        name = input("Enter Student Name: ").strip()

        if not name:
            raise ValueError("Student name cannot be empty.")

        age = int(input("Enter Student Age: "))

        if age <= 0:
            raise ValueError("Age must be greater than 0.")

        email = input("Enter Student Email: ").strip()

        if not validate_email(email):
            raise ValueError("Invalid email format.")

        with open(FILE_NAME, "a") as file:
            file.write(f"{student_id},{name},{age},{email}\n")

        print("\nStudent added successfully!")

    except ValueError as e:
        print(f"\nInvalid input: {e}")

    except IOError as e:
        print(f"\nFile error: {e}")


def read_students():
    try:
        with open(FILE_NAME, "r") as file:
            students = file.readlines()

        if not students:
            print("\nNo student records found.")
            return

        print("\n===== Student Records =====")

        for student in students:
            student_id, name, age, email = student.strip().split(",")

            print(f"Student ID : {student_id}")
            print(f"Name       : {name}")
            print(f"Age        : {age}")
            print(f"Email      : {email}")
            print("----------------------------")

    except FileNotFoundError:
        print("\nNo student records found. The file does not exist.")

    except IOError as e:
        print(f"\nFile error: {e}")


def main():
    while True:
        print("\n===== Student Record Manager =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_student()

            elif choice == 2:
                read_students()

            elif choice == 3:
                print("Thank you for using Student Record Manager!")
                break

            else:
                print("Invalid choice. Please select 1, 2, or 3.")

        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
