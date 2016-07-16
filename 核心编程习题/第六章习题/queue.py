#新建一个quene列表
#定义一个函数enQ 往列表中添加一个字符串
#定义一个函数检查quene列表，如果列表为空，打印出不能被分离, 否则使用pop函数移除列表第一个元素
#定义一个函数用来查询quene列表，前提是用str将quene列表转换成字符串

quene= []

def enq ():
     quene.append(input("Enter new queue element: "))

def deQ():
    if len(quene) == 0:
        print("Cannot dequeue from empty queue!")
    else:
        print("Removed[" ,quene.pop(0),"]")

def view():
    print(str(quene))

def showmenu():
    prompt = """
(E)nqueue
(D)equeue
(V)iew
(Q)uit

Enter choice: """
    done = 0
    while not done:
        chosen = 0
        while not chosen:
            try:
                choice = input(prompt)[0]
                print(chosen)
            except (IndexError, EOFError, KeyboardInterrupt):
                choice = "q"
            print('\nYou picked: [%s]' % chosen)
            if choice not in "devq":
                print("invalid option, try again")
            else:
                chosen = 1
        if choice == 'q': done = 1
        if choice == 'e': enq()
        if choice == 'd': deQ()
        if choice == 'v': view()

if __name__ == "__main__":
    showmenu()
