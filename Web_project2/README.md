
# Flask Web Application - Project 02 (Using render_template)

This is my second Flask web application. In this project, I learned how to use the `render_template()` function to display HTML pages stored in a separate `templates` folder.

## Description

Instead of returning HTML directly from the Python code, Flask allows us to create HTML files and render them using the `render_template()` function. This makes the application cleaner, easier to manage, and follows good web development practices.

## Features

- Built using Python and Flask
- Uses `render_template()` function
- HTML code stored in a separate `templates` folder
- Clean and organized project structure
- Beginner-friendly Flask application

## Project Structure

```
web_project2/
│
├── app.py
└── templates/
    └── index.html
```

## Code Explanation

- `from flask import Flask, render_template`
  - Imports the Flask framework and the `render_template` function.

- `app = Flask(__name__)`
  - Creates a Flask application instance.

- `@app.route('/')`
  - Defines the home page route.

- `def home():`
  - Function that executes when the home page is accessed.

- `return render_template("index.html")`
  - Loads and displays the `index.html` file from the `templates` folder.

- `if __name__ == '__main__':`
  - Ensures the application runs only when the file is executed directly.

- `app.run(debug=True, port=5500)`
  - Starts the Flask development server on port 5500 with debug mode enabled.

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

The browser displays the contents of the `index.html` page stored inside the `templates` folder.

## Conclusion

This is my second Flask project. In this project, I learned how to separate HTML from Python code using the `render_template()` function. This approach makes Flask applications more organized and is an important step toward building professional web applications.
