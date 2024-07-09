



def average(array):
    arreglo = set(array)
    sum_arreglo = sum(arreglo)
    avg = sum_arreglo / len(arreglo)
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)