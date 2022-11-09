from mrjob.job import MRJob

class MRWordFrequencyCount(MRJob):
    def mapper(self, _, line):
        company, price, date = line.split(',')
        yield company, float(price)
    def reducer(self, company, values):
        crecimiento = ""
        l = list(values)
        segundo_precio = l[1]
        for i in l:
            if i < segundo_precio:
                crecimiento = "Crece"
                break
            else:
                crecimiento = "No crece"

        yield company, crecimiento
if __name__ == '__main__':
    MRWordFrequencyCount.run()