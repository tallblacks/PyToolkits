# pip install opencv-python
import cv2
import numpy as np

def pencil_sketch(image_path, output_path):
    image = cv2.imread(image_path)

    # Convert an image from BGR color space to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    inverted_gray_image = cv2.bitwise_not(gray_image)

    # Gaussian blur with a kernel size of 21x21
    blurred_image = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)

    inverted_blurred_image = cv2.bitwise_not(blurred_image)
    # The original grayscale image is divided by the inverted blurred image to obtain the pencil sketch effect
    # This process enhances the edges of the image, making it look like it was drawn with a pencil
    # Multiply the value of each pixel by 256 to ensure that the pixel values ​​of the resulting image are between 0 and 255
    pencil_sketch_image = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)
    cv2.imwrite(output_path, pencil_sketch_image)

    cv2.imshow('Pencil Sketch', pencil_sketch_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

input_image_path = '.\images\input\DragonBall.png'
output_image_path = '.\images\output\DragonBall_Sketch.png'
pencil_sketch(input_image_path, output_image_path)