# ##########################2.collections############################# #
# 是python内建的一个集合模块，提供了许多有用的模块
# ################################################################# #
import contextlib
from contextlib import contextmanager
# 1.with 可以方便的使用资源，不必担心资源没有关闭
with open('./a.txt','r') as f:
    f.read()

# 2.只要上下文管理通过__enter__和__exit__两个方法实现的，就可以用with
class query(object):
    def __init__(self,name):
        self.name = name
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print("error")
        else:
            print("end")
    def query(self):
        print("queue info about %s..."%self.name)


with query('Bob') as q:
    q.query()

# 3.contextmanager 可以简化
# 保姆阿姨 帮忙加头尾
# class Query2(object):
#     def __int__(self,name):
#         self.name = name
#     def query(self):
#         print("queue info about %s..."%self.name)

# @contextmanager
# def create_query(name):
#     print("begin")
#     q = Query2(name)
#     yield q
#     print("end")
#
# with create_query("bob") as q:
#     q.query()

@contextmanager
def tag(name):
    print("<{}>".format(name))
    yield
    print("</{}>".format(name))

with tag("h1"):
    print("hello")
    print("world")

## 4.closing
#  如果一个对象没有实现上下文，就不能用with语句，可以使用closeing来吧对象变为上下文对象
# with使用urlopen()
from contextlib import closing
from urllib.request import urlopen
with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)