from flask import Flask, request, render_template
from uuid import UUID
app = Flask(__name__)




@app.route("/")
def home():
    
    courses = [
        "Python",
        "Flask",
        "React",
        "Django"
    ]
    student = {
        "name":"Mohit",
        "course":"Flask",
        "City" : "Delhi"
    }
    return render_template("index.html",courses=courses,student=student)



if __name__ == "__main__":
    app.run(debug=True)