from tkinter import *
from tkinter import messagebox as msgbox


class RecuperaSenha(Frame):

    def __init__(self,master=None):
        super().__init__()
        self.master.geometry("475x100") #define o tamanho da tela
        self.master.title("Recuperar Senha") #titulo da janela
        self.master.resizable(False,False)
        self.pack()

        #Monta o Frame do Titulo
        self.f_titulo = Frame(height=60)
        self.f_titulo.pack(fill=X)

        self.l_titulo = Label(self.f_titulo)
        self.l_titulo['text'] = "Digite o seu e-mail cadastrado, para que enviemos sua senha: "
        self.l_titulo['font'] = "Helvetica 12"
        self.l_titulo.pack(side=LEFT,pady=10)
        
        
        #Campo de entrada de dado
        self.f_email = Frame(height=60)
        self.f_email.pack(fill=X)

        self.entry_email = Entry(self.f_email,width=60,bg="#DEDEDE",font=("Helvetica",12))
        self.entry_email.pack(side=LEFT,padx=5)
        self.entry_email.focus_set()

        #Campo Do botão
        self.f_bnt = Frame(height=60)
        self.f_bnt.pack(fill=X)


        self.bnt_Cadastrar = Button(self.f_bnt,text="Enviar",width=15)
        self.bnt_Cadastrar.bind("<Button-1>",self.btn_CadastrarClick)
        self.bnt_Cadastrar.pack(side=RIGHT,pady=5)

        self.bnt_Cancelar = Button(self.f_bnt,text="Cancelar",width=15)
        self.bnt_Cancelar.bind("<Button-1>",self.btn_CancelarClick)
        self.bnt_Cancelar.pack(side=RIGHT,padx=5,pady=5)
    
    def btn_CadastrarClick(self):
        pass
    def btn_CancelarClick(self):
        pass

app = RecuperaSenha()
app.mainloop()
