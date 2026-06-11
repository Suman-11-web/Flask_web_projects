# Flask Web Application - Project 07 (Forms using GET & POST)

This is my seventh Flask web application. In this project, I learned how to create and process HTML forms using the GET and POST request methods in Flask.

## Description

Forms are used to collect input from users, such as names, email addresses, passwords, and other information. Flask processes this data using the `request` object.

In this project, the user enters their name into a form. When the form is submitted, Flask receives the data through a POST request and displays a personalized welcome message.

## Features

- Built using Python and Flask
- HTML form for user input
- Supports GET and POST request methods
- Reads form data using `request.form`
- Displays dynamic output based on user input
- Beginner-friendly example

## Project Structure

```
web_project7/
│
├── app.py
└── templates/
    └── index.html
```

## Code Explanation

- `from flask import Flask, render_template, request`
  - Imports Flask, the `render_template()` function, and the `request` object.

- `app = Flask(__name__)`
  - Creates a Flask application instance.

- `@app.route('/', methods=['GET', 'POST'])`
  - Defines the home route and allows both GET and POST requests.

- `request.method`
  - Checks whether the request is GET or POST.

- `request.form['name']`
  - Retrieves the value entered by the user in the form.

- `message = f"Welcome {name}!"`
  - Creates a personalized welcome message.

- `render_template("index.html", message=message)`
  - Passes the message to the HTML template for display.

- `<form method="POST">`
  - Creates an HTML form that sends data using the POST method.

- `<input type="text" name="name">`
  - Allows the user to enter their name.

- `{{ message }}`
  - Displays the message received from the Flask application.

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

- The browser displays a form asking the user to enter their name.
- After submitting the form, the application displays a personalized welcome message such as:

```
Welcome Suman!
```

## Conclusion

This is my seventh Flask project. In this project, I learned how to create HTML forms, handle GET and POST requests, receive user input using `request.form`, and display dynamic responses. Understanding forms is an essential step toward building login systems, registration pages, search forms, and many other interactive web applications.
