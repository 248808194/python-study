while True:
    num1 = input("enter num1:")
    num2 = input("enter num2:")


    try:
        raise  Exception("主动出现异常")
        num1 = int(num1)
        num2 = int(num2)
        result = num1 + num2
    except Exception as ex:
        print(ex)
    else:
        print("num1 + num2 的值为%s" %result)
    finally:
        print("执行完毕")

