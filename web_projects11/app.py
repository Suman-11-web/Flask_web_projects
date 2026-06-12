import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Create database and users table
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")

conn.commit()
conn.close()


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO users(username,password) VALUES(?,?)",
            (username, password)
        )

        conn.commit()
        conn.close()

        return redirect('/login')

    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )

        user = cursor.fetchone()

        conn.close()

        if user:
            return f"<h1>Welcome {username}</h1>"

        return "<h2>Invalid Username or Password</h2>"

    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True, port=5500)

