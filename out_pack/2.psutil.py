# ##########################psutil################################### #
# psutil 模块可以进行系统监控
# ################################################################### #
# CPU逻辑数量
import psutil
# cpu的逻辑数量
print(psutil.cpu_count())
# cpu的物理核心
print(psutil.cpu_count(logical=False))
# 统计CPU的用户/系统/空闲时间
print(psutil.cpu_times())
for x in range(10):
    print(psutil.cpu_percent(interval=1,percpu=True))
