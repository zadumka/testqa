list = [1, 2, 3, 4, 5]
print(list)
print(list[0])
print(list[:2])

list_sum = 0
for num in list :
    list_sum = list_sum + num
print(list_sum)

list1 = ['b', 'a', 'c', 'd']
print(list1)
list1.sort()
print(list1)
#new task
f =15
g = 15
if f > g :
    print('f більше g')
else:
    if f == g :
        print('f дорівнює g')
    else :
        print('f меньше g')