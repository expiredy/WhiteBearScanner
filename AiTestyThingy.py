import numpy
from PIL import Image
import os
import subprocess


def get_possibly_result_by_sigmoid(data_set):
    return 1 / (1 + numpy.exp(-data_set))


def get_average_contrast(image_for_analyze):
    avg_color_per_row = numpy.average(image_for_analyze, axis=0)
    avg_color = numpy.average(avg_color_per_row, axis=0)
    print(avg_color)
    pixels_data = image_for_analyze.load()
    print(image_for_analyze.size)
    width, height = image_for_analyze.size
    average_transition_contrast = 0
    for y_pixel in range(height):
        for x_pixel in range(width / 2):
            if pixels_data[x_pixel, y_pixel] == avg_color\
                    or pixels_data[-(x_pixel + 1), y_pixel] == avg_color:
                average_transition_contrast += x_pixel
                break
        else:
            height -= 1

    return average_transition_contrast / height


def train_ai(image, *all_bears_on_photo):

    bears_for_analyze = [image.crop(area_with_bear) for area_with_bear in all_bears_on_photo]

    synaptic_weights = 2 * numpy.random.random((3, 1)) - 1
    input_data = [get_average_contrast(bear_image) for bear_image in bears_for_analyze]



#
# image_with_bear = Image.open("TEST IMAGES/withBears/2016-04-25 13-59-32_1411_R.JPG")
# train_ai(image_with_bear, *[(i * 100,  i * 100, (i + 1) * 100,  (i + 1) * 100)
#                             for i in range(min(image_with_bear.size) // 100 - 1)])

subprocess.run("AnyalyzingSpace/image_preprocessor.exe")