from tkinter import *
from tkinter import messagebox as msgbox


class Menu(Frame):
    def __init__(self,master=None):
        super().__init__()
        self.master.geometry("350x275") #define o tamanho da tela
        self.master.title("Lolzinho") #titulo da janela
        self.master.resizable(False,False)
        self.pack()

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

    def btnMaestriaClick(self):
        pass

    def btnLigasClick(self):
        pass

    def btnHistoricoClick(self):
        pass

    def btnPartidaClick(self):
        pass

    def btnSobreClick(self):
        pass
    