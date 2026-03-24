''' 
*---------------------------------------------------------* 
* Fatec São Caetano do Sul * 
* Exemplo de Manipulação de Lista ligada * 
* Autor: Gabriel Lasinskais * 
* Objetivo:Mostrar manipulação de lista ligada em python * 
* data: 09/03/2026 * 
*---------------------------------------------------------* 
''' 
# Banco de dados em memoria (Dicionario) 
produtos = {} 
def valorExiste(listaCabeca, valorEntrada): 
    atual = listaCabeca 
    while atual is not None: 
        if atual ["valor"] == valorEntrada: 
            return True 
        atual  = atual ["proximo"] 
    return False

# funcao de Inclusao 
def inserirInicio(listaEntrada): 
    valor = input("Digite o valor: ") 
    if (valorExiste(listaEntrada, valor)): 
       print("Codigo de produto Duplicado") 
       return listaEntrada 
    novoNo = {"valor":  valor, "proximo": listaEntrada} 
    return novoNo

# funcao de consulta 
def inserirFim(): 
    print ("inserir fim")
    
# funcao de Alteracao 
def inserirMeio(): 
    print ("inserir MEIO")
    
# funcao de Exclusao 
def listar(listaRecebida): 
    if listaRecebida is None: 
        print("Lista vazia") 
        return 
    listaAtual = listaRecebida 
    while listaAtual is not None: 
        print (listaAtual["valor"], end="->" ) 
        listaAtual = listaAtual["proximo"]
        
# funcao de Lista 
def buscar(listaRecebida): 
    argumentoPesquisa = input("informe o argumento de pesquisa:") 
     
    listaAtual = listaRecebida 
    posicao = 0 
     
    while listaAtual is not None: 
        if listaAtual["valor"]==argumentoPesquisa: 
            posicao +=1 
            break 
        listaAtual = listaAtual["proximo"] 
    if posicao == 0: 
        print("Valor não encontrado") 
    else: 
        print(f"valor encontrado na posição {posicao}") 
def remover(): 
    print ("buscar")
    
# Inserir no fim
def inserirFim(listaCabeca):
    valor = input("Digite o valor: ")
    if valorExiste(listaCabeca, valor):
        print("Codigo de produto Duplicado")
        return listaCabeca
    
    novoNo = {"valor": valor, "proximo": None}
    
    if listaCabeca is None:
        return novoNo
    
    atual = listaCabeca
    while atual["proximo"] is not None:
        atual = atual["proximo"]
    atual["proximo"] = novoNo
    return listaCabeca

# Inserir no meio (após um valor específico)
def inserirMeio(listaCabeca):
    valorNovo = input("Digite o valor a inserir: ")
    valorReferencia = input("Digite o valor após o qual deseja inserir: ")
    
    if valorExiste(listaCabeca, valorNovo):
        print("Codigo de produto Duplicado")
        return listaCabeca
    
    atual = listaCabeca
    while atual is not None:
        if atual["valor"] == valorReferencia:
            novoNo = {"valor": valorNovo, "proximo": atual["proximo"]}
            atual["proximo"] = novoNo
            return listaCabeca
        atual = atual["proximo"]
    
    print("Valor de referência não encontrado")
    return listaCabeca

# Remover um nó
def remover(listaCabeca):
    valorRemover = input("Digite o valor a remover: ")
    
    if listaCabeca is None:
        print("Lista vazia")
        return None
    
    # Se o valor está no primeiro nó
    if listaCabeca["valor"] == valorRemover:
        print(f"Valor {valorRemover} removido")
        return listaCabeca["proximo"]
    
    atual = listaCabeca
    while atual["proximo"] is not None:
        if atual["proximo"]["valor"] == valorRemover:
            print(f"Valor {valorRemover} removido")
            atual["proximo"] = atual["proximo"]["proximo"]
            return listaCabeca
        atual = atual["proximo"]
    
    print("Valor não encontrado")
    return listaCabeca

# Menu de Interacao 
def menu(): 
    lista = None 
    while True:
        print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= Menu Crud =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("\n1-Inserir no Início \n2-inserir no Fim \n3-Inserir no meio \n4-listar \n5-remover \n6-Buscar \n0-Sair")
        print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        opcao = input("Escolha uma operacao: ") 
         
        if opcao == '1': 
           lista = inserirInicio(lista) 
            
        elif opcao == '2':
            lista = inserirFim(lista)
        elif opcao == '3':
            lista = inserirMeio(lista)
        elif opcao == '4': 
            listar(lista)     
        elif opcao == '5':
            lista = remover(lista)
        elif opcao == '6':   
            buscar(lista) 
        elif opcao == '0': 
            print ("Obrigado por usar o sistema") 
            break 
        else: 
            print ("**Opcao invalida**") 
            
menu() 