from database import create_tables
from queries import (
    add_student, get_all_students, update_student_email, delete_student,
    add_course, get_all_courses, delete_course,
    enroll_student, get_all_enrollments
)

def main_menu():
    print("\n📘 Student Enrollment System")
    print("1. Add Student")
    print("2. Add Course")
    print("3. Enroll Student in Course")
    print("4. View All Students")
    print("5. View All Courses")
    print("6. View All Enrollments")
    print("7. Update Student Email")
    print("8. Delete Student")
    print("9. Delete Course")
    print("0. Exit")

    return input("Select an option: ")

def main():
    create_tables()

    while True:
        choice = main_menu()

        if choice == '1':
            first = input("Enter first name: ")
            last = input("Enter last name: ")
            email = input("Enter email: ")
            add_student(first, last, email)
            print("✅ Student added.")

        elif choice == '2':
            name = input("Enter course name: ")
            code = input("Enter course code: ")
            add_course(name, code)
            print("✅ Course added.")

        elif choice == '3':
            student_id = input("Enter student ID: ")
            course_id = input("Enter course ID: ")
            enroll_student(int(student_id), int(course_id))
            print("✅ Student enrolled.")

        elif choice == '4':
            students = get_all_students()
            print("\n📋 Students:")
            for s in students:
                print(f"{s[0]}: {s[1]} {s[2]} - {s[3]}")

        elif choice == '5':
            courses = get_all_courses()
            print("\n📚 Courses:")
            for c in courses:
                print(f"{c[0]}: {c[1]} ({c[2]})")

        elif choice == '6':
            enrollments = get_all_enrollments()
            print("\n📄 Enrollments:")
            for e in enrollments:
                print(f"{e[0]}: {e[1]} in {e[2]} on {e[3]}")

        elif choice == '7':
            student_id = input("Enter student ID to update: ")
            new_email = input("Enter new email: ")
            update_student_email(int(student_id), new_email)
            print("✅ Email updated.")

        elif choice == '8':
            student_id = input("Enter student ID to delete: ")
            delete_student(int(student_id))
            print("✅ Student deleted.")

        elif choice == '9':
            course_id = input("Enter course ID to delete: ")
            delete_course(int(course_id))
            print("✅ Course deleted.")

        elif choice == '0':
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    main()
