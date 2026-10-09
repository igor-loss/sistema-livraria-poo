class Livraria:
    def __init__(self, titulo, codigo, editora, categoria, ano, valor, quantidadeEmEstoque):
        self.titulo = titulo
        self.codigo = codigo
        self.editora = editora
        self.categoria = categoria
        self.ano = ano
        self.valor = valor
        self.quantidadeEmEstoque = quantidadeEmEstoque
    
    def info(self):
        print("\nInformação do livro")
        print(f"Titulo: {self.titulo}")
        print(f"Codigo: {self.codigo}")
        print(f"Editora: {self.editora}")
        print(f"Categoria: {self.categoria}")
        print(f"Ano de publicação: {self.ano}")
        print(f"Valor: R${self.valor:.2f}")
        print(f"Quantidade em Estoque: {self.quantidadeEmEstoque}")

if __name__ == '__main__':

    livros = []
    flag = True
    while flag:

        try: 
            entrada = int(input("""
                Bem Vindo a Livraria Prog II
                
                1 - Cadastrar livro
                2 - Listar livros
                3 - Buscar livros por nome
                4 - Buscar livros por categoria
                5 - Buscar livros por preço
                6 - Busca por quantidade do estoque
                7 - Valor total do estoque
                0 - Encerrar o sistema
                                
                Escolha a opção desejada: """))
        except ValueError:
            print("\nDigite somente numeros")
            continue
        
        match entrada:
            case 1: 
                titulo = input("Digite o titulo: ")
                codigo = input("Digite o codigo: ")
                editora = input("Digite a editora: ")
                categoria = input("Digite a área do livro: ")

                try:
                    ano = int(input("Digite o ano de publicação: "))
                    valor = float(input("Digite o valor do livro: "))
                    estoque = int(input("Digite a quantidade de estoque: "))
                except ValueError:
                    print("Dados invalidos, tente novamente")
                    continue

                livros.append(Livraria(
                    titulo,codigo,editora,categoria,ano,valor,estoque
                ))


            case 2:
                for livro in livros:
                    livro.info()

            case 3:
                nomePesquisa = input("Digite o nome do livro: ")

                for livro in livros:
                    if livro.titulo == nomePesquisa:
                        livro.info()
                        break
                else:
                    print(f"Nenhum livro encontrado com o título '{nomePesquisa}'.")

            case 4:
                encontrou = False
                categoriaPesquisa = input("Digite a categoria: ")

                for livro in livros:
                    if livro.categoria == categoriaPesquisa:
                        livro.info()
                        encontrou = True

                if not encontrou:
                    print(f"Nenhum livro encontrado na categoria '{categoriaPesquisa}'.")

            case 5:
                encontrou = False
                try:
                    precoPesquisa = float(input("Digite o valor maximo: "))
                except ValueError:
                    print("Digite apenas numeros")
                    continue

                for livro in livros:
                    if livro.valor < precoPesquisa:
                        livro.info()
                        encontrou = True

                if not encontrou:
                    print(f"Nenhum livro encontrado com valor inferior a R${precoPesquisa:.2f}.")

            case 6:
                encontrou = False
                try:
                    estoquePesquisa = int(input("Digite o estoque minimo: "))
                except ValueError:
                    print("Digite apenas numeros")
                    continue

                for livro in livros:
                    if livro.quantidadeEmEstoque >= estoquePesquisa:
                        livro.info()
                        encontrou = True

                if not encontrou:
                    print(f"Nenhum livro encontrado com estoque maior ou igual a {estoquePesquisa}.")

            case 7:
                totalEstoque = 0
                
                for livro in livros:
                    totalEstoque += (livro.quantidadeEmEstoque * livro.valor)

                print(f"Valor total do estoque: R${totalEstoque:.2f}")
                
            case 0:
                flag = False

            case default:
                print("Digite apenas de 0 a 7")
        
