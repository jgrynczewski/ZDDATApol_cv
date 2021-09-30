# Wczytywanie pliku video
import cv2
import time #2

cap = cv2.VideoCapture('mysupervideo.avi')
# Zwraca None, a nie błąd jeżeli plik nie istnieje
# dlatego sprawdzamy
if not cap.isOpened(): # jeżeli plik nie może zostać otwarty oznacza to, że go nie ma lub używamy złego kodeka
    # tzn. zostało zapisany w złym kodowaniu
    print("Error file not found or wrong codec used.")

while cap.isOpened():
    ret, frame = cap.read()

    if ret:  # jeżeli coś zwrócono co oznacza
        # że wideo wciąż jest odtwarzane.

        # writer 20 fps #2
        time.sleep(1/20)  # 2
        cv2.imshow('frame', frame)

        if cv2.waitKey(10) & 0xFF == 27:
            break
    else:
        break  # jeżeli już nic nie zwróciło
        # wychodzimy, bo już wideo się skonczyło

cap.release()
cv2.destroyAllWindows()

# Jak to uruchomimy, przekonamy się że wideo
# zostało odtworzone w przyśpieszeniu. Ponieważ
# domyślnie głównym przeznaczeniem teh funkcji
# nie jest odtwarzanie pliku dla człowieka tylko
# szybkie przeczytanie zawartości pliku/każdej klatki
# i zrobienie czegoś z nią.

# Jezeli chcemy to odtworzyc w normalnym
# tempie musimy dopisać dwie liniki (patrz
# opatrzone #2).