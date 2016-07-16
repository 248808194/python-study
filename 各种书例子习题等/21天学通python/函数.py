# def print_scores(**kw):
#     print("name        scores")
#     print("-----------------")
#     print(kw)
#     for name,score in kw.items():
#         print("%s    %d" %(name,score))
#         print()
#
#
# print_scores(zhoutao=99,wangaiping=100,zhourui=91)
#
#
# data = {
#     "zhoutao":99,
#     "wangaiping":100,
#     "zhourui":91
# }
# print_scores(**data)

# def print_info(name,gender,*,city="shanghai",age):
#     print("person info")
#     print("--------")
#     print("name:",name)
#     print("gender:",gender)
#     print("city:",city)
#     print("age",age)
#     print("end")
#
# print_info("zhoutao","man",age=18)

#
# def hello(greeting,*args):
#     if (len(args) == 0):
#         print("%s!" %(greeting))
#     else:
#         print(args)
#         print("%s,%s!" %(greeting,",".join(args)))
#
#
# hello("hi")
# hello("hi","zhoutao","wangaiping","sara")

# def knight(saying):
#     def inner():
#         return "we are the kings who says %s" %(saying)
#     return inner()
#
# print(knight("zhoutao"))
#
# print()


# def edit_story(words,lambda_func):
#     for word in words:
#         print(lambda_func(word))
#
# stairs = ["wo","niu","bi"]
# #
# # def enliven(word):
# #     return word.capitalize() + "!"
# #
# # edit_story(stairs,enliven)
#
#
# edit_story(stairs,lambda word:word.capitalize() + " !!")

#拆分字符串 将 astr拆分开来分别打印
# astr="zhoutao"
# def foo(astr,func):
#     for a in range(len(astr)):
#         print(func(astr[a]))
#
# foo(astr,lambda a:a.capitalize() + "@")

def foo(a,b):
    while a < b:
        yield a
        a +=1
    else:
        yield "b"


for i in foo(1,10):
    print(i)

    type(object)

