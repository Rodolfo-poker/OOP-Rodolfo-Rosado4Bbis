import psycopg2
from controllers_lab8.connection_controller import Conexion


class UserModel:

    def __init__(self):
        self.conexion_db = Conexion()

    def registrar_usuario(self, nombre, email, password):
        conexion = self.conexion_db.conectar()

        if conexion is None:
            return "error"

        cursor = None

        try:
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO users (nombre, email, password) VALUES (%s, %s, %s)",
                (nombre, email, password)
            )
            conexion.commit()
            return "ok"

        except psycopg2.IntegrityError:
            conexion.rollback()
            return "duplicado"

        except psycopg2.Error as error:
            conexion.rollback()
            print("Error al registrar usuario:", error)
            return "error"

        finally:
            if cursor is not None:
                cursor.close()
            conexion.close()

    def validar_usuario(self, email, password):
        conexion = self.conexion_db.conectar()

        if conexion is None:
            return None

        cursor = None

        try:
            cursor = conexion.cursor()
            cursor.execute(
                "SELECT id, nombre FROM users WHERE email = %s AND password = %s",
                (email, password)
            )
            return cursor.fetchone()

        except psycopg2.Error as error:
            print("Error al validar usuario:", error)
            return None

        finally:
            if cursor is not None:
                cursor.close()
            conexion.close()

    def cerrar(self):
        pass