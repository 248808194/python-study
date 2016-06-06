#coding:utf-8
list1 = [100,12,3,4525,46,5,76,8,2,31,23,4,5] #定义一个列表list1
print  list1 #打印出这个列表
i = 1 #先定义i=1
lenlist = len(list1)#lenlist计算出list1长度
tmp = list1[0] #假定一个临时的最大值为list1第一个元素
while (i < lenlist): #按次序比较，当i小于这列表长度时候，条件成立进入循环
    print "tmp = %d list1[%d]=%d" % (tmp, i, list1[i])#打印出当前tmp值，当前处于list1列表第几个元素，值为多少
    if (tmp < list1[i]): #判断当假定的tmp值咸鱼当前list[i]元素的时候，将tmp值替换为list1[i]值，
        tmp = list1[i]
    i+=1 #将i+1
print "max value = %d" %tmp #打印出最大值