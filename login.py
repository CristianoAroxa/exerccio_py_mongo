from tkinter import *
from tkinter import messagebox
import subprocess

tela = Tk()
tela.title("Acesso ao sistema")
tela.geometry("400x200")
tela.resizable(False, False)
largura = 400
altura = 200

def sair():
    resposta =messagebox.askquestion("Sair do Sistema", "Você tem certeza que deseja sair?")
    if resposta == "yes":
        tela.destroy()

def validar_acesso(usuario, senha):
    if usuario == "admin" and senha == "123":
        abrir_app()
    
    else:
        messagebox.showerror("Erro", "Usuário ou senha inválidos")
        

def abrir_app():
    tela.destroy()
    subprocess.run(["python", "login.py"])

def click_botao():
    usuario = txt_usuario.get()
    senha = txt_senha.get()
    validar_acesso(usuario, senha)

lbl_usuario = Label(tela, text="Usuario").place(x=50, y=60)
lbl_senha = Label(tela, text="Senha").place(x=50, y=100)
txt_senha = Entry(tela, width=20, show="*")
txt_senha.place(x=100, y=100)
txt_usuario = Entry(tela, width=20)
txt_usuario.place(x=100, y=60)

foto_acesso = PhotoImage(file=r"icones/acesso.png")
foto_sair = PhotoImage(file=r"icones/sair.png")

btn_usuario = Button(tela, text="Acessar", image=foto_acesso, compound=TOP, command=click_botao)
btn_usuario.place(x=250, y=50)

btn_sair = Button(tela, text="Sair", image=foto_sair, compound=TOP, command=sair)
btn_sair.place(x=320, y=50)

largura_screen = tela.winfo_screenmmwidth()
altura_screen = tela.winfo_screenmmheight()
posx = largura_screen / 2 - largura_screen / 2

posy = altura_screen / 2 - altura_screen / 2
tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

tela.mainloop()


 