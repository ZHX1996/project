#coding:utf-8
import struct

def is_bmp(s):
	f = open(s,'rb')
	s = f.read(30)
	print(s)
	s_30 = struct.unpack('<ccIIIIIIHH', s)
	print (s_30)
	if s_30[0] + s_30[1] != b'BM':
		print('不是bmp文件')
	else:
		print('是bmp文件')
		print('文件大小为:%d字节' % s_30[2])
		print('分辨率为:%d*%d' % (s_30[6], s_30[7]))
		print('颜色数为:%d' % s_30[9])
	
is_bmp('F:\\图片\\大学\\13#634\\1.bmp')
print('\n')
is_bmp('F:\\图片\\qq名片\\1.jpg')