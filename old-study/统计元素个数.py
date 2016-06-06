#coding:utf-8
n_c = 0
n_d = 0
while(True):
    str1=raw_input("enter str:")
    if (str1 == 'q'):
        break
    for val in str1:
        if ((val >='A' and val <= 'Z') or (val >='a' and val <= 'z')):
            n_c += 1
        elif (val >='0' and val <= '9'):
            n_d += 1

print "n_c = %d n_d = %d " %(n_c,n_d)