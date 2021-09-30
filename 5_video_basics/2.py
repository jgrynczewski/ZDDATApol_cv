# Zapisywanie
# Potrzebujemy trzech linii, żeby zapisac stream do pliku.
import cv2
cap = cv2.VideoCapture(0)

# fps = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
# print(fps) cos nie działa

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_size = (width, height)
fps = 20
print(frame_size)
# Tworzymy obiekt, do którego będziemy pisać
writer = cv2.VideoWriter(
    'mysupervideo.mp4',
    cv2.VideoWriter_fourcc(*'DIVX'),
    fps,
    frame_size
)  # drugi parametr jest ważny. To kodek, którego użyjemy do zakodowania streamu (w
# pliku binarnym). Który kodek wybrać ? W linku do dokumentacji jest trochę.
# https://docs.opencv.org/master/dd/d43/tutorial_py_video_display.html
# W zależności od tego na jakim systemie pracujemy użyjemy innych
# kodeków.
# Na Ubuntu, Fedora lub MacOS - XVID
# Windows - DIVX
# Trzeci parametr - częstość próbkowania, ile klatek na sek. zapisujmy
# Ograniczeni jesteśmy możliwościami naszej kamery (pewnie około 30 fps)
# bezpiecznie wybrać coś pomiędzy 20 i 30, wybieram 20.
# Możemy sprawdzić jaka jest częstość próbkowania naszej kamery
# fps = int(cap.get(cv2.CAP_PROP_FRAME_COUNT) - u mnie cos nie dziala
# Czwarty parametr to krotka zawierająca szerokość i wysokość
# zapisywanego obrazu (rozdzielczość)
# No i teraz po wczytaniu obrazu z kamery chcemy ten obraz zapisywać
# za pomocą właśnie stworzonego obiektu.

while True:
    ret, frame = cap.read()

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Operations (tzn. tutaj wykonujemy jakieś rysunki na obrazie)
    # No i zapisujemy.
    writer.write(frame)  # no i teraz trzeba pamiętać jeszcze
    # o zwolnieniu na samym końcu również writera

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
writer.release()
cv2.destroyAllWindows()
