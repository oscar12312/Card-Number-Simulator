from tkinter import *
master = Tk()
master.geometry('600x300')
import time
import socket
from tkinter import ttk
from tkinter import messagebox

def IPSend(num):
    
    ip = "192.168.102.101" # IP of Raspberry Pi
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, 8085))
    print("connected")
    msg = num     
    client.send(msg.encode())
    time.sleep(.5)
    client.close()

def var_states():
    ProgressBar['value'] = 0

    testing = txt.get()
    if len(testing) < 3:
        print("Need a Number")
       # tkinter.messagebox.showerror(title=None, message='Need a number')
    else:
        if variable2.get() == 'Magnetic':
            cardType = 1

        if variable2.get() == '26 Bit Weigand':
            cardType = 2

        if variable2.get() == '34 Bit Weigand':
            cardType = 3

        if variable2.get() == '37 Bit Weigand':
            cardType = 4
        ProgressBar['value'] = 5

        master.update()
        
        reader_dict = {
            "C1R1": "14",
            "C1R2": "08",
            "C1R3": "12",
            "C1R4": "10",
            "C2R1": "06",
            "C2R2": "00",
            "C2R3": "04",
            "C2R4": "02",
            "C3R1": "05",
            "C3R2": "07",
            "C3R3": "03",
            "C3R4": "01",
            "C4R1": "13",
            "C4R2": "15",
            "C4R3": "11",
            "C4R4": "09" ,
        }
        ProgressBar['value'] = 10
        master.update()

        reader = reader_dict.get(variable.get(), None)
        if reader is None:
            print("NO")
            


        testing = txt.get()

        wholeNum = str(cardType) + str(reader) + testing 

        IPSend(wholeNum)
        ProgressBar['value'] = 50
        master.update()
        time.sleep(.5)   
        ProgressBar['value'] = 100
        master.update()    

            
lbl = Label(master, text="Welcome to the wiegand tester.").pack(ipadx=30, ipady=6)


OPTIONS2 = [
"Magnetic", "26 Bit Weigand", "34 Bit Weigand","37 Bit Weigand", 
] #etc

variable2 = StringVar(master)
variable2.set(OPTIONS2[0])
w = OptionMenu(master, variable2, *OPTIONS2)
w.pack(ipadx=30, ipady=6)

OPTIONS = [
"C1R1", "C1R2", "C1R3","C1R4","C2R1","C2R2","C2R3","C2R4","C3R1","C3R2","C3R3","C3R4","C4R1","C4R2","C4R3","C4R4"
] #etc

variable = StringVar(master)
variable.set(OPTIONS[0])
w = OptionMenu(master, variable, *OPTIONS)
w.pack(ipadx=30, ipady=4)

txt = Entry(master,width=30)
txt.pack( ipadx=30, ipady=6)

Button(master, text='Send', command=var_states).pack(ipadx=15, ipady=3)
Button(master, text='Quit', command=master.destroy).pack(ipadx=20, ipady=3, side= BOTTOM)

master.bind('<Return>', (lambda event:var_states()))


ProgressBar = ttk.Progressbar(master, orient='horizontal', mode='determinate', length=150)
ProgressBar.pack( padx=30)
ProgressBar['value'] = 0

mainloop()