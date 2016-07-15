def a(b):
    n=0
    while (n < b):
        if (n%2==0):
            yield n
        n=n+1



c=a(20)
for i in c:
    print(i)

