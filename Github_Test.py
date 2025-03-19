2.
def myfunc(double):
    list = double.split()
    word1 = list[0]
    word2 = list[1]
    if word1[0] == word2[0]:
        return True
    else:
        return False

print(myfunc('or oaimoni'))

