import cv2
import matplotlib.pyplot as plt
img = cv2.imread('lion.jpg')
(h, w) = img.shape[:2]
angle = 50       
scale = 0.5      
center = (w // 2, h // 2)  
rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
rotated = cv2.warpAffine(img, rotation_matrix, (w, h))
rotated_rgb = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)
plt.imshow(rotated_rgb)
plt.axis('off')
plt.show()
