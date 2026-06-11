# Flask Web Application - Project 06 (Static Files)

This is my sixth Flask web application. In this project, I learned how to use static files such as CSS, JavaScript, and Images in a Flask application.

## Description

Flask provides a special `static` folder to store files like CSS, JavaScript, and images. These files improve the appearance and functionality of a website.

In this project, the HTML page is styled using a CSS file, displays an image from the `static/images` folder, and uses JavaScript to show an alert message when a button is clicked.

## Features

- Built using Python and Flask
- Uses external CSS for styling
- Uses external JavaScript for interactivity
- Displays images from the static folder
- Uses `url_for()` to access static files
- Organized project structure

## Project Structure

```
web_project/
│
├── app.py
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
│       └── logo.png
│
└── templates/
    └── index.html
```

## Code Explanation

- `static/`
  - Stores CSS, JavaScript, images, and other static resources.

- `style.css`
  - Adds styles such as colors, fonts, and layout to the web page.

- `script.js`
  - Adds JavaScript functionality to make the page interactive.

- `logo.png`
  - Displays an image on the web page.

- `url_for('static', filename='css/style.css')`
  - Generates the correct path for the CSS file.

- `url_for('static', filename='js/script.js')`
  - Loads the JavaScript file.

- `url_for('static', filename='images/logo.png')`
  - Displays the image stored in the static folder.

- `render_template("index.html")`
  - Renders the HTML page that uses the static files.

- `app.run(debug=True, port=5500)`
  - Starts the Flask development server.

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

- A styled web page is displayed using CSS.
- An image is loaded from the `static/images` folder.
- Clicking the button executes JavaScript and displays an alert message.

## Conclusion

This is my sixth Flask project. In this project, I learned how to organize and use static files such as CSS, JavaScript, and images in a Flask application. Using static resources helps create attractive, interactive, and professional web applications while keeping the project well organized.
