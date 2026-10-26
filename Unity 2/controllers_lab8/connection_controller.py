import psycopg2


class Conexion:

    def __init__(self):
        self.host = "localhost"
        self.puerto = 5432
        self.usuario = "postgres"
        self.password = "Pepito57!"
        self.base_datos = "login_mvc"

    def conectar(self):
        try:
            return psycopg2.connect(
                host=self.host,
                port=self.puerto,
                user=self.usuario,
                password=self.password,
                dbname=self.base_datos
            )
        except psycopg2.Error as error:
            print("Error al conectar con PostgreSQL:", error)
            return None