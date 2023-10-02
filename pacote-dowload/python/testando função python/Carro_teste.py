class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def descricao(self):
        return f"Este é um {self.marca} {self.modelo} do ano {self.ano}."

# Exemplo de uso da classe Carro
meu_carro = Carro("Ford", "Mustang", 2022)
print(meu_carro.descricao())


import unittest

class CarTest(unittest.TestCase):
    def setUp(self):
        self.car = Carro("Ford", "Mustang", 2022)

    def test_car_description(self):
        expected_description = "Este é um Ford Mustang do ano 2022."
        self.assertEqual(self.car.descricao(), expected_description)

if __name__ == '__main__':
    unittest.main()