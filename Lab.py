def myfunc(double):
    list = [x.split(", ") for x in double]
    return list
print(myfunc('hello world'))