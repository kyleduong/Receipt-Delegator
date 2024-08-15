import cv2
from matplotlib import pyplot as plt
import numpy as np
import imutils
from imutils.perspective import four_point_transform
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\kyled\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

def getReceipt():
    # BOUNDING BOX
    #image= cv2.imread("RealRestaurantReceipt.jpg")
    img_orig = cv2.imread("RealRestaurantReceipt.jpg")
    image = img_orig.copy()
    #image = imutils.resize(image, width=500)
    #ratio = img_orig.shape[1] / float(image.shape[1])

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5,5), 0)
    cv2.imwrite("BLURRED.jpg", blur)

    edges = cv2.Canny(blur, 75, 200)

    cnts = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key=cv2.contourArea, reverse = False)

    receiptCnt = None

    for c in cnts:
        # approximate the contour
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        # if our approximated contour has four points, then we can
        # assume we have found the outline of the receipt
        if len(approx) == 4:
            receiptCnt = approx
            break


    # cv2.drawContours(image, [receiptCnt], -1, (0, 255, 0), 2)
    # cv2.imwrite('image_with_outline.jpg', image)
    # cv2.imshow("Receipt Outline", image)
    # cv2.waitKey(0)

    if receiptCnt is None:
        raise Exception(
            (
                "Receipt Outline Not Found"
            )
        )

    receipt = four_point_transform(image, receiptCnt.reshape(4,2) ) # * ratio
    """ * ratio """
    cv2.imwrite('transformed_receipt.jpg', receipt)

    # converts image to gray scale so it's easier to read
    def grayscaletwo(image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gray_image = grayscaletwo(receipt)
    cv2.imwrite("pictures/grayReceipt.jpg", gray_image)

    thresh, im_bw = cv2.threshold(gray_image, 170, 200, cv2.THRESH_BINARY)
    cv2.imwrite("pictures/bw_image.jpg", im_bw)

    options = "--psm 6"
    #text = pytesseract.image_to_string(im_bw, config=options)
    text = pytesseract.image_to_string(im_bw)

    # print("TEXT OUTPUT:")
    # print("==================")
    # print(text)
    # print("\n")

    return text

getReceipt()
# -------------------------------------------------------------------------------------------------------------------------

""" image_file = "RealRestaurantReceipt.jpg"
img = cv2.imread(image_file)

inverted_image = cv2.bitwise_not(img)
cv2.imwrite("pictures/invertedReceipt.jpg",inverted_image)

# converts image to gray scale so it's easier to read
def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray_image = grayscale(img)
cv2.imwrite("pictures/grayReceipt.jpg", gray_image)

thresh, im_bw = cv2.threshold(gray_image, 170, 200, cv2.THRESH_BINARY)
cv2.imwrite("pictures/bw_image.jpg", im_bw)

def noise_removal(image):
    kernel = np.ones((1,1), np.uint8)
    image = cv2.dilate(image, kernel, iterations = 1)
    kernel = np.ones((1,1), np.uint8)
    image = cv2.erode(image, kernel, iterations = 1)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    image = cv2.medianBlur(image, 3)
    return image

# HERE, CHECK TO SEE IF NO_NOISE HELPS OR HURTS OCR READING LEVEL
no_noise = noise_removal(im_bw)
cv2.imwrite("pictures/no_noise.jpg", no_noise)
#cv2.imshow("im_bw", im_bw)
#cv2.imshow("no noise", no_noise)

# HERE, CHECK TO SEE IF THICK OR THIN HELPS OR HURTS OCR READING LEVEL
def thin_font(image):
    image = cv2.bitwise_not(image)
    kernel = np.ones((2,2), np.uint8)
    image = cv2.erode(image, kernel, iterations = 1)
    image = cv2.bitwise_not(image)
    return image

eroded_image = thin_font(no_noise)
cv2.imwrite("pictures/eroded_image.jpg", eroded_image)

def thick_font(image):
    image = cv2.bitwise_not(image)
    kernel = np.ones((2,2), np.uint8)
    image = cv2.dilate(image, kernel, iterations = 1)
    image = cv2.bitwise_not(image)
    return image

dilated_image = thick_font(no_noise)
cv2.imwrite("pictures/dilated_image.jpg", dilated_image)

new = cv2.imread("pictures/RestaurantReceiptMinor.jpg")
#cv2.imshow("Roatated", new)

# STRAIGHTEN THE PICTURE
def getSkewAngle(cvImage) -> float:
    # Prep image, copy, convert to gray scale, blur, and threshold
    newImage = cvImage.copy()
    gray = cv2.cvtColor(newImage, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (9, 9), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Apply dilate to merge text into meaningful lines/paragraphs.
    # Use larger kernel on X axis to merge characters into single line, cancelling out any spaces.
    # But use smaller kernel on Y axis to separate between different blocks of text
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 5))
    dilate = cv2.dilate(thresh, kernel, iterations=2)

    # Find all contours
    contours, hierarchy = cv2.findContours(dilate, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key = cv2.contourArea, reverse = True)
    for c in contours:
        rect = cv2.boundingRect(c)
        x,y,w,h = rect
        cv2.rectangle(newImage,(x,y),(x+w,y+h),(0,255,0),2)

    # Find largest contour and surround in min area box
    largestContour = contours[0]
    print (len(contours))
    minAreaRect = cv2.minAreaRect(largestContour)
    cv2.imwrite("pictures/temp/boxes.jpg", newImage)
    # Determine the angle. Convert it to the value that was originally used to obtain skewed image
    angle = minAreaRect[-1]
    if angle < -45:
        angle = 90 + angle
    return -1.0 * angle
# Rotate the image around its center
def rotateImage(cvImage, angle: float):
    newImage = cvImage.copy()
    (h, w) = newImage.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    newImage = cv2.warpAffine(newImage, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return newImage

# Deskew image
def deskew(cvImage):
    angle = getSkewAngle(cvImage)
    return rotateImage(cvImage, -1.0 * angle)

fixed = deskew(new)
cv2.imwrite("pictures/rotated_fixed.jpg", fixed)
#cv2.imshow("fixed", fixed)


def remove_borders(image):
    contours, heiarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cntsSorted = sorted(contours, key=lambda x:cv2.contourArea(x))
    cnt = cntsSorted[-1]
    x, y, w, h = cv2.boundingRect(cnt)
    crop = image[y:y+h, x:x+w]
    return (crop)

no_borders = remove_borders(no_noise)
cv2.imwrite("pictures/no_borders.jpg", no_borders)


# ADD A THICK WHITE BORDER
color = [255, 255, 255]
top, bottom, left, right = [150]*4
image_with_border = cv2.copyMakeBorder(no_borders, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)
cv2.imwrite("pictures/image_with_border.jpg", image_with_border)
#cv2.imshow("big_borders", image_with_border)

 """








# cv2.imshow("Receipt Outline", image)
# cv2.waitKey(0)

#cv2.imshow("original image", img)
#cv2.waitKey(0)


