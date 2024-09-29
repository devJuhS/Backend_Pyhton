from poo_app.restaurante import Restaurante

restaurante_espeto = Restaurante('espeto na brasa', 'churrasco')
restaurante_japones = Restaurante('Japa food', 'Sushi')

# restaurante_espeto.receber_avaliacao('ju','10')
# restaurante_espeto.receber_avaliacao('caio','7')

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()