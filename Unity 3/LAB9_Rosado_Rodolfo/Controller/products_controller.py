from Models.products_model import Producto
from exportadores import (
    ExportadorCSV,
    ExportadorTXT,
    ExportadorJSON,
    ExportadorPDF,
)


class ProductosController:
    EXPORTADORES = {
        "CSV": ExportadorCSV,
        "TXT": ExportadorTXT,
        "JSON": ExportadorJSON,
        "PDF": ExportadorPDF,
    }

    def generar_reporte(self, formato, ruta_archivo):
        clase_exportador = self.EXPORTADORES.get(formato)
        if clase_exportador is None:
            return False, f"Formato no soportado: {formato}"

        datos = Producto().obtener_todos()
        if not datos:
            return False, "No hay productos para exportar."

        try:
            exportador = clase_exportador()
            exportador.exportar(datos, ruta_archivo)  # polimorfismo
        except Exception as e:
            return False, f"No se pudo generar el reporte:\n{e}"

        return True, f"Reporte {formato} generado en:\n{ruta_archivo}"
