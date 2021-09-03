import RegisterFile
import IFID
import PC
import ControlUnit
import time
class InstructionMemory:
    def __init__(self,instruction,array,counter,PCcounter):
        self.array=array
        self.counter=counter
        self.instruction=instruction
        self.PCcounter=PCcounter
    def fetch(self):
        a=IFID.IFID(self.array,self.counter,self.PCcounter).call()
        if(a=="Nope"):
            return a
        if(a=="NopeBranch"):
            self.array[0][0]="Nope"
            self.array[0][1]="InstructionMemory"
            return a
        opcode=""
        rs=""
        rt=""
        rd=""
        constant_address_Itype=""
        constant_address_Jtype=""
        for i in range(6):
            opcode+=self.instruction[i]
        for j in range(5):
            rs+=self.instruction[i+j+1]
        for k in range(5):
            rt+=self.instruction[i+j+k+2]
        for t in range(5):
            rd+=self.instruction[i+j+k+t+3]
        for p in range(16):
            constant_address_Itype+=self.instruction[i+j+k+p+3]
        for u in range(26):
            constant_address_Jtype+=self.instruction[i+u+1]
        p=controlKey=ControlUnit.ControlUnit(opcode).instruction()
        if(p=="Undefined opcode"):
            return "Undefined opcode"
        while(len(rs)!=32):
            rs='0'+rs
            rt='0'+rt
            rd='0'+rd
        if(controlKey=="J"):
            constant_address_Jtype=self.PCcounter[31]+self.PCcounter[30]+self.PCcounter[29]+self.PCcounter[28]+constant_address_Jtype+"00"
            self.array[0][0]=controlKey
            self.array[0][1]="InstructionMemory"
            self.array[0][2]="00000000000000000000000000000000"
            self.array[0][3]="00000000000000000000000000000000"
            self.array[0][4]="00000000000000000000000000000000"
            self.array[0][5]=constant_address_Jtype
            return "J"
        self.array[0][0]=controlKey
        self.array[0][1]="InstructionMemory"
        self.array[0][2]=rs
        self.array[0][3]=rt
        self.array[0][4]=rd
        self.array[0][5]=constant_address_Itype