revenue = int(input('введите выручку: '))
cost = int(input('введите затраты: '))

if revenue > cost:
    print('Компания прибыльная, рентабельность: ',  (revenue-cost/revenue))
    staff_number = int(input('Введите кол-во сотрудников: '))
    print(revenue-cost/staff_number)
elif revenue == cost:
    print('Компания находится в зоне риска')
else:
    print('Компания практически банкрот')


