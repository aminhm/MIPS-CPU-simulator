
class HazardDetection:
    def __init__(self,controlKey3,registerRt1,registerRs2,registerRt2):
        self.registerRt1=registerRt1
        self.controlKey3=controlKey3
        self.registerRs2=registerRs2
        self.registerRt2=registerRt2
    def detecting(self):
        if(self.controlKey3=="Lw" and (self.registerRt1==self.registerRs2
        or self.registerRt1==self.registerRt2)):
            return "Stall"