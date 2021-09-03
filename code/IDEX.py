import ALU
import Forwarding
import hazardDetection
class IDEX:
    def __init__(self,array,counter):
        self.array=array
        self.counter=counter
    def call(self):
        if(self.counter*5>=10):
            if(hazardDetection.HazardDetection(self.array[2][0],self.array[2][5],self.array[1][2],self.array[1][3]).detecting()=="Stall"):
                return "Stall"
            ALU.ALU(self.array[2][2],self.array[2][3],self.array[2][4],self.array[2][0],self.array,self.counter).operating()
    def continues(self):
        ALU.ALU(self.array[2][2],self.array[2][3],self.array[2][4],self.array[2][0],self.array,self.counter).operating()
        
