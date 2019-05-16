my_student = {
    'name': 'Rolf Smith',
    'grades': [48, 70, 88, 90, 99]
}

def student_average(student):
    return sum(student['grades']) / len(student['grades'])

print(my_student)
print('My student average is: {}'.format(student_average(my_student)))

class Student:
    def __init__(self, new_name, new_grade):
        self.name = new_name
        self.grades = new_grade

    def average(self):
        return sum(self.grades) / len(self.grades)

    def print_info(self):
        print(f'<<{self.name}>> by {self.grades}')

student_one = Student('Rolf Smith', [48, 70, 88, 90, 99])
student_two = Student('Pat Roberts', [80, 65, 25, 98, 78])

print(student_one.__class__)
student_one.print_info()
