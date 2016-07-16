num1 = input("enter num1:")
num2 = input("enter num2:")

try:
    num1 = int(num1)
    num2 = int(num2)
    result= num1 + num2
    print(result)
except Exception  as e: #Exception可以捕获所以错误
    print("出现异常，信息如下")
    print(e)

