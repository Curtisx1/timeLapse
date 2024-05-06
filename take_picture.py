import cv2
import datetime
import time
import json

def take_picture(count, cap):
    grabbed, frame = cap.read()
    cv2.waitKey(1)
    time.sleep(0.3)  # Wait 300 milliseconds
    image_path = f'D:/dev/timeLapse/pictures/capture{count}.png'
    cv2.imwrite(image_path, frame)
    cv2.destroyAllWindows()  # Close the OpenCV window
    return image_path

if __name__ == "__main__":
    cap = cv2.VideoCapture(1)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
 
    with open('count.json', 'r') as f:
        data = json.load(f)
    count = data['count'] + 1

    try:
        while True:
            image_path = take_picture(count, cap)
            print(f"Image captured: {image_path}")
            count += 1
            time.sleep(60)
            
            # Update the JSON file after each capture
            with open('count.json', 'w') as f:
                json.dump({'count': count}, f)

    except KeyboardInterrupt:
        print("Image capture process interrupted.")
    finally:
        cap.release()
        cv2.destroyAllWindows()

    print("Count value updated in the JSON file.") 