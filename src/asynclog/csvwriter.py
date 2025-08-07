import csv


class CSVWriter:
    def __init__(self, filename):
        self.buffer = {"column1": "-", "column2": "-",
                       "column3": "-", "column4": "-"}
        self.file = None
        self.filename = filename
        self.writer = None

    def open(self):
        if self.file is None:
            self.file = open(self.filename, mode='w', newline='')
            self.writer = csv.writer(self.file)

    def close(self):
        if self.file is not None:
            self.file.close()
            self.file = None

    def write(self, column, value):
        self.buffer[column] = value

    def flush(self):
        if self.file is not None:
            import datetime
            self.buffer["column1"] = datetime.datetime.now()
            self.writer.writerow([value for value in self.buffer.values()])
            self.file.flush()
