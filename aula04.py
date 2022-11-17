
#1o. passo: importar a biblioteca sqlite3
import sqlite3

#2o. passo: Vamos estabelecer uma 
#conexão com o banco de dados
conexao = sqlite3.connect("dc_universe.db")

#3o. passo: criar um objeto do tipo cursor
cursor = conexao.cursor()

sql = " INSERT INTO pessoas  (pessoa_id, nome, nome_civil, tipo) VALUES (12,'Flash', 'Vini Nobre' ,'Herói(na)')   "


cursor.execute(sql)



conexao.commit()
conexao.close()

