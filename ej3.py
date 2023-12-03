DATA_PATH = 'data/ej3.txt'
import itertools

def inputToArray(file):
    array = list(file.read().splitlines())

    return array


def ej1():
    with open(DATA_PATH) as file:
        array = inputToArray(file)
    n, m = len(array), len(array[0])
    checked = [[0]*m for _ in range(n)]
    res = 0

    def process_number(i, j):
        while j>=0 and array[i][j].isdigit():
            j -= 1
        cum = 0
        j += 1
        while j<m and array[i][j].isdigit():
            checked[i][j] = 1
            cum *= 10
            cum += int(array[i][j])
            j+=1

        return cum

    for i in range(n):
        for j in range(m):
            if (not array[i][j].isdigit()) and array[i][j] != '.':
                for _i, _j in itertools.product(range(max(i-1, 0), min(i+2, n)), range(max(j-1, 0), min(j+2, m))):
                    if array[_i][_j].isdigit() and checked[_i][_j] == 0:
                        res += process_number(_i, _j)


    print(res)


def ej2():
    with open(DATA_PATH) as file:
        array = inputToArray(file)
    n, m = len(array), len(array[0])
    checked = [[0]*m for _ in range(n)]
    res = 0

    def process_number(i, j):
        while j>=0 and array[i][j].isdigit():
            j -= 1
        cum = 0
        j += 1
        while j<m and array[i][j].isdigit():
            checked[i][j] = 1
            cum *= 10
            cum += int(array[i][j])
            j+=1

        return cum

    for i in range(n):
        for j in range(m):
            if array[i][j] == '*':
                cum = 1
                count = 0
                for _i, _j in itertools.product(range(max(i-1, 0), min(i+2, n)), range(max(j-1, 0), min(j+2, m))):
                    if array[_i][_j].isdigit() and checked[_i][_j] == 0:
                        count += 1
                        cum *= process_number(_i, _j)
                if count == 2:
                    res += cum


    print(res)



if __name__ == "__main__":
    ej1()
    ej2()