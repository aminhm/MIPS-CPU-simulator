import WriteBack
import Forwarding
class MEMWB:
    def __init__(self,array,counter):
        self.array=array
        self.counter=counter
    def call(self):
        if(self.counter*5>=20):
            if(Forwarding.Forwarding(self.array[3][0],self.array[4][0],"0",self.array[2][2],self.array[2][3],self.array[3][4],"00000000000000000000000000000000","00000000000000000000000000000000",self.array[4][4]).forwarding()=="forwardA"):
                return "a-hazard"
            if(Forwarding.Forwarding(self.array[3][0],self.array[4][0],"0",self.array[2][2],self.array[2][3],self.array[3][4],"00000000000000000000000000000000","00000000000000000000000000000000",self.array[4][4]).forwarding()=="forwardB"):
                return "b-hazard"
            WriteBack.WriteBack(self.array[4][2],self.array[4][0],self.array,self.counter).making_decition()
    def continues(self):
        WriteBack.WriteBack(self.array[4][2],self.array[4][0],self.array,self.counter).making_decition()
        