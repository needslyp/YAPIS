def function(param):
    x = 10
    param.append(0)
    param.append(1)
    return param

def main():
    x = []
    a = []
    y = 4+2
    print([2]+[2])
    a.append(4)
    for i in range(len(a)):
        print(a[i])
    while (i < 10):
        print(i)
        i = i+1
    a.append(y)
    x = function(a)
    print(x)


main()
