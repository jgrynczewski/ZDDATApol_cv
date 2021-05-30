import cv2

img = cv2.imread('puppy.jpg')
# cv2.imshow("Puppy.jpg", img)

while True:
    cv2.imshow("Puppy.jpg", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
