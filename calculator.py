a = int(input('enter first  number : '))
b = int(input('enter second number : '))
c = input(" press 'add or 1' for addition , 'sub or 2'for subtract','multi or 3 'for multiplication , 'div or 4' for division ")
if c == 'add'or c == '1':
    print(a + b)
elif c == 'sub'or c == '2':
    print(a - b)
elif c == 'multi' or c == '3':
    print(a * b)
elif c == 'divide' or c == '4':
    d = float(a / b)
    print(d)
else:
    print('invalid option')
