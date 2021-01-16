# -*- coding: utf-8 -*-
# 读取/显示/保存图片
import cv2
# 图片读取
i=cv2.imread("./lena.jpg", cv2.IMREAD_UNCHANGED)
print("the img array is :\n", i)
print(10*"##")

# 图片显示
print("the arr shape is:\n", i.shape)
cv2.imshow("Demo",i)
rtval = cv2.waitKey(0)
print(10*"##")
print("input key acaii no is %d"%rtval)
cv2.destroyAllWindows()

# 图像特定像素点值改变
pix_v_before = i.item((100,100,0))
print("(100,100) value before: \n", pix_v_before)
print(10*"##")
i.itemset((100,100,0),255)
print("(100,100) value after: \n", i.item((100,100,0)))

# 新图像保存
cv2.imwrite("./lesson1.jpg",i, [int( cv2.IMWRITE_JPEG_QUALITY), 95])
