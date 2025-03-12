import cv2
import pytesseract as pt 

pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image = cv2.imread('./assets/plate2.jpg')
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

plateText = pt.pytesseract.image_to_string(grayImage)

cv2.imshow('Plate', grayImage)

print(plateText)

cv2.waitKey(0)