# Hi Slava!
# Hope you are doing well!
# Please find lesson4 homework below.
from ast import parse

# Task num 1:
print("Task num 1:")

list_cars = ["Jeep", "Chevrolet", "Dodge", "Hummer"]
print(list_cars)

list_cities = list(["Paris", "Roma", "Madrid", "Valetta"])
print(list_cities)

list_cars.append("Volvo")
print(list_cars)

list_cities.append("Warsaw")
print(list_cities)

list_cars.insert(0, "BYD")
print(list_cars)

list_cities.insert(0, "New-York")
print(list_cities)

list_cars.extend(list_cities)
print(list_cars)

# Task num 2:
print("=============================================")
print("Task num 2:")
import this
print("=============================================")
the_zen = ['Beautiful is better than ugly.',
'Explicit is better than implicit.',
'Simple is better than complex.',
'Complex is better than complicated.',
'Flat is better than nested.',
'Sparse is better than dense.',
'Readability counts.',
"Special cases aren't special enough to break the rules.",
'Although practicality beats purity.',
'Errors should never pass silently.',
'Unless explicitly silenced.',
'In the face of ambiguity, refuse the temptation to guess.',
'There should be one-- and preferably only one --obvious way to do it.',
"Although that way may not be obvious at first unless you're Dutch.",
'Now is better than never.',
'Although never is often better than *right* now.',
"If the implementation is hard to explain, it's a bad idea.",
'If the implementation is easy to explain, it may be a good idea.',
"Namespaces are one honking great idea -- let's do more of those!"]
# Находим длину списка - это и есть кол-во строк:
print("Количество строк:")
print(len(the_zen))
# print(type(the_zen))
zen_str = str(the_zen)
# print(type(zen_str))
# print(zen_str)
count_is = zen_str.count('is')
count_and = zen_str.count('and')
count_or = zen_str.count('or')
print("Количество вхождений is:")
print(count_is)
print("Количество вхождений and:")
print(count_and)
print("Количество вхождений or:")
print(count_or)
some_dict = {}
some_dict['is'] = count_is
some_dict['and'] = count_and
some_dict['or'] = count_or
print("Словарь ниже")
print(some_dict)
splitted_zen = zen_str.split(" ")
# print(type(splitted_zen))
# print("is" in splitted_zen)
# print(splitted_zen.count("is"))
# print(len(splitted_zen))
spl_zen_str = str(splitted_zen)
# print(type(spl_zen_str))
# print(spl_zen_str)
# print(spl_zen_str.count("is"))
final_action = spl_zen_str.replace("is", "is not")
# print(final_action.count("is not"))
print("Отражение замененных вхождения на is not ниже:")
print(final_action)








