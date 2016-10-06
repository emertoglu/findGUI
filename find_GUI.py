#!/usr/bin/python3

import os , subprocess , tkinter
from tkinter import *

from tkinter.filedialog import askdirectory

from tkinter import scrolledtext
#from tkinter import filedialog


def dosyaSec():

    """
    file_path_string = filedialog.askopenfiles()
    #tkFileDialog.askdirectory(initialdir="/", title='Klasor secin')
    folder = askdirectory()

    yol=str(file_path_string)

    global liste
    liste=[]

    for i in yol.split() :
        liste.append(i)
    print(liste[1])
    dosyaAl.insert(0,liste[1])

    """



def klasorSec():

    folder = askdirectory(initialdir="/home/aspa", title='Klasor Secin')

    isim=str(folder)
    print(isim)

    klasorAl.insert(0,isim)



def ara():
    klasor=klasorAl.get()
    dosyaAdi=isimAL.get()

    yol2='find '+klasor+ ' -name' + " '"+dosyaAdi+"'"

    a=subprocess.check_output([yol2],shell=True)

    metin.insert(END, a.decode())

    #print(a.decode())





pencere = Tk()
pencere.title("DOSYA  ARA")
pencere.geometry("570x450")
pencere.resizable(False, False)


etiket = Label(text="Konum Sec ", fg="magenta", bg="light green")
etiket.place(x=5, y=5, width=80, height=30)


klasorAl = Entry(pencere)
klasorAl.place(x=100, y=5, width=350, height=30)



btn = Button(text="Dizin Sec ", bg="orange", fg="navy", command=klasorSec)
btn.place(x=470, y=5 ,width=90, height=30)


etiket2 = Label(text="Dosya İsmi Gir ", fg="magenta", bg="light green")
etiket2.place(x=5, y=50, width=80, height=30)


isimAL = Entry(pencere)
isimAL.place(x=100, y=50, width=350, height=30)


btn2 = Button(text="ARA", bg="orange", fg="navy", command=ara)
btn2.place(x=470, y=50 ,width=90, height=30)


metin= Text()
metin.place(x=5, y=100, width=560, height=345)
metin.focus_set()

scroller = Scrollbar(pencere)
scroller.place(x=550, y=415)




scroller.config(command=metin.yview)
metin.config(yscrollcommand=scroller.set)





mainloop()


