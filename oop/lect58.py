class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []

    @property # decorator car simple calcul, ne change pas l'etat de l'objet
    def average(self):
        return sum(self.marks) / len(self.marks)

student = Student('Rolf')
student.marks.append(78)
student.marks.append(85)
student.marks.append(90)
print(student.average)

class Foo:
    @classmethod
    def hi(cls):
        print(cls.__name__)

my_object = Foo()
my_object.hi()

class Bar:
    @staticmethod
    def hi():
        print('I don\'t take any parameters')

another_object = Bar()
another_object.hi()
