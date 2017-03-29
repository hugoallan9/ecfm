#-*-encoding:utf8-*-
import openpyxl
from openpyxl import load_workbook
from random import shuffle
import random
import datetime
from operator import itemgetter
import smtplib

class Listado:
    def __init__(self):
        self.listado = []
        self.horarios = []
        self.listado_nuevo = []

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

    def obtener_horas(self):
        for x in self.listado:
            if  x[1] not in self.horarios:
                self.horarios.append(x[1])
        print(self.horarios)

    def desordenar(self):
        shuffle(self.listado)

    def cambiar_horas_entrada(self):
        tarde = False
        y = []
        for x in self.listado:
            y.append(x[0])
            if self.reset() and not tarde:
                tarde = True
                if x[1].minute == 0:
                    y.append(datetime.time(x[1].hour+1, random.randint(0,10)))
                else:
                    y.append(datetime.time(x[1].hour, random.randint(x[1].minute,x[1].minute+5)))
            else:
                if x[1].minute == 0:
                    y.append(datetime.time(x[1].hour-1, random.randint(49,59)))
                else:
                    y.append(datetime.time(x[1].hour, random.randint(x[1].minute-5,x[1].minute)))
            self.listado_nuevo.append(y)
            y = []
        self.listado_nuevo.sort(key=itemgetter(1))
        print('Las nuevas horas de entrada son: \n')
        for x in self.listado_nuevo:
            print x[0], str(x[1]), '\n'


    def enviar_mail(self):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("hugoallangm@gmail.com", "")
        for x in self.listado_nuevo:
            msg = x[0] + str(x[1])
            server.sendmail("hugoallangm@hotmail.com", "hugoallangm@hotmail.com", msg)
        server.quit()

    def reset(percent=2):
        return random.randrange(100) < percent



lista = Listado()
lista.leer_libro()
lista.obtener_horas()
lista.desordenar()
lista.cambiar_horas_entrada()
lista.enviar_mail()
