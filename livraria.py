from datetime import datetime

class Livro:
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


    @staticmethod
    def validarAno(valor):

        try: 
            ano = int(valor)
        except ValueError:
            raise ValueError("Digite apenas números. ")

        if ano <= 0 or ano > datetime.now().year:
            raise ValueError("Ano inválido.")

        return ano
        
    @staticmethod
    def validarPositivo(valor, tipo):
        try:
            numero = tipo(valor)
        except ValueError:
            raise ValueError("Digite apenas números. ")

        if numero < 0:
            raise ValueError("Número negativo.")

        return numero

    @staticmethod
    def pedirValor(mensagem, validador, *args):
        while True:
            try:
                entrada = input(mensagem)
                return validador(entrada, *args)
            except ValueError as erro:
                print(f"Entrada inválida: {erro}")

    @staticmethod
    def verificarLivro(codigo):
        for livro in livros:
            if codigo == livro.codigo:
                return True

        return False
    
    @staticmethod
    def verificarEntradas(palavra):
        
        if palavra.strip() == "":
            raise ValueError("Entrada vazia!")
        
        if "," in palavra:
            raise ValueError("Não use vírgulas neste campo.")
            
        return palavra


    @classmethod
    def construtorPorInput(cls):
        titulo = cls.pedirValor("Digite o titulo: ",cls.verificarEntradas)
        codigo = cls.pedirValor("Digite o codigo: ",cls.verificarEntradas)
        editora = cls.pedirValor("Digite a editora: ",cls.verificarEntradas)
        categoria = cls.pedirValor("Digite a área do livro: ",cls.verificarEntradas)
        ano = cls.pedirValor("Digite o ano de lançamento: ", cls.validarAno)
        valor = cls.pedirValor("Digite o valor do livro: ", cls.validarPositivo, float)
        estoque = cls.pedirValor("Digite a quantidade em estoque: ", cls.validarPositivo, int)

        return livros.append(cls(titulo,codigo,editora,categoria,ano,valor,estoque))

    @classmethod
    def construtorPorBanco(cls, linha):
        try:
            if len(linha) != 7:
                raise ValueError("O registro deve conter 7 campos.")
            
            codigo = cls.verificarEntradas(linha[0])
            titulo = cls.verificarEntradas(linha[1])
            ano = cls.validarAno(linha[2])
            categoria = cls.verificarEntradas(linha[3])
            editora = cls.verificarEntradas(linha[4])
            valor = cls.validarPositivo(linha[5].replace("R$", ""), float)
            estoque = cls.validarPositivo(linha[6], int)

        except ValueError as erro:
            print(f"Registro ignorado: {erro}")
            return

        return livros.append(cls(titulo,codigo,editora,categoria,ano,valor,estoque))


if __name__ == '__main__':

    bancoDadosInseridos = False

    def atualizarBanco():

        arquivo = open("banco_dados_livros.txt", "w")

        for livro in livros:
            arquivo.write(
                f"{livro.codigo},{livro.titulo},{livro.ano},{livro.categoria},"
                f"{livro.editora},R${livro.valor},{livro.quantidadeEmEstoque}\n"
            )

        arquivo.close()


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
                8 - Carregar Estoque
                9 - Atualizar Estoque
                0 - Encerrar o sistema
                                
                Escolha a opção desejada: """))
        except ValueError:
            print("\nDigite somente numeros")
            continue
        
        match entrada:

            case 1: 
                Livro.construtorPorInput()

            case 2:
                for livro in livros:
                    livro.info()


            case 3:
                nomePesquisa = input("Digite o nome do livro: ")

                for livro in livros:
                    if livro.titulo.lower() == nomePesquisa.lower():
                        livro.info()
                        break
                else:
                    print(f"Nenhum livro encontrado com o título '{nomePesquisa}'.")


            case 4:
                encontrou = False
                categoriaPesquisa = input("Digite a categoria: ")

                for livro in livros:
                    if livro.categoria.lower() == categoriaPesquisa.lower():
                        livro.info()
                        encontrou = True

                if not encontrou:
                    print(f"Nenhum livro encontrado na categoria '{categoriaPesquisa}'.")


            case 5:
                encontrou = False
                precoPesquisa = Livro.pedirValor("Digite o valor maximo: ", Livro.validarPositivo,float)

                for livro in livros:
                    if livro.valor <= precoPesquisa:
                        livro.info()
                        encontrou = True

                if not encontrou:
                    print(f"Nenhum livro encontrado com valor inferior a R${precoPesquisa:.2f}.")


            case 6:
                encontrou = False
                estoquePesquisa = Livro.pedirValor("Digite o estoque minimo: ", Livro.validarPositivo, int)

                for livro in livros:
                    if livro.quantidadeEmEstoque > estoquePesquisa:
                        livro.info()
                        encontrou = True

                if not encontrou:
                    print(f"Nenhum livro encontrado com estoque maior ou igual a {estoquePesquisa}.")


            case 7:
                totalEstoque = 0
                
                for livro in livros:
                    totalEstoque += (livro.quantidadeEmEstoque * livro.valor)

                print(f"Valor total do estoque: R${totalEstoque:.2f}")
            

            case 8:
                try:
                    arquivo = open("banco_dados_livros.txt", "r")
                except FileNotFoundError:
                    print("Erro ao encontrar o arquivo, tente novamente.")
                    continue

                linha = arquivo.readline()

                while linha:
                    texto = linha.strip().split(",")

                    if Livro.verificarLivro(texto[0]):
                        print("Banco de dados já inserido!")
                        break

                    Livro.construtorPorBanco(texto)

                    linha = arquivo.readline()

                else:
                    bancoDadosInseridos = True
                    print("Banco de Dados inserido com sucesso! ")

                arquivo.close()


            case 9:

                if bancoDadosInseridos:
                    atualizarBanco()
                else:
                    print("Banco de dados não inserido")
                    continue  
                                
            case 0:
                atualizar = input("Deseja atualizar banco de dados? Sim/Não: ")

                if atualizar.lower() == "sim":
                    atualizarBanco()
                    flag = False
                elif atualizar.lower() == "não" or atualizar.lower() == "nao":
                    flag = False
                else:
                    print("\nDigite apenas Sim/Não. Sistema voltando ao inicio.")
                    continue

            case default:
                print("Digite apenas de 0 a 9")
        
