import os

restaurantes = [{"nome" : "praca" , "categoria" : "Japonesa" , "ativo" : False} ,
                {"nome" : "Cantina" , "categoria" : "pão" , "ativo" : True}]

def exibir_nome_do_programa() : 
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░""")

def exibir_opcoes() :
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Ativar restaurante")
    print("4. Sair\n")

def finalizar_app():
    exibir_subtitulo("Finalizando o APP")

def opecao_invalida():
    print("Opção invalida!!\n")
    voltar_ao_menu_principal()
  
def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de novos restaurantes")

    nome_restaurante = input("Digite o nome do restaurante que deseja: ")
    categoria = input(f"Digite o nome da categoria do restaurante {nome_restaurante}: ")
    
    dados_do_restaurante = {"nome" : nome_restaurante, "categoria" : categoria, "ativo" : False}
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_restaurante} foi cadastrado")

    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo("Listando os restaurantes:")

    print(f"{"Nome do Restaurante".ljust(20)} | {"Categoria".ljust(20)} | Status")

    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "ativado" if restaurante ["ativo"] else "desativado"
        print(f"{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}")

    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    input("\nDigite qualquer tecla para voltar ao Menu: ")
    main()

def exibir_subtitulo(texto):
    os.system("cls")
    linha = "*" * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()

def alternar_estado_restaurante():
    exibir_subtitulo("Alterando estado do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o estado: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"O restaurente {nome_restaurante} foi ativado com saucesso" if restaurante["ativo"] else f"O restaurente {nome_restaurante} foi desativado com saucesso"
            print(mensagem)
    if not restaurante_encontrado:
        print("O restaurante não foi encontrado")



    voltar_ao_menu_principal()

def escolher_opcao() :
    try:
        opcao_escolhida = int(input("Escolha uma opecao: "))
       # print(f"Você escolheu a opção: {opcao_escolhida}")

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opecao_invalida()
    except:
        opecao_invalida()

def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()