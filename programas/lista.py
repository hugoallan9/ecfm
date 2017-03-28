import openpyxl
from openpyxl import load_workbook

class Listado:
    def __init__(self):
        self.listado = []

    def leer_libro(self):
        wb = load_workbook('empleados.xlsx')
        sheet_ranges = wb['Hoja1']
        profesor_hora = []
        for row in sheet_ranges:
            for cell in row:
                profesor_hora.append(cell.value)
            self.listado.append(profesor_hora)
            profesor_hora = []
        print( self.listado )

lista = Listado()
lista.leer_libro()
