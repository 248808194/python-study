#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#%r %s区别

text = "I am %d years old." % 22
print(text)

print("%s" % (text))
print("%r" %(text))

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
# watch that comma at the end. try removing it to see what happens
print (end1 + end2 + end3 + end4 + end5 + end6)
print (end7 + end8 + end9 + end10 + end11 + end12)