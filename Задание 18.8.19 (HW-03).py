print("При покупке 4 и более билетов Вы получаете скидку в 10%")
tickets = int(input("Введите количесво билетов "))
cost = 0
for t in range(tickets):
    while True:
        try:
            age = int(input("Введите возраст владельца билета " + str( t + 1 ) + " "))
            if age < 0 or age >= 100:
                print("Вам не может быть столько лет")
                continue
            break
        except ValueError:
            print("Необходимо вводить числа")
    if age < 18:
        print("Билет бесплатный")
        print("Общая стоимость билетов = " + str(cost) + "р")
    elif 18 <= age < 25:
        cost += 990
        print("Стоимость билета = 990р")
        print("Общая стоимость билетов = " + str(cost) + "р")
    elif 25 <= age:
        cost += 1390
        print("Стоимость билета = 1390р")
        print("Общая стоимость билетов = " + str(cost) + "р")

if tickets > 3:
    cost = cost * 90 / 100
    print("Итоговая сумма к оплате  " + str(cost) + " рублей")
else:
    print("Итоговая сумма к оплате " + str(cost) + " рублей")