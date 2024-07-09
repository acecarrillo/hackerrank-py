
### Explicacion: 
# Se da un codigo de N integer, la tarea es obtener un patron rangoli de tamaño N 
# 
# 


import string

def print_rangoli(size):
    alphabet = list(string.ascii_lowercase)
    alphabet = alphabet[:size]
    index = list(range(size))
    index = index[:-1] + index[::-1]
    for i in index:
        start = i + 1
        right = alphabet[-start:]
        left = right[::-1]
        row = left + right[1:]
        row = "-".join(row)
        width = size * 4 - 3
        row = row.center(width,"-")
        print(row)


def main():
    print("de que tamaño desea el Rangoli?")
    n = 10
    print_rangoli(n)

main()