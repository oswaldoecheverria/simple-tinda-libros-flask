class Autor:
    def __init__(self, id, apellido, nombre, fecha_nacimeinto=None):
        self.id = id
        self.apellido = apellido
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimeinto

    def nombre_completo(self):
        return "{0}, {1}".format(self.apellido, self.nombre)
