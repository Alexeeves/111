list1 = [1, 1, 2, 3, 5, 4, 5, 5, 6]
list2 = []    
for i in list1:    
    if not i in list2:  
        list2.append(i)
print (list2)