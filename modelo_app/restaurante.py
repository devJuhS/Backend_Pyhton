#importando o script de avaliação
from modelo_app.avaliacao import Avaliacao
from modelo_app.cardapio.item_cardapio import ItemCardapio

#criando uma classe para restaurante
class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do restaurante".ljust(20)} | {"categoria".ljust(20)} | {"Avaliação".ljust(20)} | {"Status"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacao).ljust(20)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '✓ ' if self._ativo else '✗'

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        try:
            nota = float(nota)
        except ValueError:
            raise ValueError("A nota deve ser um número.")
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)

        #Certifique-se de que o return está indentado corretamente
        return media  
    
    def adicionar_cardapio(self, item):
        #isinstance() para instanciar determinados itens
        if isinstance(item,ItemCardapio):
            self._cardapio.append(item)

    # Criando método para exibir cardápio
    @property
    def exibir_cardapio(self):
        print(f'Cardápio do restaurante {self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, '_descricao'):
                # Caso seja um prato
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R${item._preco:.2f} | Descrição: {item._descricao}'
                print(mensagem_prato)
            elif hasattr(item, '_tamanho'):
                # Caso seja uma bebida
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R${item._preco:.2f} | Tamanho: {item._tamanho}'
                print(mensagem_bebida)
            # else:
            #     # Caso o item não tenha os atributos esperados
            #     print(f'{i}. Nome: {item._nome} | Preço: R${item._preco:.2f}')


            




