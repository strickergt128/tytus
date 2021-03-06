from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as FileDialog
from tkinter import ttk
import tkinter as tk
import webbrowser
#from graphviz import Digraph
import json
import os
from string import Template

from io import open
import re
from tabulate import tabulate
import os
import glob
ruta = ""  # La utilizaremos para almacenar la ruta del fichero

# esto es para la interfaz--------------------------------------------------------------------------------------------------------------------------------------------------------


def run():
    mb.showinfo("ANALISIS COMPLETADO", "Analisis Completado")
    consola_text.configure(state='normal')
    consola_text.insert(INSERT, "LA CONSOLA FUNCIONA")
    consola_text.configure(state='disabled')
    
    # END


def test():
    mb.showinfo("TytusDB",
                "Universidad de San Carlos de Guatemala\n\tFacultad de Ingenieria\n\tOrganización de lenguajes y compiladores 2\n\tversion 1.0\n\tGRUPO 11\n\tMaria Andrea Duarte Saenz\n\t201503484")  # título, mensaje
    # END


def nuevo():
    global ruta
    mensaje.set("Nuevo archivo")
    ruta = ""
    texto.delete(1.0, "end")
    root.title("TytusDB")
    # END


def abrir():
    global ruta
    mensaje.set("Abrir archivo")
    ruta = FileDialog.askopenfilename(
        initialdir='.',
        filetypes=(("HTML", "*.html"), ("CSS", "*.css"), ("JavaScript",
                                                          "*.js"), ("Arbol sintactico", "*.rmt"), ("All files", "*.*")),
        title="Abrir un archivo")

    if ruta != "":
        fichero = open(ruta, 'r', encoding="utf-8")
        contenido = fichero.read()
        texto.delete(1.0, 'end')
        print(contenido)
        texto.insert('insert', contenido)
        fichero.close()
        root.title(ruta + " - DBMS Usac editor")
    # END


def guardar():
    mensaje.set("Guardar archivo")
    if ruta != "":
        contenido = texto.get(1.0, 'end-1c')
        fichero = open(ruta, 'w+', encoding="utf-8")
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Archivo guardado correctamente")
    else:
        guardar_como()
    # END


def guardar_como():
    global ruta
    mensaje.set("Guardar como")

    fichero = FileDialog.asksaveasfile(title="Guardar archivo",
                                       mode="w", filetypes=(("SQL", "*.sql"), ("All files", "*.*")))

    if fichero is not None:
        ruta = fichero.name
        contenido = texto.get(1.0, 'end-1c')
        fichero = open(ruta, 'w+', encoding="utf-8")
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Archivo guardado correctamente")
    else:
        mensaje.set("Guardado cancelado")
        ruta = ""

    # END
# _____________________________________________INTERFAZ----------------------------------------------------

root = Tk()
root.title("TytusDB")
root.resizable(0, 0)
# root.iconbitmap("monitor.ico")
root.config(bg="gray75")
# Menú superior
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_separator()
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_command(label="Guardar Como", command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Run")
editmenu.add_command(label="Borrar todo")
#editmenu.add_command(label="Analizar HTML", command = analizarHTML)
#editmenu.add_command(label="Analizar RMT", command = analizarRMT)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Acerca de...", command=test)
menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Analizar", menu=editmenu)
menubar.add_cascade(label="Acerca de..", menu=helpmenu)

# Frame 1
frame1 = Frame(root, width=1485, height=820)
frame1.pack()  # se agrega pa paquete
frame1.config(bg="lightblue2")

frame1.config(relief="groove")
frame1.config(bd=18)
frame1.config(cursor="spider")


fname = "./img/logo.png"
imagen = PhotoImage(file=fname)
fondo = Label(frame1, image=imagen).place(x=0, y=0)
# Labels
# VIEW TREE
my_tree = ttk.Treeview(frame1)

# Definiendo las columnas
my_tree['columns'] = ("Hola")

#tv = Treeview(frame1, width = 20, height = 20)
# Seperator object
separator = ttk.Separator(frame1, orient='vertical')
separator.place(relx=0.27, rely=0, relwidth=0.001, relheight=1)

# Caja de texto
texto = Text(frame1, width=90, height=15)
texto.pack(expand=1)
texto.place(x=420, y=100)
texto.config(bd=0, font=("Consolas", 15))
label_cod = Label(frame1, text="Codigo fuente", bg="gray93",
                  font=("Berlin Sans FB", 14)).place(x=420, y=70)

# Notebook
texto4 = ttk.Notebook(frame1, width=990, height=200)
texto4.pack(fill='none', expand='yes', side='bottom')
texto4.pack(expand=1)
texto4.place(x=420, y=500)


consola_text = Text(texto4, width=90, height=10,
                    bg="gray40", fg="spring green")
consola_text.config(bd=0, font=("Consolas", 14))
consola_text.configure(state='disabled')

output_text = Text(texto4, width=90, height=10,
                    bg="gray40", fg="white")
output_text.config(bd=0, font=("Consolas", 14))
# output_text.configure(state='disabled')

errores_text = Text(texto4, width=90,  height=10,
                    bg="gray40", fg="OrangeRed2")
errores_text.config(bd=0, font=("Consolas", 14))
errores_text.configure(state='disabled')

texto4.add(consola_text, text="Consola", padding=5)
texto4.add(output_text, text="Output", padding=5)
texto4.add(errores_text, text="Errores", padding=5)

label_cod = Label(frame1, text="Consola, Output y Errores", bg="gray93",
                  font=("Berlin Sans FB", 14)).place(x=420, y=470)


# Botones
fname2 = "./img/run.png"
img = PhotoImage(file=fname2)
btn = Button(frame1, image=img, bg="gray93", command=run).place(x=835, y=20)


fname3 = "./img/borrar.png"
img2 = PhotoImage(file=fname3)
btn2 = Button(frame1, image=img2, bg="gray93").place(x=1330, y=20)

fname4 = "./img/error.png"
img3 = PhotoImage(file=fname4)
btn3 = Button(frame1, bg="gray93", image=img3, text="Errores", height=70,
              width=100, font=("Berlin Sans FB", 15)).place(x=138, y=200)

fname5 = "./img/tabla.png"
img4 = PhotoImage(file=fname5)
btn4 = Button(frame1, bg="gray93", image=img4, text="Tabla", height=70,
              width=100, font=("Berlin Sans FB", 15)).place(x=138, y=290)

fname6 = "./img/AST.png"
img5 = PhotoImage(file=fname6)
btn5 = Button(frame1, bg="gray93", image=img5, text="AST", height=70,
              width=100, font=("Berlin Sans FB", 15)).place(x=138, y=380)

fname7 = "./img/gramatica.png"
img6 = PhotoImage(file=fname7)
btn6 = Button(frame1, bg="gray93", image=img6, text="Gramatical",
              height=70, width=100, font=("Berlin Sans FB", 15)).place(x=138, y=470)


# Monitor inferior
mensaje = StringVar()
mensaje.set("TytusDB")
monitor = Label(root, textvar=mensaje, font=("Berlin Sans FB", 15))
monitor.pack(side="left")

root.config(menu=menubar)

root.mainloop()