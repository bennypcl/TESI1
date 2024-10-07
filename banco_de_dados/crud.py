from conexao import Conexao
from sqlite3 import Error

class Crud:
    def __init__(self):
        self.conexao = Conexao()
    # Inserir
    # conectar, usar a conexao e fechar
    def insert(self):
        sql = """INSERT INTO cliente (nome, cpf, email) VALUES ('Fulano', 123, 'fulano@ufac.br')"""
        try:
            con = self.conexao.get_conexao()
            cursor = con.cursor()
            cursor.execute(sql)
            con.commit()
            con.close()
        except Error as er:
            print(er)

    # Listar
    def get(self):
        sql = """SELECT * FROM cliente;"""
        try:
            con = self.conexao.get_conexao()
            cursor = con.cursor()
            cursor.execute(sql)
            resultado = cursor.fetchall() #Retorna uma lista
            con.close()
            return resultado
        except Error as er:
            print(er)
    # Atualizar
    def update(self):
        sql = """UPDATE cliente SET nome ='Chaves', email ='keys@keyboard' WHERE id == 9;"""
        try:
            con = self.conexao.get_conexao()
            cursor = con.cursor()
            cursor.execute(sql)
            if cursor.rowcount == 1:
                con.commit()
                print('Registro atualizado com sucesso.')
            con.close()
        except Error as er:
            print(er)

    # Excluir
    def delete(self):
        sql = """DELETE FROM cliente WHERE id=5;"""
        try:
            con = self.conexao.get_conexao()
            cursor = con.cursor()
            cursor.execute(sql)
            if cursor.rowcount == 1:
                con.commit()
                print('Registro Excluido com sucesso.')
            con.close()
        except Error as er:
            print(er)

# teste = Conexao().get_conexao()
crud = Crud()
# crud.insert()
# crud.delete()
crud.update()
lista = crud.get()
for item in lista:
    print(item)
