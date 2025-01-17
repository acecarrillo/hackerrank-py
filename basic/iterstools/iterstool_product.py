#usando iterstool se debe de hacer todas las posibles combinaciones de un plano carteciano con las variables A y B  

#Sample code: 
# >>> from itertools import product
# >>>
# >>> print list(product([1,2,3],repeat = 2))
# [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
# >>>
# >>> print list(product([1,2,3],[3,4]))
# [(1, 3), (1, 4), (2, 3), (2, 4), (3, 3), (3, 4)]
# >>>
# >>> A = [[1,2,3],[3,4,5]]
# >>> print list(product(*A))
# [(1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 3), (3, 4), (3, 5)]
# >>>
# >>> B = [[1,2,3],[3,4,5],[7,8]]
# >>> print list(product(*B))
# [(1, 3, 7), (1, 3, 8), (1, 4, 7), (1, 4, 8), (1, 5, 7), (1, 5, 8), (2, 3, 7), (2, 3, 8), (2, 4, 7), (2, 4, 8), (2, 5, 7), (2, 5, 8), (3, 3, 7), (3, 3, 8), (3, 4, 7), (3, 4, 8), (3, 5, 7), (3, 5, 8)
 
from itertools import product
A, B= input(), input()
A = A.split()
B = B.split()
cartezian = list(product(A,B))
resultado = ' '.join(f'({a}, {b})' for a, b in cartezian)
print(resultado)
