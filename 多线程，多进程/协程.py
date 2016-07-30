#携程人为创建出来的


#I/O请求通过携程方式更好

#原理，利用线程分解一个线程，成为多个“微线程”

#类似网页爬虫，爬A页面的时候，不等待继续去爬C,D,E,F页面，等到A页面有数据返回了在去拿A页面的内容
#程序级别实现携程

#安装gevent
#gevent为底层greenlet的上层封装

from gevent import  monkey;monkey.patch_all()
import gevent
import requests

def f(url):
    print("get %s"% url)
    resp = requests.get(url)
    date = resp.text
    print("%d,bytes revice from %s"%(len(date),url))

gevent.joinall(
    [
        gevent.spawn(f,"http://baidu.com"),
        gevent.spawn(f,"http://ttmeiju.com"),
        gevent.spawn(f,"http://www.qq.com"),

    ]

)