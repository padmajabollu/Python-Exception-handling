
class filehandling(object):

    def __init__(self, filename, mode="r"):
        self.filename = filename
        self.openFile(mode)

    def openFile(self, mode):
        try:
            self.fp = open(self.filename, mode)
            return self.fp
        except IOError:
            print("Cannot open the file ")

    def closeFile(self):
        self.fp.close()

    def readData(self):
        return self.fp.readlines()

    def writeData(self, data):
        self.fp.writelines(data)


