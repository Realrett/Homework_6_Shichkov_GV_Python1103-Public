# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import random
arr = [random()*10 for i in range(20)]
maximum = 3
minimum = 1
idx = []
for i in range(len(arr)):
	if minimum <= arr[i] <= maximum:
		idx.append(i)
		
b = []
for i in idx[::-1]:
    b.append(arr.pop(i))