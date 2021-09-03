
class Forwarding:
    def __init__(self,controlKey1,controlKey2,controlKey3,registerRs1,registerRt1,registerRd1,registerRs2,registerRt2,registerRd2):
        self.registerRs1=registerRs1
        self.registerRt1=registerRt1
        self.registerRd1=registerRd1
        self.registerRd2=registerRd2
        self.controlKey1=controlKey1
        self.controlKey2=controlKey2
        self.controlKey3=controlKey3
        self.registerRs2=registerRs2
        self.registerRt2=registerRt2
    def forwarding(self):
        if((self.controlKey1=="Add" or self.controlKey1=="Sub"
        or self.controlKey1=="And" or self.controlKey1=="Or" or self.controlKey1=="Nor"
        or self.controlKey1=="Xor" or self.controlKey1=="Slt") and (self.registerRd1)!="00000000000000000000000000000000"
        and (self.registerRd1)==self.registerRs1):
            return "ForwardA"
        elif((self.controlKey1=="Add" or self.controlKey1=="Sub"
        or self.controlKey1=="And" or self.controlKey1=="Or" or self.controlKey1=="Nor"
        or self.controlKey1=="Xor" or self.controlKey1=="Slt") and (self.registerRd1)!="00000000000000000000000000000000"
        and (self.registerRd1)==self.registerRt1):
            return "ForwardB"
        elif((self.controlKey2=="Add" or self.controlKey2=="Sub"
        or self.controlKey2=="And" or self.controlKey2=="Or" or self.controlKey2=="Nor"
        or self.controlKey2=="Xor" or self.controlKey2=="Slt") and (self.registerRd2)!="00000000000000000000000000000000"
        and not((self.controlKey1=="Add" or self.controlKey1=="Sub"
        or self.controlKey1=="And" or self.controlKey1=="Or" or self.controlKey1=="Nor"
        or self.controlKey1=="Xor" or self.controlKey1=="Slt") and (self.registerRd1)!="00000000000000000000000000000000" and (self.registerRd1)==self.registerRs1)
        and (self.registerRd2)==self.registerRs1):
            return "forwardA"
        elif((self.controlKey2=="Add" or self.controlKey2=="Sub"
        or self.controlKey2=="And" or self.controlKey2=="Or" or self.controlKey2=="Nor"
        or self.controlKey2=="Xor" or self.controlKey2=="Slt") and (self.registerRd2)!="00000000000000000000000000000000"
        and not((self.controlKey1=="Add" or self.controlKey1=="Sub"
        or self.controlKey1=="And" or self.controlKey1=="Or" or self.controlKey1=="Nor"
        or self.controlKey1=="Xor" or self.controlKey1=="Slt") and (self.registerRd1)!="00000000000000000000000000000000" and (self.registerRd1)==self.registerRt1)
        and (self.registerRd2)==self.registerRt1):
            return "forwardB"
        elif(self.controlKey2=="Lw" and not((self.controlKey1=="Nope") and (self.registerRd1)!="00000000000000000000000000000000" and (self.registerRd1)==self.registerRs1)
        and (self.registerRd2)==self.registerRs1):
            return "forwardA"
        elif(self.controlKey2=="Lw" )and not((self.controlKey1=="Nope" and (self.registerRd1)!="00000000000000000000000000000000" and (self.registerRd1)==self.registerRt1)
        and (self.registerRd2)==self.registerRt1):
            return "forwardB"