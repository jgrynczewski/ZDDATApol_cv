import cv2
import numpy as np


def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(
            blank_img,
            center=(x, y),
            radius=10,
            color=(0, 255, 0),
            thickness=-1
        )

blank_img = np.zeros(shape=(512, 512, 3), dtype=np.int8)

cv2.namedWindow(winname="window1")
cv2.setMouseCallback('window1', draw_circle)

while True:
    cv2.imshow("window1", blank_img)
    if cv2.waitKey(1) & 0xFF == 27:
        break


cv2.destroyAllWindows()
