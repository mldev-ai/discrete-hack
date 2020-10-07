import numpy
import scipy
import matplotlib.pyplot as plt

class Optimize():
    def __init__(self):
        self.size_grid = []
        self.pieces = []
        self.forbidden = []
        self.penalty = []
        self.loss = []
        input_data = (open('Problems/Problem1.txt', "r").read()).split('\n')
        self.size_grid = map(int, input_data[1].split(' '))
        for i in range(3, input_data.index('FORBIDDEN')):
            self.pieces.append(input_data[i].split(' '))
        for i in range(input_data.index('FORBIDDEN') + 1, input_data.index('PENALTY')):
            self.forbidden.append(input_data[i].split(','))
        for i in range(input_data.index('PENALTY') + 1, len(input_data)-1):
            self.penalty.append(input_data[i].split(','))
        for i in range(len(self.penalty)):
            self.loss.append(self.penalty[i][0].split(' ')[0])
            self.loss.append(self.penalty[i][0].split(' ')[1])

    def validate(self):
        print(self.size_grid)
        print(self.pieces)
        print(self.forbidden)
        print(self.loss)

    def grid(self):
        grid = numpy.zeros([self.size_grid[0], self.size_grid[1]])
        print(grid)

    def rank(self):
        rank = []
        obj = []
        for i in range(len(self.pieces)):
            rank.append(self.loss.count(self.pieces[i][0]))
            obj.append(self.pieces[i][0])
        zipped_pairs = zip(rank, obj)# fig = plt.figure()
        z = [x for _, x in sorted(zipped_pairs)]
        return z

    def box(self):
        grid = numpy.zeros([self.size_grid[0], self.size_grid[1]])
        return grid

    def plot(self):
        plt.xlim(0 ,self.size_grid[0])
        plt.ylim(0 ,self.size_grid[1])
        plt.xticks([i for i in range(self.size_grid[0])])
        plt.yticks([j for j in range(self.size_grid[1])])
        plt.grid(color = 'b', linewidth = 1.5)
        plt.title("The visulaization of pieces arrangment")
        plt.show()

    def shape(self):
        piece = self.rank()
        print(piece)
        shape = []
        for i in range(len(piece)):
            for j in range(len(self.pieces)):
                if piece[i]==self.pieces[j][0]:
                    shape.append(self.pieces[i][1])
        return shape

if __name__ == "__main__":
    Optimize().plot()