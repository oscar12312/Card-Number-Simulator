import socket
import RPi.GPIO as GPIO
import time
#GPIO.setwarnings(False)
import sys
import os

def weigand0():
    time.sleep(.00075)
    GPIO.output(15, True)
    time.sleep(.0001)     
    GPIO.output(15, False)
    time.sleep(.00075)
    
    
def weigand1():
    time.sleep(.00075)
    GPIO.output(13, True)
    time.sleep(.0001)     
    GPIO.output(13, False)
    time.sleep(.00075)


with open('Pad.py') as f:
    for line in f:
        print(line)
        sline = line.zfill(26)
   

            
             
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(13, GPIO.OUT)
        GPIO.setup(15, GPIO.OUT)

        GPIO.output(13, False)
        GPIO.output(15, False)
        time.sleep(.05)    
            
        #Referencing each of the binary numbers. 
        a = sline[0]
        b = sline[1]
        c = sline[2]
        d = sline[3]
        e = sline[4]
        f = sline[5]
        g = sline[6]
        h = sline[7]
        i = sline[8]
        j = sline[9]
        k = sline[10]
        l = sline[11]
        m = sline[12]
        n = sline[13]
        o = sline[14]
        p = sline[15]
        q = sline[16]
        r = sline[17]
        s = sline[18]
        t = sline[19]
        u = sline[20]
        v = sline[21]
        w = sline[22]
        x = sline[23]
        y = sline[24]
        z = sline[25]

           
        if a == "0":  
            weigand0()
        else:  
            weigand1()

        if b == "0":
            weigand0()
        else:
            weigand1()

        if c == "0":
            weigand0()
        else:
            weigand1()

        if d == "0":
            weigand0()
        else:   
            weigand1()

        if e == "0":
            weigand0()
        else: 
            weigand1()

        if f == "0":
            weigand0()
        else: 
            weigand1()

        if g == "0":
            weigand0()
        else: 
            weigand1()


        if h == "0":
            weigand0()
        else: 
            weigand1()

        if i == "0":
            weigand0()
        else: 
            weigand1()

        if j == "0":   
            weigand0()
        else: 
            weigand1()

        if k == "0":
            weigand0()
        else: 
            weigand1()

        if l == "0":
            weigand0()
        else: 
            weigand1()

        if m == "0":
            weigand0()
        else: 
            weigand1()

        if n == "0":
            weigand0()
        else: 
            weigand1()

        if o == "0":
            weigand0()
        else: 
            weigand1()

        if p == "0":
            weigand0()
        else: 
            weigand1()

        if q == "0":
            weigand0()
        else: 
            weigand1()

        if r == "0":
            weigand0()
        else: 
            weigand1()

        if s == "0":
            weigand0()
        else: 
            weigand1()

        if t == "0":
            weigand0()
        else: 
            weigand1()

        if u == "0":
            weigand0()
        else: 
            weigand1()

        if v == "0":
            weigand0()
        else: 
            weigand1()

        if w == "0":
            weigand0()
        else: 
            weigand1()

        if x == "0":
            weigand0()
        else: 
            weigand1()

        if y == "0":
            weigand0()
        else: 
            weigand1()

        if z == "0":
            weigand0()
        else: 
            weigand1()
        
        break