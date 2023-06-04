# ##########################4.TreadLocal############################# #
# Threadlocal 为线程提供一个公共区域 让大家访问变量
# ThreadLocal 虽然是全局变量，但是每个线程都能读写自己线程的独立副本，
# ################################################################### #
import threading

local_school = threading.local()
def process_student():
    std = local_school.student
    print('您好，{}这个学生(是线程 {}的变量嘿 )'.format(std,threading.current_thread().name))

def process_thread(name):
    # 咱们设置线程的学生是name
    local_school.student = name
    # 获取一下对不对
    process_student()

t1 =threading.Thread(target=process_thread,args=('Alice',))

t2 =threading.Thread(target=process_thread,args=('Bob',))
t1.start()
t2.start()
t1.join()
t2.join()
