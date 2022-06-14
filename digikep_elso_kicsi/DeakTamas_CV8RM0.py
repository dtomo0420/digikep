import cv2
import numpy as np

drawing = False  # amikor le van nyomva ==True
pt1_x, pt1_y = None, None
sugar = 10
# alapertelemzett festo szin (voros)
color = [0, 0, 255]


# eger esemenyek
def line_drawing(event, x, y, flags, param):
    global pt1_x, pt1_y, drawing, sugar, color

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        pt1_x, pt1_y = x, y
        cv2.circle(img, (pt1_x, pt1_y), sugar, color, -1)

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(img, (pt1_x, pt1_y), sugar, color, -1)
            pt1_x, pt1_y = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.circle(img, (pt1_x, pt1_y), sugar, color, -1)


# hatter betoltese
img = cv2.imread('hatter.jpg')
#img = np.ndarray((480,640,3),np.uint8)
#img.fill(255)
cv2.namedWindow('Egyszeru rajzoloprogram')
cv2.setMouseCallback('Egyszeru rajzoloprogram', line_drawing)

while True:
    cv2.imshow('Egyszeru rajzoloprogram', img)
    code = cv2.waitKey(1)

    # kilepes- q es esc billentyukkel
    if code == ord('q'):
        break
    if code == 27:
        break

    # sugar +/-
    if code == ord('+'):
        if sugar <= 95:
            sugar += 5
    if code == ord('-'):
        if sugar >= 10:
            sugar -= 5

    # szin beallitasa
    if code == ord('r'):
        color = [0, 0, 255]
    if code == ord('g'):
        color = [0, 255, 0]
    if code == ord('b'):
        color = [255, 0, 0]
    if code == ord('k'):
        color = [0, 0, 0]
    if code == ord('w'):
        color = [255, 255, 255]

    # hatter alaphelyzetbe allitasa
    if code == ord('t'):
        img = cv2.imread('hatter.jpg')

    # az alkotas mentese
    if code == ord('s'):
        cv2.imwrite("DeakTamas_CV8RM0.png", img)

cv2.destroyAllWindows()