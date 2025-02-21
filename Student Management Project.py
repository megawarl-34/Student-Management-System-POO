from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data storage
students = {}
courses = {}
enrollments = []

class Student:
    def __init__(self, name, age, studentID): # Initialise name, age, studentID et grades
        self._studentID = studentID
        self._grades = []
        self._name = name 
        self._age = age
    
    def get_name(self): # va chercher le name
        return self._name
    
    def get_age(self): # va chercher l'age
        return self._age
    
    def addGrade(self, grade): # va pouvoir faire en sorte d'ajouter une note
        self._grades.append(grade)
    
    def getAverageGrade(self): # va faire la moyenne de toute les notes d'un élève
        return sum(self._grades) / len(self._grades) if self._grades else 0
    
    def get_studentID(self): # va recup ID de l'élève
        return self._studentID

# création de ces deux class pour override "getAverageGrade" se qui nous permettra de modifier la class student sans modifier tous les students
class GraduateStudent(Student): 
    def getAverageGrade(self):
        return super().getAverageGrade() + 5

class UndergraduateStudent(Student):
    def getAverageGrade(self):
        return super().getAverageGrade()

class Course:
    def __init__(self, courseName, courseCode, creditHours):
        self._courseName = courseName
        self._courseCode = courseCode
        self._creditHours = creditHours
        self._students = []
    
    def enrollStudent(self, student): # définie le student qui est enroller
        self._students.append(student)
    
    def getEnrolledStudents(self): # va chercher le student enroller
        return [student.get_name() for student in self._students]

class Enrollment:
    def __init__(self, student, course):
        self._student = student
        self._course = course
    
    def register(self): 
        self._course.enrollStudent(self._student) # enregistre les donnés de l'enrollement (student, course)

# création d'un student
@app.route('/students', methods=['POST']) # définie une route POST/students
def create_student(): # fct de la requête   
    data = request.json  # recup des donné envoyer
    student_id = data['studentID']
    if student_id in students: # vérifie si l'id existe déja
        return jsonify({'error': 'Student already exists'}), 400
    students[student_id] = Student(data['name'], data['age'], student_id)
    return jsonify({'message': 'Student created successfully'}), 201

# recup de l'id d'un student
@app.route('/students/<student_id>', methods=['GET']) # définie une route GET/student_id
def get_student(student_id):
    student = students.get(student_id) # utilise get pour savoir à qui coresspond l'id récupérer
    if not student:
        return jsonify({'error': 'Student not found'}), 404
    return jsonify({'name': student.get_name(), 'age': student.get_age(), 'grades': student._grades})

# création de grades
@app.route('/students/<student_id>/grades', methods=['POST']) # définie une route POST/grades
def add_grades(student_id):
    student = students.get(student_id)
    if not student:
        return jsonify({'error': 'Student not found'}), 404
    data = request.json
    grades = data.get('grades', []) # recup la list des grades
    if not isinstance(grades, list): # check si grades est une list
        return jsonify({'error': 'Grades should be a list'}), 400
    for grade in grades: # parcours chaque grades dans la list
        student.addGrade(grade)
    return jsonify({'message': 'Grades added successfully'}), 200

# recup de la moyenne
@app.route('/students/<student_id>/average', methods=['GET']) # définie une route GET/average (grades)
def get_average_grade(student_id):
    student = students.get(student_id)
    if not student:
        return jsonify({'error': 'Student not found'}), 404
    return jsonify({'studentID': student_id, 'averageGrade': student.getAverageGrade()}) # renvoie l'id du student et sa moyenne de note (grades)

# création d'une course
@app.route('/courses', methods=['POST']) # définie une route POST/course
def create_course():
    data = request.json
    course_code = data['courseCode'] # recup des donné du course
    if course_code in courses:
        return jsonify({'error': 'Course already exists'}), 400
    courses[course_code] = { # ajout des "valeurs" du course au dictionnaire
        'courseName': data['courseName'],
        'creditHours': data['creditHours'],
        'students': []
    }
    return jsonify({'message': 'Course created successfully'}), 201

# recup de l'id d'une course
@app.route('/courses/<course_code>', methods=['GET']) # definie une route GET/course_id
def get_course(course_code):
    course = courses.get(course_code) # recup de l'id du course
    if not course:
        return jsonify({'error': 'Course not found'}), 404
    return jsonify(course)

# création d'un enrollment
@app.route('/enrollments', methods=['POST']) # définie une route POST/enrollements
def enroll_student():
    data = request.json # recup des donné de enrollement
    student_id = data['studentID'] # recup de l'id du student
    course_code = data['courseCode'] # recup du course
    
    if student_id not in students:
        return jsonify({'error': 'Student not found'}), 404
    if course_code not in courses:
        return jsonify({'error': 'Course not found'}), 404
    
    courses[course_code]['students'].append(student_id)
    enrollments.append({'studentID': student_id, 'courseCode': course_code})
    return jsonify({'message': 'Student enrolled successfully'}), 201

if __name__ == "__main__":
    app.run(debug=True)
