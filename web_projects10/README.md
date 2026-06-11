# Flask Web Application - Project 10 (CRUD Application)

This is my tenth Flask web application. In this project, I learned how to perform CRUD (Create, Read, Update, Delete) operations using Flask and SQLite.

## Description

CRUD stands for Create, Read, Update, and Delete. These are the four basic operations used to manage data in a database.

In this project, users can add new student records, view all stored records, update existing records, and delete records from the SQLite database. This project demonstrates how Flask interacts with a database to build a complete data management system.

## Features

- Built using Python and Flask
- Uses SQLite database
- Create new student records
- Read and display all records
- Update existing records
- Delete records
- Uses HTML templates for displaying data
- Beginner-friendly CRUD application

## Project Structure

```
web_project10/
│
├── app.py
├── database.db
└── templates/
    ├── index.html
    └── edit.html
```

## Code Explanation

- `sqlite3`
  - Connects the Flask application to the SQLite database.

- `CREATE TABLE IF NOT EXISTS`
  - Creates the `students` table if it does not already exist.

- `INSERT INTO students`
  - Adds a new student record to the database.

- `SELECT * FROM students`
  - Retrieves all student records from the database.

- `UPDATE students SET`
  - Updates an existing student record.

- `DELETE FROM students`
  - Removes a student record from the database.

- `redirect('/')`
  - Redirects the user back to the home page after adding, updating, or deleting data.

- `render_template()`
  - Sends database records to the HTML template for display.

- `@app.route('/edit/<int:id>')`
  - Opens the edit page for a specific student using its ID.

- `@app.route('/delete/<int:id>')`
  - Deletes the selected student record using its ID.

- `app.run(debug=True, port=5500)`
  - Starts the Flask development server on port 5500.

## How to Run

1. Install Flask

```bash
pip install flask
```

2. Run the application

```bash
python app.py
```

3. Open your browser and visit

```
http://127.0.0.1:5500/
```

## Output

- Users can add new students using the form.
- All student records are displayed in a table.
- Each record includes **Edit** and **Delete** options.
- Editing updates the selected record in the database.
- Deleting permanently removes the selected record.

## Conclusion

This is my tenth Flask project. In this project, I learned how to implement complete CRUD operations using Flask and SQLite. I gained experience in creating, reading, updating, and deleting database records, which are fundamental operations used in most real-world web applications such as management systems, blogs, inventory systems, and admin dashboards.
