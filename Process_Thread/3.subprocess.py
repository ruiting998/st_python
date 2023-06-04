# ##########################3.子进程########################### #
# 进程间的通信
# Process之间肯定需要通信，mutiprocessing模块包装了底层的机制，Queue，Pipes等多种方式交换数据
##################################################################
from multiprocessing import Process,Queue
import os,time,random
def write(q):
    print("我是写进程 id是：{}".format(os.getpid()))
    for value in ['A','B','C']:
        print('我写{}到queue'.format(value))
        q.put(value)
        time.sleep(random.random())
def read(q):
    print("我是读进程 id是：{}".format(os.getpid()))
    while True:
        value = q.get(True)
        print("我读从queue里读{}"%value)

if __name__ == '__main__':
    # 父进程创建Queue(),并传递给子进程
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    pw.start()
    pr.start()
    #写完了再读
    pw.join()
    # # pr强行终止
    # pr.terminate()
