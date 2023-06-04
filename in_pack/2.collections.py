# ##########################2.collections############################# #
# 是python内建的一个集合模块，提供了许多有用的模块
# ################################################################# #
# 1.namedtuple
# 创建一个自定义的tuple对象，规定了tuple元素的个数，并且可以用属性而非索引来引用tuple的莫个元素
from collections import namedtuple
Point = namedtuple("Point",['x','y'])
p = Point(1,2)
print(p.x)
print(p.y)
print(isinstance(p,tuple))

# 2.deque  -deque 是双向列表
# list存储数据，按照索引访问元素很快，但是插入和删除就很慢，可以
# 支持appendleft() 和 popleft() 可以向头部添加或者删除元素怒
from collections import deque
q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)

# 3.defaultdict
# 使用dict .如果key不存在，会抛出keyerror错误，如果想要抛出默认值的话 可以用defaultdict
print("# ###################3.defaultdict####################### #")
from collections import defaultdict
dd = defaultdict(lambda :'N/A')
dd ['key1']='abc'
print(dd['key1'])
print(dd['key2'])
print("# ####################################################### #")

# 4.OrderedDict
# 使用dict . Key是无序的，在对dict做迭代时候，我们无法确定key的顺序
#  利用orderdict可以保证key的顺序
#  顺序是根据插入的顺序排序
print("# ###################4.OrderedDict####################### #")
from collections import OrderedDict
d = dict([('a',1),('b',2),('c',3)])
print(d)
d2 = OrderedDict([('a',1),('b',2),('c',3)])
print(d2)
print("# ####################################################### #")

# 5.ChainMap
# chainmap 可以把一组dict串起来并组成一个逻辑上的dict。chainmap本身也是一个dict
# 我们可以用ChainMap实现参数的优先级查找，即先查命令行参数，如果没有传入，再查环境变量，如果没有，就使用默认参数
print("# ###################5.ChainMap####################### #")
from collections import ChainMap
import os,argparse
# 构造缺省参数
default = {
    'color':'red',
    'user':'guest'
}
# 构造命令行参数
parser = argparse.ArgumentParser()
parser.add_argument('-u','--user')
parser.add_argument('-c','--color')
namespace = parser.parse_args()
command_line_args = {k:v for k,v in vars(namespace).items() if v}
combined = ChainMap(command_line_args,os.environ,default)
print('color=%s'% combined['color'])
print('user=%s'%combined['user'])

print("# ####################################################### #")

# 6.Counter
# counter是一个简单的计数器，统计字符出现的个数
print("# ###################5.ChainMap####################### #")
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch]+1
print(c)
c.update('hello')
print(c)
print("# ####################################################### #")