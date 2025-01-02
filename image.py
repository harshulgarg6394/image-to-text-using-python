# C:\Users\HP\AppData\Local\Programs\Tesseract-OCR    -> tesseract path in files

import pytesseract as pyt
import cv2

# Specify the Tesseract executable's full path
pyt.pytesseract.tesseract_cmd ="C:\\Users\\HP\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"

# Read the image
img = cv2.imread("image.png")

# Extract text from the image using Tesseract
text = pyt.image_to_string(img)

# Print the extracted text
print(text)

