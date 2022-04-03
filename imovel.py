
import uuid
import pickle


class Imovel:
    def __init__(self, logradouro, cep, bairro, cidade):
        self.id = uuid.uuid4()
        self.logradouro = logradouro
        self.cep = cep
        self.bairro = bairro
        self.cidade = cidade

    def __repr__(self):
        return f'Imovel (id={self.id},logradouro={self.logradouro},cep={self.cep}, bairro={self.bairro}, cidade={self.cidade})'


imoveis = {}


def lista_imoveis():
    global imoveis
    for id, imovel in imoveis.items():
        print(f'{id} {imovel}')


def criar_imovel(logradouro, cep, bairro, cidade):
    global imoveis
    imovel = Imovel(logradouro, cep, bairro, cidade)
    imoveis[imovel.id] = imovel
    salvar_imoveis()


def deletar_imovel(id):
    global imoveis
    imoveis.pop(id)
    salvar_imoveis()


def salvar_imoveis():
    global imoveis
    with open('imoveis.pickle', 'wb') as file:
        pickle.dump(imoveis, file)


def ler_imoveis():
    global imoveis
    try:
        with open('imoveis.pickle', 'rb') as file:
            imoveis = pickle.load(file)
    except FileNotFoundError:
        imoveis = {}


def atualizar_logradouro(id, logradouro):
    imovel = imoveis[id]
    imovel.logradouro = logradouro
    salvar_imoveis()

def atualizar_cep(id, cep):
    imovel = imoveis[id]
    imovel.cep = cep
    salvar_imoveis()

def atualizar_bairro(id, bairro):
    imovel = imoveis[id]
    imovel.bairro = bairro
    salvar_imoveis()

def atualizar_cidade(id, cidade):
    imovel = imoveis[id]
    imovel.cidade = cidade
    salvar_imoveis()


