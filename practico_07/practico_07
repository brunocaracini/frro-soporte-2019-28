import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from capa_negocio_TP06 import NegocioSocio
import capa_negocio_TP06
import ejercicio_01TP5
import ejercicio_02TP5
from ejercicio_01TP5 import Socio
from ejercicio_02TP5 import DatosSocio

def alta_presentacion():
    
    def realiza():
        negocio = NegocioSocio()
        if dni_e.get() != "" and apellido_e.get() != "" and nombre_e.get() != "":
            socio = negocio.alta(Socio(dni=dni_e.get(), nombre=nombre_e.get(), apellido=apellido_e.get()))
            if socio != None:
                tree.insert("", tk.END, text = socio.id_socio , values = (socio.nombre,socio.apellido,socio.dni))
        else:
            messagebox.showerror("Error de Usuario", "No pueden quedar campos vacíos")

    #Ventana hija
    alta = tk.Toplevel(root)
    alta.geometry("300x200") #Configurar tamaño
    alta.title ("Alta Socio")

    #Labels y Botones
    lblespacio1 = tk.Label(alta, text="")
    lblespacio1.grid(column=1, row=1)

    lblNombre = tk.Label(alta, text="Ingrese Nombre del Socio")
    lblNombre.grid(column=1, row=2)
    nombre_e = ttk.Entry(alta)
    nombre_e.grid(column=2, row=2)

    lblespacio = tk.Label(alta, text="")
    lblespacio.grid(column=1, row=3)

    lblApellido = tk.Label(alta, text="Ingrese Apellido del Socio")
    lblApellido.grid(column=1, row=4)
    apellido_e = ttk.Entry(alta)
    apellido_e.grid(column=2, row=4)

    lblespacio2 = tk.Label(alta, text="")
    lblespacio2.grid(column=1, row=5)

    lblApellido = tk.Label(alta, text="Ingrese DNI del Socio")
    lblApellido.grid(column=1, row=6)
    dni_e = ttk.Entry(alta)
    dni_e.grid(column=2, row=6)

    btnGuarda = tk.Button(alta, text="Guardar", command = realiza)
    btnGuarda.place(x=80, y=150)

    btnCancelar = tk.Button(alta, text="Cancelar", command = quit)
    btnCancelar.place(x=170, y=150)

    root.iconify()

def modificar_presemtacion():
    def realiza():
        negocio = NegocioSocio()
        sel = tree.selection()[0]
        diccionario = tree.item(sel)
        id_socio = diccionario['text']
        socio_mod = negocio.modificacion(Socio(dni=dni_e.get(), nombre=nombre_e.get(), apellido=apellido_e.get()),id_socio)
        if socio_mod != False:
            tree.delete(sel)
            tree.insert("", tk.END, text = id_socio , values = (socio_mod.nombre,socio_mod.apellido,socio_mod.dni))
        else:
            messagebox.showerror('Error de datos', 'Los no cumple con los requisitos')

    #Ventana hija
    modificar = tk.Toplevel(root)
    modificar.geometry("300x200") #Configurar tamaño
    modificar.title ("Modificar Socio")
    
    #Labels y Botones
    lblespacio1 = tk.Label(modificar, text="")
    lblespacio1.grid(column=1, row=1)

    lblNombre = tk.Label(modificar, text="Ingrese Nombre del Socio")
    lblNombre.grid(column=1, row=2)
    nombre_e = ttk.Entry(modificar)
    nombre_e.grid(column=2, row=2)

    lblespacio = tk.Label(modificar, text="")
    lblespacio.grid(column=1, row=3)

    lblApellido = tk.Label(modificar, text="Ingrese Apellido del Socio")
    lblApellido.grid(column=1, row=4)
    apellido_e = ttk.Entry(modificar)
    apellido_e.grid(column=2, row=4)

    lblespacio2 = tk.Label(modificar, text="")
    lblespacio2.grid(column=1, row=5)

    lblApellido = tk.Label(modificar, text="Ingrese DNI del Socio")
    lblApellido.grid(column=1, row=6)
    dni_e = ttk.Entry(modificar)
    dni_e.grid(column=2, row=6)

    btnGuarda = tk.Button(modificar, text="Guardar", command = realiza)
    btnGuarda.place(x=80, y=150)

    btnCancelar = tk.Button(modificar, text="Cancelar", command = quit)
    btnCancelar.place(x=170, y=150)

    root.iconify()

def baja_presentacion():
    def realiza():
        negocio = NegocioSocio()
        sel = tree.selection()[0]
        diccionario = tree.item(sel)
        id_socio = diccionario['text']
        socio = negocio.baja(id_socio)
        tree.delete(sel)
            
    #Ventana hija
    modificar = tk.Toplevel(root)
    modificar.title ("Baja Socio")
    #Labels y Botones
    lbl = tk.Label(modificar, text="¿Está seguro que desea eliminar a este Socio?")
    lbl.grid(column=1, row=1)

    btnGuarda = tk.Button(modificar, text="Eliminar", command = realiza)
    btnGuarda.grid(column=2, row=2)

    btnCancelar = tk.Button(modificar, text="Cancelar", command = quit)
    btnCancelar.grid(column=3, row=2)
        
    root.iconify()

def borrar_todos_presentacion():
    a = messagebox.askquestion("¡Atención!", "Se borraran TODOS los socios. ¿Desea continuar?")
    if a == 'yes':
        datos = DatosSocio()
        for i in tree.get_children():
            tree.delete(i)
        messagebox.showinfo('Notificación', "Se han borrado todos los socios")
        datos.borrar_todos()


#Ventana principal
root = tk.Tk()
root.geometry("700x330")

#Definicion del tree
tree=ttk.Treeview(root)
tree["columns"]=("one", "two", "three")
tree.column("#0", width=100, minwidth=100)
tree.column("#1", width=200, minwidth=200)
tree.column("#2", width=200, minwidth=200)
tree.column("#3", width=200, minwidth=200)
tree.heading("#0",text="Id",anchor=tk.W)
tree.heading("#1", text="Nombre",anchor=tk.W)
tree.heading("#2", text="Apellido",anchor=tk.W)
tree.heading("#3", text="DNI",anchor=tk.W)

tree.grid(column=2, row=3)

#Botones (Root)
lblNombre = tk.Label(root, text="")
lblNombre.grid(column=2, row=1)

lblNombre = tk.Label(root, text="")
lblNombre.grid(column=2, row=2)

btnAlta = tk.Button(root, text="Alta Socio", command = alta_presentacion)
btnAlta.place(x=190,y=10)

btnMod = tk.Button(root, text="Modificacion Socio", command = modificar_presemtacion)
btnMod.place(x=270, y=10)

btnBaja = tk.Button(root, text="Baja Socio", command = baja_presentacion)
btnBaja.place(x=400, y=10)

btnBorrarTodos = tk.Button(root, text="Borrar Todos", command = borrar_todos_presentacion)
btnBorrarTodos.place(x=290, y=280)

#LLeno la tabla inicialmente con los socios cargados previamente
def todos_presentacion():
    datos = DatosSocio()
    socios = datos.todos()
    for socio in socios:
        tree.insert("", tk.END, text = socio.id_socio , values = (socio.nombre,socio.apellido,socio.dni))
    return socios

root.title("ABM Socios - Grupo 28")
todos_presentacion()
root.mainloop()
