import random
list_data = []
for i in range(3):
    list_data.append(random.randint(0,20))
print  list_data
list_len=len(list_data)

for i in range(1,list_len):
    j = 0
    while (j < i):
        if(list_data[j] > list_data[i]):
            break
        j=j+1
    tmp = list_data[i]
    k = i
    while (k > j):
        list_data[k] = list_data[k-1]
        k = k -1
    list_data[k] = tmp
    print "i=%d %s" %(i,list_data)
print list_data