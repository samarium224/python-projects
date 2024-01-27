
print('''
██████╗ ██╗███████╗███████╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗    ███╗   ███╗███████╗████████╗██╗  ██╗ ██████╗ ██████╗
██╔══██╗██║██╔════╝██╔════╝██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║    ████╗ ████║██╔════╝╚══██╔══╝██║  ██║██╔═══██╗██╔══██╗
██████╔╝██║███████╗█████╗  ██║        ██║   ██║██║   ██║██╔██╗ ██║    ██╔████╔██║█████╗     ██║   ███████║██║   ██║██║  ██║
██╔══██╗██║╚════██║██╔══╝  ██║        ██║   ██║██║   ██║██║╚██╗██║    ██║╚██╔╝██║██╔══╝     ██║   ██╔══██║██║   ██║██║  ██║
██████╔╝██║███████║███████╗╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║    ██║ ╚═╝ ██║███████╗   ██║   ██║  ██║╚██████╔╝██████╔╝
╚═════╝ ╚═╝╚══════╝╚══════╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝    ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝
''')

import sympy as sym
import math

def f(x):
    y = (4*math.exp(-x)*math.sin(x)) - 1
    return y


def bisection(f , xl, xu, tol=1e-4):
    # x = sym.symbols('x')
    # y = f(x)
    # equation_str = sym.latex(y)
    # print("Given equation:", equation_str)
    num = 1
    if f(xl) * f(xu) > 0:
        print('root does not exist in this range. Try different value for xl and xu')
        return 0
    else:
        print(f'consider xl: {xl} value of f(xl) is {f(xl)}')
        print(f'consider xu: {xu} value of f(xu) is {f(xu)}')

    while True:
        xr = (xl + xu)/2
        function_val = f(xr)
        print(f'for x{num}: {xr} and f(x{num}) --> {function_val}')

        if(abs(function_val) < tol):
            print(f'....reached termination point {tol}...')
            print(f'root is: {xr}')
            break

        if(function_val < 0):
            xl = xr
        else:
            xu = xr

        num = num + 1
        print(f'So, xl -> {xl} and xu -> {xu}')



bisection(f,0,0.5,0.0009)
