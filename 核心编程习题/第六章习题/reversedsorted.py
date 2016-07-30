print('reversed是反转的意思')
a=reversed([1,2,3])
print("返回的是一个迭代期",a)
for i in a:
    print(i)

print("sorted返回的是一个列表")
a= sorted("abc")
b= sorted([1,2,3])
c= sorted((1,2,3))
print(a,b,c)
print(type(a),type(b),type(c))


for i in reversed(['wesley', 'foo', 'bar']):
    print(i)


