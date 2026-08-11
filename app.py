from flask import Flask, render_template, request, redirect, flash, session
import re
from database import get_db_connection

app = Flask(__name__)
app.secret_key = "student-management-secret"
def is_valid_email(email):

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    return re.match(pattern, email) is not None

@app.route("/")
def home():

    # Check if user is logged in
    if not login_required():
        return redirect("/login")

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # Total students
    cursor.execute("SELECT COUNT(*) AS total_students FROM students")
    total_students = cursor.fetchone()["total_students"]

    # Average age
    cursor.execute("SELECT AVG(age) AS average_age FROM students")
    average_age = cursor.fetchone()["average_age"]

    # Total departments
    cursor.execute(
        "SELECT COUNT(DISTINCT department) AS total_departments FROM students"
    )
    total_departments = cursor.fetchone()["total_departments"]

    # Students in each department
    cursor.execute("""
        SELECT department, COUNT(*) AS student_count
        FROM students
        GROUP BY department
    """)

    department_stats = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "index.html",
        total_students=total_students,
        average_age=average_age,
        total_departments=total_departments,
        department_stats=department_stats
    )
@app.route("/students")
def students():
    if not login_required():
      return redirect("/login")

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # Search
    search = request.args.get("search", "")

    # Pagination
    page = request.args.get("page", 1, type=int)
    per_page = 5

    offset = (page - 1) * per_page

    # Count total students
    if search:

        count_query = """
            SELECT COUNT(*) AS total
            FROM students
            WHERE NAME LIKE %s
        """

        cursor.execute(count_query, ("%" + search + "%",))

    else:

        count_query = """
            SELECT COUNT(*) AS total
            FROM students
        """

        cursor.execute(count_query)

    total_students = cursor.fetchone()["total"]

    # Get students
    if search:

        query = """
            SELECT
                id,
                NAME AS name,
                email,
                age,
                department
            FROM students
            WHERE NAME LIKE %s
            LIMIT %s OFFSET %s
        """

        cursor.execute(
            query,
            ("%" + search + "%", per_page, offset)
        )

    else:

        query = """
            SELECT
                id,
                NAME AS name,
                email,
                age,
                department
            FROM students
            LIMIT %s OFFSET %s
        """

        cursor.execute(
            query,
            (per_page, offset)
        )

    students = cursor.fetchall()

    cursor.close()
    connection.close()

    # Calculate total pages
    total_pages = (total_students + per_page - 1) // per_page

    return render_template(
        "students.html",
        students=students,
        page=page,
        total_pages=total_pages,
        search=search
    )
@app.route("/add-student", methods=["GET", "POST"])
def add_student():

    if not login_required():
        return redirect("/login")

    if request.method == "POST":

        name = request.form["name"].strip()
        email = request.form["email"].strip()
        age = request.form["age"].strip()
        department = request.form["department"].strip()

        # Validate empty fields
        if not name or not email or not age or not department:
            flash("All fields are required!", "error")
            return render_template("add_student.html")

        # Validate email format
        if not is_valid_email(email):
            flash("Please enter a valid email address!", "error")
            return render_template("add_student.html")

        # Validate age
        if not age.isdigit():
            flash("Age must be a number!", "error")
            return render_template("add_student.html")

        age = int(age)

        if age < 1 or age > 100:
            flash("Age must be between 1 and 100!", "error")
            return render_template("add_student.html")

        # Connect to database
        connection = get_db_connection()
        cursor = connection.cursor()

        # Check if email already exists
        cursor.execute(
            "SELECT id FROM students WHERE email = %s",
            (email,)
        )

        existing_student = cursor.fetchone()

        if existing_student:
            cursor.close()
            connection.close()

            flash(
                "A student with this email already exists!",
                "error"
            )

            return render_template("add_student.html")

        # Insert new student
        query = """
            INSERT INTO students (name, email, age, department)
            VALUES (%s, %s, %s, %s)
        """

        values = (name, email, age, department)

        cursor.execute(query, values)

        connection.commit()

        cursor.close()
        connection.close()

        flash("Student added successfully!", "success")

        return redirect("/students")

    return render_template("add_student.html")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_student(id):
    if not login_required():
         return redirect("/login")

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    if request.method == "POST":

        name = request.form["name"].strip()
        email = request.form["email"].strip()
        age = request.form["age"].strip()
        department = request.form["department"].strip()

        # Validate empty fields
        if not name or not email or not age or not department:
            flash("All fields are required!", "error")
            cursor.close()
            connection.close()
            return redirect(f"/edit/{id}")

        # Validate email
        if not is_valid_email(email):
            flash("Please enter a valid email address!", "error")
            cursor.close()
            connection.close()
            return redirect(f"/edit/{id}")

        # Validate age
        if not age.isdigit():
            flash("Age must be a number!", "error")
            cursor.close()
            connection.close()
            return redirect(f"/edit/{id}")

        age = int(age)

        if age < 1 or age > 100:
            flash("Age must be between 1 and 100!", "error")
            cursor.close()
            connection.close()
            return redirect(f"/edit/{id}")

        # Update student
        query = """
            UPDATE students
            SET name = %s,
                email = %s,
                age = %s,
                department = %s
            WHERE id = %s
        """

        values = (name, email, age, department, id)

        cursor.execute(query, values)

        connection.commit()

        cursor.close()
        connection.close()

        flash("Student updated successfully!", "success")

        return redirect("/students")

    # Get existing student
    query = """
        SELECT
            id,
            NAME AS name,
            email,
            age,
            department
        FROM students
        WHERE id = %s
    """

    cursor.execute(query, (id,))

    student = cursor.fetchone()

    cursor.close()
    connection.close()

    return render_template(
        "edit_student.html",
        student=student
    )
@app.route("/delete/<int:id>")
def delete_student(id):
    if not login_required():
        return redirect("/login")

    connection = get_db_connection()
    cursor = connection.cursor()

    query = "DELETE FROM students WHERE id = %s"

    cursor.execute(query, (id,))

    connection.commit()

    cursor.close()
    connection.close()

    flash("Student deleted successfully!", "success")

    return redirect("/students")
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "admin123":

            session["logged_in"] = True

            flash("Login successful!", "success")

            return redirect("/")

        else:

            flash("Invalid username or password!", "error")

            return render_template("login.html")

    return render_template("login.html")
@app.route("/logout")
def logout():

    session.pop("logged_in", None)

    flash("You have been logged out.", "success")

    return redirect("/login")
def login_required():

    if not session.get("logged_in"):
        return False

    return True
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template("500.html"), 500

if __name__ == "__main__":
    app.run(debug=True)