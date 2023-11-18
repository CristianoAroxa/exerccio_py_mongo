from tkinter import *
from tkinter import messagebox
import subprocess

tela = Tk()
tela.title ("INCONCELL")
tela.geometry("400x200")
tela.resizable(False, False)
largura = 1000
altura = 700

barra_menus = Menu(tela)

opcoes_menus_arquivos = Menu(barra_menus)
opcoes_menus_gestao = Menu(barra_menus)

#opcoes_novo = Menu(opcoes_menus_arquivos)

barra_menus.add_cascade(label="Arquivo", menu=opcoes_menus_arquivos)


#opcoes_novo.add_cascade(label="Salvar Imagem")
#opcoes_novo.add_cascade(label="Pasta")

opcoes_menus_arquivos.add_command(label="Abrir")


opcoes_menus_arquivos.add_command(label="Sair", command=tela.quit)

tela.config(menu=barra_menus)

foto_sair = PhotoImage(file = r"icones\logo.png")
foto_animais = PhotoImage(file = r"icones\logo_animais.png")
foto_usuarios = PhotoImage(file = r"icones\logo_usuarios.png")
foto_servicos = PhotoImage(file = r"icones\logo_servicos.png")
foto_logout = PhotoImage(file = r"icones\logout.png")

lbl_logo = Label(tela, text="PET SHOP DOGS", compound = TOP, image = foto_sair).place(x = 890, y =580)
btn_animais = Button(tela, text="Animais", image = foto_animais, compound = TOP).place(x = 100, y =200)
btn_clientes = Button(tela, text="Clientes", image = foto_usuarios, compound = TOP).place(x = 350, y =200)

btn_servicos = Button(tela, text="Serviços", image = foto_servicos, compound = TOP).place(x = 550, y =200)

btn_logout = Button(tela, text="Sair", image = foto_logout, compound = TOP).place(x = 800, y =200)


def abrir_tela_animais():
    subprocess.run(["python", "tela_animais.py"])

def abrir_tela_clientes():
    subprocess.run(["python", "tela_clientes.py"])

def abrir_tela_servicos():
    subprocess.run(["python", "tela_servicos.py"])







tela.mainloop()