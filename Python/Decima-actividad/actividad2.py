from tkinter import *
ventana = Tk()
elemento = StringVar()
listbox = Listbox(ventana)
for item in ['BMW','PEUGEOT','MERCEDES','CHEVROLET']:
 listbox.insert(END, item)
listbox.pack()
label = Label(text="Lista marca de autos ")
label.pack()
ventana.mainloop()