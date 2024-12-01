class Biblioteca:
    livros_disponiveis = []

    @classmethod
    def listar_livros(cls):
        print(f'{"Nome do livro: ".ljust(35)} | {"Autor: ".ljust(25)} | {"Ano de publicação: ".ljust(25)} | {"Status: ".ljust(5)}\n')
        for livro in cls.livros_disponiveis:
            print(livro)

class Livro:
    def __init__(self, titulo, autor, ano_de_publicacao, status=True):
        self._titulo = titulo
        self._autor = autor
        self._ano_de_publicacao = ano_de_publicacao
        self._status = status
        Biblioteca.livros_disponiveis.append(self)

    def __str__(self):
        return f'{self._titulo.ljust(35)} | {self._autor.ljust(25)} | {str(self._ano_de_publicacao).ljust(25)} | {"❎" if self._status else "❌".ljust(5)}'
    
    def alternar_status(self):
        self._status = not self._status

livro01 = Livro('A menina que roubava livros', 'Markus Zusak', 2005)
livro02 = Livro('O pequeno príncipe', 'Antoine de Saint-Exupéry', 1943)
livro02.alternar_status()
livro03 = Livro('O senhor dos anéis', 'J.R.R. Tolkien', 1954)

Biblioteca.listar_livros()