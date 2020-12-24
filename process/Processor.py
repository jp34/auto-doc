from PIL import Image
import numpy as np
import cv2


# Image Pre-processor
class Processor:

    def __init__(self, input_path, output_path, file_range):
        self._input_path = input_path
        self._output_path = output_path
        self._width = 1400
        self._height = 5500
        self._FILE_RANGE = file_range

    def process(self):
        for i in range(self._FILE_RANGE[0], self._FILE_RANGE[1]):
            self.process_image(f"{self._input_path}{i}.jpg")

    @staticmethod
    def process_image(image_path):
        image = Image.open(image_path)
        cv2.utils.dumpInputArray(image)

        width, height = image.size

        ret, thresh = cv2.threshold(image, 127, 255, 0)
        im2, contours, hierarchy = cv2.findContours(thresh, 1, 2)
        cnt = contours[0]
        M = cv2.moments(cnt)
        print(M)

    def crop(self, file):
        north_margin = 900
        south_margin = 200

        w = self._width
        h = self._height
        i = file[:-4]

        original = Image.open(self._input_path + file)
        original.crop((80, north_margin, w, h - south_margin)).save(
            self._output_path + str(i) + '-1.png')
        original.crop((w + 1 + 540, north_margin, 2 * w - 200, h - south_margin)).save(
            self._output_path + str(i) + '-2.png')
        original.crop(((2 * w) + 1 + 545, north_margin, 3 * w - 200, h - south_margin)).save(
            self._output_path + str(i) + '-3.png')
