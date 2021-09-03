import numpy
import InstructionMEM
import PC
import BinaryToDecimal
address=[]
a=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
i=0
ClockCycle=0
file = open("instructions.txt", "r")
for each in file: 
    if(each!='\n'):
        address.append(each)
file.close()
pc="00000000000000000000000000000000"
while(True):
    i=BinaryToDecimal.BinaryToDecimal(pc).BinaryToDecimal()
    i=i//4
    if(i==len(address)+5):
        break
    f=a[4]
    a[4]=a[3]
    a[3]=a[2]
    a[2]=a[1]
    a[1]=a[0]
    a[0]=f
    if(i<len(address)):
        ins=address[i]
    else:
        ins="00000000000000000000000000000000"
    b=InstructionMEM.InstructionMemory(ins,a,ClockCycle,pc).fetch()
    ClockCycle+=1
    for j in range(5):
        print(a[j][0],a[j][1])
    print(ClockCycle)
    print('\n\n')
    if (b=="Undefined opcode"):
        print("Undefined opcode")
        break
    if(b=="NopeBranch"):
        pc=a[0][2]
    elif(b=="J"):
        pc=a[0][5]
    elif(b!="Nope"):
        pc=PC.PC(pc).PC_Add_By_four()