from flask import Flask, request
from uuid import UUID
app = Flask(__name__)


# @app.route("/user/<int:id>")
# def user(id):
#     return f"Hello User {id}"

# @app.route("/price/<float:amount>")
# def price(amount):
#     return f"Hello User {amount}"

# @app.route("/account/<string:name>")
# def account(name):
#     return f"Hello User {name}"

# # Path Converter
# @app.route("/files/<path:file_path>")
# def files(file_path):
#     return file_path

# UUID

# @app.route("/student/<uuid:user_id>")
# def student(user_id):
#     return str(user_id)


# @app.route("/users")
# def users():
#     return "Welcome to Users page"


# @app.route("/student/<name>/<course>")
# def student(name,course):
#     return f"Hello {name} is learning {course}"

# @app.route("/about")
# def about():
#     return "Welcome to About Page"

# @app.route("/contacts")
# def contacts():
#     return "Contacts Page"


# Query Parameters

# @app.route("/search")
# def search():
#     name = request.args.get("name","Guest") #Guest because default if name not available
#     return f"Hello {name}"

@app.route("/search")
def search():
    name = request.args.get("name","Guest") #Guest because default if name not available
    course = request.args.get("course","Unknown")
    return f"{name} is learning {course}"






if __name__ == "__main__":
    app.run(debug=True)