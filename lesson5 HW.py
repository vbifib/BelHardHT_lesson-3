print("""Task 5: Сумма чисел от 1 до 100""")

some_total = 0
some_number = 1
while some_number <= 100:
    some_total += some_number
    some_number +=1
    print(some_total)

print("Homework Task 1")

guests = int(input("Введите кол-во гостей: "))
if 0 <= guests < 20:
    print("Отпразднуем дома")
elif 20 <= guests < 50:
    print("Заказать кофе")
elif guests >= 50:
    print("Заказать ресторан")
else:
    print("Количество гостей должно быть больше 0")


print("Homework task 2")

while True:
    rub = int(input("Ввести количесто рублей от 0 до 10: "))
    rub_text = " "
    if rub == 0:
        rub_text = "рублей"
        break
    elif rub == 1:
        rub_text = "рубль"
        break
    elif 2 <= rub <= 4:
        rub_text = "рубля"
        break
    elif 5 <= rub <= 10:
        rub_text = "рублей"
        break
    else:
        print("Количество рублей должно быть от 0 до 10")

while True:
    coins = int(input("Введите количество копеек от 0 до 99: "))
    coins_text = " "
    if coins == 0:
        coins_text = "копеек"
        break
    elif coins == 1:
        coins_text = "копейка"
        break
    elif 2 <= coins <= 4:
        coins_text = "копейки"
        break
    elif 5 <= coins <= 20:
        coins_text = "копеек"
        break
    elif coins == 21:
        coins_text = "копейка"
        break
    elif 22 <= coins <= 24:
        coins_text = "копейки"
        break
    elif 25 <= coins <= 30:
        coins_text = "копеек"
        break
    elif coins == 31:
        coins_text = "копейка"
        break
    elif 32 <= coins <= 34:
        coins_text = "копейки"
        break
    elif 35 <= coins <= 40:
        coins_text = "копеек"
        break
    elif coins == 41:
        coins_text = "копейка"
        break
    elif 42 <= coins <= 44:
        coins_text = "копейки"
        break
    elif 45 <= coins <= 50:
        coins_text = "копеек"
        break
    elif coins == 51:
        coins_text = "копейка"
        break
    elif 52 <= coins <= 54:
        coins_text = "копейки"
        break
    elif 55 <= coins <= 60:
        coins_text = "копеек"
        break
    elif coins == 61:
        coins_text = "копейка"
        break
    elif 62 <= coins <= 64:
        coins_text = "копейки"
        break
    elif 65 <= coins <= 70:
        coins_text = "копеек"
        break
    elif coins == 71:
        coins_text = "копейка"
        break
    elif 72 <= coins <= 74:
        coins_text = "копейки"
        break
    elif 75 <= coins <= 80:
        coins_text = "копеек"
        break
    elif coins == 81:
        coins_text = "копейка"
        break
    elif 82 <= coins <= 84:
        coins_text = "копейки"
        break
    elif 85 <= coins <= 90:
        coins_text = "копеек"
        break
    elif coins == 91:
        coins_text = "копейка"
        break
    elif 92 <= coins <= 94:
        coins_text = "копейки"
        break
    elif 95 <= coins <= 99:
        coins_text = "копеек"
        break
    else:
        print("Количество копеек должно быть от 0 до 99")

print(f"{rub} {rub_text} и {coins} {coins_text}")