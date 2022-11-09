from mrjob.job import MRJob
class MRWordFrequencyCount(MRJob):
    def mapper(self, _, line):
        user, movie,rating,genre, date = line.split(',')
        yield date, float(rating)
        
    def reducer(self, movie, values):
        l = list(values)
        avg = 0
        for i in l:
            avg = avg + i[1]

        yield movie, (len(l),avg/len(l))
if __name__ == '__main__':
    MRWordFrequencyCount.run()