import EXMEM
import MEMWB
import BinaryToDecimal
import DecimalToBinary
class ALU:
    def __init__(self,firstInput,secondInput,destination,ALUopKey,array,counter):
        self.firstInput=firstInput
        self.secondInput=secondInput
        self.destination=destination
        self.ALUopKey=ALUopKey
        self.array=array
        self.counter=counter
    def operating(self):
        a=EXMEM.EXMEM(self.array,self.counter).call()
        if(a=="A-Hazard"):
            self.firstInput=self.array[3][3]
            EXMEM.EXMEM(self.array,self.counter).continues()
        if(a=="B-Hazard"):
            self.secondInput=self.array[3][3]
            EXMEM.EXMEM(self.array,self.counter).continues()
        if(a=="a-hazard"):
            self.firstInput=self.array[4][2]
            MEMWB.MEMWB(self.array,self.counter).continues()
            EXMEM.EXMEM(self.array,self.counter).continues()
        if(a=="b-hazard"):
            self.secondInput=self.array[4][2]
            MEMWB.MEMWB(self.array,self.counter).continues()
            EXMEM.EXMEM(self.array,self.counter).continues()
        if(self.ALUopKey=="Add" or self.ALUopKey=="Lw" or self.ALUopKey=="Sw"):
            result=""
            carry=0
            for i in range(32):
                if(self.firstInput[32-i-1]=='0' and self.secondInput[32-i-1]=='0' and carry==0):
                    result='0'+result
                    carry=0
                elif(self.firstInput[32-i-1]=='0' and self.secondInput[32-i-1]=='0' and carry==1):
                    result='1'+result
                    carry=0
                elif(self.firstInput[32-i-1]=='1' and self.secondInput[32-i-1]=='0' and carry==0):
                    result='1'+result
                    carry=0
                elif(self.firstInput[32-i-1]=='1' and self.secondInput[32-i-1]=='0' and carry==1):
                    result='0'+result
                    carry=1
                elif(self.firstInput[32-i-1]=='0' and self.secondInput[32-i-1]=='1' and carry==0):
                    result='1'+result
                    carry=0
                elif(self.firstInput[32-i-1]=='0' and self.secondInput[32-i-1]=='1' and carry==1):
                    result='0'+result
                    carry=1
                elif(self.firstInput[32-i-1]=='1' and self.secondInput[32-i-1]=='1' and carry==0):
                    result='0'+result
                    carry=1
                elif(self.firstInput[32-i-1]=='1' and self.secondInput[32-i-1]=='1' and carry==1):
                    result='1'+result
                    carry=1
            self.array[2][0]=self.ALUopKey
            self.array[2][1]="ALU"
            self.array[2][2]="00000000000000000000000000000000"
            self.array[2][3]=result
            self.array[2][4]=self.destination
            self.array[2][5]="00000000000000000000000000000000"
        if(self.ALUopKey=="Sub"):
            result=""
            for i in range(32):
                if(self.secondInput[32-i-1]=='1'):
                    result=self.secondInput[32-i-1]+result
                    for j in range(32-i-1):
                        if(self.secondInput[32-i-j-2]=='0'):
                            result='1'+result
                        else:
                            result='0'+result
                    break
                else:
                    result=self.secondInput[32-i-1]+result
            result_sub=""
            carry=0
            for i in range(32):
                if(self.firstInput[32-i-1]=='0' and result[32-i-1]=='0' and carry==0):
                    result_sub='0'+result_sub
                    carry=0
                elif(self.firstInput[32-i-1]=='0' and result[32-i-1]=='0' and carry==1):
                    result_sub='1'+result_sub
                    carry=0
                elif(self.firstInput[32-i-1]=='1' and result[32-i-1]=='0' and carry==0):
                    result_sub='1'+result_sub
                    carry=0
                elif(self.firstInput[32-i-1]=='1' and result[32-i-1]=='0' and carry==1):
                    result_sub='0'+result_sub
                    carry=1
                elif(self.firstInput[32-i-1]=='0' and result[32-i-1]=='1' and carry==0):
                    result_sub='1'+result_sub
                    carry=0
                elif(self.firstInput[32-i-1]=='0' and result[32-i-1]=='1' and carry==1):
                    result_sub='0'+result_sub
                    carry=1
                elif(self.firstInput[32-i-1]=='1' and result[32-i-1]=='1' and carry==0):
                    result_sub='0'+result_sub
                    carry=1
                elif(self.firstInput[32-i-1]=='1' and result[32-i-1]=='1' and carry==1):
                    result_sub='1'+result_sub
                    carry=1
            self.array[2][0]=self.ALUopKey
            self.array[2][1]="ALU"
            self.array[2][2]="00000000000000000000000000000000"
            self.array[2][3]=result_sub
            self.array[2][4]=self.destination
            self.array[2][5]="00000000000000000000000000000000"
        if(self.ALUopKey=="And"):
            result=""
            for i in range (32):
                if(self.firstInput[32-i-1]=='1' and self.secondInput[32-i-1]=='1'):
                    result='1'+result
                else:
                    result='0'+result
            self.array[2][0]=self.ALUopKey
            self.array[2][1]="ALU"
            self.array[2][2]="00000000000000000000000000000000"
            self.array[2][3]=result
            self.array[2][4]=self.destination
            self.array[2][5]="00000000000000000000000000000000"
        if(self.ALUopKey=="Or"):
            result=""
            for i in range(32):
                if(self.firstInput[32-i-1]=='0' and self.secondInput[32-i-1]=='0'):
                    result='0'+result
                else:
                    result='1'+result
            self.array[2][0]=self.ALUopKey
            self.array[2][1]="ALU"
            self.array[2][2]="00000000000000000000000000000000"
            self.array[2][3]=result
            self.array[2][4]=self.destination
            self.array[2][5]="00000000000000000000000000000000"
        if(self.ALUopKey=="Nor"):
            result=""
            for i in range(32):
                if(self.firstInput[32-i-1]=='0' and self.secondInput[32-i-1]=='0'):
                    result='1'+result
                else:
                    result='0'+result
            self.array[2][0]=self.ALUopKey
            self.array[2][1]="ALU"
            self.array[2][2]="00000000000000000000000000000000"
            self.array[2][3]=result
            self.array[2][4]=self.destination
            self.array[2][5]="00000000000000000000000000000000"
        if(self.ALUopKey=="Xor"):
            result=""
            for i in range(32):
                if ((self.firstInput[32-i-1]=='0' and self.secondInput[32-i-1]=='0') or (self.firstInput[32-i-1]=='1' and self.secondInput[32-i-1]=='1')):
                    result='0'+result
                else:
                    result='1'+result
            self.array[2][0]=self.ALUopKey
            self.array[2][1]="ALU"
            self.array[2][2]="00000000000000000000000000000000"
            self.array[2][3]=result
            self.array[2][4]=self.destination
            self.array[2][5]="00000000000000000000000000000000"
        if(self.ALUopKey=="Slt"):
            result=""
            if(BinaryToDecimal.BinaryToDecimal(self.firstInput).BinaryToDecimal()<BinaryToDecimal.BinaryToDecimal(self.secondInput).BinaryToDecimal()):
                result="00000000000000000000000000000001"
            else:
                result="00000000000000000000000000000000"
            self.array[2][0]=self.ALUopKey
            self.array[2][1]="ALU"
            self.array[2][2]="00000000000000000000000000000000"
            self.array[2][3]=result
            self.array[2][4]=self.destination
            self.array[2][5]="00000000000000000000000000000000"
        if(self.ALUopKey=="None" or self.ALUopKey=="Nope" or self.ALUopKey=="Beq" or self.ALUopKey=="Bne" or self.ALUopKey=="J"):
            self.array[2][0]=self.ALUopKey
            self.array[2][1]="ALU"
            self.array[2][2]="00000000000000000000000000000000"
            self.array[2][3]="00000000000000000000000000000000"
            self.array[2][4]="00000000000000000000000000000000"
            self.array[2][5]="00000000000000000000000000000000"

