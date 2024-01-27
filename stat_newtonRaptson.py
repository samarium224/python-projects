from sympy import *
import math

print('''
███╗   ██╗███████╗██╗    ██╗████████╗ ██████╗ ███╗   ██╗      ██████╗  █████╗ ██████╗ ██╗  ██╗███████╗ ██████╗ ███╗   ██╗
████╗  ██║██╔════╝██║    ██║╚══██╔══╝██╔═══██╗████╗  ██║      ██╔══██╗██╔══██╗██╔══██╗██║  ██║██╔════╝██╔═══██╗████╗  ██║
██╔██╗ ██║█████╗  ██║ █╗ ██║   ██║   ██║   ██║██╔██╗ ██║█████╗██████╔╝███████║██████╔╝███████║███████╗██║   ██║██╔██╗ ██║
██║╚██╗██║██╔══╝  ██║███╗██║   ██║   ██║   ██║██║╚██╗██║╚════╝██╔══██╗██╔══██║██╔═══╝ ██╔══██║╚════██║██║   ██║██║╚██╗██║
██║ ╚████║███████╗╚███╔███╔╝   ██║   ╚██████╔╝██║ ╚████║      ██║  ██║██║  ██║██║     ██║  ██║███████║╚██████╔╝██║ ╚████║
╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝    ╚═╝    ╚═════╝ ╚═╝  ╚═══╝      ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝

''')
x = symbols('x')

Xi = 3.1416
f = x*sin(x) + cos(x)
df = diff(f,x)
steps = 0
tol = 0.0000000000001

print(f'Given Equation {f} | starting value {Xi} | tolerance value {tol}')

while True:
    steps = steps + 1
    Xi_r = (Xi - (f/df))
    cal_Xi_r = Xi_r.subs(x,Xi)
    functional_val = f.subs(x,cal_Xi_r)
    print(f'|iteration {steps}|')
    print(f'xi = {Xi} \nXi+1 = {cal_Xi_r} \nf(Xi+1) = {functional_val}\n')
    if(abs(functional_val) < tol):
        print('maximum tolerance has reached')
        print(f'root is {cal_Xi_r}')
        break
    Xi = cal_Xi_r

