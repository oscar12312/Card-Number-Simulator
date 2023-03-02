import socket
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
import sys
import os

def weigandClock():
    time.sleep(.00017)
    GPIO.output(13, True)
    time.sleep(.00025)     
    GPIO.output(13, False)
    time.sleep(.00092) 
    
def onePresent():
    GPIO.output(15, True)
    time.sleep(.00017)
    GPIO.output(13, True)
    time.sleep(.00025)
    GPIO.output(15, False)
    GPIO.output(13, False)
    time.sleep(.0007)
    
def is_even(num):
    return num % 2 == 0
    
def get_5bit_chunks(binary_string):
    chunks = [binary_string[i:i+5] for i in range(0, len(binary_string), 5)]
    return chunks

def xor(*args):
    result = args[0]
    for arg in args[1:]:
        result = (result != arg)
    return int(result)


def convert_to_binary(num):
    if num == 0: 
        return "00001"
    
    elif num == 1:  
        return "10000"
    
    elif num == 2:   
        return "01000"
    
    elif num == 3:       
        return "11001"
    
    elif num == 4:     
        return "00100"
    
    elif num == 5:   
        return "10101"
    
    elif num == 6:    
        return "01101"

    elif num == 7:
        
        return "11101"
    
    elif num == 8:
        return "00011"
    
    
    elif num == 9:
        return "10011"

GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

GPIO.output(15, False)
GPIO.output(13, False)
with open('Pad.py') as f:
    for line in f:
       # print(line)
       # sline = line.zfill(26)
  
        oscar = line[3:].zfill(13)
        bytes = [convert_to_binary(int(oscar[i])) for i in range(-13, 0, 1)] #converts digits to the necessary binary format
        byte1, byte2, byte3, byte4, byte5, byte6, byte7, byte8, byte9, byte10, byte11, byte12, byte13 = bytes


        byteData= byte1 + byte2 + byte3 + byte4 + byte5 + byte6 + byte7 + byte8 + byte9 + byte10 + byte11 + byte12 + byte13 


        SS = "11010" #Never Changes
        ES = "11111" #Never Changes


        lrc_values = [int(SS[i]) ^ int(byte1[i]) ^ int(byte2[i]) ^ int(byte3[i]) ^ int(byte4[i]) ^ int(byte5[i]) ^ int(byte6[i]) ^ int(byte7[i]) ^ int(byte8[i]) ^ int(byte9[i]) ^ int(byte10[i]) ^ int(byte11[i]) ^ int(byte12[i]) ^ int(byte13[i]) ^ int(ES[i]) for i in range(5)]
        LRC1, LRC2, LRC3, LRC4, LRC5 = lrc_values

        LRCNum = "".join("0" if is_even(x) else "1" for x in [LRC1, LRC2, LRC3, LRC4, int(not(xor(LRC1, LRC2, LRC3, LRC4)))]) #Parity Check


        z = "0000000000"+SS+  byteData+ ES+ LRCNum + "0000000000"

      #  print(z)

      #  print(LRCNum)

        for i in range(len(z)):
            if z[i] == "1":
                onePresent()
            else:
                weigandClock()





