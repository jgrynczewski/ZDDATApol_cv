# Pisanie na kamerze live
import cv2
cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Narysujemy prostokąt na streamie
# o współrzędnych górnego, prawego wierzchołka
x = width // 2
y = height // 2
# i szerokości wysokości
w = width // 4
h = height //4
# najczęściej te parametry są definiowane
# przez jakiś algorytm detekcji

while True:
    ret, frame = cap.read()

    # frame to nasz obraz
    cv2.rectangle(
        frame,
        (x, y),
        (x+w, y+w),
        color=(0, 0, 255),
        thickness=4
    )
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
