from PIL import Image, ImageFilter

im = Image.open('F:\\图片\\qq名片\\1.jpg')
w,h = im.size
print('%s*%s' % (w,h))

im1 = im.filter(ImageFilter.GaussianBlur(radius=1))
im1.save('F:\\图片\\qq名片\\1A.jpg',"JPEG")

im.thumbnail((50, 50))
print('resize  image to:%s*%s' % (50,50))
im.save('F:\\图片\\qq名片\\11AT.jpg',"JPEG")
