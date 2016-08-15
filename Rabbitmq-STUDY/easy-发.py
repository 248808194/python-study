import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(host="127.0.0.1")) #创建连接
channel = connection.channel() #创建发消息的频道
channel.queue_declare(queue="hello") #如果不存在回去定义hello队列
channel.basic_publish(exchange="",routing_key="hello",body="hello world") #往hello这个队列中发送helloworld数据
print("[x] Sent hello world")
connection.close()
