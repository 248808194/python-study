
import os
"""
查找目录下所有文件
"""
# def gci(filepath):
#     files = os.listdir(filepath)
#     print(files)
#     for f1 in files:
#         fi_d = os.path.join(filepath,f1)
#         if os.path.isdir(fi_d):
#             gci(fi_d)
#         else:
#             print(os.path.join(filepath,fi_d))
# gci("C:/Users/ZhouTao/PycharmProjects/python-study/")

#2查找目录下所有文件，并且查到特定后缀名的文件
# def gci(filepath):
#     files = os.listdir(filepath)
#     for f1 in files:
#         fi_d = os.path.join(filepath,f1)
#         if os.path.isdir(fi_d):
#             gci(fi_d)
#         else:
#             ffile = os.path.join(filepath,fi_d)
#             if os.path.isfile(ffile) and os.path.splitext(ffile)[1] == ".py":
#                 print(ffile)
# gci("C:/Users/ZhouTao/PycharmProjects/python-study/data_mysql")

# print(os.path.join(filepath,fi_d))

#3查找目录下所有文件，并且查到特定后缀名的文件,并且统计出这些文件一共多少行
linecount=[]
def gci(filepath):
    files = os.listdir(filepath)
    global linecount
    for each_files in files:
        real_file = os.path.join(filepath,each_files)
        if os.path.isdir(real_file):
            gci(real_file)
        else:
            if os.path.isfile(real_file) and os.path.splitext(real_file)[1] == ".py" :
                with open(real_file,"r",encoding="utf8") as rfile:
                    filelines =len(rfile.readlines())
                    linecount.append(filelines)

gci("C:/Users/ZhouTao/PycharmProjects/python-study/")

print(linecount)
s=0
for i in linecount:
    s+=i

print(s)