from Tkinter import *
from chk2 import chk
from namechk import namech
ii=0
def cheek():
    m = Tk()
    m.title("Check Window")
    def nama():
        global ss,ii
        nam=Label(m,text=("_________________________________________"))
        nam.grid(row=2,column=1)
        ss = namE.get()
        
        na=Label(m,text=("You entered Name = "+ss))
        na.grid(row=2,column=1)
        ii=namech(ss)
        print ii
       
    def che():
        global ii
        print ii
        if ii!=1:
            print "wrong name"
            naa=Label(m,text=("You Entered Wrong Name = "+ss))
            naa.grid(row=3,column=1)
        else:
            i=chk()
            if i==1 and ii==1:
                CH=Label(m,text=("_________________________________________"))
                CH.grid(row=3,column=1)
                CH=Label(m,text=("Access Granted"))
                CH.grid(row=3,column=1)
            else:
                CH=Label(m,text=("_________________________________________"))
                CH.grid(row=3,column=1)
                CH=Label(m,text=("Access Denied"))
                CH.grid(row=3,column=1)


    nam=Label(m,text="Name")
    passw=Label(m,text="Password")
    namE=Entry(m)
    namEE=Label(m,text=("_________________________________________"))

    namepas=Button(m,text="Enter",command=nama)
    butpas=Button(m,text="Click To Input",command=che)

    nam.grid(row=0,column=0)
    passw.grid(row=1,column=0)
    namE.grid(row=0,column=1)
    namepas.grid(row=0,column=2)
    butpas.grid(row=1,column=1)
    namEE.grid(row=2,column=1)

    m.mainloop()




