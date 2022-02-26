import cv2
import os


dream_name = 'starry_night'
dream_path = 'dream/{}'.format(dream_name)

fourcc = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter('{}.mp4'.format(dream_name),fourcc, 25.0, (1280,720))

dream_length = len(os.listdir(dream_path))

for i in range(dream_length):
    repeat = 20 # Repeat the first frame 20 times.
    if i != 0:  
        repeat = 1
    for j in range(repeat):    
        img_path = os.path.join(dream_path,'img_{}.jpg'.format(i))
        print(img_path)
        frame = cv2.imread(img_path)
        out.write(frame)
out.release()    