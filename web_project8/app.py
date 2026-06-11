from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Go to /user/YourName in the URL</h1>"

@app.route('/user/<name>')
def user(name):
    return render_template("index.html", username=name)

if __name__ == '__main__':
    app.run(debug=True, port=5500)
