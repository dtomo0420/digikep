import cv2
import numpy as np

def feladat(img, candy, ca, cb, also, felso):
    # eredeti kép megjelenítése
    # cv2.imshow('Eredeti kep', img)

    # a medián szűrés -> homogénebb kép
    med_filter = cv2.medianBlur(img, 3)
    # cv2.imshow('Median szures eredmenye', med_filter)

    # canny éldetektor
    edges = cv2.Canny(med_filter, also, felso, None, candy, True)

    # az élek megvastagítása
    struct = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (ca, cb))

    # morfológiai dilatáció
    segment_filtered = cv2.dilate(edges, struct, iterations=1)
    # cv2.imshow('Morf', segment_filtered)

    # rgb színcsatornákra bontás
    segment_filtered_rgb = cv2.merge([segment_filtered, segment_filtered, segment_filtered])

    # rgb élkép invertálása
    segment_filtered_negativ = np.invert(segment_filtered_rgb)

    # logikai összefűzés
    result = cv2.bitwise_and(segment_filtered_negativ, med_filter)
    return result

# színes kép beolvasása
img = cv2.imread('input.jpg', cv2.IMREAD_COLOR)

elso = feladat(img, 5, 3, 3, 1700, 2500)
masodik = feladat(img, 3, 3, 3, 130, 250)
harmadik = feladat(img, 3, 3, 5, 150, 180)

cv2.imshow("Elso lehetoseg", elso)
cv2.imshow("Masodik lehetoseg ", masodik)
cv2.imshow("Harmadik lehetoseg", harmadik)

cv2.imwrite("output.jpg", masodik)

cv2.waitKey(0)
cv2.destroyAllWindows()
