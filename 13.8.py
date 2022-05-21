price_all = 0
while True:
    try:
        tic_num = input('Сколько билетов вы хотите приобрести на мероприятие? ')
        tic_num = int(tic_num)
        if type(tic_num) == int:
for i in range(tic_num):
    i += 1
    while True:
        try:
            age_for_ticket = input(f'Введите ваш возраст №{i}? ')
            age_for_ticket = int(age_for_ticket)
            if age_for_ticket < 18:
                print('Билет бесплатный')
            elif 25 > age_for_ticket >= 18:
                price_all += 990
                print('Стоимость билета: 990 руб.')
            else:
                price_all += 1390
                print('Стоимость билета: 1390 руб.')
            if type(age_for_ticket) == int:
if tic_num > 5:
    price_all = price_all - ((price_all / 100) * 20)
    print(f'Сумма к оплате {price_all} руб. с учетом 20%-ой скидки на полную стоимость заказа за регистрацию больше 5-и человек')
else:
    print(f'Сумма к оплате {price_all} руб.')
