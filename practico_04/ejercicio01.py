## 1 Ejercicio Hacer un formulario tkinter que es una calculadora, tiene 2 entry para ingresar los valores V1 y V2.
## Y 4 botones de operaciones para las operaciones respectivas + , - , * , / ,
## al cliquearlos muestre el resultado de aplicar el operador respectivo en los V1 y V2 . 

from tkinter import *

def suma():
    cVar1 = int(numVar1.get())
    cVar2 = int(numVar2.get())
    print("Resultado: ", cVar1 + cVar2)

def resta():
    cVar1 = int(numVar1.get())
    cVar2 = int(numVar2.get())
    print("Resultado: ", cVar1 - cVar2)

def multiplicacion():
    cVar1 = int(numVar1.get())
    cVar2 = int(numVar2.get())
    print("Resultado: ", cVar1 * cVar2) 

def division():
    cVar1 = int(numVar1.get())
    cVar2 = int(numVar2.get())
    print("Resultado: ", cVar1/cVar2)


frm1 = Tk()
lblNum1 = Label(frm1, text="Ingrese Valor 1")
numVar1 = IntVar()
numVar1.set(1)
lblNum2 = Label(frm1, text="Ingrese Valor 2")
numVar2 = IntVar()
numVar2.set(2)
txtNum1 = Entry(frm1, textvariable=numVar1)
txtNum2 = Entry(frm1, textvariable=numVar2)
btnListo1 = Button(frm1, text="Resta (-)", command=resta)
btnListo2 = Button(frm1, text="Suma (+)", command=suma)
btnListo3 = Button(frm1, text="Multiplicación (*)", command=multiplicacion)
btnListo4 = Button(frm1, text="División (/)", command=division)

lblNum1.pack()
txtNum1.pack()
lblNum2.pack()
txtNum2.pack()
btnListo1.pack()
btnListo2.pack()
btnListo3.pack()
btnListo4.pack()
frm1.mainloop()
