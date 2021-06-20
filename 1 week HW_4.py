figure  = int(input('ведите число '))
r = -1

while figure > 10:
    d = figure % 10
    figure //= 10
    if d > r:
        r = d
print(r)