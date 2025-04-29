from flask import Flask, render_template, request, redirect, url_for, flash
import re
from queries import (
    get_all_students, add_student,
    get_all_courses, add_course,
    enroll_student, get_all_enrollments, get_student_by_email
)

app = Flask(__name__)
app.secret_key = 'spa-gen-36'

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/students", methods=["GET", "POST"])
def students():
    if request.method == "POST":
        first_name = request.form["first_name"].strip()
        last_name = request.form["last_name"].strip()
        email = request.form["email"].strip()

        # Basic validation
        if not first_name or not last_name or not email:
            flash("All fields are required.", "danger")
            return redirect("/students")

        # Email format check
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            flash("Invalid email format.", "warning")
            return redirect("/students")

        # Check if student already exists
        existing = get_student_by_email(email)
        if existing:
            flash("A student with this email already exists.", "warning")
            return redirect("/students")

        # All good – add student
        add_student(first_name, last_name, email)
        flash("Student added successfully!", "success")
        return redirect("/students")

    all_students = get_all_students()
    return render_template("students.html", students=all_students)

@app.route('/add_student', methods=['POST'])
def add_student_route():
    first = request.form['first_name']
    last = request.form['last_name']
    email = request.form['email']
    add_student(first, last, email)
    return redirect(url_for('students'))

@app.route('/courses')
def courses():
    all_courses = get_all_courses()
    return render_template('courses.html', courses=all_courses)

@app.route('/add_course', methods=['POST'])
def add_course_route():
    name = request.form['course_name']
    code = request.form['course_code']
    add_course(name, code)
    return redirect(url_for('courses'))

@app.route('/enrollments', methods=['GET', 'POST'])
def enrollments():
    if request.method == 'POST':
        # Get form data
        student_id = request.form['student_id']
        course_id = request.form['course_id']
        
        # Enroll the student in the course
        enroll_student(student_id, course_id)
        
        # Redirect to the enrollments page
        return redirect(url_for('enrollments'))
    
    # Fetch data for the template
    students = get_all_students()
    courses = get_all_courses()
    enrollments = get_all_enrollments()
    
    return render_template('enrollments.html', students=students, courses=courses, enrollments=enrollments)

@app.route('/enroll', methods=['POST'])
def enroll():
    student_id = request.form['student_id']
    course_id = request.form['course_id']
    enroll_student(int(student_id), int(course_id))
    return redirect(url_for('enrollments'))

if __name__ == '__main__':
    app.run(debug=True)
