from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "Hello Flask"

@app.route("/users")
def users():
    return "Welcome to Users page"
@app.route("/user/<name>")
def user(name):
    return f"Hello {name}"

@app.route("/student/<name>/<course>")
def student(name,course):
    return f"Hello {name} is learning {course}"

@app.route("/about")
def about():
    return "Welcome to About Page"

@app.route("/contacts")
def contacts():
    return "Contacts Page"
if __name__ == "__main__":
    app.run(debug=True)