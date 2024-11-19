# показывал If

# a = 5
# while True:
#         if a == 4:
#             print("four")
#         if a == 6:
#             print("Шесть")
#         else:
#             print("No")
#         break
#======================================================
# class A:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def get_name(self):
#         return self.name
#
# class B(A):
#     def get_age(self):
#        return self.age
#
# a = A('Python', 50)
# b = B("C++", 100)
#
# print(a.get_name())
# print(b.get_age())
#================================
#Task1 в презентации:
# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def voice(self):
#         return "Что-то говорит..."
#
# class Dog(Animal):
#     pass
#
# a = Dog("Taksa", 2)
#
# print(a.voice())
#=============================================
# Метод Super пробую пример с вызыванием метода через if
# class Parent:
#     def __init__(self, name, hobby):
#         self.name = name
#         self.hobby = hobby
#
#     def show_info(self):
#         print("Name:", self.name)
#
#     def hobby_info(self):
#         print(self.name, self.hobby )
#
# class Child(Parent):
#     def __init__(self, name, age, hobby):
#         super().__init__(name, hobby)
#         self.age = age
#
#     def show_info(self):
#         super().show_info()
#         print("Age", self.age)
#
#     def hobby_child(self):
#         if self.age > 18:
#             super().hobby_info()
#         else:
#             print("No hobbies")
#
#
# Mother = Parent("Anna", "Tennis")
# Mother.show_info()
# Mother.hobby_info()
# Child_1 = Child("Andrey", 20, "tanks")
# Child_1.show_info()
# Child_1.hobby_child()
#===========================================
# Пробую композицию
# class Engine:
#     def start(self):
#         print("Двигатель запущен")
#
# class Car:
#     def __init__(self):
#         self.engine = Engine()
#
#     def drive(self):
#         print("Автомобиль начал движение")
#         self.engine.start()
# my_car = Car()
# my_car.drive()
#===================================================
# Task 2 в презентации:
# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def voice(self):
#         return "Что-то говорит..."
#
# class Dog(Animal):
#     pass
#
# a = Dog("Taksa", 2)
#
# a.voice()
#
# class Bird(Animal):
#     def fly(self):
#         return ("Я на Юг")
# bird = Bird("Kolibri", 5)
#
# print(bird.fly())
#==============================================
# Иерархия наследования
# class A:
#     def __init__(self):
#         self.name = self
#     def who_am_i(self):
#         print("A")
# class B(A):
#     def who_am_i(self):
#         print("B")
# class C(A):
#     def who_am_i(self):
#         print("C")
# class D(B, C):
#     pass
#
# object_D = D()
# object_D.who_am_i()
#===========================================
#Task 3
# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def voice(self):
#         return "Что-то говорит..."
#
# class Dog(Animal):
#     pass
#
# a = Dog("Taksa", 2)
#
# # print(a.voice())
#
# class Bird(Animal):
#     def fly(self):
#         return ("Я на Юг")
#
# bird = Bird("Kolibri", 5)
#
# # print(bird.fly())
#
# class Insect(Dog, Bird):
#     pass
#
# insect_1 = Insect("Bug", 1)
#
# # print(insect_1.voice(), insect_1.fly())
# # print(insect_1.voice())
# # print(insect_1.fly())
#
# print(Insect.mro())
#===============================================
#Task 4 презентации
# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def voice(self):
#         return "Что-то говорит..."
#
# class Dog(Animal):
#     def voice(self):
#         return "Гав-Гав"
#
# class Bird(Animal):
#     def fly(self):
#         return ("Я на Юг")
#     def voice(self):
#         return "Чирик-Чирик"
#
# class Insect(Dog, Bird):
#     def voice(self):
#         return "штрекочет"
#
#     def jump(self):
#         return "Букашка прыгает все время"
#
# dog = Dog("Taksa", 2)
# bird = Bird("Kolibri", 5)
# insect = Insect("Bug", 1)
#
# print(insect.voice())
# print(bird.voice())
# print(dog.voice())
# print(insect.jump())
#==========================================================
#Инкапсуляци и обходной метод
# class A:
#     _protected = 0
#     __private = 1
#
# class D(A):
#     def what_i_see(self):
#         print(self._protected)
#
# a = A()
# print(a._protected)
# # print(a.__private)
# print(a._A__private)
#==========================================================
# Геттеры и сетторы
# class Person:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
#     def get_name(self):
#             return self._name
#
#     def get_age(self):
#         return self._age
#
#     def set_name(self, name):
#         self._name = name
#
#     def set_age(self, age):
#         if age >= 0:
#             self._age = age
#         else:
#             print("Возраст не может быть отрицательным")
#
# person = Person("Mike", 30)
# print("Имя:", person.get_name())
# print("Возраст:", person.get_age())
# person.set_name("Anna")
# person.set_age(-1)
# print("Имя:", person.get_name())
# print("Возраст:", person.get_age())
#=======================================================





