import csv
import json
from abc import ABC, abstractmethod

from fpdf import FPDF

CAMPOS = ("id", "nombre", "precio", "stock")


class Exportador(ABC):
    @abstractmethod
    def exportar(self, datos, ruta_archivo):
        raise NotImplementedError("Este método debe ser implementado por la subclase.")


class ExportadorTXT(Exportador):
    def exportar(self, datos, ruta_archivo):
        with open(ruta_archivo, "w", encoding="utf-8") as file:
            file.write("--- REPORTE DE PRODUCTOS ---\n")
            for p in datos:
                file.write(
                    f"ID: {p['id']} | Nombre: {p['nombre']} | "
                    f"Precio: ${p['precio']:.2f} | Stock: {p['stock']}\n"
                )
        print(f"Archivo TXT generado en: {ruta_archivo}")


class ExportadorCSV(Exportador):
    def exportar(self, datos, ruta_archivo):
        # utf-8-sig para que Excel muestre bien los acentos
        with open(ruta_archivo, "w", newline="", encoding="utf-8-sig") as file:
            writer = csv.DictWriter(file, fieldnames=CAMPOS, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(datos)
        print(f"Archivo CSV generado en: {ruta_archivo}")


class ExportadorJSON(Exportador):
    def exportar(self, datos, ruta_archivo):
        # precio viene como Decimal (no serializable): default=float lo convierte
        with open(ruta_archivo, "w", encoding="utf-8") as file:
            json.dump(
                [dict(p) for p in datos],
                file,
                ensure_ascii=False,
                indent=4,
                default=float,
            )
        print(f"Archivo JSON generado en: {ruta_archivo}")


class ExportadorPDF(Exportador):
    @staticmethod
    def _texto(valor):
        return str(valor).encode("latin-1", "replace").decode("latin-1")

    def exportar(self, datos, ruta_archivo):
        pdf = FPDF()
        pdf.add_page()

        # Título
        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, txt="Reporte de Inventario de Productos", ln=1, align="C")
        pdf.ln(5)

        # Encabezado de la tabla
        anchos = (20, 90, 40, 30)
        pdf.set_font("Arial", "B", 12)
        for ancho, titulo in zip(anchos, ("ID", "Nombre", "Precio", "Stock")):
            pdf.cell(ancho, 10, txt=titulo, border=1, align="C")
        pdf.ln()

        # Filas
        pdf.set_font("Arial", size=12)
        for p in datos:
            pdf.cell(anchos[0], 10, txt=str(p["id"]), border=1, align="C")
            pdf.cell(anchos[1], 10, txt=self._texto(p["nombre"]), border=1)
            pdf.cell(anchos[2], 10, txt=f"${p['precio']:.2f}", border=1, align="R")
            pdf.cell(anchos[3], 10, txt=str(p["stock"]), border=1, align="C")
            pdf.ln()

        pdf.output(ruta_archivo)
        print(f"Archivo PDF generado en: {ruta_archivo}")
