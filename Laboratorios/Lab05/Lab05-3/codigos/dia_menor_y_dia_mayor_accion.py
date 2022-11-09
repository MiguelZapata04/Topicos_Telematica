from mrjob.job import MRJob

class MRWordFrequencyCount(MRJob):
    def mapper(self, _, line):
        company, price, date = line.split(',')
        lista = [float(price), date]
        yield company, lista
    def reducer(self, company, values):
        l = list(values)
        menor = 10000000000
        mayor = 0
        mayor_fecha = 0
        menor_fecha = 0
        for i in l:
            if i[0]>mayor:
                if mayor != 0 and mayor < menor:
                    menor_fecha = mayor_fecha
                    menor = mayor
                mayor_fecha = i[1]
                mayor = i[0]
            elif i[0]<menor:
                menor_fecha = i[1]
                menor = i[0]
        yield company, (mayor_fecha, menor_fecha)
if __name__ == '__main__':
    MRWordFrequencyCount.run()