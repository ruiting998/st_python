# ##########################2.collections############################# #
# 是python内建的一个集合模块，提供了许多有用的模块
# ################################################################# #
import base64
print(base64.b64encode(b'binary\x00string'))
print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))
# 可能出现字符+ / 分别编程-和_
# 可以用urlsafe_b64encode 避免

print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64decode(b'abcd--__'))
