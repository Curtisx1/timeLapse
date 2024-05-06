import cv2
import datetime
import os

date = datetime.date.today().strftime('%Y-%m-%d')
path = "D:/dev/timeLapse/pictures"
out_path = "D:/dev/timeLapse"
out_video_name = f'{date}.mp4'

# Create a new directory with today's date
output_dir = os.path.join(out_path, date)
os.makedirs(output_dir, exist_ok=True)

pre_imgs = os.listdir(path)

# Sort the images by their number
pre_imgs.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))
img = []

for i in pre_imgs:
    img.append(os.path.join(path, i))

cv2_fourcc = cv2.VideoWriter_fourcc(*'mp4v')

frame = cv2.imread(img[0])
size = list(frame.shape)
del size[2]
size.reverse()

video = cv2.VideoWriter(os.path.join(output_dir, out_video_name), cv2_fourcc, 120, size)

for i in range(len(img)): 
    video.write(cv2.imread(img[i]))
    print('Processed frame ', i+1, ' of ', len(img), end='\r')

video.release()
print('Outputed video to: ', output_dir)
