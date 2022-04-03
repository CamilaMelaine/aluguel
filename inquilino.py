import uuid
import pickle


class Inquilino:
    def __init__(self, nome, data_nascimento):
        self.id = uuid.uuid4()
        self.nome = nome
        self.data_nascimento = data_nascimento

    def __repr__(self):
        return f'inquilino(id={self.id},nome={self.nome},data_nascimento={self.data_nascimento})'


inquilinos = {}


def lista_inquilinos():
    global inquilinos
    for id, inquilino in inquilinos.items():
        print(f'{id} {inquilino}')


def criar_inquilino(nome, data_nascimento):
    global inquilinos
    inquilino = Inquilino(nome, data_nascimento)
    inquilinos[inquilino.id] = inquilino
    salvar_inquilinos()


def deletar_inquilino(id):
    global inquilinos
    inquilinos.pop(id)
    salvar_inquilinos()


def salvar_inquilinos():
    global inquilinos
    with open('inquilinos.pickle', 'wb') as file:
        pickle.dump(inquilinos, file)


def ler_inquilinos():
    global inquilinos
    try:
        with open('inquilinos.pickle', 'rb') as file:
            inquilinos = pickle.load(file)
    except FileNotFoundError:
        inquilinos = {}


def atualizar_nome(id, nome):
    inquilino = inquilinos[id]
    inquilino.id_imovel = nome
    salvar_inquilinos()


def atualizar_data_nascimento(id, data_nascimento):
    inquilino = inquilinos[id]
    inquilino.id_inquilino = data_nascimento
    salvar_inquilinos()
