# Flask Web Application - Project 03 (Multiple Pages)

This is my third Flask web application. In this project, I learned how to create a website with multiple pages using Flask routing and HTML templates.

## Description

This application contains three different pages: **Home**, **About**, and **Contact**. Each page has its own URL route and HTML template. Users can easily navigate between these pages using navigation links.

This project demonstrates how Flask can handle multiple routes and render different HTML files for each page, making the website more organized and user-friendly.

## Features

- Built using Python and Flask
- Multiple routes (`/`, `/about`, `/contact`)
- Separate HTML files for each page
- Navigation links between pages
- Clean project structure using the `templates` folder

## Project Structure

```
web_project3/
│
├── app.py
└── templates/
    ├── index.html
    ├── about.html
    └── contact.html
```

## Code Explanation

- `from flask import Flask, render_template`
  - Imports the Flask framework and the `render_template()` function.

- `app = Flask(__name__)`
  - Creates a Flask application instance.

- `@app.route('/')`
  - Defines the Home page route.

- `def home():`
  - Executes when the Home page is accessed.

- `return render_template("index.html")`
  - Renders the Home page.

- `@app.route('/about')`
  - Defines the About page route.

- `def about():`
  - Executes when the About page is accessed.

- `return render_template("about.html")`
  - Renders the About page.

- `@app.route('/contact')`
  - Defines the Contact page route.

- `def contact():`
  - Executes when the Contact page is accessed.

- `return render_template("contact.html")`
  - Renders the Contact page.

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

You can also access:

```
http://127.0.0.1:5500/about
```

```
http://127.0.0.1:5500/contact
```

## Output

- The Home page displays a welcome message.
- The About page displays information about the website.
- The Contact page displays contact details.
- Users can navigate between all pages using the navigation menu.

## Conclusion

This is my third Flask project. In this project, I learned how to create multiple routes and render different HTML templates using Flask. It helped me understand how to build a simple multi-page website and improve the organization of web applications.
