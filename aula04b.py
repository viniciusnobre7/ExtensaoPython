import sqlite3




conexao = sqlite3.connect("dc_universe.db")


cursor = conexao.cursor()


sql = " INSERT INTO pessoas  (pessoa_id, nome, nome_civil, tipo) VALUES (12,'Flash', 'Vini Nobre' ,'Herói(na)')   "


cursor.execute(sql)



conexao.commit()
conexao.close()