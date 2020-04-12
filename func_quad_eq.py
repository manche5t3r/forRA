# решение квадратного уравнения через дискриминант

def my_func(a, b, c):
    print('equation:', a,'*x2+', b, '*x+', c)
    d = b**2 - 4*a*c

    if d>0:
        return 'x1=', (-b+d**1/2)/(2*a), 'x2=', (-b-d**1/2)/(2*a)
    elif d==0:
        return 'x=', -b/2*a
    else:
        return 'kornei net'


print(my_func(3, 15, 5))
print(my_func(1, 2, 1))
print(my_func(1, 1, 1))

