# Automatyczne wskazywanie źródła

import cv2
import numpy as np

# Wczytujemy obraz
road = cv2.imread('road_image.jpg')

# Tworzymy kopię obrazu
road_copy = np.copy(road)

# Pusty obraz na który bedziemy nanosili wynik
print(road.shape[:2])
marker_image = np.zeros(road.shape[:2], dtype=np.int32)

segments = np.zeros(road.shape, dtype=np.uint8)

print(marker_image.shape)
print(segments.shape)

# How to create colors for the marker?
# For this we'll use matplotlib color mappings - qualitative colormaps.
# Let's take tab10)
from matplotlib import cm

print(cm.tab10(0))  # R, G, B, A
print(cm.tab10(0)[:3])  # R, G, B

print(tuple(np.array(cm.tab10(0)[:3])*255))


def create_rgb(idx):
    return tuple(np.array(cm.tab10(idx)[:3])*255)


colors = []
for i in range(10):
    colors.append(create_rgb(i))

print(colors)

# Callback function
# 3 major components:
# global variables, callback functiona, while True loop

# GLOBAL VARIABLES
n_markers = 10  # 0-9
current_marker = 1  # What was the color choice.
# Index position for the list of color.
marks_updated = False  # flag to check if the markers have been
# updated by watershed algorithm


# CALLBACK FUNCTION
def mouse_callback(event, x, y, flags, param):
    global marks_updated

    if event == cv2.EVENT_LBUTTONDOWN:  # drawing two markers on two images
        # Circle (marker) passed to the watershed algorithm later on
        cv2.circle(marker_image, (x, y), 10, current_marker, -1)

        # Circle user sees on the road image
        cv2.circle(road_copy, (x, y), 10, colors[current_marker], -1)

        marks_updated = True


# WHILE TRUE
cv2.namedWindow('Road Image')
cv2.setMouseCallback('Road Image', mouse_callback)

while True:
    cv2.imshow('Watershed Segments', segments)
    cv2.imshow('Road Image', road_copy)

    # CLOSE ALL WINDOWS
    k = cv2.waitKey(1)

    if k == 27:  # ESC
        break

    # CLEARING ALL THE COLORS PRESS (C KEY)
    elif k == ord('c'):
        road_copy = road.copy()
        marker_image = np.zeros(road.shape[:2], dtype=np.int32)
        segments = np.zeros(road.shape, dtype=np.uint8)

    # UPDATE COLOR CHOICE
    elif k > 0 and chr(k).isdigit():  # if the key being entered is greater than 0
        # key is mapped to ascii code. So we transform it back using chr function
        # and check if this key is a digit. If so:
        current_marker = int(chr(k))

    # UPDATE THE MARKERS
    if marks_updated:  # they are updated every time left button is being clicked
        marker_image_copy = marker_image.copy()
        cv2.watershed(road, marker_image_copy)

        segments = np.zeros(road.shape, dtype=np.uint8)

        for color_ind in range(n_markers):
            # COLORING SEGMENTS, NUMPY CALL
            segments[marker_image_copy == color_ind] = colors[color_ind]

cv2.destroyAllWindows()
