

class DecimalToBinary:
    def __init__(self,decimal):
        self.decimal=decimal
    def DecimalToBinary(self,binary):
        while(abs(self.decimal)>1):
            binary=str(abs(self.decimal)%2)+binary
            self.decimal=int(abs(self.decimal)/2)
        binary=str(abs(self.decimal))+binary
        while(len(binary)!=32):
            binary='0'+binary
        return binary
