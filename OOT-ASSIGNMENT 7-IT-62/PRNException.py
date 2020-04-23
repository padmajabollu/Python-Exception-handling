class PRN(Exception):

    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return "Error Occured : "+ str(self.msg)

