#1 10/04 imoport lib os (operational system)
import os


#restaurantes=['Bife Sujo', 'Saco de Feijão']
#inserir dicionario-em outras linguagens chave valor
restaurantes=[{'nome':'Bife-sujo','categoria':'Prato-Feito','ativo': True},
              {'nome':'Saco do feijão','categoria':'Feijoada','ativo': False},
              {'nome':'Lauxen Porquinhos','categoria':'Assados','ativo': True},] 

def mostrar_subtitulo(texto):
    '''
    Essa função é por responsavel por exibir o nome que o usuário solicitou
    '''
    os.system('clear')
    linha='*'*(len(texto))
    print(linha)
    print (texto)
    print(linha)
    print()

#2 declarando a função finalizar_app
def finalizar_app():
    '''
    Essa função e responsavel por finalizar o programa

    outpts:
    -aiciona um titulo quando finaliza um programa
    '''
    
    mostrar_subtitulo("Finalizando app")

def chamar_nome_do_app():
    '''
    Essa função e responsavel por exibir o nome do programa
    '''
    print ('''
    
    𝓡𝓔𝓢𝓣𝓐𝓤𝓡𝓐𝓝𝓣𝓔 𝓔𝓧𝓟𝓡𝓔𝓢𝓢𝓞 𝓑𝓔𝓡𝓝𝓐𝓡𝓓𝓞
    
    ''')

def voltar_ao_menu_principal():
     input('\nDigite uma tecla para voltar ao menu principal')
     main()

# 12 criando opção_invalida
def opcao_invalida():
    '''
    Essa função e responsavel por exibir que a opção que o usuário digitou e invalida

    output:
    -Pede que o usuário digite uma tecla para voltar ao menu principal
    '''
    print ('opção invalida\n')
    #input('Digite uma tecla para voltar ao menu principal:')
    #main()
    voltar_ao_menu_principal()
    
def exibir_opcoes():
    '''
    Essa função e responsavel por exibir opções disponiveis para seu restaurante
    '''
    print ("1 Cadastrar Restaurante")
    print ("2 Listar Restaurante")
    print ("3 Ativar Restaurente")
    print ("4 Sair\n")


def cadatrar_novo_restaurante():
    #DOCSTRING
    '''
    Essa função e responavel por cadastrar um novo restaurante

    inputs:
    -nome do restaurante
    -categoria do restaurante

    outputs
    -adiciona um novo retaurante ao dicionario restaurantes
    '''
    os.system('clear')
    nome_do_restaurante= input('digite o nome do novo restaurante:')
    categoria=input(f'Digite a categoria do restaurante {nome_do_restaurante}:')
    dados_do_restaurante={'nome':nome_do_restaurante, 'categoria':categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante}, foi cadastrado com sucesso\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''
    Essa função e responsavel por listar os restaurantes disponíveis

    outputs:
    -lista os restaurantes incluindo o restaurante que o usuário cadastrou
    '''
    mostrar_subtitulo('Listando os restaurantes')
    print(f"\n"'Nome do restaurante'.ljust(22),"Categoria".ljust(20),'Ativo'"\n")
    for restaurante in restaurantes:
     
       nome_restaurante=restaurante['nome']
       categoria=restaurante['categoria']
       ativo="ativado" if restaurante ['ativo'] else "Desativado"
       print(f'-{nome_restaurante.ljust(20)}  {categoria.ljust(20)}  {ativo}')

    voltar_ao_menu_principal()


def alterar_estado_restaurante():
    '''
    Essa função é responsavel por alterar o status do restaurante (true ou False)

    input:
    -nome do restaurante 

    output:
    -altera o estado do restaurante
    '''
    mostrar_subtitulo('Alternando o estado do restaurante')
    nome_restaurante=input('Digite o nome do restaurante que desejas alternar o estado: ')
    restaurante_encontrado=False

    for restaurante in restaurantes:
        if nome_restaurante==restaurante['nome']:
            restaurante_encontrado=True
            restaurante['ativo']=not restaurante['ativo']
            mensagem=f'O restaurante {nome_restaurante} foi ativado com sucesso'if restaurante['ativo'] else f'Restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')        
    voltar_ao_menu_principal()


#8 declarando a função opcao_digitada1
def escolher_opcao():
    '''
    Essa função é responsavel por exibir e requisitar ao usuário que escolha uma das opções 

    input:
    -opção escolhida

    output:
    -redireciona para a função escolhida
    '''
    
    try:
        opcao_digitada = (int(input("Escolha uma opção:  ")))
        print ("Você selecionou:",opcao_digitada, "\n")
        if(opcao_digitada==1):
            print("Você escolheu Cadastrar Restaurante\n")
            cadatrar_novo_restaurante()
            finalizar_app()
        elif(opcao_digitada==2):
           # print("Você escolheu Listar Restaurante\n") 
           listar_restaurantes()
           finalizar_app()
        elif(opcao_digitada==3):
            #mostrar_subtitulo("Voce escolheu Ativar Restaurante")
            alterar_estado_restaurante()
            finalizar_app()
        elif(opcao_digitada==4):
            # print('Voce escolheu sair do programa') 
             finalizar_app()
        #3 chamando a função finalizar_app 
        else:
            opcao_invalida()
    except:
        opcao_invalida()         
  
  #5 escrever a funçaõ main
def main():
    '''
    Essa função é responsavel por ervir como ponto de patida para a execução do programa

    outputs:
    -exibi nome do app
    -exibir opções disponíveis
    -pede ao usuario que escolha uma opção
    '''
    #10 clear
    os.system('clear')
    #6 chamar o nome do app
    chamar_nome_do_app()
    #7 chamar a escolha de opções
    exibir_opcoes()
    #9 chamar a opção digitada
    escolher_opcao()

#4 criando a entrada através da variável main
if(__name__=='__main__'):
    main()