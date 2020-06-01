import unittest
from person import Person
from personService import PersonService
from repository import Repository
from parameterized import parameterized


class TestAgregar(unittest.TestCase):

    @parameterized.expand([
        ("Marian", "Colman", "21", 1),
        ("Jose", "Colman", "21", 2),
        ("Pepe", "Colman", "21", 3)
        ])

    def test_agregar(self, nombre, apellido, edad, key):
        persona = Person(nombre, apellido, edad, key)
        service = PersonService()
        service.agregarPersona()
        self.assertEqual(Repository.person[key], persona.__dict__)

class TestModificar(unittest.TestCase):

    @parameterized.expand([
        (1, {'_name': "MARIANO", '_surname': "COLMAN", '_age': 21, '_key': 1})
        ])

    def test_modificar(self, key, resultado):
        service = PersonService()
        service.update_person(False)
        self.assertEqual(Repository.person[key], resultado)


if __name__ == "__main__":
    unittest.main()