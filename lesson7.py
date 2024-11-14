
# class MyClass:
#     name: str
#     class_num = 11
#
#     def __init__(self, name):
#         self.name = name
#
# stud1 = MyClass("Anna")
# stud2 = MyClass("Lena")
#
# print(stud1.name, stud1.class_num)
# print(stud2.name, stud1.class_num)
#
# stud1.class_num = 10
# stud2.class_num = 8
# print(stud1.name, stud1.class_num)
# print(stud2.name, stud2.class_num)

#====================================================
#Task 1
# class Animals:
#     animal_type: str
#     type_zoo = "Minsk Zoo"
#
#     def __init__(self, animal_type):
#         self.animal_type = animal_type
#
# animal1 = Animals("Lion")
#
# print(animal1.animal_type,"/ ", animal1.type_zoo)

#====================================

# class MyClass:
#     state = "active class"
#     student_name: str
#     student_age: int
#
#     def __init__(self,student_name):
#         self.student_name = student_name
#
#     def age_sum(self, student_age):
#         self.student_age = sum(student_age)
#
#     @classmethod
#     def state_change(cls):
#         cls.state = "Super active class"
#
#     @staticmethod
#     def staticmethod():
#         print("Hello Guys!")
#
# student1 = MyClass("Anna")
# student1.student_age = 20
# student2 = MyClass("Lena")
# student2.student_age = 21
#
#
# print(student1.student_name, student1.student_age, student1.state)
# print(student2.student_name, student2.student_age, student2.state)

#=======================================
#Task 2
# class Animals:
#     animal_type: str
#     type_zoo = "Minsk Zoo"
#     animal_type_count = 1
#
#     def __init__(self, animal_type):
#         self.animal_type = animal_type
#
#     @classmethod
#     def increase_animals(cls):
#         cls.animal_type_count += 1
#         print("One animal is addded")
#
#
# animal1 = Animals("Lion")
#
# print(animal1.animal_type,"/ ", animal1.type_zoo)
#
# print(Animals.animal_type_count)
# Animals.increase_animals()
# print(Animals.animal_type_count)

#Task 3
# class Calculator:
#
#     @staticmethod
#     def calc_summa(a, b):
#         return a + b
#
#     @staticmethod
#     def calc_minus(a, b):
#         return a - b
#
#     @staticmethod
#     def calc_multiply(a,b):
#         return a * b
#
#     @staticmethod
#     def calc_divide(a, b):
#         return a / b
#
# print(Calculator.calc_summa(2, 10))
# print(Calculator.calc_minus(20, 5))
# print(Calculator.calc_multiply(5, 10))
# print(Calculator.calc_divide(50, 2))

#==================================================




