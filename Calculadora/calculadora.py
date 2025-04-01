# Calculadora básica utilizando el módulo tkinter y programación orientada a objetos
# Ejercicio realizado en curso de Python avanzado, Educación IT

import tkinter as tk
from tkinter import messagebox


class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculadora")
        self.config(background= "#00BFFF",width=280, height=420)
        self.resizable(False,False)

        self.result_var = tk.StringVar()

        self.display = tk.Entry(self,textvariable=self.result_var,font=("Arial",24), bd=10, relief="sunken", justify="right")
        self.display.place(x=20, y=20, width=240, height=60)

        botones = [
            ('7',20,100),('8',80,100),('9',140,100),('/',200,100),
            ('4',20,160),('5',80,160),('6',140,160),('*',200,160),
            ('1',20,220),('2',80,220),('3',140,220),('-',200,220),
            ('0',20,280),('.',80,280),('=',140,280),('+',200,280)
        ]

        for (simbolo,x,y) in botones:
            self.create_button(simbolo,x,y)

        self.create_button("C",20,340, width=240)
        
    def create_button(self,simbolo,x,y, width=60, height=60):
        button = tk.Button(self,text= simbolo, font=("Arial",18), width= 4, height= 2, command= lambda:self.on_button_click(simbolo))
        button.place(x= x, y= y, width= width, height= height)
        button.config(background="#2ECCFA")

    def on_button_click(self,simbolo):
        current = self.result_var.get()

        if simbolo == "C":
            self.result_var.set('')
            aux = ''
        elif simbolo == "=":
            try:
                result = str(eval(current))
                self.result_var.set(result)
            except ZeroDivisionError:
                messagebox.showerror("Error","No es posible dividir por cero")
            except Exception as e:
                messagebox.showerror("Error inesperado", f"Ocurrió un error inesperado:{str(e)}")
        else:
            self.result_var.set(current + simbolo)

if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()