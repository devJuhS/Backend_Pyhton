#chamando as classes dos demais scrpts
from modelo_app.restaurante import Restaurante
from modelo_app.cardapio.bebida import Bebida
from modelo_app.cardapio.prato import Prato

restaurante_espeto = Restaurante('engenheiros do cafe', 'Cafeteria')

bebida_suco = Bebida('Suco de laranja', 5.0, 'grande')
prato_paozinho = Prato('paozinho', 2.0, 'o melhor pao da cidade')

restaurante_espeto.adicionar_cardapio(bebida_suco)
restaurante_espeto.adicionar_cardapio(prato_paozinho)
def main():
        restaurante_espeto.exibir_cardapio


if __name__ == '__main__':
        main()