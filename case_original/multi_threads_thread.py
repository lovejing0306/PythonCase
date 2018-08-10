# coding=utf-8

import _thread as thread
import time

# 使用thread的方式创建线程

# 为线程定义一个函数（线程函数）
def print_time(thread_name, delay):
    """
        时间输出
    """
    print('start......')
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print('%s : %s' % (thread_name, time.ctime(time.time())))

thread.start_new_thread(print_time, ('thread_1', 2))
thread.start_new_thread(print_time, ('thread_2', 4))
# 暂时不太清楚为什么只有加while才可以执行
while 1:
    pass