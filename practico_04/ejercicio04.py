## 4. Ejercicio al Formulario del Ejercicio 3 ,  agrege  los siguientes botones 1- un  botón  Alta 
## que inicia otra venta donde puedo ingresar una ciudad y su código postal .
## 2 – un botón Baja que borra del listad de ciudades la ciudad que esta selecionada en Treeview .
## 3 – un botón Modificar . Todos los cambios se deben ver reflejados en la lista que se muestra . 

import tkinter as tk
from tkinter import ttk


def alta():
    
    def realiza():
        nombre = nombre_e.get()
        cp = cp_e.get()
        tree.insert("", 2, "6", text = nombre, values = cp)

    #Ventana hija
    alta = tk.Toplevel(root)
    alta.title ("Alta ciudad")
    #Labels y Botones
    lblNombre = tk.Label(alta, text="Ingrese Nombre Ciudad")
    lblNombre.grid(column=1, row=1)
    nombre_e = ttk.Entry(alta)
    nombre_e.grid(column=1, row=2)

    lblCp = tk.Label(alta, text="Codigo Postal")
    lblCp.grid(column=2, row=1)
    cp_e = ttk.Entry(alta)
    cp_e.grid(column=2, row=2)

    btnGuarda = tk.Button(alta, text="Guardar", command = realiza)
    btnGuarda.grid(column=3, row=2)
    
    root.iconify()

def modificar():
    def realiza():
        sel = tree.selection()[0]
        tree.delete(sel)    
        nombre = nombre_e.get()
        cp = cp_e.get()
        tree.insert("", 2, "6", text = nombre, values = cp)
        
    #Ventana hija
    modificar = tk.Toplevel(root)
    modificar.title ("Modificar ciudad")
    #Labels y Botones
    lblNombre = tk.Label(modificar, text="Ingrese Nombre Ciudad")
    lblNombre.grid(column=1, row=1)
    nombre_e = ttk.Entry(modificar)
    nombre_e.grid(column=1, row=2)

    lblCp = tk.Label(modificar, text="Codigo Postal")
    lblCp.grid(column=2, row=1)
    cp_e = ttk.Entry(modificar)
    cp_e.grid(column=2, row=2)

    btnGuarda = tk.Button(modificar, text="Guardar", command = realiza)
    btnGuarda.grid(column=3, row=2)
        
    root.iconify()

def baja():
    def realiza():
        sel = tree.selection()[0]
        tree.delete(sel)    
        
    #Ventana hija
    modificar = tk.Toplevel(root)
    modificar.title ("Baja ciudad")
    #Labels y Botones
    lbl = tk.Label(modificar, text="Está seguro que desea eliminar esta ciudad?")
    lbl.grid(column=1, row=1)

    btnGuarda = tk.Button(modificar, text="Eliminar", command = realiza)
    btnGuarda.grid(column=2, row=1)
        
    root.iconify()

#Ventana principal
root = tk.Tk()

#Definicion del tree
tree=ttk.Treeview(root)
tree["columns"]=("one")
tree.column("#0", width=400, minwidth=400)
tree.column("#1", width=200, minwidth=200)
tree.heading("#0",text="Ciudad",anchor=tk.W)
tree.heading("#1", text="Codigo Postal",anchor=tk.W)

tree.insert("", 2, "1", text="San Juan", values=("5441"))
tree.insert("", 2, "2", text="Funes", values=("2132"))
tree.insert("", 2, "3", text="Comodoro Rivadavia", values=("9000"))
tree.insert("", 2, "4", text="Ushuaia", values=("9410"))
tree.insert("", 2, "5", text="Corrientes", values=("7800"))
tree.grid(column=1, row=2)

#Botones (Root)
btnAlta = tk.Button(root, text="Alta Ciudad", command = alta)
btnAlta.grid(column=1, row=1)

btnMod = tk.Button(root, text="Modificacion Ciudad", command = modificar)
btnMod.grid(column=2, row=1)

btnBaja = tk.Button(root, text="Baja Ciudad", command = baja)
btnBaja.grid(column=3, row=1)

root.title("Ejercicio 4 - Grupo 28")
root.mainloop()
