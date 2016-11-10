import os
import sqlite3
import io
import datetime
import names
import csv
from gen_random_values import *

class Connect(object):
	
	def __init__(self, db_name):
		try:
			#conecta
			self.conn = sqlite3.connect(db_name)
			self.cursor= self.conn.cursor()
			
			#printa nome do bd
			print("Banco:",db_name)
			
			#lendo a versão do SQLite
			self.cursor.execute('SELECT SQLITE_VERSION()')
			self.data = self.cursor.fetchone()
			
			#imprimindo a versao do SQLite
			print("SQLite version: %s" % self.data)
		
		except sqlite3.Error:
			print("Erro ao abrir banco.")
			return False
			
	def close_db(self):
		if self.conn:
			self.conn.close()
			print("Conexão fechada.")
			
class ClientesDb(object):
	tb_name = 'clientes'
	
	def __init__(self):
		self.db = Connect('clientes.db')
		self.tb_name
	
	def fechar_conexao(self):
		self.db.close_db()

	def criar_schema(self, schema_name='sql/clientes_schema.sql'):
		print("Criando tabela %s ..." % self.tb_name)
		
		try:
			with open(schema_name, 'rt') as f:
				schema = f.read()
				self.db.cursor.executescript(schema)
		except sqlite3.Error:
			print("Aviso: A tabela %s já existe." % self.tb_name)
			return False
			
		print("Tabela %s criada com sucesso."% self.tb_name)
	
	def inserir_um_registro(self):
		try:
			self.db.cursor.execute("""
			INSERT INTO clientes (nome, idade, cpf, email,
			VALUES ('Regis da Silva', 35, '12345678901', 'regis@email.com', '(11) 9876-5342', 'São Paulo', 'SP', '2014-07-30 11:23:00.199000')
			""")
			
			self.db.commit_db()
			print("Um registro inserido com sucesso.")
		
		except sqlite3.IntegrityError:
			print("Aviso: O email deve ser único.")
			return False
			
		
		
if __name__ == '__main__':
	c = ClientesDb()	
	c.criar_schema()
	c.inserir_um_registro()
