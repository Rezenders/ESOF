import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

id_cliente = 1
novo_fone = '11-1000-2014'
novo_criado_em = '2016-11-08'

cursor.execute("""
UPDATE clientes
SET fone = ?, criado_em = ?
WHERE id = ?
""", (novo_fone, novo_criado_em, id_cliente))

conn.commit()
print('dados atualizados')
conn.close()

