from repository import Repository
from person import Person


class PersonService:
    def __init__(self):
        pass

    def get_personList(self):
        print("\nLista de personas:")
        print(Repository.person)

    def agregarPersona(self):
        print("\n Agreganddo persona")
        name = str(input("\nIngrese el nombre: "))
        surname = str(input("Ingrese el apellido: "))
        age = str(input("Ingrese la edad: "))
        key = int(input("Ingrese la clave que quiere asignarle: "))
        person = Person(name, surname, age, key)
        self.add_person(person)

    def add_person(self, person):
        print("\n Agregar persona")
        key = person.key
        Repository.person[key] = person.__dict__

    def update_person(self, resultado = False):
        print("\n Update persona")
        print("\n La lista de personas es: ")
        print(Repository.person)
        if resultado == False:
            clave = int(input("\nIngrese la clave de la persona que quiere modificar: "))
        print("\n La persona a actualizar es:")
        print(Repository.person[clave])
        respuesta = str(input("\nEsta seguro que quiere modificar esta persona? (S/N): "))
        if respuesta.upper() == "S":
            person = Repository.person[clave]
            entrada = str(input("\nIngrese el nombre: "))
            person['_name'] = entrada.upper()
            entrada = str(input("Ingrese el apellido: "))
            person['_surname'] = entrada.upper()
            person['_age'] = int(input("Ingrese la edad: "))
        elif respuesta.upper() == "N":
            pass

    # Elimina persona segun key del dic person
    def delete_person(self):
        print("\n Eliminar persona")
        print("\n La lista de personas es: ")
        print(Repository.person)
        clave = int(input("\nIngrese la clave de la persona que desea eliminar: "))
        print("\nLa persona a eliminar es: ")
        print(Repository.person[clave])
        respuesta = str(input("\nEsta seguro que quiere eliminar esta persona? (S/N): "))
        if respuesta.upper() == "S":
            del Repository.person[clave]
        elif respuesta.upper() == "N":
            pass
