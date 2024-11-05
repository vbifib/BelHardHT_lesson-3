from tkinter.font import nametofont

# list_1 = list()
# list_2 = ['First', 'second', 'third']
# print(type(list_1))
# print(type(list_2))
# print(list_1)
# print(list_2)

# #it is tuple (кортеж)
# a = ('Ready', 'steady', 'go')
# #it is set (множество)
# b = {'Ready', 'steady', 'go'}
# #it is str (строка)
# c = 'Hello'
# #it is diсt (словарь)
# d = {1: 'one', 2: 'two'}
# print(list(a))
# print(list(b))
# print(list(c))
# print(list(d))

# aa = [1, 2, 3, 4, 5, 6, 7]
# print(aa[2])
# print(aa[-1])

# bb = [1, 2, [3, 2], 5]
# print(bb[1])
# print(bb[2])
#
# bc = list([1, 2, 3, [5, 6], 4])
# print(bc)
# print(bc[3])

# dd = ["one", "two", "three", "four", "five"]
# print(dd)
# print(dd[:])
# print(dd[1:])
# print(dd[:3])
# print(dd[1:-1])
# print(dd[1::2])
# print(dd[::-1])

# dd = ["one", "two", "three", "four", "five"]
# print(len(dd))

# Задача 1

# new_list = [1, 2, 3, 4, 5]
# print(new_list [1])
# print(new_list[1] + len(new_list))
# del new_list[1]
# print(new_list)

# print(5 in new_list)

# new_list = [1, 2, 3, 4, 5]
# new_list.append("Hi Python")
# print(new_list)
#
# new_list.insert(0, 'Hi everybody')
# print(new_list)

# Задача 2

# a = [1, 2, 3, 4]
# a.append(5)
# a.insert(2, 'python')
# print(a)
# a = [1, 2, 3, 4]
# a.extend(('From', 'Tuple'))
# print(a)
# a.extend(['from', 'list'])
# print(a)
# a.extend("Stroka")
# print(a)
# a = [1, 2, 3, 4]
# a.pop(2)
# print(a)
#
# a.pop()
# print(a)
#
# a = [1, 2, 3, 4]
# print(a.index(2, 0, 3))
# a = [1, 2, 3, 4, 3, 5, 3]
# print(a.count(3))
# a = [1, 2, 8, 4, 6, 5, 7, 3]
# # print(sorted(a))
# # print(sorted(a, reverse=True))
# a.sort()
# print(a)
# # a.sort(reverse=True)
# # print(a)
# a.sort(key=lambda x: x%2)
# print(a)

# a = [1, 2, 8, 4, 6, 5, 7, 3]
# a.clear()
# print(a)

# a = [1, 2, 8, 4, 6, 5, 7, 3]
# b = a[:]
# print(b == a)
# print(b is a)
# print(b)

# a = [1, 2, 8]
# print(a)
# a.append(4)
# print(a)
# import copy
# b = copy.copy(a)
# b.append(5)
# print(a)
# print(b)

# av = {1, 2, 3}
# print(type(av))
# ab = set({1, 2, 3})
# print(type(ab))

# a = {1, 2, 3}
# b = {3, 4}
# print(a.isdisjoint(b))
# c = {6, 7}
# print(a.isdisjoint(c))

# a = {1, 2, 5, 8}
# b = {1, 2, 5, 6, 7}
# print(a.issubset(b))
# print(a <= b)

# a = {1, 2, 3}
# b = {1, 2}
#
# print(a >= b)
# c = {1, 2, 3, 4}
# print(a >= c)

# a = 2
# print(hash(a))
# b = 'str'
# print(hash(b))
# c = tuple((1, 2, 3))
# print(hash(c))
# d = [1, 2, 3]
# print(hash(d))

# a = {1: "One", 2: " two"}
# print(type(a))
# b = dict({"a": "one", "b": "two"})
# print(type(b))
# word = "letter"
# c = {let: word.count(let) for let in word}
# print(type(c))
# print(c)

# Задача 3
# user = {}
# user["name"] = "Mike"
# user["age"] = "35"
# user['skills'] = ["Python"]
# print(user)
# user['skills'] = ['Python', 'Django']
# print(user)




