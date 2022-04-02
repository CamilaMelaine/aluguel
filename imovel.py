
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


def ler_entrada():
    comando = ''
    while comando != 'sair':
        comando = input('digite um comando, ou sair para sair\n')
        if comando == 'listar imoveis':
            lista_imoveis()
        elif comando == 'criar imovel':
            logradouro = input('digite o logradouro\n')
            cep = input('digite o cep\n')
            bairro = input('digite bairro\n')
            cidade = input('digite cidade\n')
            criar_imovel(logradouro, cep, bairro, cidade)
        elif comando == 'remover imovel':
            id = input('digite o id\n')
            uid = uuid.UUID(id)
            deletar_imovel(uid)
        elif comando == 'atualizar imovel':
            id = input('digite o id\n')
            uid = uuid.UUID(id)
            campo = input('digite o campo do imovel que desja atualizar\n')
            if campo == 'logradouro':
                logradouro = input('qual o novo logradouro?\n')
                atualizar_logradouro(uid,logradouro)
            elif campo == 'cep':
                cep = input('qual o novo cep?\n')
                atualizar_cep(uid,cep)
            elif campo == 'bairro':
                bairro = input('qual o novo bairro?\n')
                atualizar_bairro(uid,bairro)
            elif campo == 'cidade':
                cidade = input('qual o novo cidade?\n')
                atualizar_cidade(uid,cidade)