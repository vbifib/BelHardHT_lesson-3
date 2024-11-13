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

# class A:
#     def __int__(self, name, age):
#         self.name = name
#         self.age = age
#     def get_name(self):
#         return self.name
#
# class B(A):

# Task 1 and 2 and 3 (voice это метод)
# class Animal:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def voice(self):
#         return "Say Hello!"
#
#
# class Dog(Animal):
#     pass
#
# dog = Dog('Pitbul', 5)
#
# # print(dog.voice())
#
# class Bird(Animal):
#
#     def fly(self):
#         return "Я на Юг!"
#
# bird =Bird("Drozd", 2)
#
# # print(bird.fly())
#
# class Insect(Dog, Bird):
#     pass
#
# insect = Insect("Bug", 7)
#
# print(insect.fly())
# print(insect.voice())
#
# print(Insect.mro())


# Task 4
class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def voice(self):
        return "Say Hello!"

class Dog(Animal):
    def voice(self):
        return "Скажи Гав!"

dog = Dog('Pitbul', 5)

class Bird(Animal):

    def fly(self):
        return "Я на Юг!"

    def voice(self):
        return "Скажи чирик-чирик!"

bird =Bird("Drozd", 2)

class Insect(Dog, Bird):
    def voice(self):
        return "Прожжужжи!"

    def jump(self):
        return "попрыгай"

insect = Insect("Bug", 7)

print(insect.voice())

print(bird.voice())

print(dog.voice())

print(insect.jump())











