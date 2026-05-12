'''
 ---------------------------------------------------------------------------
                FATEC São Caetano do Sul
		  Atividade B2 - 2  
 Autor: 1681432612010 - Gabriel Lasinskais
 Objetivo: Árvore Binária
 Data: 05/05/2026
  ---------------------------------------------------------------------------
'''

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None


class ArvoreBST:
    def __init__(self, raiz=None):
        self.raiz = raiz

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir(self.raiz, valor)

    def _inserir(self, no, valor):
        if valor < no.valor:
            if no.esq is None:
                no.esq = No(valor)
            else:
                self._inserir(no.esq, valor)
        else:
            if no.dir is None:
                no.dir = No(valor)
            else:
                self._inserir(no.dir, valor)

    def buscar(self, no, valor):
        if no is None or no.valor == valor:
            return no
        if valor < no.valor:
            return self.buscar(no.esq, valor)
        return self.buscar(no.dir, valor)

    def imprimir_nos_internos(self):
        def internos(no):
            if no:
                if no.esq or no.dir:
                    print(no.valor, end=" ")
                internos(no.esq)
                internos(no.dir)
        internos(self.raiz)
        print()

    def imprimir_folhas(self):
        def folhas(no):
            if no:
                if not no.esq and not no.dir:
                    print(no.valor, end=" ")
                folhas(no.esq)
                folhas(no.dir)
        folhas(self.raiz)
        print()

    def imprimir_niveis(self):
        if not self.raiz:
            return

        fila = [(self.raiz, 0)]
        atual = 0

        while fila:
            no, nivel = fila.pop(0)

            if nivel != atual:
                print()
                atual = nivel

            print(no.valor, end=" ")

            if no.esq:
                fila.append((no.esq, nivel + 1))
            if no.dir:
                fila.append((no.dir, nivel + 1))
        print()

    def calcular_altura(self, no):
        if no is None:
            return -1
        return 1 + max(self.calcular_altura(no.esq), self.calcular_altura(no.dir))

    def calcular_profundidade(self, valor):
        profundidade = 0
        no = self.raiz

        while no:
            if valor == no.valor:
                return profundidade
            elif valor < no.valor:
                no = no.esq
            else:
                no = no.dir
            profundidade += 1

        return -1

    def imprimir_ancestrais(self, valor):
        caminho = []

        def busca(no):
            if no is None:
                return False
            if no.valor == valor:
                return True

            if busca(no.esq) or busca(no.dir):
                caminho.append(no.valor)
                return True
            return False

        busca(self.raiz)
        print("Ancestrais:", caminho)

    def imprimir_descendentes(self, valor):
        no = self.buscar(self.raiz, valor)

        def descendentes(n):
            if n:
                print(n.valor, end=" ")
                descendentes(n.esq)
                descendentes(n.dir)

        if no:
            descendentes(no.esq)
            descendentes(no.dir)
        print()

    def analisar_arvore(self, valor_busca):
        print("=== DIAGNÓSTICO GERAL ===")
        print("Raiz:", self.raiz.valor if self.raiz else None)

        print("Nós internos:")
        self.imprimir_nos_internos()

        print("Folhas:")
        self.imprimir_folhas()

        print("Níveis:")
        self.imprimir_niveis()

        print("\n=== DIAGNÓSTICO ESPECÍFICO ===")
        no = self.buscar(self.raiz, valor_busca)

        if not no:
            print("Valor não encontrado.")
            return

        grau = 0
        if no.esq:
            grau += 1
        if no.dir:
            grau += 1

        print("Grau do nó:", grau)

        self.imprimir_ancestrais(valor_busca)

        print("Descendentes:")
        self.imprimir_descendentes(valor_busca)

        print("Altura do nó:", self.calcular_altura(no))
        print("Profundidade:", self.calcular_profundidade(valor_busca))


if __name__ == "__main__":
    arvore = ArvoreBST()

    valores = [50, 30, 70, 20, 40, 60, 80]
    for v in valores:
        arvore.inserir(v)

    arvore.analisar_arvore(30)
