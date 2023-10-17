class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students
if __name__ == "__main__":
    students = [
        Student("Alice", "001", 3.9),
        Student("Bob", "002", 3.7),
        Student("Charlie", "003", 3.8),
        Student("David", "004", 3.6)
    ]
    sorted_students = sort_students(students)
    for student in sorted_students:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
