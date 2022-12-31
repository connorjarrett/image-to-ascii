# ❗This is a few years old and no longer maintained

# Image to Ascii Art
Turns an image into ASCII Art.

# How to use
### Requirements
This program requires the `cv2` library. Install by running `pip install opencv-python` in the Terminal. <br/>
More info can be found at the [opencv website](https://pypi.org/project/opencv-python/)

### Setup
There are 2 variables which you can change `debug` and `compression`<br/>
- Setting `debug` to `True`shows extra data like the image in a window and prints image data, This is reccomended off.
- Setting `compression` to `True` will adjust the size of the image based on how big it is to fit smaller screens.

### Running
Before you run the program, you will need to either make sure there is an image in the same directory as the file or replace the line containing `image = cv2.imread(findImages(None), 0)` to contain a specific file name / path (fx. `image = cv2.imread(findImages('Image.JPG'), 0)` or `image = cv2.imread(findImages('C:/Pictures/Image.JPG'), 0)`.
