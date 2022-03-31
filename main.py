# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
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


def print_hi(name):
    global imoveis
    ler_imoveis()
    imovel = Imovel('Av.Domingos Ferreira', '66085650', 'marco', 'Belém')
    print(f'{imovel}')
    imoveis[imovel.id] = imovel
    for id,imovel in imoveis.items():
        print(f'{id} {imovel}')
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
        imoveis={}

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
