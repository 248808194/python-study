#coding:utf-8
N=20
n=N
total = 1
while(n>0):
    print "total = %d n=%d" %(total,n)
    total *=n
    n=n-1
print ("%d!=%d") % (N,total)