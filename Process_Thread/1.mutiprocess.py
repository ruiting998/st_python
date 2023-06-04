# ####################1.多进程##################### #
# mutiprocessing 模块提供了一个进程对象 Process
#
# ################################################ #
import os
from multiprocessing import Process
# 子进程要执行的代码
def run_proc(name):
    print('子进程_name:{}_id:{}'.format(name,os.getpid()))


if __name__ == '__main__':
    print("父进程_id:{}".format(os.getpid()))
    # 1.创建进程
    # p = Process(targrt="要执行的函数名",args=('函数要传入的参数',))
    p = Process(target = run_proc,args=('test',))
    # 2.启动进程
    # 调用start() 函数
    # join可以等待子进程结束之后再继续运行下去，通常用于进程之间的同步
    p.start()
    p.join()
    print("谁是我儿")