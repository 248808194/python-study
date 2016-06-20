"""
a:输入一串数字，并且从大到校排列
b: 和a一样，不过要用字典从大到校排列
"""

# 多个数字
anumber = input("Enter a number,split with ','\n")
alist = []

for anu in anumber.split(","):
    alist.append(int(anu))

alist.sort(reverse=True)
print(alist)
#
# #单个数字
numberstring = input("enter a number")
numberstring_list = list(numberstring)
new_list = []
for numstr in numberstring_list:
    new_list.append(numstr)

new_list.sort()
# print(new_list)


B,无解





