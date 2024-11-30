class Restaurante:

    restaurantes = list()

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = bool(False)
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')


restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Itáliana')

Restaurante.listar_restaurantes()