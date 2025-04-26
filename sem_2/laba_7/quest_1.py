import numpy as np
import random
import time



def main():
    print("Enter the size of the matrix: ")
    n = input()

    if n.isdigit():
        n = int(n)
    else:
        print("Size is incorrect")
        return

    A = np.zeros((n,n))
    B = np.zeros((n,n))
    C = np.zeros((n,n))
    random.seed(time.time())

    for i in range(n):
        for j in range(n):
            A[i][j] = random.randint(0, 100)
            B[i][j] = (random.random()*100) // 1
            print(A[i][j], B[i][j])
            if A[i][j] == B[i][j]:
                C[i][j] = True
            else:
                C[i][j] = False

    print(C)


if __name__ == "__main__":
    main()