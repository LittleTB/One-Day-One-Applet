'''将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。'''

# 引入Pillow
from PIL import Image, ImageDraw, ImageFont, ImageColor
def add_num(img):
    # 创建一个Draw对象
    draw = ImageDraw.Draw(img)
    # 创建一个 Font
    myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=40)
    fillcolor = ImageColor.colormap.get('red')
    width, height = img.size
    draw.text((width-30, 0), '2', font=myfont, fill=fillcolor)
    img.save('E:/文档/result.jpg', 'jpeg')
    return 0
if __name__ == '__main__':
    image = Image.open('E:/文档/test.jpg')
    add_num(image)