import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Create database and table
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
""")

conn.commit()
conn.close()


# ------------------------------
# Home Route
# ------------------------------
@app.route('/')
def home():
    return "<h1>Flask REST API is Running 🚀</h1>"


# ------------------------------
# Temporary Route to Add Data
# Visit: http://127.0.0.1:5500/add
# ------------------------------
@app.route('/add')
def add():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students(name, age) VALUES(?, ?)",
        ("Suman", 17)
    )

    conn.commit()
    conn.close()

    return "<h2>Student Added Successfully!</h2>"


# ------------------------------
# GET All Students
# ------------------------------
@app.route('/students', methods=['GET'])
def get_students():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    conn.close()

    data = []

    for student in students:

        data.append({
            "id": student[0],
            "name": student[1],
            "age": student[2]
        })

    return jsonify(data)


# ------------------------------
# POST Student
# ------------------------------
@app.route('/students', methods=['POST'])
def add_student():

    data = request.get_json()

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students(name, age) VALUES(?, ?)",
        (data["name"], data["age"])
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Student Added Successfully"
    })


# ------------------------------
# UPDATE Student
# ------------------------------
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):

    data = request.get_json()

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE students SET name=?, age=? WHERE id=?",
        (data["name"], data["age"], id)
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Student Updated Successfully"
    })


# ------------------------------
# DELETE Student
# ------------------------------
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Student Deleted Successfully"
    })


if __name__ == '__main__':
    app.run(debug=True, port=5500)