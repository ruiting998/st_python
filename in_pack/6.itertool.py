# ##########################2.collections############################# #
# 是python内建的一个集合模块，提供了许多有用的模块
# ################################################################# #
import itertools
natuals = itertools.count(1)


# 0.count() 会创建一个无线循环迭代器，一直循环
# ctrl +c 停下
# import itertools
# cs = itertools.count(1)
# for c in cs:
#     print(c)

# 1.cycle() 会创建一个无线循环迭代器，一直循环
# ctrl +c 停下
# import itertools
# cs = itertools.cycle('ABC')
# for c in cs:
#     print(c)

# 2.repeat() 可以限制循环次数
ns = itertools.repeat('A',3)
for n in ns:
    print(n)
# 3. takewhile()函数根据条件判断来截取一个有限的序列
# 循环1次，x从0-10
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x:x<=10,natuals)
list(ns)

# 4.chain()
# 迭代对象串联起来，形成一个更大的迭代器：
for c in itertools.chain('ABC','XYZ'):
    print(c)
# 5.groupby()
# 把迭代器中相邻的重复元素挑出来放在一起:
for key,group in itertools.groupby("AAABBBCCAA"):
    print(key,list(group))
    