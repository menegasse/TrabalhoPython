from tkinter import *
from tkinter import messagebox as msgbox
from Banco import *
from string import punctuation

class Sistema(Frame):
    def __init__(self):
        self.TelaLogin = Tk()
        self.TelaLogin.geometry("350x275") #define o tamanho da tela
        self.TelaLogin.title("Login Lozinho") #titulo da janela
        self.TelaLogin.resizable(False,False)
        

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

        self.TelaLogin.mainloop()
        
    def btnEntrarClick(self,event):
        bd = Banco()
        user = self.entry_usuario.get()
        pas = self.entry_senha.get()

        try:
           if not len(bd.verificar_user(user,pas)) == 0:
               self.limpar_campo_login()
               msgbox.showinfo("Welcome","Seja Bem-Vindo!")
               self.TelaLogin.destroy()
               self.TelaMenu()
           else:
               self.limpar_campo_login()
               msgbox.showerror("Erro","Usuário ou Senha invalida!")
        except ValueError:
            msgbox.showerror("Erro","Usuário ou Senha invalida!")
        
    def limpar_campo_login(self):
        self.entry_usuario.delete(0,'end')
        self.entry_senha.delete(0,'end')
        self.entry_usuario.focus_set()

    def btnEsqueceuClick(self,event):
        self.TelaLogin.destroy()
        self.TelaRecuperaSenha()

    def btnCadastrarClick(self,event):
        self.TelaLogin.destroy()
        self.TelaCadastro()




################################ TELA MENU ################################


    def TelaMenu(self):
        self.Menu = Tk()
        self.Menu.geometry("350x275") #define o tamanho da tela
        self.Menu.title("Lolzinho") #titulo da janela
        self.Menu.resizable(False,False)

        #Monta o Frame do Titulo
        self.f_titulo = Frame(height=60)
        self.f_titulo.pack(fill=X)

        self.l_titulo = Label(self.f_titulo)
        self.l_titulo['text'] = "Menu"
        self.l_titulo['font'] = "Helvetica 26 bold"
        self.l_titulo.pack(ipady=15)
        
        #Opção Menus
        self.bnt1_frame = Frame(height=30)
        self.bnt1_frame.pack(fill=X)

        self.bntMaestria = Button(self.bnt1_frame,text=" Maestria ",width=30)
        self.bntMaestria.bind("<Button-1>",self.btnMaestriaClick)
        self.bntMaestria.pack(pady=5)

        self.bnt2_frame = Frame(height=30)
        self.bnt2_frame.pack(fill=X)

        self.bntLigas = Button(self.bnt2_frame,text=" Ligas ",width=30)
        self.bntLigas.bind("<Button-1>",self.btnLigasClick)
        self.bntLigas.pack(pady=5)

        self.bnt3_frame = Frame(height=30)
        self.bnt3_frame.pack(fill=X)

        self.bntHistorico = Button(self.bnt3_frame,text=" Historico de Partida ",width=30)
        self.bntHistorico.bind("<Button-1>",self.btnHistoricoClick)
        self.bntHistorico.pack(pady=5)

        self.bnt4_frame = Frame(height=30)
        self.bnt4_frame.pack(fill=X)

        self.bntPartida = Button(self.bnt4_frame,text=" Partida Ativa ",width=30)
        self.bntPartida.bind("<Button-1>",self.btnPartidaClick)
        self.bntPartida.pack(pady=5)

        self.bnt5_frame = Frame(height=30)
        self.bnt5_frame.pack(fill=X)

        self.bntSobre = Button(self.bnt5_frame,text=" Sobre ",width=30)
        self.bntSobre.bind("<Button-1>",self.btnSobreClick)
        self.bntSobre.pack(pady=5)

        self.Menu.mainloop()

    def btnMaestriaClick(self,event):
        pass

    def btnLigasClick(self,event):
        pass

    def btnHistoricoClick(self,event):
        pass

    def btnPartidaClick(self,event):
        pass

    def btnSobreClick(self,event):
        self.Menu.destroy()
        self.TelaSobre()


################################ TELA CADASTRO ################################

    def TelaCadastro(self):
        self.Cadastro = Tk()
        self.Cadastro.geometry("400x425") #define o tamanho da tela
        self.Cadastro.title("Cadastro") #titulo da janela
        self.Cadastro.resizable(False,False)

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
        
        ##Campo Email
        self.f_email = Frame(height =60)
        self.f_email.pack(fill=X,padx=10,pady=10)

        self.lb_email = Label(self.f_email)
        self.lb_email['text'] = "Email:"
        self.lb_email['font'] = "Helvetica 12"
        self.lb_email.grid(row=0)
        #Campo de entrada de dado
        self.entry_email = Entry(self.f_email,width=30,bg="#DEDEDE",font=("Helvetica",12))
        self.entry_email.grid(row=1,padx=21)
        self.entry_email.focus_set()
        

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
        self.bnt_frame.pack(fill=X,padx=15,pady=10)

        self.bnt_Cadastrar = Button(self.bnt_frame,text="Cadastrar",width=15)
        self.bnt_Cadastrar.bind("<Button-1>",self.btn_CadastrarClick)
        self.bnt_Cadastrar.grid(row=0,column=1,padx=5)

        self.bnt_Cadastrar = Button(self.bnt_frame,text="Cancelar",width=15)
        self.bnt_Cadastrar.bind("<Button-1>",self.btn_CancelarClick_Cadastro)
        self.bnt_Cadastrar.grid(row=0,column=0,padx=5)

        self.Cadastro.mainloop()
        
    def limpar_campos_cadastro(self):
        self.entry_idade.delete(0,'end')
        self.entry_usuario.delete(0,'end')
        self.entry_nome_completo.delete(0,'end')
        self.entry_senha.delete(0,'end')
        self.entry_c_senha.delete(0,'end')
        self.entry_email.delete(0,'end')
        
    def btn_CancelarClick_Cadastro(self,event):
        self.Cadastro.destroy()
        self.__init__()

    def btn_CadastrarClick(self,event):
        idade = 0 if self.entry_idade.get() ==  "" else self.entry_idade.get()
        usuario = self.entry_usuario.get()
        nome = self.entry_nome_completo.get()
        senha = self.entry_senha.get()
        c_senha = self.entry_c_senha.get()
        email = self.entry_email.get()

        if self.VerificaCampos(idade,usuario,nome,senha,c_senha,email) == True:
            bd = Banco()
            bd.cadastrar_user(idade,usuario,nome,senha,email)
            msgbox.showinfo("Cadastro","Cadastro Realizado com Sucesso!")
            self.limpar_campos_cadastro()
        else:
            self.limpar_campos_cadastro()

    def VerificaCampos(self,idade=0,user_name='',nome_user="",senha='',c_senha='',email=''):
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
        
        if email == "":
            msg = msg + "-Campo email invalido!\n"

        if not msg == "":
            msgbox.showwarning("Cadastro",msg)
            return False
        else:
            return True

##########################################  TELA RECURPERAR SENHA  ##########################################

    def TelaRecuperaSenha(self):
        self.Recupera = Tk()
        self.Recupera.geometry("475x100") #define o tamanho da tela
        self.Recupera.title("Recuperar Senha") #titulo da janela
        self.Recupera.resizable(False,False)
        

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
        self.bnt_Cadastrar.bind("<Button-1>",self.btn_EnviarClick)
        self.bnt_Cadastrar.pack(side=RIGHT,pady=5)

        self.bnt_Cancelar = Button(self.f_bnt,text="Cancelar",width=15)
        self.bnt_Cancelar.bind("<Button-1>",self.btn_CancelarClick)
        self.bnt_Cancelar.pack(side=RIGHT,padx=5,pady=5)

        self.Recupera.mainloop()

    def btn_EnviarClick(self,event):
        pass
    def btn_CancelarClick(self,event):
        self.Recupera.destroy()
        self.__init__()
#################################################### TELA SOBRE ####################################################

    def TelaSobre(self,master=None):
        self.Sobre = Tk()
        self.Sobre.geometry("475x275") #define o tamanho da tela
        self.Sobre.title("Recuperar Senha") #titulo da janela
        self.Sobre.resizable(False,False)

        #Monta o Frame do Titulo
        self.f_titulo = Frame(height=60)
        self.f_titulo.pack(fill=X)

        self.l_titulo = Label(self.f_titulo)
        self.l_titulo['text'] = "O Aplicativo desenvolvido tem o objetivo de mostrar informações\nsobre os jogadores do jogo League of Leagend, atraves do\nconsumo da API da RiotGames (desenvolvedora do jogo) e de\nalgumas API terceiras!\n\n\nAlunos: \n\n-Hugo Cossalter Menegasse RA:2840481621016\n\n-Lucas (Cardosinho) RA:?"
        self.l_titulo['font'] = "Helvetica 12"
        self.l_titulo.pack(side=LEFT,pady=10)

        self.f_btn = Frame(height=60)
        self.f_btn.pack(fill=X)

        self.btn = Button(self.f_btn,text=" Voltar ",width=15)
        self.btn.bind("<Button-1>",self.btnVoltarClick)
        self.btn.pack()

        self.Sobre.mainloop()

    def btnVoltarClick(self,event):
        self.Sobre.destroy()
        self.TelaMenu()

app = Sistema()