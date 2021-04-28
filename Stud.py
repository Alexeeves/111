for i in range(1,101):
    x = ''
    if (i % 3 == 0):
        x += 'Fizz'
    if (i % 5 == 0):
        x += 'Buzz'
    if not x:
        x += str(i)
    print (x)