def tokenize(text):
    l = ""
    for i in text:
        if i.isalnum() == True and i not in ["0","1","2","3","4","5","6","7","8","9"]:
            #print(i)
            l += i.lower()
        else:
            #print("not: ", i )
            l += " "
    #print(l)
    return l.split(" ")

def computeWordFrequencies(l):
    s = set(l)
    #print(l)
    #print(set(l))
    #print({x : len([y for y in l if y == x])for x in s})
    return {x : len([y for y in l if y == x])for x in s if x !='' and len(x) > 3}

def Frequencies(dic):
    #print(dic)
    print({k: v for k, v in sorted(dic.items(), key=lambda item: item[1], reverse=True)})
    return dic


def all(s):
    x = tokenize(s)
    dic = computeWordFrequencies(x)
    d = Frequencies(dic)
    return d

    


if __name__ == "__main__":
    x = tokenize("meow@Meow 1meow wow /down 000 i")
    dic = computeWordFrequencies(x)
    Frequencies(dic)

