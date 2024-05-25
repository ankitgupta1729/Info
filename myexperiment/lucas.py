from sympy import *
from sympy.abc import n
init_printing(use_unicode=True)
def lucas(Fib):
    global s
    s = rsolve(Fib, f(n), {f(0): 0, f(1): 1})
    print(s)
if __name__== "__main__":
    f = Function('f')
    Fib = f(n+2) - f(n+1) - f(n)
    lucas(Fib)