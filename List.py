a = [1, 1, 2, 3, 5, 4, 5, 5, 6]
b= []
for i in a:
    if not i in b:
       b.append(i)
print (b)
