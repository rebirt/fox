# -*- coding:utf-8 -*- 
# 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果


from PIL import Image,ImageFont,ImageDraw
import os,sys,random

num = str(random.randint(1,99))
imagepath = os.path.join(sys.path[0],'panda.jpg')
outpath = os.path.join(sys.path[0],'panda_ch.jpg')

def add_num(im,w,h):
    font = ImageFont.truetype('Arial.ttf',50)
    draw = ImageDraw.Draw(im)
    draw.ellipse([x1,x2,x1+30,x2+30],outline = 'red',fill = 'red')
    draw.text((w,h),num,font = font,fill = 'white')
    im.save(outpath,'jpeg')

im = Image.open(imagepath)    
wim,him = im.size      
w = int(0.8*wim)
h = int(0.1*him)
x1,x2 = w,h
