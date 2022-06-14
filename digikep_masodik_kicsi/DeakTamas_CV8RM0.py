import cv2
import numpy as np

# kep betoltese
img = cv2.imread('hk_flower.jpg', cv2.IMREAD_COLOR)
# cv2.imshow('image', img)

# a szirmok kep betoltese
img2 = cv2.imread('hk_flower_szirom.png', cv2.IMREAD_GRAYSCALE)
# cv2.imshow('A masik',img2)

# szurkearnyalatos kulonallo csatornakra bontas
b, g, r = cv2.split(img)

# voros kuszobolese
r_th = np.ndarray(r.shape, np.uint8)
r_th.fill(0)
r_th[r > 155] = 255
# zold kuszoboles
g_th = np.ndarray(g.shape, np.uint8)
g_th.fill(0)
g_th[g > 154] = 255
# kek kuszoboles
b_th = np.ndarray(b.shape, np.uint8)
b_th.fill(0)
b_th[b > 153] = 255

# a kuszobolesekkel eloallitott csatornakbol a maszk letrehozasa
mask_th = cv2.bitwise_and(r_th, g_th)
res_th = cv2.bitwise_and(mask_th, b_th)
cv2.imshow('mask', res_th)

# abszolut kulonbseg kep, es L1 ertek
absdiff = cv2.absdiff(img2, res_th)
cv2.imshow('absdiff', absdiff)
print("Az L1 norma értéke: ")
print(cv2.norm(absdiff / 255, cv2.NORM_L1))

# az eredeti csatornak maszkolasa
res_bgr = cv2.merge([cv2.bitwise_and(b, res_th), cv2.bitwise_and(g, res_th), cv2.bitwise_and(r, res_th)])
cv2.imshow('res_segm', res_bgr)

cv2.imwrite("res_segm.png", res_bgr)

cv2.waitKey(0)
cv2.destroyAllWindows()