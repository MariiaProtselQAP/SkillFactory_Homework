tickets = int(input('Введите количество билетов, которое хотите приобрести: '))
price=[]
for i in range(tickets):
    age = int(input("Введите возраст посетителя №{}: ".format(i+1)))
    if age < 18:
        price.append(0)
    elif 18 <= age < 25:
        price.append(990)
    elif age >=25:
        price.append(1390)
if tickets>3:
    print("Общая стоимость билетов:",(sum(price)*0.9),"рублей")
else:
    print("Общая стоимость билетов:",sum(price),"рублей")