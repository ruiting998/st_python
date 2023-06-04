# ##########################2.collections############################# #
# 是python内建的一个集合模块，提供了许多有用的模块
# ################################################################# #
import argparse
# 在命令行程序中，经常需要获得命令行参数 python内置的sys.argv保存了完整的参数列表
import sys
print(sys.argv)
source = sys.argv[1]
target = sys.argv[2]

def main():
    parser = argparse.ArgumentParser(
        prog="backop",
        description="Backup MySQl"
    )
    # 定义位置参数
    parser.add_argument('outfile')
    # 定义关键字参数
    parser.add_argument('--host',default="localhost")
    # 此参数必须为int类型:
    parser.add_argument('--port', default='3306', type=int)
    # 允许用户输入简写的-u:
    parser.add_argument('-u', '--user', required=True)
    parser.add_argument('-p', '--password', required=True)
    parser.add_argument('--database', required=True)
    # gz参数不跟参数值，因此指定action='store_true'，意思是出现-gz表示True:
    parser.add_argument('-gz', '--gzcompress', action='store_true', required=False, help='Compress backup files by gz.')

    args = parser.parse_args()
    # 打印参数:
    print('parsed args:')
    print(f'outfile = {args.outfile}')
    print(f'host = {args.host}')
    print(f'port = {args.port}')
    print(f'user = {args.user}')
    print(f'password = {args.password}')
    print(f'database = {args.database}')
    print(f'gzcompress = {args.gzcompress}')