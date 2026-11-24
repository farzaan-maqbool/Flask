from flask import Flask, request, render_template
from uuid import UUID
app = Flask(__name__)




@app.route("/")
def home():
    name = "Mohit"
    course = "Flask"
    city = "Delhi"
    return render_template("index.html", name=name,
                           course=course,
                           city=city)



if __name__ == "__main__":
    app.run(debug=True)