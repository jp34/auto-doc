import openpyxl

class Writer:

    __current_row = 1

    def __init__(self, out_path):
        self._out_path = out_path
        self._book = openpyxl.load_workbook(self._out_path)
        self._book.template = False
        self._sheet = self._book.active

    def write(self, person):
        columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

        data = person.get_print_info()
        self.set_starting_row()
        for i in range(len(data)):
            column = columns[i]
            self._sheet[column + str(self.__current_row)] = data[i]

        self._book.save(self._out_path)

        print("[Info] Row written: " + str(self.__current_row))

    def set_starting_row(self):
        row = 1
        while True:
            current_cell = self._sheet['A' + str(row)].value
            if current_cell is None:
                self.__current_row = row
                break
            row += 1
