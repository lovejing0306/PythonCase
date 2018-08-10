# coding=utf-8

import threading
import time

# 使用threading的方式创建线程

# 为线程定义一个函数（线程函数）
def print_time(thread_name, count, delay):
    """
        时间输出
    """
    print('start......')
    i = 0
    while i < count:
        time.sleep(delay)
        i += 1
        print('%s : %s' % (thread_name, time.ctime(time.time())))

thread_1 = threading.Thread(target=print_time, args=('thread_1', 5, 2))
thread_2 = threading.Thread(target=print_time, args=('thread_2', 5, 2))

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

print('退出主线程')


# 使用类的方式创建线程

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("开始线程：" + self.name)
        print_time(self.name, self.counter, 2)
        print ("退出线程：" + self.name)

# 创建新线程
thread_3 = myThread(3, 'thread_3', 5)
thread_4 = myThread(4, 'thread_4', 5)

thread_3.start()
thread_4.start()

thread_3.join()
thread_4.join()

print('退出主线程')