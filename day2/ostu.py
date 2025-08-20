import cv2
import matplotlib.pyplot as plt
img = cv2.imread('lion.jpg', cv2.IMREAD_GRAYSCALE)
ret, otsu_thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

plt.subplot(1, 2, 2)
plt.imshow(otsu_thresh, cmap='gray')
plt.title("Otsu's Thresholding")
plt.axis('off')

plt.show()