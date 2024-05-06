import cv2

def list_cameras(limit=10):
    for index in range(limit):
        cap = cv2.VideoCapture(index)
        if cap.isOpened():
            ret, frame = cap.read()
            if ret:
                cv2.imshow(f'Camera Index: {index}', frame)
                cv2.waitKey(0)  # Press any key to close the window and check next camera
            cap.release()
        else:
            print(f"Camera at index {index} not found.")
    cv2.destroyAllWindows()

list_cameras()