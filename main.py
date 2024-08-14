from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
from PIL import ImageTk, Image
from tkcalendar import Calendar, DateEntry
from datetime import date

from view import criar_curso, ver_cursos, update_cursos, deletar_curso

# cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"  # letra
co6 = "#003452"  # azul
co7 = "#ef5350"  # vermelha

co6 = "#038cfc"  # azul
co8 = "#263238"  # + verde
co9 = "#e9edf5"  # + verde

# Criando Janela
janela = Tk()
janela.title('')
janela.geometry('850x620')
janela.configure(background=co1)
janela.resizable(width=False, height=False)

style = Style(janela)
style.theme_use('clam')

# Criando frames
frame_logo = Frame(janela, width=850, height=52, bg=co6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680)

frame_dados = Frame(janela, width=850, height=65, bg=co1)
frame_dados.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=3, columnspan=1, ipadx=680)

frame_detalhes = Frame(janela, width=850, height=200, bg=co1)
frame_detalhes.grid(row=4, column=0, pady=0, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=850, height=200, bg=co1)
frame_tabela.grid(row=5, column=0, pady=0, padx=10, sticky=NSEW)

# trabalhando no frame logo
app_lg = Image.open('logo.png')
app_lg = app_lg.resize((50, 50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text="Cadastro de Alunos", width=850, compound=LEFT, relief=RAISED,
                 anchor=NW, font=('Ivy 15 bold'), bg=co6, fg=co1)
app_logo.place(x=0, y=0)


# função para cadastrar alunos
def alunos():
    # Criando campos de entrada
    l_nome = Label(frame_detalhes, text="Nome *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_nome.place(x=4, y=10)
    e_nome = Entry(frame_detalhes, width=45, justify=LEFT, relief='solid')
    e_nome.place(x=7, y=40)

    l_nome = Label(frame_detalhes, text="E-mail *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_nome.place(x=4, y=70)
    e_email = Entry(frame_detalhes, width=45, justify=LEFT, relief='solid')
    e_email.place(x=7, y=100)

    l_tel = Label(frame_detalhes, text="Telefone *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_tel.place(x=4, y=130)
    e_tel = Entry(frame_detalhes, width=20, justify=LEFT, relief='solid')
    e_tel.place(x=7, y=160)

    # Seleção de sexo
    l_sexo = Label(frame_detalhes, text="Sexo", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_sexo.place(x=190, y=130)
    c_sexo = Combobox(frame_detalhes, width=12, font=('Ivy 8 bold'))
    c_sexo['values'] = ('Masculino', 'Feminino')
    c_sexo.place(x=190, y=160)

    # seleção data de nascimento
    l_data_nascimento = Label(frame_detalhes, text="Data de nascimento", height=1, anchor=NW, font=('Ivy 10'), bg=co1,
                              fg=co4)
    l_data_nascimento.place(x=446, y=10)
    data_nascimento = DateEntry(frame_detalhes, width=18, backgound='darblue', foreground='white', borderwidth=2,
                                year=2024)
    data_nascimento.place(x=450, y=40)

    l_cpf = Label(frame_detalhes, text="CPF", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_cpf.place(x=446, y=70)
    e_cpf = Entry(frame_detalhes, width=20, justify=LEFT, relief='solid')
    e_cpf.place(x=450, y=100)

    # Selecionando turma
    turmas = ['Turma A', 'Turma B']
    turma = []

    for i in turmas:
        turma.append(i)

    l_turma = Label(frame_detalhes, text="Turma", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_turma.place(x=446, y=130)
    c_turma = Combobox(frame_detalhes, width=20, font=('Ivy 8 bold'))
    c_turma['values'] = (turma)
    c_turma.place(x=450, y=160)

    # função para escolher imagem
    global imagem, imagem_string, l_imagem

    def escolher_imagem():
        global imagem, imagem_string, l_imagem
        imagem = fd.askopenfilename()
        imagem_string = imagem

        # abrindo imgem
        imagem = Image.open(imagem)
        imagem = imagem.resize((130, 130))
        imagem = ImageTk.PhotoImage(imagem)
        l_imagem = Label(frame_detalhes, image=imagem, bg=co1, fg=co4)
        l_imagem.place(x=300, y=10)

        botao_carregar['text'] = 'Alterar Foto'.upper()

    botao_carregar = Button(frame_detalhes, command=escolher_imagem, text='Carregar Foto'.upper(), width=20,
                            compound=CENTER, anchor=CENTER, overrelief=RIDGE,
                            font=('Ivy 7'), bg=co1, fg=co0)
    botao_carregar.place(x=300, y=160)

    # linha separatoria
    l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co0,
                    fg=co0)
    l_linha.place(x=610, y=10)

    l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co1,
                    fg=co0)
    l_linha.place(x=608, y=10)

    l_nome = Label(frame_detalhes, text="Procurar Aluno [ Digite o nome ]", height=1, anchor=NW, font=('Ivy 10'),
                   bg=co1, fg=co4)
    l_nome.place(x=627, y=10)
    e_nome_procurar = Entry(frame_detalhes, width=17, justify='center', relief='solid', font=('Ivy 10'))
    e_nome_procurar.place(x=630, y=35)

    # botao procurar foto
    botao_procurar = Button(frame_detalhes, anchor=CENTER, text='Procurar'.upper(), width=9, overrelief=RIDGE,
                            font=('Ivy 7 bold'), bg=co3, fg=co1)
    botao_procurar.place(x=757, y=35)

    # Botoes
    # botao salvar
    botao_salvar = Button(frame_detalhes, anchor=CENTER, text='Salvar'.upper(), width=9,
                          overrelief=RIDGE,
                          font=('Ivy 7 bold'), bg=co3, fg=co1)
    botao_salvar.place(x=627, y=110)

    # botao atualzar
    botao_atualizar = Button(frame_detalhes, anchor=CENTER, text='Atualizar'.upper(), width=9, overrelief=RIDGE,
                             font=('Ivy 7 bold'), bg=co6, fg=co1)
    botao_atualizar.place(x=627, y=135)

    # botao deletar
    botao_deletar = Button(frame_detalhes, anchor=CENTER, text='Deletar'.upper(), width=9, overrelief=RIDGE,
                           font=('Ivy 7 bold'), bg=co7, fg=co1)
    botao_deletar.place(x=627, y=160)

    # botao ver
    botao_ver = Button(frame_detalhes, anchor=CENTER, text='Ver'.upper(), width=9, overrelief=RIDGE,
                       font=('Ivy 7 bold'), bg=co1, fg=co0)
    botao_ver.place(x=727, y=160)

    # mostrar alunos
    def mostrar_alunos():
        app_nome = Label(frame_tabela, text="Tabela de estudantes", height=1, pady=0, padx=0, relief="flat", anchor=NW,
                         font=('Ivy 10 bold'), bg=co1, fg=co4)
        app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        list_header = ['id', 'Nome', 'email', 'Telefone', 'sexo', 'imagem', 'Data', 'CPF', 'Curso']

        df_list = []

        global tree_curso

        tree_aluno = ttk.Treeview(frame_tabela, selectmode="extended", columns=list_header, show="headings")

        vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_aluno.yview)

        hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_aluno.xview)

        tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree_aluno.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_tabela.grid_rowconfigure(0, weight=12)

        hd = ["nw", "nw", "nw", "center", "center", "center", "center", "center", "center"]
        h = [40, 150, 150, 70, 70, 70, 80, 80, 100]
        n = 0

        for col in list_header:
            tree_aluno.heading(col, text=col.title(), anchor=NW)
            tree_aluno.column(col, width=h[n], anchor=hd[n])

            n += 1

        for item in df_list:
            tree_aluno.insert('', 'end', values=item)

    mostrar_alunos()


# função para adicionar cursos e turmas
def adicionar():
    # Criando frames para tabelas
    frame_tabela_curso = Frame(frame_tabela, width=300, height=200, bg=co1)
    frame_tabela_curso.grid(row=0, column=0, pady=0, padx=10, sticky=NSEW)

    frame_tabela_linha = Frame(frame_tabela, width=30, height=200, bg=co1)
    frame_tabela_linha.grid(row=0, column=1, pady=0, padx=10, sticky=NSEW)

    frame_tabela_turma = Frame(frame_tabela, width=300, height=200, bg=co1)
    frame_tabela_turma.grid(row=0, column=2, pady=0, padx=10, sticky=NSEW)

    # detalhes do curso

    def novo_curso():
        nome = e_nome_curso.get()
        duracao = e_duracao.get()
        preco = e_preco.get()

        lista = [nome, duracao, preco]

        # verificando se os valores estão vazios
        for item in lista:
            if item == "":
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return

        # inserindo dados
        criar_curso(lista)
        # mensagem de sucesso
        messagebox.showinfo('Sucesso', 'O dados foram inseridos com sucesso')

        e_nome_curso.delete(0, END)
        e_duracao.delete(0, END)
        e_preco.delete(0, END)

        # mostrando valores na tabela
        mostrar_cursos()

        # Atualizar curso

    def update_curso():
        try:
            tree_itens = tree_curso.focus()
            tree_dicionario = tree_curso.item(tree_itens)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]

            # inserindo os valores na entry
            e_nome_curso.insert(0, tree_lista[1])
            e_duracao.insert(0, tree_lista[2])
            e_preco.insert(0, tree_lista[3])

            # função atualizar
            def update():

                nome = e_nome_curso.get()
                duracao = e_duracao.get()
                preco = e_preco.get()

                lista = [nome, duracao, preco, valor_id]

                # verificando se os valores estão vazios
                for i in lista:
                    if i == "":
                        messagebox.showerror('Erro', 'Preencha todos os campos')
                        return

                # inserindo dados
                update_cursos(lista)
                # mensagem de sucesso
                messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

                e_nome_curso.delete(0, END)
                e_duracao.delete(0, END)
                e_preco.delete(0, END)

                # mostrando valores na tabela
                mostrar_cursos()

                # destruindo botao salvar apos salvar os dados
                botao_salvar.destroy()

            botao_salvar = Button(frame_detalhes, command=update, anchor=CENTER, text='Salvar Atualização'.upper(),
                                  overrelief=RIDGE,
                                  font=('Ivy 7 bold'), bg=co3, fg=co1)
            botao_salvar.place(x=227, y=130)
        except IndexError:
            messagebox.showerror('Erro', 'Selecione um dos cursos da tabela')

    # função deletar curso
    def delete_curso():
        try:
            tree_itens = tree_curso.focus()
            tree_itens = tree_curso.focus()
            tree_dicionario = tree_curso.item(tree_itens)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]

            # deletando dados co banco de dados
            deletar_curso([valor_id])
            # mensagem de sucesso
            messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso')
            # mostrando valores na tabela
            mostrar_cursos()
        except IndexError:
            messagebox.showerror('Erro', 'Selecione um dos cursos da tabela')

    l_nome = Label(frame_detalhes, text="Nome do Curso", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_nome.place(x=4, y=10)
    # textfield curso
    e_nome_curso = Entry(frame_detalhes, width=35, justify=LEFT, relief='solid')
    e_nome_curso.place(x=7, y=40)

    l_duracao = Label(frame_detalhes, text="Duração", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_duracao.place(x=4, y=70)
    e_duracao = Entry(frame_detalhes, width=20, justify=LEFT, relief='solid')
    e_duracao.place(x=7, y=100)

    l_nome = Label(frame_detalhes, text="Preço", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_nome.place(x=4, y=130)
    e_preco = Entry(frame_detalhes, width=10, justify=LEFT, relief='solid')
    e_preco.place(x=7, y=160)

    # botoa carregar
    botao_carregar = Button(frame_detalhes, command=novo_curso, anchor=CENTER, text='Novo'.upper(), width=10,
                            overrelief=RIDGE,
                            font=('Ivy 7 bold'), bg=co3, fg=co1)
    botao_carregar.place(x=107, y=160)

    # botao atualizar
    botao_atualizar = Button(frame_detalhes, command=update_curso, anchor=CENTER, text='Atualizar'.upper(), width=10,
                             overrelief=RIDGE,
                             font=('Ivy 7 bold'), bg=co6, fg=co1)
    botao_atualizar.place(x=187, y=160)

    # botao carregar
    botao_deletar = Button(frame_detalhes, command=delete_curso, anchor=CENTER, text='Deletar'.upper(), width=10,
                           overrelief=RIDGE,
                           font=('Ivy 7 bold'), bg=co7, fg=co1)
    botao_deletar.place(x=267, y=160)

    # Tabela Cursos

    def mostrar_cursos():
        app_nome = Label(frame_tabela_curso, text="Tabela de Cursos", height=1, pady=0, padx=0, relief="flat",
                         anchor=NW,
                         font=('Ivy 10 bold'), bg=co1, fg=co4)
        app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        # creating a treeview with dual scrollbars
        list_header = ['ID', 'Curso', 'Duração', 'Preço']

        df_list = ver_cursos()

        global tree_curso

        tree_curso = ttk.Treeview(frame_tabela_curso, selectmode="extended", columns=list_header, show="headings")

        # vertical scrollbar
        vsb = ttk.Scrollbar(frame_tabela_curso, orient="vertical", command=tree_curso.yview)
        # horizontal scrollbar
        hsb = ttk.Scrollbar(frame_tabela_curso, orient="horizontal", command=tree_curso.xview)

        tree_curso.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree_curso.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_tabela_curso.grid_rowconfigure(0, weight=12)

        hd = ["nw", "nw", "e", "e"]
        h = [30, 150, 80, 60]
        n = 0

        for col in list_header:
            tree_curso.heading(col, text=col.title(), anchor=NW)
            # adjust the column's width to the header string
            tree_curso.column(col, width=h[n], anchor=hd[n])

            n += 1

        for item in df_list:
            tree_curso.insert('', 'end', values=item)

    mostrar_cursos()

    # linha separatoria
    l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co0,
                    fg=co0)
    l_linha.place(x=374, y=10)

    l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co1,
                    fg=co0)
    l_linha.place(x=372, y=10)

    # linha separatoria tabela
    l_linha = Label(frame_tabela_linha, relief=GROOVE, text='h', width=1, height=140, anchor=NW, font=('Ivy 1'), bg=co0,
                    fg=co0)
    l_linha.place(x=6, y=10)

    l_linha = Label(frame_tabela_linha, relief=GROOVE, text='h', width=1, height=140, anchor=NW, font=('Ivy 1'), bg=co1,
                    fg=co0)
    l_linha.place(x=4, y=10)

    # Detalhes da turma
    l_nome = Label(frame_detalhes, text="Nome da turma", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_nome.place(x=404, y=10)
    e_nome_turma = Entry(frame_detalhes, width=35, justify='left', relief="solid")
    e_nome_turma.place(x=407, y=40)

    l_turma = Label(frame_detalhes, text="Curso", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_turma.place(x=404, y=70)

    # cursos
    cursos = ['curso 1', 'curso 2']
    curso = []

    for i in cursos:
        curso.append(i)

    c_curso = Combobox(frame_detalhes, width=20, font=('Ivy 8 bold'))
    c_curso['values'] = (curso)
    c_curso.place(x=407, y=90)

    l_data_inicio = Label(frame_detalhes, text="Data de inicio", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_data_inicio.place(x=404, y=120)
    data_incio = DateEntry(frame_detalhes, width=10, backgound='darblue', foreground='white', borderwidth=2, year=2024)
    data_incio.place(x=406, y=150)

    # botoes turma

    # botoa carregar
    botao_carregar = Button(frame_detalhes, anchor=CENTER, text='Salvar'.upper(), width=10, overrelief=RIDGE,
                            font=('Ivy 7 bold'), bg=co3, fg=co1)
    botao_carregar.place(x=545, y=150)

    # botao atualizar
    botao_atualizar = Button(frame_detalhes, anchor=CENTER, text='Atualizar'.upper(), width=10, overrelief=RIDGE,
                             font=('Ivy 7 bold'), bg=co6, fg=co1)
    botao_atualizar.place(x=625, y=150)

    # botao carregar
    botao_carregar = Button(frame_detalhes, anchor=CENTER, text='Deletar'.upper(), width=10, overrelief=RIDGE,
                            font=('Ivy 7 bold'), bg=co7, fg=co1)
    botao_carregar.place(x=705, y=150)

    # Tabela Turmas

    def mostrar_turmas():
        app_nome = Label(frame_tabela_turma, text="Tabela de Turmas", height=1, pady=0, padx=0, relief="flat",
                         anchor=NW,
                         font=('Ivy 10 bold'), bg=co1, fg=co4)
        app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        # creating a treeview with dual scrollbars
        list_header = ['ID', 'Nome da turma', 'Curso', 'Inicio']

        df_list = []

        global tree_turma

        tree_turma = ttk.Treeview(frame_tabela_turma, selectmode="extended", columns=list_header, show="headings")

        # vertical scrollbar
        vsb = ttk.Scrollbar(frame_tabela_turma, orient="vertical", command=tree_curso.yview)
        # horizontal scrollbar
        hsb = ttk.Scrollbar(frame_tabela_turma, orient="horizontal", command=tree_curso.xview)

        tree_turma.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree_turma.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_tabela_turma.grid_rowconfigure(0, weight=12)

        hd = ["nw", "nw", "e", "e"]
        h = [30, 130, 150, 80]
        n = 0

        for col in list_header:
            tree_turma.heading(col, text=col.title(), anchor=NW)
            # adjust the column's width to the header string
            tree_turma.column(col, width=h[n], anchor=hd[n])

            n += 1

        for item in df_list:
            tree_turma.insert('', 'end', values=item)

    mostrar_turmas()


# função para salvar
def salvar():
    print('Salvar')


# função de controle
def control(i):
    # cadastro de aluno
    if i == 'cadastro':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

        for widget in frame_tabela.winfo_children():
            widget.destroy()

        # chamando a função alunos
        alunos()

    if i == 'adicionar':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

        for widget in frame_tabela.winfo_children():
            widget.destroy()

        # chamando a função adicionar
        adicionar()

    if i == 'salvar':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

        for widget in frame_tabela.winfo_children():
            widget.destroy()

        # chamando a função salvar
        salvar()


# criando botoes
app_img_cadastro = Image.open('add.png')
app_img_cadastro = app_img_cadastro.resize((18, 18))
app_img_cadastro = ImageTk.PhotoImage(app_img_cadastro)
app_cadastro = Button(frame_dados, command=lambda: control('cadastro'), image=app_img_cadastro, text="Cadastro",
                      width=100, compound=LEFT, overrelief=RIDGE,
                      font=('Ivy 11'), bg=co1, fg=co0)
app_cadastro.place(x=10, y=30)

app_img_adicionar = Image.open('add.png')
app_img_adicionar = app_img_adicionar.resize((18, 18))
app_img_adicionar = ImageTk.PhotoImage(app_img_adicionar)
app_adicionar = Button(frame_dados, command=lambda: control('adicionar'), image=app_img_adicionar, text="Adicionar",
                       width=100, compound=LEFT, overrelief=RIDGE,
                       font=('Ivy 11'), bg=co1, fg=co0)
app_adicionar.place(x=123, y=30)

app_img_salvar = Image.open('save.png')
app_img_salvar = app_img_salvar.resize((18, 18))
app_img_salvar = ImageTk.PhotoImage(app_img_salvar)
app_salvar = Button(frame_dados, command=lambda: control('salvar'), image=app_img_salvar, text="Salvar",
                    width=100, compound=LEFT, overrelief=RIDGE,
                    font=('Ivy 11'), bg=co1, fg=co0)
app_salvar.place(x=236, y=30)

alunos()
janela.mainloop()
