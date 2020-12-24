from PIL import Image
import pytesseract
import os

class Converter:

    def __init__(self, input_path, output_path, file_range):
        self._input_path = input_path
        self._output_path = output_path
        self._file_range = file_range


    def convert(self):
        for i in range(self._file_range[0], self._file_range[1]):
            for j in range(1, 4):
                file_name = str(i) + '-' + str(j) + '.png'
                if os.path.exists(self._input_path + file_name):
                    new_file_name = str(i) + '-' + str(j) + '.txt'
                    self.extract(file_name, new_file_name)


    def extract(self, file_name, new_file_name):
        data = pytesseract.image_to_string(Image.open(self._input_path + file_name))
        file = open(self._output_path + new_file_name, 'a')
        file.write(data)
        file.close()


    def __repr__(self):
        file = open(self._output_path, 'r')
        for line in file:
            print(line)
        print("\t")
