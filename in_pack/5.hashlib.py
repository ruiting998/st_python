# ##########################2.collections############################# #
# 是python内建的一个集合模块，提供了许多有用的模块
# ################################################################# #
import hashlib
md5 = hashlib.md5()
md5.update("username".encode('utf-8'))
md5.update("password".encode('utf-8'))
print(md5.hexdigest())
# 可以再通过＋salt 增加账户和密码

