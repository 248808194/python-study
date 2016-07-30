import memcache
mc = memcache.Client(['112.124.102.118:12000'], debug=True, cache_cas=True)
# mc.servers

v = mc.gets('product_count')
mc.cas('product_count', "111")
# ...
# 如果有人在gets之后和cas之前修改了product_count，那么，下面的设置将会执行失败，剖出异常，从而避免非正常数据的产生
mc.cas('product_count', "899")