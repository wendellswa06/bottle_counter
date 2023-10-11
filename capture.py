import cv2
import uuid
import os
import time

labels = ['thumbsup', 'hi', 'loveyou', 'livelong']
number_imgs = 20

IMAGES_PATH = os.path.join('images')

if not os.path.exists(IMAGES_PATH):
    os.mkdir(IMAGES_PATH)

for label in labels:
    path = os.path.join(IMAGES_PATH, label)
    if not os.path.exists(path):
        os.mkdir(path)
        
for label in labels:
    cap = cv2.VideoCapture(0)
    print(f'Collecting images for {label}')
    time.sleep(10)
    
    for imgnum in range(number_imgs):
        print(f'Collecting images {imgnum}')
        ret, frame = cap.read()
        imgname = os.path.join(IMAGES_PATH, label, label+'.'+f'{str(uuid.uuid1())}.jpg')
        cv2.imwrite(imgname, frame)
        cv2.imshow('frame', frame)
        
        time.sleep(2)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
    