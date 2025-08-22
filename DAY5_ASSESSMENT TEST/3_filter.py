import cv2
import matplotlib.pyplot as plt
img=cv2.imread("sample.jpeg")
blur=cv2.blur(img,(5,5))
gaussian=cv2.medianBlur(img,5)
median=cv2.medianBlur(img, 5)
title=["Origenal","Blur","Gaussiam","Median"]
images=[img,blur,gaussian,median]
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[1])
    plt.axis("off")

plt.show()