import pandas as pd
def carregar_dados():
    arquivo='dados.csv'
    colunas = ['nome','cpf','telefone','email']
    return pd.read_csv(arquivo,usecols=colunas,dtype={'cpf': str})
def salvar_dados(df):
    df.to_csv('dados.csv', index=False)

def funcao_mostrar():
        print("\nClientes já cadastrados:")
        df=carregar_dados()
        print(df)

def funcao_cadastro():
     df=carregar_dados()
     novo_cliente={
          'nome':input("\nDigite o nome do novo cliente: "),
          'cpf':input("Digite o cpf: "),
          'telefone':input("Digite o telefone: "),
          'email':input("Digite o e-mail: ")
     }
     df_novo = pd.DataFrame([novo_cliente])
     df= pd.concat([df,df_novo],ignore_index=True)
     salvar_dados(df)
     print("Cliente cadastrado com sucesso!")

def funcao_busca():
    df=carregar_dados()
    cpf_busca=input("\nDigite o cpf do cliente que deseja buscar: ")
    resultado= df[df['cpf']==cpf_busca]
    if not resultado.empty:
        print("Cliente encontrado: ")
        print(resultado)
    else:
         print("Cliente não encontrado.")
    
def funcao_alter():
    df=carregar_dados()
    cpf_busca=input("\nDigite o cpf do cliente que deseja alterar: ")
    resultado= df[df['cpf']==cpf_busca]
    cols=df.columns
    if not resultado.empty:
        print("Cliente encontrado: ")
        print(resultado)
        campo=input("Qual campo deseja alterar? (nome, telefone, email) ")
        if campo in cols:
             novo_valor=input(f"Digite o novo valor para {campo}: ")
             df.loc[df['cpf'].astype(str) == cpf_busca, campo] = novo_valor
             salvar_dados(df)
             print("Dados atualizados.")
        else:
             print("Campo inválido.") 
    else:
         print("Cliente não encontrado.")

def funcao_apagar():
    df=carregar_dados()
    cpf_busca=input("\nDigite o cpf do cliente que deseja apagar: ")
    resultado= df[df['cpf']==cpf_busca]
    if not resultado.empty:
        print("Cliente encontrado: ")
        print(resultado)
        campo=input("Deseja realmente apagar? (s/n) ")
        if campo=="s":
             df=df[df['cpf']!= cpf_busca]             
             salvar_dados(df)
             print("Dados atualizados.")
        else:
             print("Operação cancelada.") 
    else:
         print("Cliente não encontrado.")
     

