# Przechwytywanie streamu kamery
import cv2
cap = cv2.VideoCapture(0)

# Rzutujemy na int, żeby uniknąć nieprzyjemności
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(width)
print(height)

while True:
    ret, frame = cap.read()
    # 2
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
