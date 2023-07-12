import cv2
import os
from moviepy.editor import VideoFileClip
 
def get_duration(filename):
    clip = VideoFileClip(filename)
    return clip.duration


print(cv2.__version__)

filepath = './14842800001.avi'
video = cv2.VideoCapture(filepath)

if not video.isOpened():
    print("Could not Open : ", filepath)
    exit(0)

length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
fps = video.get(cv2.CAP_PROP_FPS)
frame = 10
print("length :", length)
print("fps :", fps)


try:
    if not os.path.exists(filepath[:-4]):
        os.makedirs(filepath[:-4])
except OSError:
    print ('Error: Creating directory. ' +  filepath[:-4])

count = 0

while(video.isOpened()):
    if length <= (fps//frame) * (count + 1):
        break
    ret, image = video.read()
    if(int(video.get(1)) % (fps//frame) == 0): #앞서 불러온 fps 값을 사용하여 1초마다 추출
        cv2.imwrite(filepath[:-4] + "/frame%d.jpg" % count, image)
        print('Saved frame number :', str(int(video.get(1))))
        count += 1
    
        
video.release()