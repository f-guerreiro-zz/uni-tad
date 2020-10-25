from DateStruct import DateStruct
from Controller import Controller

date = DateStruct(0,0,0)
d = Controller(date)

##atividade a
d.readDate()
print("Date:", d)

##atividade b
d.validDate()

##atividade c
d.isBissexto()

##atividade d
d.dataPascoa()

##atividade e
d.acrescentarDias()
d.escreveData()