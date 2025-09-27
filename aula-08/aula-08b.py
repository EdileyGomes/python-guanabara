import math
from emoji import emojize
import random
from tkinter import *
from tkinter import ttk


aleatorio = random.randint(1, 10)
print( emojize(f'Vamos colocar um número aleatório aqui, que é o... {aleatorio} :alien:'))

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text= emojize("Hello World! :alien:")).grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()


