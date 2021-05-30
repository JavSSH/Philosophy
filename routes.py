from flask import Flask, render_template
app = Flask(__name__)

# Home Page
@app.route('/')
def home_page():
    return render_template("index.html")

# Contact Page
@app.route('/contact')
def contact():
    return render_template("contact.html")

# About Page
@app.route('/about')
def about():
    return render_template("about.html")

# Error Page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)
