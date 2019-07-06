## 2 Ejercicio Hacer un formulario en Tkinter una calculadora que tenga 1 entry y 12 botones para los dígitos 0 al 9
## y las operaciones + - / * = , que al apretar cada botón vaya agregando al valor que muestra en el entry el carácter 
## que le corresponde ( como se ve imagen ) y cuando se aprieta en = pone el resultado de evaluar la cadena entrada . 

from tkinter import *
from tkinter import messagebox


class Calculator:

    def ClearAll(self):
        self.e.delete(0, END)


    def Action(self, num):
        self.e.insert(END, num)
 

    def Equal(self):
        try:
            self.igual = self.e.get()
            self.equialidad =  eval(self.igual)
            self.e.delete(0, END)
            self.e.insert(END, self.equialidad)
        except ZeroDivisionError:
            messagebox.showinfo("Mensaje", "Error: División por cero")
            self.e.delete(0, END)
        except SyntaxError or NameError:
            messagebox.showinfo("Mensaje", "Error: Entrada de datos inválidos")
            self.e.delete(0, END)


    def __init__(self, ventana):
        ventana.title("Calculadora")
        ventana.geometry("260x200")
        self.e = Entry(ventana, width=25)
        self.e.grid(row=0, column=0, columnspan=4, pady=5)
        self.e.focus_set()


ventana = Tk()
objeto = Calculator(ventana)


botCero = Button(ventana, text="0", width=6, height=2, command=lambda: objeto.Action(0))
botUno = Button(ventana, text="1", width=6, height=2, command=lambda: objeto.Action(1))
botDos = Button(ventana, text="2", width=6, height=2, command=lambda: objeto.Action(2))
botTres = Button(ventana, text="3", width=6, height=2, command=lambda: objeto.Action(3))
botCuatro = Button(ventana, text="4", width=6, height=2, command=lambda: objeto.Action(4))
botCinco = Button(ventana, text="5", width=6, height=2, command=lambda: objeto.Action(5))
botSeis = Button(ventana, text="6", width=6, height=2, command=lambda: objeto.Action(6))
botSiete = Button(ventana, text="7", width=6, height=2, command=lambda: objeto.Action(7))
botOcho = Button(ventana, text="8", width=6, height=2, command=lambda: objeto.Action(8))
botNueve = Button(ventana, text="9", width=6, height=2, command=lambda: objeto.Action(9))
botSuma = Button(ventana, text="+", width=6, height=2, command=lambda: objeto.Action('+'))
botResta = Button(ventana, text="-", width=6, height=2, command=lambda: objeto.Action('-'))
botMultiplicacion = Button(ventana, text="x", width=6, height=2, command=lambda: objeto.Action('*'))
botDivision = Button(ventana, text="/", width=6, height=2, command=lambda: objeto.Action('/'))
botIgual = Button(ventana, text="=", width=6, height=2, command=objeto.Equal)
botClear = Button(ventana, text="AC", width=6, height=2, command=objeto.ClearAll)
botSiete.grid(column=0, row=1)
botOcho.grid(column=1, row=1)
botNueve.grid(column=2, row=1)
botCuatro.grid(column=0, row=2)
botCinco.grid(column=1, row=2)
botSeis.grid(column=2, row=2)
botUno.grid(column=0, row=3)
botDos.grid(column=1, row=3)
botTres.grid(column=2, row=3)
botCero.grid(row=4, column=1)
botSuma.grid(column=4, row=1)
botResta.grid(column=5, row=1)
botMultiplicacion.grid(column=4, row=2)
botDivision.grid(column=5, row=2)
botIgual.grid(column=4, row=3)
botClear.grid(column=5, row=3)

ventana.mainloop()