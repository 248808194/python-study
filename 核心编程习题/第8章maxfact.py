#检查 一个数字范围内偶数和基数(能被2整除)


def check(number):
    if number % 2 == 0:
        return  True
    else:
        return False



def tongji(x,y):
    for eachone in range(x,y):
        result = check(eachone)
        print(result)
        if result == True:
            print("%d 是偶数" %eachone)
        else:
            print("%d是基数" %eachone)

if __name__ == "__main__":
    tongji(1,10)