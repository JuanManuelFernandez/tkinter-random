#ejercicio_desafio

#librerias

from tkinter import *
import random

#funciones

def alta(): 
    print("nueva alta de datos")
    print("Titulo: ", str(a_val.get()), "Ruta: ", str(b_val.get()), "Descripcion: ", str(c_val.get()))


def cambiar_color():
    colors = ["green", "blue", "red", "purple", "cyan", "black", "yellow", "pink", "orange"]
    random_colors = random.choice(colors)
    master.config(background= random_colors)

#ventana

master = Tk()
master.title("ejercicio desafio")
master.resizable(False, False)


titulo = Label(master, text="ingrese sus datos", bg="purple", fg="thistle1", height=1, width=50)
titulo.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky=W+E)

#Labels

titulo_campo = Label(master, text="Titulo")
titulo_campo.grid(row=1, column=0, sticky=W)
ruta_campo = Label(master, text="Ruta")
ruta_campo.grid(row=2, column=0, sticky=W)
descripcion_campo = Label(master, text="Descripcion")
descripcion_campo.grid(row=3, column=0, sticky=W)

#Entrys

a_val, b_val, c_val = StringVar(), StringVar(), StringVar()
ancho = 25


entry_titulo = Entry(master, textvariable= a_val, width= ancho)
entry_titulo.grid(row=1, column=1)
entry_ruta = Entry(master, textvariable= b_val, width= ancho)
entry_ruta.grid(row=2, column=1)
entry_campo = Entry(master, textvariable= c_val, width= ancho)
entry_campo.grid(row=3, column=1)


#botones

boton_alta = Button(master, text="Alta", command=lambda: alta())
boton_alta.grid(row=4, column=1)

boton_sorpresa = Button(master, text="Sorpresa", command= lambda:cambiar_color())
boton_sorpresa.grid(row=5, column=1)


master.mainloop()

