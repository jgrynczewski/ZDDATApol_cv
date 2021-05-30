import cv2
import numpy as np

blank_img = np.zeros(shape=(512, 512, 3), dtype=np.int8)
print(blank_img.shape)

cv2.rectangle(
    blank_img,
    pt1=(350, 0),
    pt2=(510, 150),
    color=(0, 255, 0),
    thickness=2
)

cv2.rectangle(
    blank_img,
    pt1=(200, 200),
    pt2=(300, 300),
    color=(255, 0, 0),
    thickness=2
)

cv2.circle(
    img=blank_img,
    center=(100, 100),
    radius=50,
    color=(0, 0, 255),
    thickness=2
)

cv2.circle(
    img=blank_img,
    center=(400, 400),
    radius=50,
    color=(0, 0, 255),
    thickness=-1
)

cv2.line(
    blank_img,
    pt1=(0, 0),
    pt2=(512, 512),
    color=(255, 0, 255),
    thickness=2
)

font = cv2.FONT_ITALIC

cv2.putText(
    blank_img,
    text="Hello",
    org=(10, 350),
    fontFace=font,
    fontScale=4,
    color=(255, 255, 255),
    thickness=3,
)

vertices = np.array(
    [[100, 300],
    [200, 200],
    [400, 300],
    [200, 400]],
    dtype=np.int32
).reshape(-1, 1, 2)

cv2.polylines(
    blank_img,
    [vertices],
    isClosed=True,
    color=(255, 0, 0),
    thickness=5
)

while True:
    cv2.imshow("Puppy.jpg", blank_img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
