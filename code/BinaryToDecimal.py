import math

class BinaryToDecimal:
    def __init__(self,binary):
        self.binary=binary
    def BinaryToDecimal(self):
        decimal=0
        for i in range(0,len(self.binary)):
            decimal+=int(self.binary[len(self.binary)-i-1])*int(math.pow(2,i))
        return decimal