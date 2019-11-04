import random
import threading
import time
from queue import Queue


# 生产者
class Producer(threading.Thread):
    def __init__(self, name, q):
        threading.Thread.__init__(self, name=name)
        self.data = queue

    def run(self):
        for i in range(1000):
            print("生产者正在生产%d!" % i)
            time.sleep(random.randrange(10)/5)
            self.data.put(i)
            print("%d生产完成，已加入队列!" % i)
        print("所有产品生产完成!")


# 消费者类
class Consumer(threading.Thread):
    def __init__(self, name, q):
        threading.Thread.__init__(self, name=name)
        self.data = queue

    def run(self):
        for i in range(1000):
            val = self.data.get()
            print("消费者正在消费%d!" % val)
            time.sleep(random.randrange(10)/4)
            print("%d消费完成，已从队列移除!" % val)
        print("所有产品消费完成!")


queue = Queue()
producer = Producer('Producer', queue)
consumer = Consumer('Consumer', queue)

producer.start()
consumer.start()

producer.join()
consumer.join()
print('所有进程已完成!')
