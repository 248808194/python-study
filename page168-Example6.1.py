import  string
alphas = string.letters + '_'
nums = string.digits
print 'welcome to identifier checker V1.0'
print 'testees must be at least 2 chars log'
myinput = raw_input('id to test? ')
if len(myinput) > 1:
    if myinput[0] not in alphas:
        print 'invalid first symbol must be alphas'
    else:
        for otherchar in myinput[1:]:
            if otherchar not in alphas + nums:
                print 'invalid first symbol must be alphasnumbers'
                break
        else:
            print 'ok it is a id'