from modelo_app.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self,nome,preco, tamanho):
        super().__init__(nome,preco)
        self._tamanho = tamanho
    
    #defindo o retorno especial script dev
    def __str__(self):
        return self._nome