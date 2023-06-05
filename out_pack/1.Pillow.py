# ##########################Pillow################################### #
# PIL:python Imageing Library
#
# ################################################################### #
# 1.PIL 生成绘图方法 生成字母验证码
# import chardet
# from PIL import Image,ImageDraw,ImageFilter,ImageFont
# import random
# # 随机字母：
# def rndChar():
#     return chr(random.randint(65,90))
#
# def rndColor():
#     return(random.randint(64,255),random.randint(64,255),random.randint(64,255))
# def rndColor2():
#     return(random.randint(32,127),random.randint(32,127),random.randint(32,127))
#
# width = 60*4
# height =  60
# # 全白
# image = Image.new('RGB',(width,height),(255,255,255))
# # 创建Font对象
# font = ImageFont.truetype('/Library/Fonts/Arial.ttf',36)
# # 创建Draw对象：
# draw = ImageDraw.Draw(image)
# # 填充每个像素
# for x in range(width):
#     for y in range(height):
#         draw.point((x,y),fill = rndColor())
#
# # 输出文字：
# for t in range(4):
#     draw.text((60*t+10,10),rndChar(),font=font,fill=rndColor2())
#
# # 模糊
# image = image.filter(ImageFilter.BLUR)
# image.save("code.jpg",'jpeg')

# ##########################Chardet################################## #
# chardet：提供了Unicode表示的str和bytes两种数据类型，并且
#          通过encode()和decode()方法转化
# ################################################################### #
import  chardet
print(chardet.detect(b'Hello world'))