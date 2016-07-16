db ={'123': '234'}

def newuser():
    promet = "login desired:"
    while True:
        name = input(promet)
        if name in db:
            promet = "name taken, try another:"
            continue
        else:
            break
    passwd = input("enter your passwd")
    db[name] = passwd


def olduser():
    while True:
        name = input("enter you username: ")
        passwd = input("enter your passwd ")
        if name in db and db[name] == passwd:
            print("welcome %s" %(name))
            break
        else:
            print("name or passwd missmath pls try again ")



def showmenu():
    showm = """
        (N)ew User Login
        (E)xisting User Login
        (Q)uit
         Enter you chose:
    """
    done = 0
    while not done:
        choise = 0
        while not choise:
            try:
                inp = input(showm)[0]
                print(inp)
            except Exception as  ex:
                print(ex)
                choise = 1
            print ('\nYou picked: [%s]' % inp)

            if inp not in "neq":
                print("invalid menu option, try again")
            else:
                choise = 1

        if inp == "n": newuser()
        if inp == "e": olduser()
        if inp == "q": done =1



if __name__ == "__main__":
    showmenu()


