import cv2  # Importing cv2 library
import numpy  # Importing library for working with arrays

vGauss = 5  # Define variable for Gaussian blur
vKernel = 5  # Define variable for kernel
original = cv2.imread('monedaMX.png')  # Read image
gris = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)  # Convert image to grayscale
desenfoque = cv2.GaussianBlur(gris, (vGauss, vKernel), 0)  # Apply Gaussian blur
canny = cv2.Canny(desenfoque, 60, 100)  # Edge detection

kernel = numpy.ones((vKernel, vKernel), numpy.uint8)  # Define kernel to 8 bits
cierre = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)  # Remove internal noise (unwanted edges)
contornos, jerarquia = cv2.findContours(cierre.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # Find contours in the closed image
print("Number of coins found: {}".format(len(contornos)))  # Print number of coins found
cv2.drawContours(original, contornos, -1, (255, 0, 0), 2)  # Draw contours on the original image

# Show results
cv2.imshow("Grayscale", gris)  # Image transformed to grayscale
cv2.imshow("Blurred", desenfoque)  # Image with Gaussian blur
cv2.imshow("Canny", canny)  # Edge detection
cv2.imshow("Closing", cierre)  # Removal of internal noise (unwanted edges)
cv2.imshow("Final Result", original)  # Original image with drawn edges
cv2.waitKey(0)  # Wait for a key press to close the windows
