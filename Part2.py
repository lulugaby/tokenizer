from Part1 import *

def read(filename):
    f = open(filename, "r")
    return f.read()

def match(p1, p2):
    print(set(p1.keys()).intersection(set(p2)))
    return set(p1.keys()).intersection(set(p2))

def length(m):
    return len(m)


if __name__ == "__main__":
    f1 = input("file 1: ")
    f2 = input("file 2: ")
    s1 = read("f1.txt")
    s2 = read("f2.txt")

    p1 = all(s1)
    #print(sorted(p1.keys(), reverse=True))

    #are strings of numbers allowed?
    p2 = all(s2)

    m = match(p1,p2)

    print(length(m))
    