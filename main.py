from database import create_tables

def main_menu():
    print("\n📘 Student Enrollment System")
    print("1. Add Student")
    print("2. Add Course")
    print("3. Enroll Student in Course")
    print("4. View All Students")
    print("5. View All Courses")
    print("6. View All Enrollments")
    print("0. Exit")

    choice = input("Select an option: ")
    return choice

def main():
    create_tables()

    while True:
        choice = main_menu()
        if choice == '0':
            print("Goodbye!")
            break
        else:
            print(f"You selected option {choice} (feature coming soon...)")

if __name__ == "__main__":
    main()
