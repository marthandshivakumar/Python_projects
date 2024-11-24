class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}

    def add_or_update_grade(self, subject, grade):
        """Add or update the grade for a specific subject."""
        self.grades[subject] = grade

    def calculate_average_grade(self):
        """Calculate the average grade of the student."""
        if self.grades:
            return sum(self.grades.values()) / len(self.grades)
        return 0

    def __str__(self):
        """Return a formatted string representation of the student."""
        return f"Name: {self.name}, ID: {self.student_id}, Grades: {self.grades}, Average: {self.calculate_average_grade():.2f}"

class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, name, student_id):
        """Add a new student to the system."""
        if student_id not in self.students:
            self.students[student_id] = Student(name, student_id)
            print(f"Student {name} added successfully.")
        else:
            print(f"Student ID {student_id} already exists.")

    def add_or_update_grade(self, student_id, subject, grade):
        """Add or update the grade of an existing student."""
        if student_id in self.students:
            student = self.students[student_id]
            student.add_or_update_grade(subject, grade)
            print(f"Grade for {subject} updated successfully for {student.name}.")
        else:
            print("Student not found.")

    def calculate_average_grade(self, student_id):
        """Calculate and display the average grade of a student."""
        if student_id in self.students:
            student = self.students[student_id]
            print(f"{student.name}'s average grade is {student.calculate_average_grade():.2f}.")
        else:
            print("Student not found.")

    def display_all_students(self):
        """Display all students and their grades."""
        if not self.students:
            print("No students found.")
        else:
            print("\nAll Students:")
            for student in self.students.values():
                print(student)

    def search_student(self, name):
        """Search for a student by name."""
        found = False
        for student in self.students.values():
            if student.name.lower() == name.lower():
                print(student)
                found = True
                break
        if not found:
            print("Student not found.")

    def update_student_information(self, student_id, name=None):
        """Update student information."""
        if student_id in self.students:
            student = self.students[student_id]
            if name:
                student.name = name
            print(f"Student information updated. New details: {student}")
        else:
            print("Student not found.")

    def exit_system(self):
        """Exit the system."""
        print("Exiting the system. Goodbye!")
        exit()

sms = StudentManagementSystem()

while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. Add/Update Grade")
    print("3. Calculate Average Grade")
    print("4. Display All Students")
    print("5. Search for Student")
    print("6. Update Student Information")
    print("7. Exit")
    
    choice = input("Choose an option (1-7): ").strip()

    if choice == "1":
        name = input("Enter student name: ").strip()
        student_id = input("Enter student ID: ").strip()
        sms.add_student(name, student_id)

    elif choice == "2":
        student_id = input("Enter student ID: ").strip()
        subject = input("Enter subject name: ").strip()
        grade = float(input(f"Enter grade for {subject}: ").strip())
        sms.add_or_update_grade(student_id, subject, grade)

    elif choice == "3":
        student_id = input("Enter student ID: ").strip()
        sms.calculate_average_grade(student_id)

    elif choice == "4":
        sms.display_all_students()

    elif choice == "5":
        name = input("Enter student name to search: ").strip()
        sms.search_student(name)

    elif choice == "6":
        student_id = input("Enter student ID to update: ").strip()
        name = input("Enter new name (leave blank to keep current): ").strip()
        if not name:
            name = None
        sms.update_student_information(student_id, name)

    elif choice == "7":
        sms.exit_system()

    else:
        print("Invalid option. Please choose between 1-7.")
