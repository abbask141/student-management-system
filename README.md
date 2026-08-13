# Student Management System

A web-based Student Management System built with **Python Flask** and **PostgreSQL**. The application allows users to manage student records through a simple and user-friendly interface.

## 🌐 Live Website

[Open Student Management System](https://student-management-system-xext-px588x00p-abbas1-d8c4.vercel.app)

## 📌 Project Overview

The Student Management System is a CRUD-based web application developed using Flask.

The system allows an administrator to:

- Login securely
- View dashboard statistics
- View all students
- Search students
- Add new students
- Edit existing student records
- Delete student records
- View students by department
- Use pagination for student records
- Logout from the system

The application is connected to a cloud-based PostgreSQL database using **Neon**, while the Flask application is deployed using **Vercel**.

---

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3
- Jinja2 Templates

### Backend
- Python
- Flask

### Database
- PostgreSQL
- Neon

### Deployment
- Vercel

### Version Control
- Git
- GitHub

---

## ✨ Features

### 🔐 Authentication
- Admin login system
- Session-based authentication
- Logout functionality
- Protected dashboard and student management pages

### 📊 Dashboard
The dashboard displays:

- Total number of students
- Average student age
- Total number of departments
- Number of students in each department

### 👨‍🎓 Student Management

Users can:

- Add students
- View students
- Edit student information
- Delete students
- Search students by name

### ✅ Validation

The application validates:

- Required fields
- Email format
- Age format
- Age range
- Duplicate email addresses

### 🔎 Search & Pagination

The student list includes:

- Name-based search
- Pagination
- Five students displayed per page

---

## 🔑 Demo Login

Use the following credentials to access the live demo:

**Username:**
admin
Password:

admin123

These credentials are provided for demonstration and educational purposes.

📁 Project Structure
student-management-system/
│
├── app.py
├── database.py
├── database.sql
├── requirements.txt
├── README.md
├── .gitignore
│
├── static/
│   └── style.css
│
└── templates/
    ├── 404.html
    ├── 500.html
    ├── add_student.html
    ├── base.html
    ├── edit_student.html
    ├── index.html
    ├── login.html
    └── students.html
🗄️ Database

The application uses PostgreSQL hosted on Neon.

The main database table is:

students

The student table contains:

Column	Description
id	Unique student ID
name	Student name
email	Student email
age	Student age
department	Student department

The application connects to the database using the DATABASE_URL environment variable.

⚙️ Environment Variables

For local development, create a .env file in the project root:

SECRET_KEY=your_secret_key
DATABASE_URL=your_database_connection_string
🚀 Running the Project Locally
1. Clone the repository
git clone https://github.com/abbask141/student-management-system.git
2. Open the project folder
cd student-management-system
3. Create a virtual environment
python -m venv venv
4. Activate the virtual environment

On Windows:

venv\Scripts\activate
5. Install dependencies
pip install -r requirements.txt
6. Create the .env file

Add:

SECRET_KEY=your_secret_key
DATABASE_URL=your_database_connection_string
7. Run the application
python app.py

The application will run locally at:

http://127.0.0.1:5000
📦 Dependencies

The project uses the following Python packages:

Flask
psycopg2-binary
python-dotenv

These dependencies can be installed using:

pip install -r requirements.txt
☁️ Deployment

The application is deployed using Vercel.

The database is hosted on Neon PostgreSQL.

Deployment Architecture
                 User
                  │
                  ▼
           ┌─────────────┐
           │   Vercel    │
           │   Flask App │
           └──────┬──────┘
                  │
                  │ DATABASE_URL
                  ▼
           ┌─────────────┐
           │    Neon     │
           │ PostgreSQL  │
           └─────────────┘
🔒 Security Notes
Database credentials are stored using environment variables.
The .env file is excluded from GitHub.
The Flask secret key is stored as an environment variable.
Database passwords and connection strings are not included in the source code.

The current demo login credentials are intentionally included in this README for educational demonstration purposes.

🎯 Project Objectives

The main objectives of this project are:

To develop a practical web application using Flask.
To implement CRUD operations.
To connect a Flask application with a PostgreSQL database.
To implement authentication and sessions.
To practice database operations using SQL.
To deploy a web application to a cloud platform.
To understand environment variables and cloud database connectivity.
📚 Learning Outcomes

Through this project, the following concepts were practiced:

Python programming
Flask web development
HTML and CSS
Jinja2 templating
CRUD operations
SQL queries
PostgreSQL
Database connectivity
Authentication
Sessions
Form validation
Search functionality
Pagination
Environment variables
Git and GitHub
Cloud database deployment
Web application deployment
👨‍💻 Author

Muhammad Abbas

BS Computer Science
Department of Computer Science
BUITEMS
