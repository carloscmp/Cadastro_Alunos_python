import sqlite3

# criando conexão
try:
    con = sqlite3.connect('cadastro_alunos.db')
    print('Conexão com banco de dados feita com sucesso')
except sqlite3.Error as e:
    print("Erro ao conctar com banco de dados", e)

    # CRUD tabela de cursos

    # Criar Cursos(Create)

def criar_curso(i):
    with con:
        cur = con.cursor()
        query = "insert into cursos (nome, duracao,preco) values (?, ?, ?)"
        cur.execute(query,i)

#criar_curso(['Python', '2 Semanas', 50])

#Ver todos os cursos(Read)
def ver_cursos():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute("select * from cursos")
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista

#print(ver_cursos())

#atualizar cursos (Update)
def update_cursos(i):
    with con:
        cur = con.cursor()
        query = "UPDATE cursos SET nome = ?, duracao = ?, preco = ? WHERE id = ?"
        cur.execute(query,i)


#Deletar curso(Delete)
def deletar_curso(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM cursos WHERE id = ?"
        cur.execute(query,i)

#delete_curso([])


# CRUD tabela de turma---------------------------------

# Adicionar turma(Create)
def criar_turmas(i):
    with con:
        cur = con.cursor()
        query = "insert into turmas (nome, curso_nome, data_inicio) values (?, ?, ?)"
        cur.execute(query,i)

#Ver todas as turmas(Read)
def ver_turmas():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute("select * from turmas order by nome")
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista

#atualizar turmas (Update)
def update_turmas(i):
    with con:
        cur = con.cursor()
        query = "UPDATE turmas SET nome = ?, curso_nome = ?, data_inicio = ? WHERE id = ?"
        cur.execute(query,i)

#Deletar curso(Delete)
def delete_turma(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM turmas WHERE id = ?"
        cur.execute(query,i)

#Tabela de Alunos------------------------

# Adicionar turma(Create)
def criar_aluno(i):
    with con:
        cur = con.cursor()
        query = "insert into alunos (nome, email, telefone, sexo, imagem, data_nascimento, cpf, turma_nome) values (?, ?, ?, ?, ?, ?, ?, ?)"
        cur.execute(query,i)

#Ver todos alunos(Read)
def ver_alunos():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute("select * from alunos order by nome")
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista

#atualizar alunos (Update)
def update_alunos(i):
    with con:
        cur = con.cursor()
        query = "UPDATE alunos SET nome = ?, email = ?, telefone = ?, sexo = ?, imagem = ?, data_nascimento = ?, cpf = ?, turma_nome = ? WHERE id = ?"
        cur.execute(query,i)

#Deletar alunos(Delete)
def delete_alunos(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM alunos WHERE id = ?"
        cur.execute(query,i)