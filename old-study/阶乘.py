#coding:utf-8
# N=20
# n=N
# total = 1
# while(n>0):
#     print ("total = %d n=%d" %(total,n))
#     total *=n
#     n=n-1
# print ("%d!=%d"% (N,total))


def func(num):
    if num == 7:
        return  1
    print(  num * func(num -1))

x=func(7)
