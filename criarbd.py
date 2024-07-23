# importando sqlite3
import sqlite3
from sqlite3 import connect

# criando conexão
try:
    con = sqlite3.connect('cadastro_alunos.db')
    print('Conexão com banco de dados feita com sucesso')
except sqlite3.Error as e:
    print("Erro ao conctar com banco de dados", e)

# criando tabela de curso
try:
    with con:
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS cursos(
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           nome TEXT,
           duracao TEXT,
           preco REAL
           )''')
        print('Table Cursos criada com sucesso')

except sqlite3.Error as e:
    print("Erro ao criar tabela de cursos", e)

    # criando tabela de turmas
try:
    with con:
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS turmas(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT,
               curso_nome TEXT,
               data_inicio DATE,
               FOREIGN KEY(curso_nome) REFERENCES cursos (nome) ON UPDATE CASCADE ON DELETE CASCADE
               )''')
        print('Table Turmas criada com sucesso')

except sqlite3.Error as e:
    print("Erro ao criar tabela de Turmas", e)


    # criando tabela de alunos
try:
    with con:
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS alunos(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT,
               email TEXT,
               telefone TEXT,
               sexo TEXT,
               imagem TEXT,
               data_nascimento DATA,
               cpf TEXT,
               turma_nome TEXT,               
               FOREIGN KEY(turma_nome) REFERENCES turmas (nome) ON DELETE CASCADE
               )''')
        print('Table Alunos criada com sucesso')

except sqlite3.Error as e:
    print("Erro ao criar tabela de Alunos", e)