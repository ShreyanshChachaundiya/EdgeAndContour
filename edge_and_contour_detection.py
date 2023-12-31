import cv2
import matplotlib.pyplot as plt
# Open the image
img = cv2.imread('/content/img.jpg')
# Apply Canny
edges = cv2.Canny(img, 100, 200, 3, L2gradient=True)
plt.figure()
plt.title('Spider')
plt.imsave('/content/img.jpg', edges, cmap='gray', format='png')
plt.imshow(edges, cmap='gray')
plt.show()

# Import OpenCV
import cv2
from google.colab.patches import cv2_imshow

# Load image
image = cv2.imread('/content/img.jpg')

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Find Canny edges
edged = cv2.Canny(gray, 30, 200)

# Find contours
contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Print number of contours found
print("Number of Contours found = " + str(len(contours)))

# Draw all contours
cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

# Display images
cv2_imshow(edged)
cv2_imshow(image)

