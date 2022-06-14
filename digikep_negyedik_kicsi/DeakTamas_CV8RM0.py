import cv2
import numpy as np

def hsv_segment(interval_H, interval_S, interval_V):
    global imgHSV

    minHSV = np.array([interval_H[0], interval_S[0], interval_V[0]])
    maxHSV = np.array([interval_H[1], interval_S[1], interval_V[1]])
    segmented = cv2.inRange(imgHSV, minHSV, maxHSV)

    # rgb felbontás
    segmented_rgb = cv2.merge([segmented, segmented, segmented])

    return segmented_rgb


# eredeti kép betöltése
img = cv2.imread('PalPant_800.jpg', cv2.IMREAD_COLOR)

# simítás az eredeti képen
blurred = cv2.GaussianBlur(img, (3, 3), sigmaX=2.0, sigmaY=2.0)
# BGR->HSV
imgHSV = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

# szegmentálás HSV színtartományon
segmented_rgb = hsv_segment((101, 113), (8, 140), (129, 205))
# cv2.imshow("segmented_rgb", segmented_rgb)

# maszk és eredeti összeolvasztása
mask_color = cv2.bitwise_and(segmented_rgb, img)
# cv2.imshow("mask_color", mask_color)

# az invertált maszk és eredeti összeolvasztása -> szürke
mask_inv = cv2.bitwise_not(mask_color)
background_color = cv2.bitwise_and(mask_inv, img)
background = cv2.cvtColor(background_color, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Background', background)
alma = cv2.merge([background, background, background])

result = cv2.add(alma, mask_color)
# cv2.imshow('Result', result)

cv2.imwrite('output.jpg', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
