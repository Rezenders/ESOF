import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

cursor.execute("""
ALTER TABLE clientes 
ADD COLUMN bloqueado BOOLEAN;
""")

conn.commit()
print('Nova coluna adicionada')
conn.close()
