import  random
import string

while True:
    enter = raw_input("Enter S(start game) / Q(Quit Game):").upper()
    if (enter == 'Q'):
        break
    elif(enter == 'S'):
    val = random.randint(0, 100)
        while True:
            num = int(raw_input("Enter num(0~100,):"))
            num = 10
            if (num == val):
                print "guess ok!\n play again"

            elif( num > val):
                print "bigger"
            else:
                print "litter"

    else:
        print 'wrong enter pls try again'