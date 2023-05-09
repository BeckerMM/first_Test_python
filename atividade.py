
import requests
from tkinter import *

import pandas as pd 
tabela=pd.read_csv(r"C:\Users\matheus_becker\Desktop\telecom_users.csv")

tabela = tabela.drop("Unnamed: 0", axis=1)
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")
#tabela = tabela.drop("Unnamed: 0", axis=0)

janela = Tk()
texto=Label(janela, text=tabela)
texto.grid(column=0,row=0)
janela.title("Atividade")
janela.mainloop()
