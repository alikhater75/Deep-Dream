# Deep Dream


## Introduction
**Deep dream** is a  method we can use to allow a neural network to "amplify" the patterns it notices in images, What happens is that the neural network sees small traces of the patterns in the image and we merely amplify the patterns using the gradient.

When you do this, you will generally do it on a specific layer at the time. Initial layers in a convolutional neural network, for example, will often see straight lines. As you progress, you will see squares/corners, then maybe some circles, then things will get a bit more advanced, depending on what your network was trained on. In our case, we're going to use the inception model, which means we're likely to see things like eyes, faces, fur, buildings, and various animals as we get deeper into the layers and allow the model to run wild.

## How does it work?

We are using **Inception5h** model which was designed to classify images.

During the classification process we are providing input images and using **gradient descent** to adapt weights to the images through filters.

**DeepDream** algorithm does the opposite. It adapts the input images to match the network weights with **gradient ascent** which results in visualizing network filters on the input images giving them psychodelic look.


## Example

Here's an example of a deep dream that I created. I find that starting with one of van gogh best paintings is fun, but you can start with anything you want, including random noise. The starting image in this case was The Starry Night:

![img_0](https://user-images.githubusercontent.com/48808661/155849392-f3faf0bd-2400-4baf-a38a-ba0685ca5d37.jpg)

After some iterations of a dream:

![img_863](https://user-images.githubusercontent.com/48808661/155849375-be381d26-65af-41c1-9297-300d37af2970.jpg)


Pretty neat! I think it certainly makes fascinating art.

## Deep dream movies?

While you could easily play with just this for days, another fun thing to do is to make deep dream movies just like this one. This is a bit more of a challenge to do, but the results are pretty neat!


![Alt Text](https://i.giphy.com/media/A2pobmsg2laVv3oiBb/giphy.webp)

## Usage

After cloning this repo, Create new folder with the name of the dream you want. And put your image in that folder and name it img_0.jpg. To make the frames run:
    
    python3 dream_frames.py 

To make a video of those frames:

	python3 dream_video.py



## References

https://github.com/Hvass-Labs/TensorFlow-Tutorials/blob/master/14_DeepDream.ipynb
