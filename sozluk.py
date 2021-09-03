from tkinter import *
from tkinter.ttk import *
import sqlite3
vt = sqlite3.connect('ceviri.db')
im = vt.cursor()



pencere = Tk()
pencere.title("Sözlük")
pencere.geometry("400x150")
pencere.maxsize(400,150)
pencere.config(padx=15,pady=35)


yazi = Entry(pencere, width=35)
yazi.grid(row=2, column=0)

# Bunu sonradan ekleyeceğiz
def ceviriyap() :
    e = yazi.get()
    if e != "" :
        im.execute("""SELECT * FROM sozcukler WHERE turkce='%s'"""%(str(e)))
        veriler = im.fetchone()
        if veriler :
            label.config(text=veriler[1])
        else :
            label.config(text="Sözcük Bulunamadı")


btn  = Button(pencere, text="Çevir", command=ceviriyap, width=25)
btn.grid(row=2, column=1)
label = Label(pencere, text="", font="Arial 14")
label.grid(row=3, columnspan=2, pady=15)



pencere.mainloop()