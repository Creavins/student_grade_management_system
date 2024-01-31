"""A Python Student Management System Project by Kakeeto Francis Creavins"""

class Student:
    def __init__(self, name, roll_number, marks):
        """
        Initialize a Student object with name, roll_number, and marks.
        """
        self.name = name
        self.roll_number = roll_number
        self.marks = marks
        self.grade = self.calculate_grade()


    def calculate_grade(self):
        """
        Calculate the grade based on the student's marks.
        """
        if 100 >= self.marks >= 90:
            return 'A'
        elif 89 >= self.marks >= 80:
            return 'B'
        elif 79 >= self.marks >= 70:
            return 'C'
        elif 69>= self.marks >= 60:
            return 'D'
        elif 59 >=self.marks >= 50:
            return 'E'
        elif 49 >= self.marks >= 0:
            return 'F'
        else:
            return'Invalid marks! Marks should be from 0 to 100!'
            

    def display_student(self):
        """
        Display the details of the student.
        """
        print(f"\n\tName: {self.name}")
        print(f"\tRoll Number: {self.roll_number}")
        print(f"\tMarks: {self.marks}")
        print(f"\tGrade: {self.grade}")


class StudentManagementSystem:
    def __init__(self):
        """
        Initialize the Student Management System.
        """
        self.students = {}


    def validate_roll_number(self, roll_number):
        """
        Validate if the given roll number already exists in the system.
        """
        if roll_number in self.students:
            return False
        return True


    def add_student(self, name, roll_number, marks):
        """
        Add a student to the system.
        """
        if not self.validate_roll_number(roll_number):
            print("\n\tRoll number already exists. Please choose a different roll number.\n")
            return
        student = Student(name, roll_number, marks)
        self.students[roll_number] = student
        print("\n\tStudent added successfully.\n")


    def display_student_details(self, roll_number):
        """
        Display the details of a student.
        """
        if roll_number in self.students:
            student = self.students[roll_number]
            student.display_student()
        else:
            print("\n\tStudent with the given roll number does not exist.\n")


    def update_student_details(self, roll_number, name, marks):
        """
        Edit the details of a student.
        """
        if roll_number in self.students:
            student = self.students[roll_number]
            student.name = name
            student.marks = marks
            student.grade = student.calculate_grade()
            print("\n\tStudent details updated successfully.\n")
        else:
            print("\n\tStudent with the given roll number does not exist.\n")


    def delete_student(self, roll_number):
        """
        Delete a student from the system.
        """
        if roll_number in self.students:
            del self.students[roll_number]
            print("\n\tStudent deleted successfully.\n")
        else:
            print("\n\tStudent with the given roll number does not exist.\n")


    def display_menu(self):
        """
        Display the menu options.
        """
        print("\n----- Student Management System -----\n")
        print("Select the option you want!\n")
        print("\t1. Add Student")
        print("\t2. Display Student Details")
        print("\t3. Update Student Details")
        print("\t4. Delete Student")
        print("\t5. Exit")


    def run_system(self):
        """
        Run the Student Management System until the user selects the exit option.
        """
        while True:
            self.display_menu()
            choice = input("\nEnter your choice (1-5): ")

            if choice == '1':
                name = input("\nEnter student name: ")
                roll_number = input("Enter roll number: ")
                marks = int(input("Enter marks: "))
                self.add_student(name, roll_number, marks)
            elif choice == '2':
                roll_number = input("\nEnter roll number: ")
                self.display_student_details(roll_number)
            elif choice == '3':
                roll_number = input("\nEnter roll number: ")
                name = input("Enter updated name: ")
                marks = int(input("Enter updated marks: "))
                self.update_student_details(roll_number, name, marks)
            elif choice == '4':
                roll_number = input("\nEnter roll number: ")
                self.delete_student(roll_number)
            elif choice == '5':
                print("\n\tExiting the Student Management System.\n")
                break
            else:
                print("\n\tInvalid choice. Choice must be from 1 to 5! Please try again.\n")


start_system = StudentManagementSystem()
start_system.run_system()
