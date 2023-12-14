class Course:
    def __init__(self, code, title, capacity):
        self._code = code
        self._title = title
        self._capacity = capacity
        self._enrolled_students = []

    def available_slots(self):
        return self._capacity - len(self._enrolled_students)

    def status(self):
        if self.available_slots() == 0:
            print(f'This course is full. ({len(self._enrolled_students)}/{self._capacity})')
        else:
            print(f'There is/are {self.available_slots()} slots left for this course. ({len(self._enrolled_students)}/{self._capacity})')

    def enroll(self, name):
        if self.available_slots() > 0:
            self._enrolled_students.append(name)
            return True
        else:
            return False
        
    def status(self):
        print(f"Course: {self._title} - {self._code}")
        print(f"Slots: {self._capacity - len(self._enrolled_students)}/{self._capacity}")

class Student:
    def __init__(self, id, name):
        self._id = id
        self._name = name
        self._courses = []

    def enroll_course(self, course):
        if course.enroll(self):
            self._courses.append(course)
            print(f'Enrollment successful.')
            return True
        else:
            print(f'Enrollment failed.')
            return False
        
    def status(self):
        print(f'{self._name} - {self._id}')
        print(f'Enrolled Courses: {[course._title for course in self._courses]}')
    
def find_student(student_id, students):
    return next((s for s in students if s._id == student_id), None)

def find_course(course_code, courses):
    return next((c for c in courses if c._code == course_code), None)

def main():
    courses = [
        Course("MATH123", "Mathematics", 10),
        Course("SCI987", "Science", 2),
        Course("ENG345", "English", 3),
        Course("TOK543", "Theory of Knowledge", 5),
    ]

    students = [
        Student("123789", "Cindy"),
        Student("789121", "Mandy"),
        Student("673452", "Cassie"),
        Student("349121", "Ivana")
    ]

    while True:
        print("1. Enroll student.")
        print("2. Display course status.")
        print("3. Display student status.")
        print("4. Quit")

        choice = input("What would you like to do? ")

        if choice == "1":
            student_id = input("Enter student id: ")
            student = find_student(student_id, students)

            if not student:
                print("Student not found.")
            else:
                course_code = input("Enter course code: ")
                course = find_course(course_code, courses)

                if not course:
                    print("Course not found.")
                else:
                    student.enroll_course(course)

        elif choice == "2":
            course_code = input("Enter course code: ")
            course = find_course(course_code, courses)

            if course:
                course.status()
            else:
                print("Course not found.")

        elif choice == "3":
            student_id = input("Enter student id: ")
            student = find_student(student_id, students)

            if student:
                student.status()
            else:
                print("Student not found.")

        elif choice == "4":
            print("Quit.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()