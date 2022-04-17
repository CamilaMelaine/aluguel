# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
from imovel import *
from inquilino import *
from aluguel import *
from corretor import *


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
                atualizar_logradouro(uid, logradouro)
            elif campo == 'cep':
                cep = input('qual o novo cep?\n')
                atualizar_cep(uid, cep)
            elif campo == 'bairro':
                bairro = input('qual o novo bairro?\n')
                atualizar_bairro(uid, bairro)
            elif campo == 'cidade':
                cidade = input('qual o novo cidade?\n')
                atualizar_cidade(uid, cidade)
        elif comando == 'listar inquilinos':
            lista_inquilinos()
        elif comando == 'criar inquilino':
            nome = input('digite o nome\n')
            data_nascimento = input('digite data_nascimento\n')
            criar_inquilino(nome, data_nascimento)
        elif comando == 'remover inquilino':
            id = input('digite o id\n')
            uid = uuid.UUID(id)
            deletar_inquilino(uid)
        elif comando == 'atualizar inquilino':
            id = input('digite o id\n')
            uid = uuid.UUID(id)
            campo = input('digite o campo do inquilino que desja atualizar\n')
            if campo == 'nome':
                nome = input('qual o novo nome?\n')
                atualizar_nome(uid, nome)
            elif campo == 'data_nascimento':
                data_nascimento = input('qual a nova data?\n')
                atualizar_data_nascimento(uid, data_nascimento)
        elif comando == 'listar corretores':
            lista_corretores()
        elif comando == 'criar corretor':
            nome = input('digite o nome\n')
            data_nascimento = input('digite data_nascimento\n')
            criar_corretor(nome, data_nascimento)
        elif comando == 'remover corretor':
            id = input('digite o id\n')
            uid = uuid.UUID(id)
            deletar_corretor(uid)
        elif comando == 'atualizar corretor':
            id = input('digite o id\n')
            uid = uuid.UUID(id)
            campo = input('digite o campo do corretor que desja atualizar\n')
            if campo == 'nome':
                nome = input('qual o novo nome?\n')
                atualizar_nome(uid, nome)
            elif campo == 'data_nascimento':
                data_nascimento = input('qual a nova data?\n')
                atualizar_data_nascimento(uid, data_nascimento)
        elif comando == 'listar alugueis':
            lista_alugueis()
        elif comando == 'criar aluguel':
            id_imovel = input('digite o id imóvel\n')
            id_inquilino = input('digite o id inquilino\n')
            id_corretor = input('digite o id corretor\n')
            uid_imovel=uuid.UUID(id_imovel)
            uid_inquilino=uuid.UUID(id_inquilino)
            uid_corretor = uuid.UUID(id_corretor)
            criar_aluguel(uid_imovel, uid_inquilino, uid_corretor)
        elif comando == 'remover aluguel':
            id = input('digite o id\n')
            uid = uuid.UUID(id)
            deletar_aluguel(uid)
        elif comando == 'atualizar aluguel':
            id = input('digite o id\n')
            uid = uuid.UUID(id)
            campo = input('digite o campo do aluguel que desja atualizar\n')
            if campo == 'id_imovel':
                id_imovel = input('qual o novo id_imovel?\n')
                atualizar_id_imovel(uid, id_imovel)
            elif campo == 'id_inquilino':
                id_inquilino = input('qual o novo id_inquilino?\n')
                atualizar_id_inquilino(uid, id_inquilino)
            elif campo == 'id_corretor':
                id_corretor = input('qual o novo id_corretor?\n')
                atualizar_id_corretor(uid, id_corretor)





if __name__ == '__main__':
    ler_imoveis()
    ler_inquilinos()
    ler_alugueis()
    ler_corretores()
    ler_entrada()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
