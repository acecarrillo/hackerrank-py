def split_and_join(line):
    splits = line.split(" ")
    joins = "-".join(splits)
    return joins

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)