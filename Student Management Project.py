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
        return super().getAverageGrade() + 5 # Exemple : ajout de 5 point seulement au student définie dans cette class

class UndergraduateStudent(Student):
    def getAverageGrade(self):
        return super().getAverageGrade()


class Course:
    def __init__(self, courseName, courseCode, creditHours):
        self._courseName = courseName
        self._courseCode = courseCode
        self._creditHours = creditHours
        self._students = []
    
    def enrollStudent(self, student):
        self._students.append(student)
    
    def getEnrolledStudents(self):
        return [student.get_name() for student in self._students]


class Enrollment:
    def __init__(self, student, course):
        self._student = student
        self._course = course
    
    def register(self):
        self._course.enrollStudent(self._student)

if __name__ == "__main__":
    # création d'un student
    student1 = UndergraduateStudent("Alice", 20, "U001")
    student2 = GraduateStudent("Bob", 25, "G001")
    student3 = UndergraduateStudent("John", 23, "U002")
    
    # ajout de notes
    student1.addGrade(85)
    student1.addGrade(90)
    student2.addGrade(88)
    student2.addGrade(92)
    student3.addGrade(34)
    student3.addGrade(74)
    
    # création d'une course
    course1 = Course("Math", "M101", 3)
    course2 = Course("Physics", "P102", 4)
    course3 = Course("Economie", "E103", 6)
    
    # ajout d'un student dans une course
    enrollment1 = Enrollment(student1, course1)
    enrollment2 = Enrollment(student2, course2)
    enrollment3 = Enrollment(student3, course3)
    
    # enregistrement d'un student dans une course
    enrollment1.register()
    enrollment2.register()
    enrollment3.register()
    
    # affiche les résultats
    print(f"{student1.get_name()} has an average grade of {student1.getAverageGrade()}")
    print(f"{student2.get_name()} has an average grade of {student2.getAverageGrade()}")
    print(f"{student3.get_name()} has an average grade of {student3.getAverageGrade()}")
    
    print(f"Students enrolled in {course1._courseName}: {course1.getEnrolledStudents()}")
    print(f"Students enrolled in {course2._courseName}: {course2.getEnrolledStudents()}")
    print(f"Students enrolled in {course3._courseName}: {course3.getEnrolledStudents()}")