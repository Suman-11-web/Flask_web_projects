# Flask Web Application - Project 11 (User Authentication)

This is my eleventh Flask web application. In this project, I learned how to build a basic user authentication system using Flask and SQLite.

## Description

User authentication is one of the most important features in modern web applications. It allows users to create an account, log in with their credentials, and access personalized content.

In this project, users can register with a username and password. The registration details are stored in an SQLite database. Users can then log in using their registered credentials, and the application verifies the information before granting access.

This project introduces the fundamentals of authentication and serves as the foundation for secure web applications.

---

## Features

- Built using Python and Flask
- User Registration
- User Login
- SQLite Database Integration
- HTML Forms
- GET and POST Methods
- User Credential Verification
- Dynamic Routing
- Beginner-friendly Authentication System

---

## Project Structure

```
web_projects11/
│
├── app.py
├── database.db
└── templates/
    ├── home.html
    ├── register.html
    └── login.html
```

---

## Code Explanation

- `import sqlite3`
  - Imports the SQLite library to create and manage the local database.

- `from flask import Flask, render_template, request, redirect`
  - Imports the required Flask modules for routing, rendering templates, processing forms, and redirecting users.

- `app = Flask(__name__)`
  - Creates a Flask application instance.

- `CREATE TABLE IF NOT EXISTS users`
  - Creates the `users` table if it does not already exist.

- `id INTEGER PRIMARY KEY AUTOINCREMENT`
  - Creates a unique ID for every registered user.

- `username TEXT UNIQUE`
  - Stores the username and ensures duplicate usernames are not allowed.

- `password TEXT`
  - Stores the user's password.

- `@app.route('/')`
  - Defines the home page route.

- `@app.route('/register', methods=['GET', 'POST'])`
  - Creates the registration page and accepts both GET and POST requests.

- `request.form['username']`
  - Retrieves the username entered by the user.

- `request.form['password']`
  - Retrieves the password entered by the user.

- `INSERT INTO users`
  - Saves the user's registration details into the SQLite database.

- `redirect('/login')`
  - Redirects the user to the login page after successful registration.

- `@app.route('/login', methods=['GET', 'POST'])`
  - Creates the login page and handles user authentication.

- `SELECT * FROM users WHERE username=? AND password=?`
  - Checks whether the entered username and password exist in the database.

- `cursor.fetchone()`
  - Retrieves the matching user record if it exists.

- `if user`
  - Verifies whether the login credentials are valid.

- `return f"<h1>Welcome {username}</h1>"`
  - Displays a welcome message after successful login.

- `return "<h2>Invalid Username or Password</h2>"`
  - Displays an error message if authentication fails.

- `app.run(debug=True, port=5500)`
  - Starts the Flask development server on port 5500.

---

## How to Run

### 1. Install Flask

```bash
pip install flask
```

### 2. Run the application

```bash
python app.py
```

### 3. Open your browser

```
http://127.0.0.1:5500/
```

---

## Application Flow

1. Open the home page.
2. Click **Register**.
3. Enter a username and password.
4. Submit the registration form.
5. The data is stored in the SQLite database.
6. You are redirected to the login page.
7. Enter the registered username and password.
8. Flask verifies the credentials.
9. If valid, a welcome message is displayed.
10. If invalid, an error message is shown.

---

## Output

### Home Page

- Register
- Login

### Registration Page

- Username field
- Password field
- Register button

### Login Page

- Username field
- Password field
- Login button

### Successful Login

```
Welcome Suman
```

### Invalid Login

```
Invalid Username or Password
```

---

## What I Learned

- Creating a user registration system
- Creating a user login system
- Working with HTML forms
- Handling GET and POST requests
- Using SQLite with Flask
- Storing user information in a database
- Retrieving data from a database
- Verifying user credentials
- Redirecting users between pages
- Building the foundation of authentication systems

---

## Note

This project stores passwords as plain text for learning purposes only.

In real-world applications, passwords should **never** be stored directly in the database. They should always be encrypted (hashed) using secure methods such as `generate_password_hash()` and verified using `check_password_hash()` to protect user accounts.

---

## Conclusion

This is my eleventh Flask project. In this project, I learned how to build a basic user authentication system with registration and login functionality using Flask and SQLite. This project serves as the foundation for developing secure web applications and prepares me for implementing advanced authentication features such as password hashing, user sessions, role-based access control, and secure login management in production-level Flask applications.
