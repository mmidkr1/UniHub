# UniHub

UniHub is a Flask web application designed to help students view and organize their course information and academic deadlines, including quizzes, exams, TMAs, and assignments.

This version of the project uses mock student data to simulate an external university data source.

## Features

- Search for a student by Student ID.
- Display the student's name and ID.
- Display all courses registered for the student.
- Display quizzes, exams, TMAs, and assignments for each course.
- Validate Student IDs and handle invalid or nonexistent students.
- Handle courses with missing or empty assessment data.

## Technologies Used

- Python
- Flask
- HTML
- CSS
- Jinja2
- Object-Oriented Programming (OOP)

## Project Structure

- `app.py` - Handles web routes, Student ID validation, and rendering HTML templates.
- `services/university_api.py` - Handles retrieving and preparing student data.
- `services/mock_data.py` - Contains mock student data used for development and testing.
- `utils/models.py` - Defines Student, Course, Quiz, Exam, Tma, and Assignment classes.
- `templates/` - Contains the HTML templates used by the application.

## How to Run the Project

1. Clone the repository.

2. Create a virtual environment:

   `python -m venv venv`

3. Activate the virtual environment on Windows:

   `venv\Scripts\activate`

4. Install the required dependencies:

   `pip install -r requirements.txt`

5. Run the application:

   `python app.py`

6. Open the application in your browser:

   `http://127.0.0.1:5059`

## Data Source

The current version uses mock student data stored in `services/mock_data.py`.

`fetch_student()` retrieves the mock data and passes it to `build_student()`, which converts the raw data into application objects such as Student, Course, Quiz, Exam, Tma, and Assignment.

The project separates the data source from the Flask application logic, allowing the data source to be replaced or extended in the future without redesigning the entire application.

## Future Improvements

Possible future improvements include:

- Student accounts and authentication.
- A database for storing student courses and deadlines.
- Allowing students to add, edit, and delete courses and assessments.
- A dashboard for upcoming academic deadlines.
- External university API integration if API access becomes available.