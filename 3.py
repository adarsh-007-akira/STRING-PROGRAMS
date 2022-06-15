def remove(string, index):
    n=index
    word=string
    half_1=word[:n]
    half_2=word[n+1:]
    newword=half_1+half_2
    return newword
print(remove("Aakira", 1))