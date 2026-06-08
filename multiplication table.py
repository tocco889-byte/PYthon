a = int(input('enter a number for multiplication table '))
st = int(input('enter the starting table number '))
lim = int(input('enter the limit'))
for i in range(st, lim + 1):
    print(a, '*', i, '=', a * i)
