import xlrd


class ReadFromExcel():

    def __init__(self, filename):
        self.filename = filename

    def readData(self, index, row, column):
        loc = self.filename

        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(index)

        return sheet.cell_value(row, column)

