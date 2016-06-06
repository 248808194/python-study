import  random

list_data = []

for i in range(10):
    list_data.append(random.randint(0,10))
print  list_data

for i in range(len(list_data)-1):
    for j in range(i+1,len(list_data)):
        if list_data[i] > list_data[j]:
            list_data[i],list_data[j] = list_data[j],list_data[i]


print list_data

