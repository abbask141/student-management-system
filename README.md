
# Student Management System

A web-based Student Management System developed using Flask and MySQL.

## Features

- Admin Login and Logout
- Dashboard
- Add Student
- Edit Student
- Delete Student
- Search Students
- Pagination
- Email Validation
- Age Validation
- Duplicate Email Checking
- Department Statistics
- Department Bar Chart
- Flash Messages
- 404 Error Page
- 500 Error Page
- Responsive User Interface

## Technologies Used

- Python
- Flask
- MySQL
- HTML
- CSS
- JavaScript
- Chart.js

## Project Structure

student-management-system/
│
├── app.py
├── database.py
├── requirements.txt
├── database.sql
├── .env
├── .gitignore
├── README.md
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── students.html
│   ├── add_student.html
│   ├── edit_student.html
│   ├── login.html
│   ├── 404.html
│   └── 500.html
│
└── static/
    └── style.css
## Installation

### 1. Create a virtual environment

```bash
python -m venv venv
```

### 2. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 3. Install required packages

```bash
pip install -r requirements.txt
```

### 4. Configure MySQL

Create/import the database using:
database.sql

Then create a `.env` file and add your MySQL credentials:

```text
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=student_management
```

### 5. Run the application

```bash
python app.py
```

Open the application in your browser.

## Admin Login

Use the administrator credentials configured in the application.

## Database

The project uses MySQL database:

```text
student_management
```

The database structure and sample data are provided in:

```text
database.sql
```


