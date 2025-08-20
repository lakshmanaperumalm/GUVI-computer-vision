import cv2
import matplotlib.pyplot as plt
img = cv2.imread("lion.jpg")
gaussian = cv2.GaussianBlur(img, (5, 15), 5)
gray = cv2.cvtColor(gaussian, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 300)
threshold, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
plt.imshow(edges, cmap='gray')
plt.axis("off")
plt.title("Canny Edges")
plt.show()