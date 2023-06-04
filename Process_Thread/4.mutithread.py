# ##########################3.多线程############################# #
# 两个模块：_thread 和 threading
# _thread 是低级模块，threading是高级模块
# ############################################################## #
import time,threading

def loop():
    print("线程%s开始跑..."%threading.current_thread().name)
    n =0
    while n<5:
        n = n+1
        print("线程 %s >>> %s"%(threading.current_thread().name,n))
        time.sleep(1)
    print("线程%s跑完啦..."%threading.current_thread().name)
print("线程{}正在跑".format(threading.current_thread().name))
t = threading.Thread(target=loop,name="LoopThread")
t.start()
t.join()
print("线程{}结束了".format(threading.current_thread().name))
