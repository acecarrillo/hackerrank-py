# se desea que la primera letra de cada palabra sea una mayuscula, se dara un nombre y se debe de estar seguro que tenga las mayusculas apropiadas  



# def solve(s):
#     new_s = s.split()
#     for i in range(len(new_s)):
#         new_s[i] = new_s[i].capitalize()
#     full_name = " ".join(new_s)
#     return full_name

def solve(s):
    for name in s.split():
        s = s.replace(name, name.capitalize())
    return s

def main():
    s = input()
    result = solve(s)
    print(result)
    
main()