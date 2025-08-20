import cv2
import matplotlib.pyplot as plt
img=cv2.imread("lion.jpg")
print(img.shape)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
edges=cv2.Canny(gray,100,300)
rect=cv2.rectangle(img,(50,50),(100,100),(0,0,255),2)
rect=cv2.circle(img,(180,90),50,(255,0,0),2)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()



