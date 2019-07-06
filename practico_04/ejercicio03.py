## 3 Ejercicio Crear un Formulario que usando el control Treeview muestre la una lista con los nombre de
## Ciudades Argentinas y su código postal ( por lo menos 5 ciudades ) . 

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
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
tree.pack(side=tk.TOP,fill=tk.X)
root.title("Ejercicio 3 - Grupo 28")
root.mainloop()