# sample input
# ABCDCDC
# CDC

# Sample output
# 2

def count_substring(string, sub_string):
    cont = 0
    for i in range(0,len(string)):
        if string[i:i + len(sub_string)] == sub_string:
            cont = cont +1
    return cont

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)