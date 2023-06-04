# ##########################1.datatime############################# #
# datatime 是python 处理日期和时间的标准库
# ################################################################### #
from datetime import datetime,timedelta
# 获得当前日期和时间
now = datetime.now()
print(now)
# 获得指定日期和时间
dt = datetime(2015,4,19,12,20)
print(dt)
# 转化为时间戳
#  把1970年1月1日0点0分0秒UTC时区成为epoch time记为0
# python 中的时间戳    是秒为单位
# java和javascript 是以毫秒为单位
dt = dt.timestamp()
print(dt)

# datastamp 转化为 时间
print(datetime.fromtimestamp(dt))

# UTC时间
print(datetime.utcfromtimestamp(dt))
# 把字符串转化为data
# cday = datetime.strftime("2015-6-1 18:19:59",'%Y-%m-%d %H:%M:%S')
# print(cday)
# 时间加减
now = datetime.now()
print(now+timedelta(days=2))

# 转化时区
from datetime import datetime,timedelta,timezone
tz_utc_8 = timezone(timedelta(hours=8))
now = datetime.now()
# dt = datetime.datetime(2015, 5, 18, 17, 2, 10, 871012)
dt = now.replace(tzinfo=tz_utc_8)
print(dt)

# 时区转化
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)

bj_dt =utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)

