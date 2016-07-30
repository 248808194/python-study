

#如果try执行没有报错就执行else
#如果try执行报错就去执行except
#finally不管报错或不报错都不执行

#例子

while True:
    num1 = input("enter num1:")
    num2 = input("enter num2:")


    try:
        num1 = int(num1)
        num2 = int(num2)
        result = num1 + num2
    except Exception as ex:
        print(ex)
    else:
        print("num1 + num2 的值为%s" %result)
    finally:
        print("执行完毕")










