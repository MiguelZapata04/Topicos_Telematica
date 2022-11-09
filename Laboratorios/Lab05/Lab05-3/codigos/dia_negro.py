from mrjob.job import MRJob

global precio_dia_negro
global fecha_dia_negro

class MRWordFrequencyCount(MRJob):
    def mapper(self, _, line):
        lista_datos = []
        list_linea = line.split(',')
        while len(list_linea) != 0:
            lista_datos.append(list_linea)
        yield lista_datos, "Dia negro"

    def reducer(self, lista_datos, values):
        precio_dia_negro = 1000000000
        fecha_dia_negro = ""
        suma_valores = 0
        for j in lista_datos:
            suma_valores = suma_valores + j[1]

if __name__ == '__main__':
    MRWordFrequencyCount.run()