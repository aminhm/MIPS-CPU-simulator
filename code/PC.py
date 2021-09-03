import DecimalToBinary
# import InstructionMEM
class PC :
    def __init__(self,PCcounter):
        self.PCcounter=PCcounter
        # InstructionMEM.InstructionMemory(self.PCcounter,self.ClockCycle).fetch()
    def PC_Add_By_four(self):
        result=""
        four=DecimalToBinary.DecimalToBinary(4).DecimalToBinary("")
        carry=0
        for i in range(32):
            if(self.PCcounter[32-i-1]=='0' and four[32-i-1]=='0' and carry==0):
                result='0'+result
                carry=0
            elif(self.PCcounter[32-i-1]=='0' and four[32-i-1]=='0' and carry==1):
                result='1'+result
                carry=0
            elif(self.PCcounter[32-i-1]=='1' and four[32-i-1]=='0' and carry==0):
                result='1'+result
                carry=0
            elif(self.PCcounter[32-i-1]=='1' and four[32-i-1]=='0' and carry==1):
                result='0'+result
                carry=1
            elif(self.PCcounter[32-i-1]=='0' and four[32-i-1]=='1' and carry==0):
                result='1'+result
                carry=0
            elif(self.PCcounter[32-i-1]=='0' and four[32-i-1]=='1' and carry==1):
                result='0'+result
                carry=1
            elif(self.PCcounter[32-i-1]=='1' and four[32-i-1]=='1' and carry==0):
                result='0'+result
                carry=1
            elif(self.PCcounter[32-i-1]=='1' and four[32-i-1]=='1' and carry==1):
                result='1'+result
                carry=1
        return result

    