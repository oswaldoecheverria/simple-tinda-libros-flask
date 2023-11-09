class Compra:

    def __init__(self, uuid, libro_isbn, usuario_id, fecha=None):
        self.uuid = uuid
        self.libro_isbn = libro_isbn
        self.usuario_id = usuario_id
        self.fecha = fecha