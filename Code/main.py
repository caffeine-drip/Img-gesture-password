from Tkinter import *
from Input_gui import innn
from check_gui import cheek
mi = Tk()
mi.geometry("270x200")
mi.title("Main Window")
def inn():
    innn()
def ch():
    cheek()

i=Label(mi,text="To Setup Account")
ii=Button(mi,text="Click",command=inn)

iii=Label(mi,text="To Visite Your File")
iiii=Button(mi,text="Click",command=ch)

iia=Label(mi,text="Created by Anindya,")
iiaa=Label(mi,text="Anirudh,Anshul and Akansha")
i.grid(row=0,column=1)
ii.grid(row=0,column=2)
iii.grid(row=1,column=1)
iiii.grid(row=1,column=2)

ivv=Label(mi,text="              ")
iv=Label(mi,text="              ")
ivv.grid(row=0,column=0)
iv.grid(row=1,column=0)

ivp=Label(mi,text="              ")
ivpp=Label(mi,text="              ")
ivp.grid(row=2,column=0)
ivpp.grid(row=3,column=0)


iia.grid(row=4,column=1)
iiaa.grid(row=5,column=1)
mi.mainloop()
