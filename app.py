import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                {'nome':'Pizza', 'categoria':'Italiana', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Francesa', 'ativo':True}]

def main():
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

def exibir_nome_do_programa():
    print('Sabor Express\n')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Encerrando o app')

def voltar_ao_menu_principal():
    input('Digite uma tecla para voltar ao menu principal')
    main()

def opcao_invalida():
    print('\nOpção Invalida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('clear')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha,'\n')

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')
        
    print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status\n')         
    for restaurante in restaurantes:
        nome_do_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_do_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo} \n')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alternando estado do restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante para alterar o estado: ')
    restaurante_econtrado = False

    for restaurante in restaurantes:
        if nome_do_restaurante == restaurante['nome']:
            restaurante_econtrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'\nO restaurante {nome_do_restaurante} foi ativado com sucesso\n' if restaurante['ativo'] else f'\nO restaurante {nome_do_restaurante} foi desativado com sucesso\n'
            print(mensagem)

    if not restaurante_econtrado:
        print('\nO restaurante não foi encontrado\n')
    
    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('\nEscolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
        

if __name__ == '__main__':
    main()