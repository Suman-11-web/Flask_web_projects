# Flask Web Application - Project 05 (Jinja2 Loops & Conditions)

This is my fifth Flask web application. In this project, I learned how to use Jinja2 template syntax to display data using loops and conditions inside HTML templates.

## Description

Jinja2 is the default template engine used by Flask. It allows developers to write dynamic HTML by using Python-like syntax inside template files.

In this project, a list of items is passed from the Flask application to the HTML template. The template uses a `for` loop to display each item and an `if` condition to check whether data is available.

This makes web pages more dynamic and reduces repetitive HTML code.

## Features

- Built using Python and Flask
- Uses Jinja2 template engine
- Displays data using `for` loops
- Uses `if` and `else` conditions
- Generates dynamic HTML content
- Beginner-friendly example

## Project Structure

```
web_project5/
│
├── app.py
└── templates/
    └── index.html
```

## Code Explanation

- `from flask import Flask, render_template`
  - Imports Flask and the `render_template()` function.

- `app = Flask(__name__)`
  - Creates a Flask application instance.

- `fruits = ["Apple", "Banana", "Mango", "Orange"]`
  - Creates a Python list.

- `return render_template("index.html", fruits=fruits)`
  - Passes the list to the HTML template.

- `{% for fruit in fruits %}`
  - Starts a loop that iterates through every item in the list.

- `{{ fruit }}`
  - Displays the current item from the loop.

- `{% endfor %}`
  - Ends the loop.

- `{% if fruits %}`
  - Checks whether the list contains data.

- `{% else %}`
  - Executes when the list is empty.

- `{% endif %}`
  - Ends the conditional statement.

- `app.run(debug=True, port=5500)`
  - Starts the Flask development server.

## How to Run

1. Install Flask

```bash
pip install flask
```

2. Run the application

```bash
python app.py
```

3. Open your browser

```
http://127.0.0.1:5500/
```

## Output

The browser displays:

- Apple
- Banana
- Mango
- Orange

If the list is empty, the page displays:

```
No fruits available.
```

## Conclusion

This is my fifth Flask project. In this project, I learned how to use Jinja2 loops and conditional statements to create dynamic HTML pages. These concepts are essential for displaying data from databases, APIs, and user input in real-world Flask applications.
