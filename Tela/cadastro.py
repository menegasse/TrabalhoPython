from tkinter import *
from tkinter import messagebox as msgbox
from Banco  import *
from string import punctuation

class Cadastro(Frame):

    def __init__(self,master=None):
        super().__init__()
        self.master.geometry("400x375") #define o tamanho da tela
        self.master.title("Cadastro") #titulo da janela
        self.master.resizable(False,False)
        self.pack()

        #Monta o Frame do Titulo
        self.f_titulo = Frame(height=60)
        self.f_titulo.pack(fill=X)

        self.l_titulo = Label(self.f_titulo)
        self.l_titulo['text'] = "Cadastro"
        self.l_titulo['font'] = "Helvetica 26 bold"
        self.l_titulo.pack(ipady=15)
        
        #Montando os Frames do Usuário
        #Label User name
        self.f_lb_usuario = Frame(height =60)
        self.f_lb_usuario.pack(fill=X,padx=10)

        self.lb_usuario = Label(self.f_lb_usuario)
        self.lb_usuario['text'] = "User Name:"
        self.lb_usuario['font'] = "Helvetica 12"
        self.lb_usuario.grid(row=0,column=0)
        #Campo de entrada de dado
        self.entry_usuario = Entry(self.f_lb_usuario,width=15,bg="#DEDEDE",font=("Helvetica",12))
        self.entry_usuario.grid(row=1,column=0,padx=20)
        self.entry_usuario.focus_set()

        #Campo Idade
        self.lb_idade = Label(self.f_lb_usuario)
        self.lb_idade['text'] = "Idade:"
        self.lb_idade['font'] = "Helvetica 12"
        self.lb_idade.grid(row=0,column=1)

        #Campo de entrada de dado
        self.entry_idade = Entry(self.f_lb_usuario,width=15,bg="#DEDEDE",font=("Helvetica",12))
        self.entry_idade.grid(row=1,column=1,padx=20)
        self.entry_idade.focus_set()

        ##Campo nome completo
        self.f_nome_completo = Frame(height =60)
        self.f_nome_completo.pack(fill=X,padx=10,pady=10)

        self.lb_nome_completo = Label(self.f_nome_completo)
        self.lb_nome_completo['text'] = "Nome Completo:"
        self.lb_nome_completo['font'] = "Helvetica 12"
        self.lb_nome_completo.grid(row=2)
        #Campo de entrada de dado
        self.entry_nome_completo = Entry(self.f_nome_completo,width=30,bg="#DEDEDE",font=("Helvetica",12))
        self.entry_nome_completo.grid(row=3,padx=21)
        self.entry_nome_completo.focus_set()

        ##Campo senha
        self.f_senha = Frame(height =60)
        self.f_senha.pack(fill=X,padx=10)

        self.lb_senha = Label(self.f_senha)
        self.lb_senha['text'] = "Senha:"
        self.lb_senha['font'] = "Helvetica 12"
        self.lb_senha.grid(row=0)

        #Campo senha
        self.entry_senha = Entry(self.f_senha,width=15,bg="#DEDEDE",font=("Helvetica",12))
        self.entry_senha.grid(row=1,padx=21)
        self.entry_senha.focus_set()

        #Confirmar Senha
        self.lb_senha = Label(self.f_senha)
        self.lb_senha['text'] = "Confirmar Senha:"
        self.lb_senha['font'] = "Helvetica 12"
        self.lb_senha.grid(row=2)

        #Confirmar Senha
        self.entry_c_senha = Entry(self.f_senha,width=15,bg="#DEDEDE",font=("Helvetica",12))
        self.entry_c_senha.grid(row=3,padx=21)
        self.entry_c_senha.focus_set()

        #Campo Botão

        self.bnt_frame = Frame(height=30)
        self.bnt_frame.pack(fill=X)

        self.bnt_Cadastrar = Button(self.bnt_frame,text="Cadastrar",width=30)
        self.bnt_Cadastrar.bind("<Button-1>",self.btn_CadastrarClick)
        self.bnt_Cadastrar.pack(pady=25,ipady=20)
    
    def limpar_campos(self):
        self.entry_idade.delete(0,'end')
        self.entry_usuario.delete(0,'end')
        self.entry_nome_completo.delete(0,'end')
        self.entry_senha.delete(0,'end')
        self.entry_c_senha.delete(0,'end')
        

    def btn_CadastrarClick(self,event):
        idade = 0 if self.entry_idade.get() ==  "" else int(self.entry_idade.get())
        usuario = self.entry_usuario.get()
        nome = self.entry_nome_completo.get()
        senha = self.entry_senha.get()
        c_senha = self.entry_c_senha.get()
        if self.VerificaCampos(idade,usuario,nome,senha,c_senha) == True:
            bd = Banco()
            bd.cadastrar_user(idade,usuario,nome,senha)
            msgbox.showinfo("Cadastro","Cadastro Realizado com Sucesso!")
            self.limpar_campos()
        else:
            self.limpar_campos()

    def VerificaCampos(self,idade=0,user_name='',nome_user="",senha='',c_senha=''):
        msg = ""

        if idade < 13 or idade == 0:
            msg = msg + "-Idade minima para o Cadastro é de 13 anos!\n"
            

        if not user_name == "":
            for ponto in user_name:
                if ponto in punctuation:
                    msg = msg + "-Nome de usuário com pontuação!\n"                   
        else: 
            msg = msg + "-Nome de usuário em branco!\n"

         
        if not senha == "" :
          if not c_senha == "":
              if not senha == c_senha:
                msg = msg + "-Campo de confirmar senha invalido!\n"
          else:
              msg = msg + "-Campo confirmar senha invalido!\n"
        else:
             msg = msg + "-Campo senha invalido!\n"          
        
        if not msg == "":
            msgbox.showwarning("Cadastro",msg)
            return False
        else:
            return True

app = Cadastro()
app.mainloop()