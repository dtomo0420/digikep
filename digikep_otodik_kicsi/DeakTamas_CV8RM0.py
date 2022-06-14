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
img = cv2.imread('car_numberplate_rs.jpg', cv2.IMREAD_COLOR)

# gauss szűrés (maszkméret, szórás)
blurred = cv2.GaussianBlur(img, (25, 25), sigmaX=13.0, sigmaY=13.0)
imgHSV = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

# kék objektumok szegmentálása
segmented_rgb = hsv_segment((90, 105), (50, 190), (140, 170))

# az eredeti és a szegmentált összefűzése
res = cv2.bitwise_and(img, segmented_rgb)
# cv2.imshow('Szegmentalt', res)

# a már szegmentált kép szürkeárnyalatossá konvertálása, mediánszűrés
gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 7)

# körök detektálása
row = gray.shape[0]
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 18, param1=15, param2=10, minRadius=8, maxRadius=17)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        center = (i[0], i[1])

        radius = i[2]
        cv2.circle(res, center, radius, (0, 255, 255), 4)

cv2.imshow('Eredmeny', res)
cv2.imwrite('output.jpg', res)

cv2.waitKey(0)
cv2.destroyAllWindows()