list function(list &param)
{
    element x = 10;
    param.append(0);
    param.append(1);
    return param;
};

element main(){
    list x = [];
    list a = [];
    y = 4 + 2;
    print([2] + [2]);
    a.append(4);
    for (element i = 0, i < range(len(a)), i++)
    {
        print(a[i]);
    };

    while (element i < 10)
    {
        print(i);
        i = i+1;
    };

    a.append(y);
    x = function(a);
    print(x);
};
