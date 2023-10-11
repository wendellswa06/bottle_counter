import cv2
from ultralytics import YOLO
import threading

video_file1 = 'test.mp4'
video_file2 = 0

model1 = YOLO('yolov8l.pt')
model2 = YOLO('yolov8s.pt')

def run_tracker_in_thread(filename, model, file_index):
    
    video = cv2.VideoCapture(filename)
    while True:
        ret, frame = video.read()
        
        if not ret:
            break
        results = model.track(frame, persist=True)
        print(results)
        res_plotted = results[0].plot()
        cv2.imshow("Tracking_Stream_" + str(file_index), res_plotted)
        
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    video.release()
    
tracker_thread1 = threading.Thread(target=run_tracker_in_thread, args=(video_file1, model1, 1), daemon=True)
tracker_thread2 = threading.Thread(target=run_tracker_in_thread, args=(video_file2, model2, 2), daemon=True)

tracker_thread1.start()
tracker_thread2.start()

tracker_thread1.join()
tracker_thread2.join()

cv2.destroyAllWindows()
