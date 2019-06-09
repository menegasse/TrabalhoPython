from tkinter import *
from tkinter import messagebox as msgbox
from Banco import *
from menu import *


class TelaLogin(Frame):

    def __init__(self,master=None):
     super().__init__()
            self.master.geometry("350x275") #define o tamanho da tela
            self.master.title("Login Lozinho") #titulo da janela
            self.master.resizable(False,False)
            self.pack()

            #Monta o Frame do Titulo
            self.f_titulo = Frame(height=60)
            self.f_titulo.pack(fill=X)

            self.l_titulo = Label(self.f_titulo)
            self.l_titulo['text'] = "Login"
            self.l_titulo['font'] = "Helvetica 26 bold"
            self.l_titulo.pack(ipady=15)
            
            #Montando os Frames do Usuário
            #Label
            self.f_lb_usuario = Frame(height =60)
            self.f_lb_usuario.pack(fill=X)

            self.lb_usuario = Label(self.f_lb_usuario)
            self.lb_usuario['text'] = "Usuário"
            self.lb_usuario['font'] = "Helvetica 16 "
            self.lb_usuario.pack(side=LEFT,ipadx=15)

            #Campo de entrada de dado
            self.f_entry_usuario = Frame(height =60)
            self.f_entry_usuario.pack(fill=X,padx=15)

            self.entry_usuario = Entry(self.f_entry_usuario,width=15,bg="#DEDEDE",font=("Helvetica",12))
            self.entry_usuario.pack(side=LEFT,ipadx=15)
            self.entry_usuario.focus_set()
            
            #Montando os Frames da Senha
            #Label
            self.f_lb_senha = Frame(height =60)
            self.f_lb_senha.pack(fill=X)

            self.lb_senha = Label(self.f_lb_senha)
            self.lb_senha['text'] = "Senha"
            self.lb_senha['font'] = "Helvetica 16 "
            self.lb_senha.pack(side=LEFT,ipadx=15)

            #Campo de entrada de dado
            self.f_entry_senha = Frame(height =60)
            self.f_entry_senha.pack(fill=X,padx=15)

            self.entry_senha = Entry(self.f_entry_senha,width=15,bg="#DEDEDE",font=("Helvetica",12))
            self.entry_senha.pack(side=LEFT,ipadx=15)
            self.entry_senha.focus_set()

            #Campo Botão Esqueci a Senha
            self.bnt_frame = Frame(height=30)
            self.bnt_frame.pack(fill=X)

            self.bntEsquece = Button(self.bnt_frame,text=" Esqueceu a Senha ",width=15)
            self.bntEsquece.bind("<Button-1>",self.btnEsqueceuClick)
            self.bntEsquece.grid(row=0,column=0,padx=35,pady=12)
            
            #Campo Botão Cadastrar

            self.bntCadastro = Button(self.bnt_frame,text=" Cadastrar ",width=15)
            self.bntCadastro.bind("<Button-1>",self.btnCadastrarClick)
            self.bntCadastro.grid(row=0,column=1,padx=15,pady=12)


            #Campo do Botão Entrar
            self.bnt_frame_1 = Frame(height=30)
            self.bnt_frame_1.pack(fill=X)

            self.bntEntrar = Button(self.bnt_frame_1,text=" Entrar ",width=38)
            self.bntEntrar.bind("<Button-1>",self.btnEntrarClick)
            self.bntEntrar.pack()

        
        def btnEntrarClick(self,event):
            bd = Banco()
            user = self.entry_usuario.get()
            pas = self.entry_senha.get()

            try:
                if not len(bd.verificar_user(user,pas)) == 0:
                    self.limpar_campo()
                    msgbox.showinfo("Welcome","Seja Bem-Vindo!")
                else:
                    self.limpar_campo()
                    msgbox.showerror("Erro","Usuário ou Senha invalida!")
            except ValueError:
                msgbox.showerror("Erro","Usuário ou Senha invalida!")
        
        def limpar_campo(self):
            self.entry_usuario.delete(0,'end')
            self.entry_senha.delete(0,'end')
            self.entry_usuario.focus_set()

        def btnEsqueceuClick(self):
            pass

        def btnCadastrarClick(self):
            pass



app = TelaLogin()
app.mainloop() 