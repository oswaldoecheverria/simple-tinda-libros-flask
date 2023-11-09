from .entities.Autor import Autor
from .entities.Libro import Libro


class ModeloLibro:

    """_summary_
    *   Este metodo recibira la como parametro la conexion
    *   Dentro de este metodo tendremos todo lo referente al cursos
            las sentencias sql, la ejecucion y el procesamiento de los datos
            resultantes
    *   Tambien este sera un metodo de clase con mediante el
            decorador @classmethod para poder utilizarlo sin utilizar
            una instancia de la clase del ModeloLibro que es la instancia
            que tenemos en la BD
    *   En data=cursor.fetchall() tenemos todos los datos resultantes
            en forma de tupla ademas es un objeto que podemos iterar
            Ahora lo que hacemos es que podriamos colocarlos esos datos
            en la plantilla con sus debidas posiciones pero no es lo mas optimo
            lo mas optimo es iterarlos
    *   aut = Autor(0, row[4], row[5])
            Lo que hacemos en esta linea es crear una instancia de la clase Autor
            row[4] y row[5] representan la posicion que en el orden que se pide
            y se devuelven los datos de LA secuencia sql que esta en la variable sql,
            comenzando a contar desde la posicion 0
    """

    @classmethod
    def listar_libros(self, db):
        try:
            cursor = db.connection.cursor()
            sql = """ SELECT LIB.isbn, LIB.titulo, LIB.anioedicion, LIB.precio, AUT.apellido, AUT.nombre
                        FROM libro AS LIB JOIN autor AUT ON LIB.autor_id = AUT.id
                        ORDER BY LIB.titulo ASC; """
            cursor.execute(sql)
            # Obtenemos los datos
            data = cursor.fetchall()
            # Devolvemos el listado de objetos
            libros = []
            for row in data:
                # Intancia de clases
                aut = Autor(0, row[4], row[5])
                lib = Libro(row[0], row[1], aut, row[2], row[3])
                # Anexamos el libro que vamos a ir recorriendo
                libros.append(lib)
            return libros
        except Exception as ex:
            raise Exception(ex)
