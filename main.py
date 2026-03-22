import module1
print("Lista de cadastro de clientes")
while True:
    opcao=input("\nDigite a opcao desejada: 1.Cadastrar | 2.Buscar | 3.Alterar | 4.Apagar | 5.Mostrar tudo | 6.Encerrar: ")
    if opcao=="6":
        print("\nSessão encerrada.")
        break
    
    elif opcao == "1":
        module1.funcao_cadastro()

    elif opcao=="2":
        module1.funcao_busca()

    elif opcao=="3":
        module1.funcao_alter()

    elif opcao=="4":
        module1.funcao_apagar()

    elif opcao=="5":
        module1.funcao_mostrar()

    else:
        print("\nEssa opção não existe, tente novamente.")