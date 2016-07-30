from logger2 import logmod


try:
    inp=int(input("enter you number:"))
    if inp == 2:
        logmod(inp)
except Exception as ex:
    logmod(ex)

finally:
    print("执行结束")


