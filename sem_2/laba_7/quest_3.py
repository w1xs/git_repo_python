import numpy as np


def main():
    with open("data.txt", "r") as f:
        n = int(f.readline())
        A = np.zeros((n, n))
        B = np.ndarray((n))
        for i in range(n):
            buff = f.readline().split()
            for j in range(len(buff)):
                A[i][j] = float(buff[j])
        buff = f.readline().split()
        if np.linalg.det(A) == 0:
            print("Matrix det == 0")
            return
        else:
            for i in range(len(buff)):
                B[i] = float(buff[i])
            x = np.linalg.solve(A, B)
            print(x)


if __name__ == "__main__":
    main()
