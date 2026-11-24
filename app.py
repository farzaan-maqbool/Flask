from flask import Flask, request, render_template
from uuid import UUID
app = Flask(__name__)


# @app.route("/")
# def home():
#     return "<h1>Welcome to Flask</h1>"

# @app.route("/")
# def home():
#     return """
# <html>
# <head>
# <title>Farzaan Decodes</title>
# </head>
# <body>
# <h1>Farzaan</h1>
# </body>
# </html>
# """


@app.route("/")
def home():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)