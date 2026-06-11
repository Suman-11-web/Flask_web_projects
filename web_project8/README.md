# Flask Web Application - Project 08 (URL Parameters)

This is my eighth Flask web application. In this project, I learned how to use URL parameters to create dynamic routes and display different content based on the value provided in the URL.

## Description

URL parameters allow Flask to capture values directly from the URL and use them inside the application. This helps create dynamic web pages without creating separate routes for every user or page.

In this project, the user enters a name in the URL, and Flask receives that value and displays a personalized welcome message on the web page.

## Features

- Built using Python and Flask
- Uses dynamic URL parameters
- Captures values from the URL
- Passes data to an HTML template
- Displays personalized content
- Beginner-friendly example

## Project Structure

```
web_project8/
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

- `@app.route('/user/<name>')`
  - Defines a dynamic route where `<name>` acts as a URL parameter.

- `def user(name):`
  - Receives the value entered in the URL as the variable `name`.

- `return render_template("index.html", username=name)`
  - Passes the captured value to the HTML template as `username`.

- `{{ username }}`
  - Displays the value received from Flask inside the HTML page.

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

3. Open your browser and visit:

```
http://127.0.0.1:5500/user/Suman
```

You can replace **Suman** with any name:

```
http://127.0.0.1:5500/user/Rahul
http://127.0.0.1:5500/user/Alice
http://127.0.0.1:5500/user/John
```

## Output

If the URL is:

```
http://127.0.0.1:5500/user/Suman
```

The browser displays:

```
Welcome Suman

This username is received from the URL parameter.
```

## Conclusion

This is my eighth Flask project. In this project, I learned how to create dynamic routes using URL parameters, capture values directly from the URL, pass them to HTML templates, and display personalized content. URL parameters are widely used in real-world applications such as user profiles, product pages, blog posts, and category pages.
