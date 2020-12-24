from process.Processor import Processor
from convert.Converter import Converter
from collect.Collector import Collector
from write.Writer import Writer
from PIL import Image
import os

PATH_RAW = './AutoDoc/data/raw/'
PATH_PROCESSED = './AutoDoc/data/processed/'
FILE_RANGE = [900, 901]
# Image size: 5096, 6600
# Target: 900-1336


def main():

    processor = Processor(PATH_RAW, PATH_PROCESSED)

    for i in range(FILE_RANGE[0], FILE_RANGE[1]):
        file_name = str(str(i) + '.png')
        full_path = PATH_RAW + file_name
        if os.path.exists(full_path):
            processor.process_image(full_path)


main()
