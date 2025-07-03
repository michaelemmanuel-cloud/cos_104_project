import cv2
import os

image_path = 'Screenshot 2025-07-03 003535.png'
face_haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow("Gray", "gray")
#cv2.waitKey()

Faces = face_haar_cascade.detectMultiScale(gray, 1.1 , 4)

filename = os.path.basename(image_path)

for (x, y, w, h) in Faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 5)
   

cv2.imshow("Faces", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
