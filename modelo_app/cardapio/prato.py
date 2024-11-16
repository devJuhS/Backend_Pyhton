#chamando o script Herança
from modelo_app.cardapio.item_cardapio import ItemCardapio

#herdando a outra classe
class Prato(ItemCardapio):
    def __init__(self, nome,preco,descricao):
       #super(). permite que acessamos informaçoes de outra classe
       super().__init__(nome,preco)
       self._descricao = descricao

    def __str__(self):
        return self._nome