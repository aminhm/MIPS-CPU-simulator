import RegisterFile
import ControlUnit
class IFID:
    def __init__(self,array,counter,PCcounter):
        self.array=array
        self.counter=counter
        self.PCcounter=PCcounter
    def call(self):
        if(self.counter*5>=5):
            a=RegisterFile.RegisterFile(self.array[1][2],self.array[1][3],self.array[1][4],self.array[1][0],self.array[1][5],self.array,self.counter,self.PCcounter).registerInputs()
            if(a=="Nope" or a=="NopeBranch"):
                return a