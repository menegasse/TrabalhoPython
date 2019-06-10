import psycopg2 as pg

class Banco():
    connection =""
    def __init__(self):
           try: 
            self.connection = pg.connect(
                database = "db_lolzim",
                user = "postgres",
                password="root",
                host="127.0.0.1",
                port='5432'
            )

           except Exception as erro:
               print(erro) 
    def cadastrar_user(self,idade=0,user_name='',nome_user='',senha='',email=''):
        sql = "INSERT INTO tb_usuario(id_user,idade,user_name,nome_user,senha,email) values (DEFAULT,%s,%s,%s,%s,%s)"
        cur = self.connection.cursor()
        cur.execute(cur.mogrify(sql,(idade,user_name,nome_user,senha,email)))
        self.connection.commit()
        self.connection.close()

    def verificar_user(self,user_name,senha):
        sql ="SELECT user_name FROM tb_usuario WHERE user_name = %s AND senha = %s"
        cur = self.connection.cursor()
        cur.execute(cur.mogrify(sql,(user_name,senha)))
        linha = cur.fetchall()
        self.connection.close()
        return linha 
    
    def recupera_senha(self,email=''):
         sql =f"SELECT senha FROM tb_usuario WHERE email = '{email}'"
         cur = self.connection.cursor()
         cur.execute(cur.mogrify(sql))
         linha = cur.fetchall()
         self.connection.close()
         return linha 