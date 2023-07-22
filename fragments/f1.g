list def(list &param)
{
    param.append(0);
    return param;
};

element main(){
    sometext
    list a = [];
    element b = 10;

    a.append(b);

    x1 = (element) a;
    moreerror
    list a1 = make_list(1, 2);
    element x = 1;
    element y = 10;
    a1.append(x);
    a1.append(y);

    list a2 = a + a1;
    list a3 = a - a1;
    list a4 = a * a1;
    list a5 = a / a1;

    if (a == a1)
    {
        print(a);
    }
    else
    {
        element x = input();
        a1.append(x);
    };

    a = def(a, x1);

    a = make_list(tree, 1);
    a.append(left, 1, 2);
    print(a);

    a.balance();


    list b = function(queue, 1);
    element x = 'x';
    b.append(x)
    b.pop();

    list a = [1, 2, 3, 4, 5, 6];

    for (element k = 0, i < range(len(a)), i++)
    {
        print(a[i]);
    };

    return 0;
};
