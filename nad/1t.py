# Дана целочисленная матрица A(N, N). 
# Необходимо реализовать функцию, которая будет менять местами
# элементы главной и побочной диагоналей.

import random

def swap_diagonals(matrix_, n):
    tmp = 0
    i = 0
    j = n-1
    
    while i < n:
        tmp = matrix_[i][i]
        matrix_[i][i] = matrix_[i][j]
        matrix_[i][j] = tmp
        i += 1
        j -= 1

def print_matrix(matrix_, n):
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=' ')
        print()
        
    
n = int(input())

if (n <= 0):
    print("Error! The number cannot be negative or null!")
else:
    matrix = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            matrix[i][j] = random.randint(1, 9)
        
    print_matrix(matrix, n)
    print()
    swap_diagonals(matrix, n)
    print_matrix(matrix, n)
