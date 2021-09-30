# Pisanie na kamerze live interaktywnie
import cv2

# Pierwsze kliknięcie wskazuje na
# górny prawy róg prostokąta
# Drugie na dolny lewy róg prostokąta
# i rysuje prostoką
# Trzecie resetuje obraz do stanu
# początkowego

# Callback function rectangle
def draw_rectangle(event, x, y, flags, param):
    global pt1, pt2, top_left_clicked, bottom_right_clicked

    if event == cv2.EVENT_LBUTTONDOWN:

        # jeżeli jeszcze w ogóle nie kliknąłem
        if not top_left_clicked:
            pt1 = (x, y)
            top_left_clicked = True

        elif not bottom_right_clicked:
            pt2 = (x, y)
            bottom_right_clicked = True

        # reset the rectangle
        elif top_left_clicked and bottom_right_clicked:
            pt1 = (0, 0)
            pt2 = (0, 0)
            top_left_clicked = False
            bottom_right_clicked = False


# Global variables
pt1 = (0, 0)
pt2 = (0, 0)
top_left_clicked = False  # Dwa trackery
bottom_right_clicked = False

# Connect to the callback
cap = cv2.VideoCapture(0)
cv2.namedWindow('Test')
cv2.setMouseCallback('Test', draw_rectangle)

while True:
    ret, frame = cap.read()

    # Drawing on the frame based on the
    # gloabal variables
    if top_left_clicked:
        cv2.circle(
            frame,
            center=pt1,
            radius=5,
            color=(0, 0, 255),
            thickness=-1
        )
    if top_left_clicked and bottom_right_clicked:
        cv2.rectangle(
            frame,
            pt1,
            pt2,
            (0, 0, 255),
            3
        )
    cv2.imshow('Test', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
