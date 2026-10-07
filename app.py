from flask import Flask, render_template, request
from services.university_api import fetch_student



app = Flask(__name__)




@app.route("/")
def home():
    return render_template("index.html")

@app.route("/student")
def student():

    
    student_id = request.args.get("student_id")

    if not student_id:
        return "Student ID is required", 400

    
    try:

        student_id = int(student_id)

    except ValueError:    

        return "Student ID must be a number", 400
    student = fetch_student(student_id)

    

    if student is None:
        return "Student not found", 404

    return render_template(
        "student.html",
        student_id=student.id,
        student_name=student.name,
        courses=student.courses 
    )


 
if __name__ == "__main__":
    app.run(
        debug=True,
        port=5059,
        use_reloader=False
    )