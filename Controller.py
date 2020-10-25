from time import strftime

from DateStruct import DateStruct
from datetime import datetime, timedelta



class Controller:
    def __init__(self, date):
        self.date = date

    def __str__(self):
        return f"{self.date.day}/{self.date.month}/{self.date.year}"

    def startDate(self, day, month, year):
        return DateStruct(day, month, year)

    def readDate(self):
        day = int(input("Day: "))
        month = int(input("Month: "))
        year = int(input("Year: "))
        self.date = self.startDate(day, month, year)

    def verifyDay(self):
        if 1 <= self.date.day <= 31:
            return True
        else:
            return False

    def verifyMonth(self):
        if 1 <= self.date.month <= 12:
            return True

    def verifyYear(self):
        if ((len(str(self.date.year)) == 4) and (self.date.year > 0)):
            return True
        else:
            return False

    def validDate(self):
        d = self.verifyDay()
        m = self.verifyMonth()
        y = self.verifyYear()
        if (d == True and m == True and y == True):
            print("Data Valida")
            return True
        else:
            print("Data Invalida")
            return False

##atividade c
    def isBissexto(self):
        year = int(input("Coloque o ano: "))

        #checa se é bissexto
        if year % 4 == 0 and year % 100 != 0:
            print(year, "1 é bissexto")
        elif year % 100 == 0:
            print(year, "0 não é bissexto")
        elif year % 400 == 0:
            print(year, "0 não é bissexto")
        else:
            print(year, "0 não é bissexto")

##atividade d
    def dataPascoa(self):
        y = int(input("Coloque um ano para calcular data da pascoa: "))

        d = (y % 19 * 19 + 15) % 30
        e = (y % 4 * 2 + y % 7 * 4 - d + 34) % 7 + d + 127
        m = e / 31
        a = e % 31 + 1 + (m > 4)

        if a > 30: a, m = 1, 5
        print (a, '/', m, '/', y)

##atividade e 1
    def acrescentarDias(self):
        day = int(input("Day: "))
        month = int(input("Month: "))
        year = int(input("Year: "))
        daysToBeAdd = int(input("Dias a acrescentar: "))
        self.date = datetime(year, month, day)

        new_date = self.date + timedelta(days= daysToBeAdd)
        print(new_date)

##atividade e 2
    def escreveData(self):
        day = int(input("Day: "))
        month = int(input("Month: "))
        year = int(input("Year: "))
        self.date = datetime(year, month, day)

        print(self.date.strftime('%d %B %Y'))




