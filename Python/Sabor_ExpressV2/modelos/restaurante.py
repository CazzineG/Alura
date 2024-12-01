class Restaurante:

    restaurantes = list()

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.capitalize()
        self._ativo = bool(False)
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'.ljust(5)} \n')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo.ljust(5)}')

    @property
    def ativo(self):
        return '✅' if self._ativo else '❌'
    
    def alternar_estado(self):
        self._ativo = not self._ativo


restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('Pizza Express', 'Itáliana')
restaurante_padaria = Restaurante('Padaria Torre Forte', 'Padaria')
restaurante_padaria.alternar_estado()

Restaurante.listar_restaurantes()

