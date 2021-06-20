sec = int(input('Введите время в секундах: '))
sec_hours = 3600
min_hours = 60

hours = sec//sec_hours
mins = sec%sec_hours//min_hours
secs = (sec%sec_hours)%60

print(f"Время в формате чч:мм:сс {hours} : {mins} : {secs}")

