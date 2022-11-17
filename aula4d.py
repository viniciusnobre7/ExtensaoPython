import aula4c

con, cur = aula4c.conectar() 

nome = input("Informe o nome do herói/vilão: ")
nome_civil = input("Informe o nome civil do herói/ (identidade secreta): ")
tipo_numerico = input("Tecle 1 para herói(na) ou 2 para vilão ")


sql = "SELECT MAX(pessoa_id)+1 FROM pessoas"
cur.execute (sql)
pessoa_id = cur.fetchone() [0]


if tipo_numerico == "1"
   tipo = "Herói(na)"
else
   tipo = "vilão"

sql = f"INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES ({pessoa_id}, '{nome}', '{nome_civil}', '{tipo}')"


cur.execute(sql)
con.commit()
con.close()