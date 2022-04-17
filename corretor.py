import uuid
import pickle


class Corretor:
    def __init__(self, nome, data_nascimento):
        self.id = uuid.uuid4()
        self.nome = nome
        self.data_nascimento = data_nascimento

    def __repr__(self):
        return f'corretor(id={self.id},nome={self.nome},data_nascimento={self.data_nascimento})'


corretores = {}


def lista_corretores():
    global corretores
    for id, corretor in corretores.items():
        print(f'{id} {corretor}')


def criar_corretor(nome, data_nascimento):
    global corretores
    corretor = Corretor(nome, data_nascimento)
    corretores[corretor.id] = corretor
    salvar_corretores()


def deletar_corretor(id):
    global corretores
    corretores.pop(id)
    salvar_corretores()


def salvar_corretores():
    global corretores
    with open('corretores.pickle', 'wb') as file:
        pickle.dump(corretores, file)


def ler_corretores():
    global corretores
    try:
        with open('corretores.pickle', 'rb') as file:
            corretores = pickle.load(file)
    except FileNotFoundError:
        corretores = {}


def atualizar_nome(id, nome):
    corretor = corretores[id]
    corretor.id_imovel = nome
    salvar_corretores()


def atualizar_data_nascimento(id, data_nascimento):
    corretor = corretores[id]
    corretor.id_corretor = data_nascimento
    salvar_corretores()
