from tools.Abilities import Abilities


class Matrix:
    """ This class represents a simple matrix so that we can store tools.Abilities in it """
    def __init__(self):
        self.x_len = 0
        self.y_len = 0
        self.matrix = [[Abilities]]

    def init_matrix(self, matrix):
        self.x_len = len(matrix)
        self.y_len = len(matrix[0])
        self.matrix = matrix

    def get_item(self, x, y):
        return self.matrix[x][y]

    def get_x_len(self):
        return self.x_len

    def get_y_len(self):
        return self.y_len

    def get_matrix(self):
        return self.matrix

    def pprint(self):
        if self.x_len != 0:
            for y in range(self.y_len):
                line = ''
                for x in range(self.x_len):
                    line += self.matrix[x][-y-1].value + '\t'
                print(line)
