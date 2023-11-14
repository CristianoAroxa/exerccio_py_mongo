from tkinter import *
from tkinter import ttk
import tkinter as tk
import pymongo


tela = Tk()
tela.title("Exemplo mongo Db")
tela.geometry("800x600")
tela.resizable(True,True)
tela.configure(background=="#ffffff")

exemplo = pymongo.MongoClient("mongodb://localhost:27017/")
db = exemplo["exemplo"]
collection = db["clientes"]

lbl_titulo = Label(tela, text="Cadastro de Clientes", font=("Arial", 30, "bold"), bg="#ffffff").place(x=200, y=50)

lbl_titulo = Label(tela, text="Código", font=("Arial", 30, "bold"), bg="#ffffff").place(x=130, y=140)
txt_codigo = Entry(tela, width=20, borderwidth=2, fg="black", bg="white")
txt_codigo.place(x=190, y=140)

lbl_titulo = Label(tela, text="Nome", font=("Arial", 30, "bold"), bg="#ffffff").place(x=130, y=140)
txt_nome = Entry(tela, width=20, borderwidth=2, fg="black", bg="white")
txt_nome.place(x=190, y=170)
txt_nome.insert(0, "")



