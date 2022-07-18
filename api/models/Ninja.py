from django.db import models
from api.models.Persona import Persona
class Ninja(Persona):
    chakra_max = models.IntegerField(default=0)
    sobrenombre = models.CharField(max_length=50, default="")
    def save(self, *args, **kargs):
        try:
            file = open("file.txt", "r")
            msg = file.read()
            file.close()
            print(msg)
            self.id = int(msg)
            objecto=Persona.objects.filter(id=self.id)
            if len(objecto)>0:
                self.nombre=objecto[0].nombre
                self.edad=objecto[0].edad
                self.clan=objecto[0].clan
                self.sexo=objecto[0].sexo
                self.fecha_nacimiento=objecto[0].fecha_nacimiento
            super().save(*args, **kargs)
        except Exception as e:
            print(e)

    def __iter__(self):
        yield self.pk
        yield self.nombre
        yield self.edad
        yield self.sexo
        yield self.clan
        yield self.fecha_nacimiento
        yield self.chakra_max
        yield self.sobrenombre
    def add_values(self, values):
        headers = Ninja.get_headers()
        headers.pop(0)
        for i in range(len(headers)):
            if headers[i] == 'Nombre':
                self.nombre = values[i]
            elif headers[i] == 'Edad':
                self.edad = values[i]
            elif headers[i] == 'Sexo':
                self.sexo = values[i]
            elif headers[i] == 'Clan':
                self.clan = values[i]
            elif headers[i] == 'Fecha Nacimiento':
                self.fecha_nacimiento = values[i]
            elif headers[i] == 'Chakra Maximo':
                self.chakra_max = values[i]
            elif headers[i] == 'Sobrenombre':
                self.sobrenombre = values[i]
    @staticmethod
    def get_headers():
        headers = Persona.get_headers()
        headers.append('Chakra Maximo')
        headers.append('Sobrenombre')
        return headers
    @staticmethod
    def get_types():
        types = Persona.get_types()
        types.append('Int')
        types.append('Char')
        return types
    @staticmethod
    def get_pointers():
        pointers = Persona.get_pointers()
        pointers.append('')
        pointers.append('')
        return pointers
