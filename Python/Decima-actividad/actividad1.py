from tkinter import *

def seleccionar():
    windows.config(text="{}".format(opcion.get()))
def reset():
    opcion.set(None)
    windows.config(text="")

root = Tk()
opcion = StringVar()
opcion.set(None)
Radiobutton(root, text="Python", variable=opcion, 
            value='Python', command=seleccionar).pack(anchor=W)

Radiobutton(root, text="Javascript", variable=opcion, 
            value='Javascript', command=seleccionar).pack(anchor=W)
Radiobutton(root, text="SQL", variable=opcion,   
            value='SQL', command=seleccionar).pack(anchor=W)
Radiobutton(root, text="C++", variable=opcion,   
            value='C++', command=seleccionar).pack(anchor=W)

windows = Label(root)
windows.pack()
Button(root, text="Reiniciar", command=reset).pack()

root.mainloop()