class Matrix:

    def __init__(self, list_1, list_2):
        
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matrix = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                matrix[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix]))


my_matrix = Matrix([[3, 5, 32],
                    [2, 4, 6],
                    [-1, 64, -8]],
                   [[7, 5, 8],
                    [8, 6, 4],
                    [11, 6, 18]])

print(my_matrix.__add__())