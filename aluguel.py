import uuid
import pickle


class Aluguel:
    def __init__(self, id_imovel, id_inquilino, id_corretor):
        self.id = uuid.uuid4()
        self.id_imovel = id_imovel
        self.id_inquilino = id_inquilino
        self.id_corretor = id_corretor

    def __repr__(self):
        return f'Aluguel(id={self.id},id_imovel={self.id_imovel},id_inquilino={self.id_inquilino}, id_corretor={self.id_corretor} )'


alugueis = {}


def lista_alugueis():
    global alugueis
    for id, aluguel in alugueis.items():
        print(f'{id} {aluguel}')


def criar_aluguel(id_imovel, id_inquilino, id_corretor):
    global alugueis
    aluguel = Aluguel(id_imovel, id_inquilino, id_corretor)
    alugueis[aluguel.id] = aluguel
    salvar_alugueis()


def deletar_aluguel(id):
    global alugueis
    alugueis.pop(id)
    salvar_alugueis()


def salvar_alugueis():
    global alugueis
    with open('alugueis.pickle', 'wb') as file:
        pickle.dump(alugueis, file)


def ler_alugueis():
    global alugueis
    try:
        with open('alugueis.pickle', 'rb') as file:
            alugueis = pickle.load(file)
    except FileNotFoundError:
        alugueis = {}


def atualizar_id_imovel(id, id_imovel):
    aluguel = alugueis[id]
    aluguel.id_imovel = id_imovel
    salvar_alugueis()


def atualizar_id_inquilino(id, id_inquilino):
    aluguel = alugueis[id]
    aluguel.id_inquilino = id_inquilino
    salvar_alugueis()


def atualizar_id_corretor(id, id_corretor):
    aluguel = alugueis[id]
    aluguel.id_corretor = id_corretor
    salvar_alugueis()
