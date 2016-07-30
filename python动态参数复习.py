# *args
#实例将元祖中的元素分别打印出来

def print_single_tuple(*args):
    print(args,type(args))
    for index,item in enumerate(args):
        print("each single name is:%s,index is %s" %(item,index) )
    return "finished"


#print_single_tuple('a', 'b', 'c', 'd', 'e', 'f', 'g')


#将字母A-Z的位置加入到一个列表中去 类是{ "a":0,"b":1,"c":2}这样

def foo(*args,**kwargs):
    for index,item in enumerate(args):
        kwargs[item] = index
    print(kwargs)

foo('a', 'b', 'c', 'd', 'e', 'f', 'g')

#实例三，创建用户，将用户名，密码存放在kwargs下

def foo(**kwargs):
    while True:
        inp_username = input("enter you username: ")
        inp_password = input("enter your password")
        if inp_username in kwargs.keys():
             print("username %s is existx "%(inp_username))
             continue
        else:
            kwargs[inp_username] = inp_password
            print("you name is %s and password is %s" %(inp_username,inp_password))

# foo()