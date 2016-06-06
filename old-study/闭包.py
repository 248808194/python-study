def count(base):
    return lambda sales: sales * 10000 * base

# def count(base):
#     def in_count(sales):
#         return sales * 10000 * base
#     return in_count

salses20=count(0.03)
salses10=count(0.02)
salses1=count(0.01)




def count1(sales):
    if sales > 20:
        return salses20(sales)
    elif sales > 10:
        return salses10(sales)
    else:
        return salses1(sales)

while (True):
    sales=int(raw_input("enter sales:"))
    print "salary =%d RMB" %(count1(sales))