# Flask Web Application - Project 04 (Dynamic Data Passing)

This is my fourth Flask web application. In this project, I learned how to pass data from the Flask backend to an HTML template using the `render_template()` function.

## Description

This application demonstrates how to send dynamic data from Python to an HTML page. Instead of displaying fixed content, Flask passes a variable to the template, and the HTML page displays the value using Jinja2 template syntax.

This makes web pages dynamic and allows different content to be displayed based on the data provided by the application.

## Features

- Built using Python and Flask
- Uses `render_template()` to pass data
- Displays dynamic content on the web page
- Uses Jinja2 template syntax (`{{ }}`)
- Beginner-friendly example of dynamic rendering

## Project Structure

```
web_project4/
│
├── app.py
└── templates/
    └── index.html
```

## Code Explanation

- `from flask import Flask, render_template`
  - Imports the Flask framework and the `render_template()` function.

- `app = Flask(__name__)`
  - Creates a Flask application instance.

- `@app.route('/')`
  - Defines the home page route.

- `name = "Suman"`
  - Creates a Python variable containing data.

- `return render_template("index.html", username=name)`
  - Passes the value of `name` to the HTML template as `username`.

- `{{ username }}`
  - Jinja2 template syntax used inside the HTML file to display the passed value.

- `if __name__ == '__main__':`
  - Ensures the application runs only when the file is executed directly.

- `app.run(debug=True, port=5500)`
  - Starts the Flask development server on port 5500 with debug mode enabled.

## How to Run

1. Install Flask:

```bash
pip install flask
```

2. Run the application:

```bash
python app.py
```

3. Open your browser and visit:

```
http://127.0.0.1:5500/
```

## Output

The browser displays:

```
Welcome Suman

This data is passed from Flask to the HTML template.
```

## Conclusion

This is my fourth Flask project. In this project, I learned how to pass variables from the Flask backend to an HTML template using `render_template()`. I also learned to use Jinja2 template syntax (`{{ }}`) to display dynamic content, which is an essential concept for building interactive web applications.