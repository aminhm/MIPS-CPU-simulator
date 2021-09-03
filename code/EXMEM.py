import DataMemory
import Forwarding
class EXMEM:
    def __init__(self,array,counter):
        self.array=array
        self.counter=counter
    def call(self):
        if(self.counter*5>=15):
            if(Forwarding.Forwarding(self.array[3][0],"0","0",self.array[2][2],self.array[2][3],self.array[3][4],"00000000000000000000000000000000","00000000000000000000000000000000","00000000000000000000000000000000").forwarding()=="ForwardA"):
                return "A-Hazard"
            if(Forwarding.Forwarding(self.array[3][0],"0","0",self.array[2][2],self.array[2][3],self.array[3][4],"00000000000000000000000000000000","00000000000000000000000000000000","00000000000000000000000000000000").forwarding()=="ForwardB"):
                return "B-Hazard"
            a=DataMemory.DataMemory(self.array[3][3],self.array[3][4],self.array[3][0],self.array,self.counter).hazard()
            if(a=="a-hazard"):
                return a
            if(a=="b-hazard"):
                return a
            DataMemory.DataMemory(self.array[3][3],self.array[3][4],self.array[3][0],self.array,self.counter).DataMemory()
    def continues(self):
        DataMemory.DataMemory(self.array[3][3],self.array[3][4],self.array[3][0],self.array,self.counter).DataMemory()
