# a = 5
# if a > 4:
#     print("Yes")
# elif a < 10:
#     print('YES')
from Tools.scripts.verify_ensurepip_wheels import print_notice

# Task 1
# some_str = "Hello!"
# if len(some_str) > 10:
#     print('Long')
# elif len(some_str) < 10:
#     print("Short")

# Тернарный оператор
# x = 10
# x_2 = x if x < 5 else "Больше десяти"
# print(x_2)


# Task 2
# a = int(input("Введите чиловое значение: "))
# if a %2 == 0:
#     print(f"Это число {a} четное")
# else :
#     print(f"Это число {a} нечетное")

# some_value = input("Введите число:")
# some_vv = int(some_value)
# if isinstance(some_vv, int):
#     if some_vv >= 100:
#         print("больше ста")
#     else:
#         print("меньше ста")
# else:
#     print("Строка")
# print(type(some_vv))
# elif isinstance(some_value, str):
#     if some_value.isdigit():
#         print("digital")
#     else:
#         print("not digital")

# some_mark = int(input("Введите оценку от 0 до 100: "))
# if some_mark >= 85:
#     print("Отлично")
# elif some_mark >= 60:
#     print("Хорошо")
# elif some_mark >= 40:
#     print("Удовлетворительно")
# else:
#     print("не удовлетворительно")

# Task4


# while True:
#     a = str(input("Введите любую строку: "))
#     if a.lower() == "stop":
#         break

# Task 5:

# some_total = 0
# some_number = 1
# while some_number <= 100:
#     some_total += some_number
#     some_number +=1
#     print(some_total)
#
# print(sum(range(1, 101)))

# Task 6

some_list = ['a', 'b', 'c']
for letter in some_list:
    if type(letter) == str:
        some_list.append("d")
print(some_list)




























