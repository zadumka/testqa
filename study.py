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

a = 3
b = 3
if a < b :
    print('a меньше b')
else:
    print ('a дорівнює b')

name = 'Tom'
height = 2
weight = 140

bmi = weight/(height **2)
print ('Індекс маси тіла: '+ str(bmi))

if bmi < 25:
    print(" У "  + name + " нема зайвої ваги")
else :
    print ("У " + name + " є надмірна вага")