import csv
import numpy as np


def main():
    with open('udemy_courses.csv', 'r') as f:
        data = []
        names = f.readline()
        data.append(names)
        for line in f:
            buff = line.strip().split(",")
            buff[0] = 0
            match buff[4]:
                case 'All Levels':
                    buff[4] = 0
                case 'Beginner Level':
                    buff[4] = 1
                case 'Intermediate Level':
                    buff[4] = 2
                case 'Expert Level':
                    buff[4] = 3
            buff = list(map(float, buff))
            data.append(buff)
        data = data[1:]
        data = np.array(data)
        mean_price = data.mean(axis=0)[1]
        min_count_sub = np.min(data, axis=0)[2]
        max_lection_length = np.max(data, axis=0)[5]
        levels = [data[_][4] for _ in range(len(data))]
        counts = np.bincount(levels)
        max_count = np.argmax(counts)
        match max_count:
            case 0:
                max_count = 'All Levels'
            case 1:
                max_count = 'Beginner Level'
            case 2:
                max_count = 'Intermediate Level'
            case 3:
                max_count = 'Expert Level'

        print(f"Mean course price {mean_price}")
        print(f"Min course subs {min_count_sub}")
        print(f"Max course length {max_lection_length}")
        print(f"Most popular level {max_count}")


if __name__ == "__main__":
    main()
