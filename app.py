import os

restaurantes = [
                {'nome': 'japa', 'categoria':'Sushi', 'Ativo':False},
                {'nome':'rei do churrasco', 'categoria': 'Churrasco', 'Ativo': True},
                {'nome': 'domes', 'categoria':'hamburguer', 'Ativo':False}
                ] #lista #dicionario é relacionado a chave e valor 

def main(): #funçao principal
    os.system('cls')#para limpar  a tela apos fechear o programa
    nome_do_app()
    exibir_opcoes()
    escolher_opcoes()

#   listas saão estruturas mutaveis o que significa que é possivel modificar seus elementos
#    adicionar novos itens ou remover itens existentes após  a criação de listas podendo
#    inclusive utilizar funções propias como pop() append() remove() insert()

def nome_do_app(): #funçao principal exibir o nome do app
    print("""
██████████████████████████████████████████████████████████████████████████
█─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀███▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█
█▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄████─▄█▀██▀─▀███─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀""")
    
def exibir_opcoes(): #funcao principal exibir as opçoes
    print('1.Cadastrar restaurante')
    print('2.Listar restaurantes')
    print('3.Ativar restaurante')
    print('4.Sair \n')

def finalizar_app(): #funçao pra limpar a tela
    exibir_subtitulo('finalizar app')

def voltar_ao_menu_principal():
    input('Digite umma tecla pra voltar ao menu  ')
    main()

def opcao_invalida():
    print('Opção invalida \n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def cadastrar_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: \n')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}:\n ')
    dados_do_restaurante = {'nome': nome_do_restaurante,
                            'categoria': categoria,
                            'Ativo': False}#dicionarios 
    
    restaurantes.append(nome_do_restaurante) #append coloca o nome na lista
    print(f'o Restaurante {nome_do_restaurante} foi cadastrado com sucesso! \n')

    
    voltar_ao_menu_principal()

def listar_restaurante():
    exibir_subtitulo('Listando os restaurantes cadastrados ')

    for restaurante in restaurantes:
        nome_do_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        print(f'- {nome_do_restaurante} | {categoria}  \n')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alterando o estado do restaurante')
    nome_restaurante =  str(input('Digite o nome do restaurante que deseja alterar o estado: \n'))
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante ['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if  restaurante['ativo'] else f'O restaurante{nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante nao foi encontrado')

    voltar_ao_menu_principal()


def escolher_opcoes():#funçao pra escolher opções
        try: #tentar
            opcao_escolha = int(input('escolha uma opção: '))
        
            if (opcao_escolha == 1):
                cadastrar_restaurante()
            elif (opcao_escolha == 2):
                listar_restaurante()
            elif (opcao_escolha == 3):
                alternar_estado_restaurante()
            elif (opcao_escolha == 4):
                finalizar_app()
            else:
                opcao_invalida()
        except:#caso nao encontre apresente
            opcao_invalida()


if __name__ == '__main__':
    main()






