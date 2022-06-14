import numpy as np
import cv2

interval_H = (13, 33)
interval_S = (0, 121)
interval_V = (120, 193)
num = 500

src = cv2.imread('SourceData/crosswalk.jpg', cv2.IMREAD_COLOR)
cv2.imshow('Eredeti', src)

def hsv_segment(interval_H, interval_S, interval_V):
    global imgHSV

    minHSV = np.array([interval_H[0], interval_S[0], interval_V[0]])
    maxHSV = np.array([interval_H[1], interval_S[1], interval_V[1]])
    segmented = cv2.inRange(imgHSV, minHSV, maxHSV)

    return segmented

def main(num):
    global imgHSV

    # zajszures
    bilateral = cv2.bilateralFilter(src, 25, 30, 100)
    # cv2.imshow('Billiteralis szures utan', bilateral)

    imgHSV = cv2.cvtColor(bilateral, cv2.COLOR_BGR2HSV)

    segmented_rgb = hsv_segment(interval_H, interval_S, interval_V)
    # cv2.imshow('segmented', segmented_rgb)

    # konturkereses
    contours, hierarchy = cv2.findContours(segmented_rgb, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # ebben a tombben fogjuk tarolni a komplex alakzatokat
    hull = []

    for i in range(0, len(contours)):
        hull.append(cv2.convexHull(contours[i], False))

        # ahol a kontur altal kozrezart terulet > x -> szinezes
        if num < cv2.contourArea(contours[i]):
             cv2.drawContours(src, hull, i, (0, 0, 255), -1)

        # cv2.drawContours(src, contours, i, (0, 0, 255), -1, cv2.LINE_4)

    cv2.imshow('Eredmeny', src)
    return src


while True:
    code = cv2.waitKeyEx(100)

    if code == ord('q') or code == 27:
        print('Kilepes a programbol')
        break

    if code == 49 or code == 97:
        cv2.destroyAllWindows()
        interval_H = (13, 105)
        interval_S = (0, 121)
        interval_V = (83, 193)
        src = cv2.imread('SourceData/crosswalk.jpg', cv2.IMREAD_COLOR)
        cv2.imshow('Eredeti', src)
        num = 1200
        cv2.imwrite('crosswalk_res.jpg', main(num))
        print('Elso kep')
        print('A szegmentalas a (', interval_H, interval_S, interval_V, ') intervallon tortent HSV szinterben')
        print('A konturteruletre hozott also kuszob erteke:', num)
        print('****************************************')

    if code == 50 or code == 98:
        cv2.destroyAllWindows()
        interval_H = (12, 26)
        interval_S = (0, 44)
        interval_V = (129, 250)
        src = cv2.imread('SourceData/2.jpg', cv2.IMREAD_COLOR)
        cv2.imshow('Eredeti', src)
        num = 220
        cv2.imwrite('2_res.jpg', main(num))
        print('Masodik kep')
        print('A szegmentalas a (', interval_H, interval_S, interval_V, ') intervallon tortent HSV szinterben')
        print('A konturteruletre hozott also kuszob erteke:', num)
        print('****************************************')

    if code == 51 or code == 99:
        cv2.destroyAllWindows()
        interval_H = (5, 25)
        interval_S = (12, 50)
        interval_V = (184, 255)
        src = cv2.imread('SourceData/3.jpg', cv2.IMREAD_COLOR)
        cv2.imshow('Eredeti', src)
        num = 220
        cv2.imwrite('3_res.jpg', main(num))
        print('Harmadik kep')
        print('A szegmentalas a (', interval_H, interval_S, interval_V, ') intervallon tortent HSV szinterben')
        print('A konturteruletre hozott also kuszob erteke:', num)
        print('****************************************')

    if code == 52 or code == 99:
        cv2.destroyAllWindows()
        interval_H = (18, 126)
        interval_S = (4, 14)
        interval_V = (120, 265)
        src = cv2.imread('SourceData/4.jpg', cv2.IMREAD_COLOR)
        cv2.imshow('Eredeti', src)
        num = 350 #200
        cv2.imwrite('4_res.jpg', main(num))
        print('Negyedik kep')
        print('A szegmentalas a (', interval_H, interval_S, interval_V, ') intervallon tortent HSV szinterben')
        print('A konturteruletre hozott also kuszob erteke:', num)
        print('****************************************')

    if code == 53 or code == 101:
        cv2.destroyAllWindows()
        interval_H = (18, 26)
        interval_S = (63, 255)
        interval_V = (159, 245)
        src = cv2.imread('SourceData/5.jpg', cv2.IMREAD_COLOR)
        cv2.imshow('Eredeti', src)
        num = 220
        cv2.imwrite('5_res.jpg', main(num))
        print('Otodik kep')
        print('A szegmentalas a (', interval_H, interval_S, interval_V, ') intervallon tortent HSV szinterben')
        print('A konturteruletre hozott also kuszob erteke:', num)
        print('****************************************')

cv2.destroyAllWindows()