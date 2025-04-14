import numpy
import numpy as np
import random


def main():
    print("Enter the size of the matrix: ")
    n = input()

    if n.isdigit():
        n = int(n)
    else:
        print("Size is incorrect")
        return

    A = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            A[i][j] = random.random() * 100 // 1

    colomn_summ = A.sum(axis=0)
    min_sum = min(colomn_summ)
    for i in range(len(colomn_summ)):
        if min_sum == colomn_summ[i]:
            print(f"Minimal mean is on the {i} colomn")
            return


if __name__ == "__main__":
    main()
