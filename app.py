from flask import Flask, render_template, request, redirect, url_for
from queries import (
    get_all_students, add_student,
    get_all_courses, add_course,
    enroll_student, get_all_enrollments
)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/students')
def students():
    all_students = get_all_students()
    return render_template('students.html', students=all_students)

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

@app.route('/enrollments')
def enrollments():
    all_enrollments = get_all_enrollments()
    return render_template('enrollments.html', enrollments=all_enrollments)

@app.route('/enroll', methods=['POST'])
def enroll():
    student_id = request.form['student_id']
    course_id = request.form['course_id']
    enroll_student(int(student_id), int(course_id))
    return redirect(url_for('enrollments'))

if __name__ == '__main__':
    app.run(debug=True)
