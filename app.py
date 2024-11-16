import os

restaurantes = [
                {'nome': 'japa', 'categoria':'Sushi', 'ativo':False},
                {'nome':'rei do churrasco', 'categoria': 'churrasco', 'ativo': True},
                {'nome': 'domes', 'categoria':'hamburguer', 'ativo':False}] #lista #dicionario é relacionado a chave e valor 

#funçao principal
def main(): 
    #para limpar  a tela apos fechear o programa
    os.system('cls')
    nome_do_app()
    exibir_opcoes()
    escolher_opcoes()

 
#funçao principal exibir o nome do app
def nome_do_app(): 
    print("""
██████████████████████████████████████████████████████████████████████████
█─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀███▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█
█▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄████─▄█▀██▀─▀███─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀""")

#funcao principal exibir as opçoes    
def exibir_opcoes(): 
    print('1.Cadastrar restaurante')
    print('2.Listar restaurantes')
    print('3.Alternar restaurante')
    print('4.Sair \n')

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '#' * (len(texto) + 5)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_restaurante():
    '''essa função é responsavel por cadastrar um novo restaurante 
    
    Inputs :
    - Nome do restaurante
    - categoria

    Outputs:
    - adiciona um novo restaurante a lista de restaurantes
    
    
    '''
    exibir_subtitulo('#### Cadastro de novos restaurantes ####')
    nome_do_restaurante = input('Digite o restaurante que deseja cadastrar:\n')
    categoria =  input(f'Digite o nome da categoria do restaurante {nome_do_restaurante} \n')
    dados_do_restaurante = {'nome': nome_do_restaurante , 'categoria': categoria, 'ativo': False }
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso ')
    voltar_ao_menu_principal()
    
def listar_restaurante():
    exibir_subtitulo('##### Listando os restaurantes cadastrados #####')
    
    print(f'{'nome_do_restaurante'.ljust(22)} || {'categoria'.ljust(20)}|| Status')
    for restaurante in restaurantes:
       nome_do_restaurante = restaurante['nome']
       categoria = restaurante['categoria']
       ativo = 'ativado' if restaurante['ativo'] else 'desativado'
       print(f'- {nome_do_restaurante.ljust(20)} || {categoria.ljust(20)} || {ativo}\n')
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('##### Alterando o estado do restaurante #####')
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

#funçao pra escolher opções
def escolher_opcoes():
         #tentar
        try:
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
        #caso nao encontre apresente        
        except:
            opcao_invalida()

def voltar_ao_menu_principal():
    input('Digite umma tecla pra voltar ao menu  ')
    main()

def opcao_invalida():
    print('Opção invalida \n')
    voltar_ao_menu_principal()

#funçao pra limpar a tela
def finalizar_app(): 
    exibir_subtitulo('finalizar app')



if __name__ == '__main__':
    main()






