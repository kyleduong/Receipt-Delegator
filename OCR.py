import cv2
from PIL import Image
import pytesseract

img_artificial = "pictures/RestaurantReceipt.jpg"
img_real = "pictures/bw_image.jpg"

im_artificial = Image.open(img_artificial)
#im_artificial.show()

im_real = Image.open(img_real)
#im_real.show()

# Path to tesseract executable
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\kyled\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

ocr_result = pytesseract.image_to_string(img_real)
print(ocr_result)