from tkinter import *
from tkinter import messagebox as msgbox


class Sobre(Frame):

    def __init__(self,master=None):
        super().__init__()
        self.master.geometry("475x275") #define o tamanho da tela
        self.master.title("Recuperar Senha") #titulo da janela
        self.master.resizable(False,False)
        self.pack()

        #Monta o Frame do Titulo
        self.f_titulo = Frame(height=60)
        self.f_titulo.pack(fill=X)

        self.l_titulo = Label(self.f_titulo)
        self.l_titulo['text'] = "O Aplicativo desenvolvido tem o objetivo de mostrar informações\nsobre os jogadores do jogo League of Leagend, atraves do\nconsumo da API da RiotGames (desenvolvedora do jogo) e de\nalgumas API terceiras!\n\n\nAlunos: \n\n-Hugo Cossalter Menegasse RA:2840481621016\n\n-Lucas Cardoso de Assis(Cardosinho) RA:2840481613024"
        self.l_titulo['font'] = "Helvetica 12"
        self.l_titulo.pack(side=LEFT,pady=10)

        self.f_btn = Frame(height=60)
        self.f_btn.pack(fill=X)

        self.btn = Button(self.f_btn,text=" Voltar ",width=15)
        self.btn.bind("<Button-1>",self.btnVoltarClick)
        self.btn.pack()
    
    def btnVoltarClick(self,event):
        pass

app = Sobre()
app.mainloop()
