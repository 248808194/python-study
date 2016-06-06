#conding: utf-8
import random #
list_data = []
for i in range(10):
    list_data.append(random.randint(0,20))
print  list_data

list_len=len(list_data) -1

for i in range(len(list_data)):

    for j in range(list_len - i):
        if(list_data[j] > list_data[j+1]):
            list_data[j] , list_data[j+1] = list_data[j+1],list_data[j]
print list_data