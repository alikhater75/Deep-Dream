'''
Some info on various layers, so you know what to expect
depending on which layer you choose:

layer 1: wavy
layer 2: lines
layer 3: boxes
layer 4: circles
layer 5: eyes.
layer 6: dogs, bears, cute animals.
layer 7: faces, buildings
layer 8: fish begin to appear, frogs/reptilian eyes.
layer 10: Monkies, lizards, snakes, duck

Choosing various parameters like num_iterations, rescale,
and num_repeats really varies on which layer you're doing.


We could probably come up with some sort of formula. The
deeper the layer is, the more iterations and
repeats you will want.

Layer 3: 20 iterations, 0.5 rescale, and 8 repeats is decent start
Layer 10: 40 iterations and 25 repeats is good.
'''
from deepdreamer import model, load_image, recursive_optimize
import numpy as np
import PIL.Image
import cv2
import os
import random

dream_name = 'starry_night'

# HD frames: 1280x720
x_size = 1280
y_size = 720


# Adding some randomaiztion, Feel free to play with these numbers.
layers_subset_1 = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 7, 7, 8, 9, 10 , 11, 10]
layers_subset_2 = [0, 1, 2, 3]
layers_subset_3 = [4, 4, 7, 5, 5, 6, 7]
layers_subset_4 = [7, 8, 9, 10, 11]

layers = random.choice([layers_subset_1, layers_subset_2, layers_subset_2,  layers_subset_2, layers_subset_3, layers_subset_4, layers_subset_4])

# Use these to modify the general colors and brightness of results.
# results tend to get dimmer or brighter over time, so you want to adjust this over time.
# +1, +2 is slowly dimmer
# +3, +4, +5 is slowly brighter
red = random.choice([1, 2, 3, 4, 5])
green = random.choice([1, 2, 3, 4, 5])
blue = random.choice([1, 2, 3, 4, 5])


start = 0
max_count = 1800 # Number of frames you want. This makes a 60seconds 30FPS video. 

for i in range(start, max_count):
    if i % 60 == 0 : # Change paramters every 60 frames
        layers = random.choice([layers_subset_1, layers_subset_2, layers_subset_3, layers_subset_4])
        red = random.choice([1, 2, 3, 4, 5])
        green = random.choice([1, 2, 3, 4, 5])
        blue = random.choice([1, 2, 3, 4, 5])
        
    num_iterations = random.choice([15, 15, 20])
    layer_number = random.choice(layers)
    layer_tensor = model.layer_tensors[layer_number]
    
    if os.path.isfile('dream/{}/img_{}.jpg'.format(dream_name, i+1)):
        print('{} already exists, continuing along...'.format(i+1))

    else:
        img_result = load_image(filename='dream/{}/img_{}.jpg'.format(dream_name, i))

        # this impacts how quick the "zoom" is
        x_trim = 2
        y_trim = 1

        img_result = img_result[0+x_trim:y_size-y_trim, 0+y_trim:x_size-x_trim]
        img_result = cv2.resize(img_result, (x_size, y_size))

        # Use these to modify the general colors and brightness of results.
        # results tend to get dimmer or brighter over time, so you want to
        # manually adjust this over time.


        img_result[:, :, 0] += red  # reds
        img_result[:, :, 1] += green  # greens
        img_result[:, :, 2] += blue # blues

        img_result = np.clip(img_result, 0.0, 255.0)
        img_result = img_result.astype(np.uint8)

        img_result = recursive_optimize(layer_tensor=layer_tensor,
                                        image=img_result,
                                        num_iterations=num_iterations,
                                        step_size=1.0,
                                        rescale_factor=0.7,
                                        num_repeats=1,
                                        blend=0.2)

        img_result = np.clip(img_result, 0.0, 255.0)
        img_result = img_result.astype(np.uint8)
        result = PIL.Image.fromarray(img_result, mode='RGB')
        result.save('dream/{}/img_{}.jpg'.format(dream_name, i+1))
