import re

# task = open("./6/example.txt","r")
task = open("./6/task.txt","r")

inputStrig = task.read() # 'bvwbjplbgvbhsrlpgdmjqwftvncz' # 

k = 0

def GetStartPacket(message):    
    for i in range(0, len(inputStrig)-4):
        stringMatch = False
        subStr = message[i:4+i]
        for j in range(0,4):
            if(len(re.findall(subStr[j],subStr))>1):
                stringMatch = True

        if(not stringMatch):
        
            return i+4

def GetStartMessage(message):    
    for i in range(0, len(inputStrig)-14):
        stringMatch = False
        subStr = message[i:14+i]
        for j in range(0,14):
            if(len(re.findall(subStr[j],subStr))>1):
                stringMatch = True

        if(not stringMatch):
        
            return i+14
    
print("Start of Packet: " + str(GetStartPacket(inputStrig)))
print("Start of Message: " + str(GetStartMessage(inputStrig)))

task.close()