km = int(input('введите 1 день, км: '))
km_max = int(input('введите макс км: '))
day = 0

while km < km_max:
    km = km + (km * 0.1)
    day +=1
    print(day, km)
print(f"Вы достигнете показателей на %.d км, на  %.d день" % (km_max, day))




