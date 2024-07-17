# Дана целочисленная матрица A(N, N). 
# Необходимо реализовать функцию, которая будет менять местами
# элементы главной и побочной диагоналей.

def swap_diagonals(matrix_, n):
    if n < 0:
        print("Error! The size of the matrix must be positive.")
        return
    
    i = 0
    j = n - 1
    while i < n:
        tmp = matrix_[i][i]
        matrix_[i][i] = matrix_[i][j]
        matrix_[i][j] = tmp
        i += 1
        j -= 1



def print_matrix(matrix_, n):
    for i in range(n):
        for j in range(n):
            print(matrix_[i][j], end=' ')
        print()
        
        
def is_eq(matrix_1, matrix_2, n):
    flag = 1
    for i in range (n):
        for j in range (n):
            if matrix_1[i][j] != matrix_2[i][j]:
                flag = 0
    return flag


test = [
    [2, 8, 5, 2, 6],
    [7, 2, 7, 6, 4],
    [3, 7, 6, 3, 6],
    [1, 3, 2, 2, 9],
    [7, 9, 2, 1, 3]
]

correct = [
    [6, 8, 5, 2, 2],
    [7, 6, 7, 2, 4],
    [3, 7, 6, 3, 6],
    [1, 2, 2, 3, 9],
    [3, 9, 2, 1, 7]
]

swap_diagonals(test, 5)
if (test, correct, 5):
    print("TEST1: PASS")
else:
    print("TEST1: FAIL")


test = [
    [1, 0],
    [0, 1]
]

correct = [
    [0, 1],
    [1, 0]
]

swap_diagonals(test, 2)

if (is_eq(test, correct, 2)):
    print("TEST2: PASS")
else:
    print("TEST2: FAIL")
    

test = [
    [1]
]

correct = [
    [1]
]

swap_diagonals(test, 1)
if (is_eq(test, correct, 1)):
    print("TEST3: PASS")
else:
    print("TEST3: FAIL")
    
test = [[]]
correct = [[]]

swap_diagonals(test, 0)
if (is_eq(test, correct, 0)):
    print("TEST4: PASS")
else:
    print("TEST4: FAIL")
