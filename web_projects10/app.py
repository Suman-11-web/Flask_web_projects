import sqlite3
from flask import Flask, render_template, request, redirect

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

        return redirect('/')

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    conn.close()

    return render_template("index.html", students=students)


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    if request.method == 'POST':
        name = request.form['name']

        cursor.execute(
            "UPDATE students SET name=? WHERE id=?",
            (name, id)
        )

        conn.commit()
        conn.close()

        return redirect('/')

    cursor.execute("SELECT * FROM students WHERE id=?", (id,))
    student = cursor.fetchone()

    conn.close()

    return render_template("edit.html", student=student)


@app.route('/delete/<int:id>')
def delete(id):

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE id=?", (id,))

    conn.commit()
    conn.close()

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, port=5500)