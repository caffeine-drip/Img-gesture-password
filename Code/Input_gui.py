from Tkinter import *
from input_chk_1 import inpu
from nameinpu import jack
def innn():
    m = Tk()
    m.title("Input Window")

    def nama():
        global s
        nameEE=Label(m,text=("_________________________________________"))
        nameEE.grid(row=2,column=1)
        s = nameE.get()
        jack(s)
        nameEE=Label(m,text=("You entered Name = "+s))
        nameEE.grid(row=2,column=1)
       
    def inputt():
        inpu()
        print s
        CHH=Label(m,text=("_________________________________________"))
        CHH.grid(row=3,column=1)
        CHH=Label(m,text=("Password saved"))
        CHH.grid(row=3,column=1)



    name=Label(m,text="Name")
    password=Label(m,text="Password")
    nameE=Entry(m)
    nameEE=Label(m,text=("_________________________________________"))

    namepass=Button(m,text="Enter",command=nama)
    butpass=Button(m,text="Click To Input",command=inputt)

    name.grid(row=0,column=0)
    password.grid(row=1,column=0)
    nameE.grid(row=0,column=1)
    namepass.grid(row=0,column=2)
    butpass.grid(row=1,column=1)
    nameEE.grid(row=2,column=1)

    m.mainloop()


