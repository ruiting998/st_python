# ##########################1.Pool进程########################### #
# 如果要批量创建子进程
##################################################################
from multiprocessing import Pool
import os,time,random
def long_time_task(name):
    print('跑任务 %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print("子任务%s跑了%0.2f seconds"%(name,(end-start)))
if __name__ == '__main__':
    print("父进程_pid:{}".format(os.getpid()))
    # 设置最多可执行4个进程
    p= Pool(4)
    for i in range(5):
        # Pool 创建进程
        p.apply_async(long_time_task,args=(i,))

    print("等待所有子进程完成")

    # Pool对象调用join()方法前必须调用close
    # close() 之后就不能继续添加新的process
    p.close()
    p.join()
    print("所有子进程已经完成")