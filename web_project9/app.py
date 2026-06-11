import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

# Create database and table
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
""")

conn.commit()
conn.close()

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        name = request.form['name']

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute("INSERT INTO students(name) VALUES(?)", (name,))

        conn.commit()
        conn.close()

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    conn.close()

    return render_template("index.html", students=students)

if __name__ == '__main__':
    app.run(debug=True, port=5500)