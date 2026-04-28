''' 
*---------------------------------------------------------* 
* Fatec São Caetano do Sul * 
* Exemplo de Manipulação de Lista ligada * 
* Autor: Gabriel Lasinskais * 
* Objetivo: Criar 3 listas com um sensor de prioridade* 
* data: 28/04/2026 * 
*---------------------------------------------------------* 
''' 
def criar_pessoa(nome, arquivo, paginas, adm):
    return {
        "nome": nome,
        "documento": {
            "arquivo": arquivo,
            "paginas": paginas
        },
        "adm": adm
    }



fila_adm = []
fila_aluno = []
fila_geral = []



def adicionar(pessoa):

    if pessoa["adm"]:
        fila_adm.append(pessoa)
    else:
        fila_aluno.append(pessoa)


def reorganizar():

    global fila_geral


    if len(fila_geral) > 0:
        print("Não pode reorganizar. Fila geral ainda não está vazia.")
        return


    fila_geral.extend(fila_adm)
    fila_geral.extend(fila_aluno)


    fila_adm.clear()
    fila_aluno.clear()

    print("Reorganização concluída")



def consumir():

    if len(fila_geral) == 0:
        print("Fila geral vazia.")
        return

   
    fila_geral.sort(key=lambda x: not x["adm"])

    pessoa = fila_geral.pop(0)

    doc = pessoa["documento"]

    print("\nATENDIDO")
    print("Nome:", pessoa["nome"])
    print("Arquivo:", doc["arquivo"])
    print("Páginas:", doc["paginas"])



def listar():

    print("\nFILA ADM")
    if not fila_adm:
        print("Vazia")
    else:
        for p in fila_adm:
            d = p["documento"]
            print(p["nome"], "-", d["arquivo"], "(", d["paginas"], ")")

    print("\nFILA ALUNO")
    if not fila_aluno:
        print("Vazia")
    else:
        for p in fila_aluno:
            d = p["documento"]
            print(p["nome"], "-", d["arquivo"], "(", d["paginas"], ")")

    print("\nFILA GERAL")

    if len(fila_geral) == 0:
        print("Vazia")
    else:
        for p in fila_geral:
            tipo = "ADM" if p["adm"] else "ALUNO"
            d = p["documento"]
            print(p["nome"], "(", tipo, ")", "-", d["arquivo"], "(", d["paginas"], ")")


adicionar(criar_pessoa("Maria", "contrato.pdf", 10, False))
adicionar(criar_pessoa("João", "relatorio.docx", 5, False))
adicionar(criar_pessoa("Ana", "processo.pdf", 12, True))
adicionar(criar_pessoa("Carlos", "requerimento.pdf", 7, False))
adicionar(criar_pessoa("Fernanda", "peticao.pdf", 20, True))


while True:

    print("\nMENU")
    print("1 Adicionar")
    print("2 Consumir")
    print("3 Listar")
    print("4 Reorganizar")
    print("0 Sair")

    op = input("Escolha: ")

    if op == "1":
        nome = input("Nome: ")
        arquivo = input("Arquivo: ")
        paginas = int(input("Páginas: "))
        adm = input("ADM (s/n): ").lower() == "s"

        adicionar(criar_pessoa(nome, arquivo, paginas, adm))

    elif op == "2":
        consumir()

    elif op == "3":
        listar()

    elif op == "4":
        reorganizar()

    elif op == "0":
        break

    else:
        print("Opção inválida")