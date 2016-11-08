import sqlite3

#conecta ao banco
conn = sqlite3.connect('clientes.db')

#definindo um cursor(interador q permite navegar e manipular os registros do bd)
cursor = conn.cursor()

#criando a tabela #execute ( le e executa comandos SQL puro diretamento no bd)
cursor.execute("""
CREATE TABLE clientes(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nome TEXT NOT NULL,
	idade INTEGER,
	cpf VARCHAR(11) NOT NULL,
	email TEXT NOT NULL,
	fone TEXT,
	cidade TEXT,
	uf VARCHAR(2) NOT NULL,
	criado_em DATE NOT NULL
);
""")

print('Tabela criada com sucesso.')

#desconecta o banco
conn.close()
