num1 = input("enter num1:")
num2 = input("enter num2:")

try:
    num1 = int(num1)
    num2 = int(num2)
    result= num1 + num2
    print(result)
except Exception  as e:
    print("出现异常，信息如下")
    print(e)


#如果try快里面报错了，就会去自动执行except里面的内容
#在try快里面放正常执行的代码。，如果出错就会执行except代码
