from database import connect_db
from datetime import datetime

# Students
#-------------------
def add_student(first_name, last_name, email):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Students (first_name, last_name, email)
            VALUES (?, ?, ?)
        """, (first_name, last_name, email))
        conn.commit()

def get_all_students():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Students")
        return cursor.fetchall()

def update_student_email(student_id, new_email):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Students SET email = ? WHERE student_id = ?
        """, (new_email, student_id))
        conn.commit()

def delete_student(student_id):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Students WHERE student_id = ?", (student_id,))
        conn.commit()





#Courses
#-------------------------------------------------------
def add_course(course_name, course_code):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Courses (course_name, course_code)
            VALUES (?, ?)
        """, (course_name, course_code))
        conn.commit()

def get_all_courses():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Courses")
        return cursor.fetchall()

def delete_course(course_id):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Courses WHERE course_id = ?", (course_id,))
        conn.commit()


# Enrollments
#-------------------------------------------------------
def enroll_student(student_id, course_id):
    enrolled_on = datetime.now().strftime("%Y-%m-%d")
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Enrollments (student_id, course_id, enrolled_on)
            VALUES (?, ?, ?)
        """, (student_id, course_id, enrolled_on))
        conn.commit()

def get_all_enrollments():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT e.enrollment_id, s.first_name || ' ' || s.last_name AS student_name,
                   c.course_name, e.enrolled_on
            FROM Enrollments e
            JOIN Students s ON e.student_id = s.student_id
            JOIN Courses c ON e.course_id = c.course_id
        """)
        return cursor.fetchall()
