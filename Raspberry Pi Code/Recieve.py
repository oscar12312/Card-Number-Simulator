import RPi.GPIO as GPIO
import socket
import time
GPIO.setwarnings(False)
import sys
import os
import subprocess



def main():
    
    ip = "192.168.102.101" # IP of Raspberry Pi
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind((ip, 8085))
    serv.listen(1)
    print("SERVER: started")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
    while True:

        conn, addr = serv.accept()
        from_client = ''
        
       # print("SERVER: connection to Client established")

        while True:
            # receive data and print
            data = conn.recv(4096).decode()
            if not data: break
            
            from_client += data
            
            print("Recieved: " + from_client)
            
            CardNum = from_client
            reader = CardNum[1:3]
            
            
            def readerChannel(digit):
                binary = bin(int(digit))[2:].zfill(4)
                
                pins = [31, 18, 22, 29]  # Pin numbers to display binary number
                GPIO.setmode(GPIO.BOARD)

                for i in range(4):
                    GPIO.setup(pins[i], GPIO.OUT)
                    if binary[i] == '1':
                        GPIO.output(pins[i], GPIO.LOW)  # Turn on pin if bit is 1
                    else:
                        GPIO.output(pins[i], GPIO.HIGH)  # Turn off pin if bit is 0
                
                
                        
            if CardNum[0] == "2":
                

                print("26 Bit Card Number")
                
                FC26 = int(CardNum[3:6])
                CN26 = int(CardNum[6:11].zfill(5))
                bin_key_one = f'{FC26:07b}'
                key = f'{FC26:b}'.zfill(8)
                
                bin_key_two = f'{CN26:07b}'
                keyOne = f'{CN26:b}'.zfill(16)
               
                ggg = int(key[0]) + int(key[1]) + int(key[2]) + int(key[3]) + int(key[4]) + int(key[5]) + int(key[6]) + int(key[7]) + int(keyOne[0]) + int(keyOne[1]) + int(keyOne[2]) + int(keyOne[3])
                if (ggg % 2) == 0:
                    parityOne = "0"
                else:
                    parityOne = "1"
                
                gg = int(keyOne[4]) + int(keyOne[5]) + int(keyOne[6]) + int(keyOne[7]) + int(keyOne[8]) + int(keyOne[9]) + int(keyOne[10]) + int(keyOne[11]) + int(keyOne[12]) + int(keyOne[13]) + int(keyOne[14]) + int(keyOne[15])
            
                if (gg % 2) == 0:
                    parityTwo = "1"
                else:
                    parityTwo = "0"
                 
                readerChannel(reader)    
                    
                f = open("Pad.py", "a")
                f.write(parityOne)
                f.write(key)
                f.write(keyOne)
                f.write(parityTwo)
                
                f.close()
                
                exec(open('26Bit.py').read())
                time.sleep(.5)
                
                f = open("Pad.py", "r+")
                f.truncate()   
                f.close()
                   
        #---------------------------------------------------------
             #not done 
            if CardNum[0] == "3":
                print("34 Bit Card Number")
                
                FC34 = int(CardNum[3:6])
                CN34 = int(CardNum[6:14].zfill(8))
                       
                bin_key_one = f'{FC34:07b}'
                CardNum = f'{FC34:b}'.zfill(16)
                
                bin_key_two = f'{CN34:07b}'
                CardNumOne = f'{CN34:b}'.zfill(16)
                
                ggg = int(CardNum[0]) + int(CardNum[1]) + int(CardNum[2]) + int(CardNum[3]) + int(CardNum[4]) + int(CardNum[5]) + int(CardNum[6]) + int(CardNum[7]) + int(CardNum[8]) + int(CardNum[9]) + int(CardNum[10]) + int(CardNum[11]) + int(CardNum[12]) + int(CardNum[13]) + int(CardNum[14])+ int(CardNum[15])   
                gg = int(CardNumOne[0]) + int(CardNumOne[1]) + int(CardNumOne[2]) + int(CardNumOne[3]) + int(CardNumOne[4]) + int(CardNumOne[5]) + int(CardNumOne[6]) + int(CardNumOne[7]) + int(CardNumOne[8]) + int(CardNumOne[9]) + int(CardNumOne[10]) + int(CardNumOne[11]) + int(CardNumOne[12]) + int(CardNumOne[13]) + int(CardNumOne[14]) + int(CardNumOne[15]) 
                if (ggg % 2) == 0:
                    parityOne = "0"
                else:
                    parityOne = "1"
                    
                if (gg % 2) == 0:
                    parityTwo = "1"
                else:
                    parityTwo = "0"
                
                readerChannel(reader)
                
                f = open("Pad.py", "a")
                f.write(parityOne)
                f.write(CardNum)
                f.write(CardNumOne)
                f.write(parityTwo)
                    
                f.close()
                
                exec(open('34Bit.py').read())
                time.sleep(.5)
                
                f = open("Pad.py", "r+")
                f.truncate()   
                f.close()
                
                
            #---------------------------------------------
            
            if CardNum[0] == "4":
                print("37 Bit Card Number")
              #  print("CN",CardNum[3:11].zfill(8))
            
                FC37 = int(CardNum[3:11])
                        
                bin_key_one = f'{FC37:07b}'
                CardNum = f'{FC37:b}'.zfill(35)
                
                
                
                ggg = int(CardNum[0]) + int(CardNum[1]) + int(CardNum[2]) + int(CardNum[3]) + int(CardNum[4]) + int(CardNum[5]) + int(CardNum[6]) + int(CardNum[7]) + int(CardNum[8]) + int(CardNum[9]) + int(CardNum[10]) + int(CardNum[11]) + int(CardNum[12]) + int(CardNum[13])  + int(CardNum[14]) + int(CardNum[15]) + int(CardNum[16]) + int(CardNum[17])  
                gg =  int(CardNum[17]) + int(CardNum[18]) + int(CardNum[19]) + int(CardNum[20]) + int(CardNum[21]) + int(CardNum[22]) + int(CardNum[23]) + int(CardNum[24]) + int(CardNum[25]) + int(CardNum[26]) + int(CardNum[27]) + int(CardNum[28]) + int(CardNum[29]) + int(CardNum[30]) + int(CardNum[31]) + int(CardNum[32]) + int(CardNum[33]) + int(CardNum[34]) 
            
                
                if (ggg % 2) == 0:
                    parityOne = "0"
                else:
                    parityOne = "1"
                    
                if (gg % 2) == 0:
                    parityTwo = "1"
                else:
                    parityTwo = "0"
                    
                readerChannel(reader)
                
                f = open("Pad.py", "a")
                f.write(parityOne)
                f.write(CardNum)
                f.write(parityTwo)
                    
                f.close()
                
                exec(open('37Bit.py').read())
                time.sleep(.5)
                
                f = open("Pad.py", "r+")
                f.truncate()   
                f.close()
  
  
            if CardNum[0] == "1": # Magetic
                
                # exec(open('37 bit 11111111.py').read())
                readerChannel(CardNum[1:3])
                
                print("Magnetic")
                f = open("Pad.py", "a")
                f.write(CardNum)
             
                f.close()
                
               # exec(open('Magnetic.py').read())
                subprocess.run(["python", "Magnetic.py"])
                
                time.sleep(.5)
                
                f = open("Pad.py", "r+")
                f.truncate()   
                f.close()            
                                 
            # send message back to client
            msg = "I am SERVER"
            conn.send(msg.encode())
            

        # close connection and exit
        conn.close()
        
        
main()
     