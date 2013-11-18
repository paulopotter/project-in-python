class dbSchema:
    def __init__(self):
        self.chosen_file = './db-2x1.db'
        self.open_file   = open(self.chosen_file, 'rb')

    def length_of_file(self):
        size_of_file = len(self.open_file.read())
        return size_of_file