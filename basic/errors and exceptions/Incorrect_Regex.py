import re

numero = int(input())

for i in range(numero):
    try:
        re.compile(input())
        print("True")
    except re.error as  e:
            print("False")
