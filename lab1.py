import numpy as np

def print_condition(A, A_rev, x, i):

    print("Матрица A:")
    for row in A:
        print("  ".join(f"{num:3}" for num in row))

    print("\nОбратная матрица A^(-1):")
    for row in A_rev:
        print("  ".join(f"{num:3}" for num in row))
    
    print("\nСтолбец x:")
    for num in x: 
        print(f"{num:3}")
    print()

    A_bar = A.copy()
    A_bar[:, i-1] = x 

    print(f"После замены {i}-го столбца получилась матрица A̅:")
    for row in A_bar:
        print("  ".join(f"{num:3}" for num in row))
    print()


def find_inverse_matrix(A_rev, x, i):

    rows_A, cols_A = A_rev.shape
    rows_x = x.shape

    #Шаг 1 алгоритма
    l = np.dot(A_rev, x)
    if (l[i - 1] == 0): 
        print("Матрица A̅ необратима!")
        return
    else: 
        print("Матрица A̅ обратима!")
    print()

    #Шаг 2 алгоритма
    l_tilde = l.copy()
    l_tilde[i - 1] = -1

    #Шаг 3 алгоритма
    l_hat = (-1 / l[i - 1]) * l_tilde

    #Шаг 4 алгоритма
    Q = np.eye(rows_A)
    Q[:, i - 1] = l_hat

    A_bar_rev = np.empty((rows_A, rows_A))

    #Шаг 5 алгоритма
    for j in range(rows_A): 
        for k in range(rows_A):
            if (k == i - 1):
                A_bar_rev[k, j] = Q[k, k] * A_rev[i - 1, j]
            else: A_bar_rev[k, j] = Q[k, k] * A_rev[k, j] +  Q[k, i - 1] * A_rev[i - 1, j]

    print("Обратная матрица A̅^(-1):")
    for row in A_bar_rev:
        print("  ".join(f"{num:5.1f}" for num in row))
    print()


    
def main():

    A = np.array([[1, -1, 0], [0, 1, 0], [0, 0, 1]])
    A_rev = np.array([[1, 1, 0], [0, 1, 0], [0, 0, 1]])
    x = np.array([1, 0, 1])
    i = 3

    '''
    A = np.array([[1, 2, 3], [0, 1, 4], [0, 0, 1]])
    A_rev = np.array([[1, -2, 5], [0, 1, -4], [0, 0, 1]])
    x = np.array([1, 1, 1])
    i = 1
    '''
    
    '''
    A = np.array([[1, -1, 0, 1], [-1, 2, -1, 0], [0, 2, 0, 1], [2, 0, 1, 2]])
    A_rev = np.array([[-2, 3, -4, 3], [-1, 1, -1, 1], [0, -2, 2, -1], [2, -2, 3, -2]])
    x = np.array([1, 0, 2, 5])
    i = 1
    '''

    '''
    A = np.array([[1, 5, 3], [4, 8, 6], [7, 0, 9]])
    A_rev = np.round(np.linalg.inv(A), 2)
    x = np.array([2, 5, 8])
    i = 2
    '''


    print_condition(A, A_rev, x, i)
    find_inverse_matrix(A_rev, x, i)

if __name__ == "__main__":
    main()
