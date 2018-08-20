import math
import cmath
import random
#from SummerProjects import EquationSolver



def print_solution(s):
    return print(str(format(s, '.4f')).replace('j', 'i').replace('+0.0000i', '').replace('-0.0000i', '').replace('-0.0000', '0')
                 .replace('0.0000', '0').replace('.0000', '').replace('1i', 'i'))


'''def fun(x):
    return a*x**5 + b*x**4 + c*x**3 + d*x**2 + e*x + f
    #return a*x**deg + b*x**(deg-1) + c*x**(deg-2) + d*x**(deg-3) + e*x**(deg-4) + f*x**(deg-5) + g*x**(deg-6)

print('\nSolutions:\n')
s1 = (-b - K - cmath.sqrt(-K*K - C + D/K))/4/a
print_solution(s1)
s2 = (-b - K + cmath.sqrt(-K*K - C + D/K))/4/a
print_solution(s2)
s3 = (-b + K - cmath.sqrt(-K*K - C - D/K))/4/a
print_solution(s3)
s4 = (-b + K + cmath.sqrt(-K*K - C - D/K))/4/a
print_solution(s4)
if degree == 5:
    print_solution(s5)
    recursionError = True
    while recursionError:
        try:
            s5 = algorithm(random.randint(-1e3, 1e3))
            recursionError = False
        except RecursionError:
            pass
def fun(x):
    function = [0, 0, 0, 0, 0, a*x**5 + b*x**4 + c*x**3 + d*x**2 + e*x + f]

    return function[degree]

     K = cmath.sqrt((-2*C + cubic_root(Y + math.sqrt(Y*Y + Z*Z*Z)) + cubic_root(Y - math.sqrt(Y*Y + Z*Z*Z)))/6)
    if abs(K) < h and Z != 0:
        X = sorted([cmath.sqrt((-C + cmath.sqrt(-Z)*cmath.cos(cmath.acos(Y/cmath.sqrt(-Z*Z*Z))/3 - 2*math.pi/3))/3),
                    cmath.sqrt((-C + cmath.sqrt(-Z)*cmath.cos(cmath.acos(Y/cmath.sqrt(-Z*Z*Z))/3 - 4*math.pi/3))/3),
                    cmath.sqrt((-C + cmath.sqrt(-Z)*cmath.cos(cmath.acos(Y/cmath.sqrt(-Z*Z*Z))/3))/3)], key=abs)
        K = X[2]
except ValueError:
    X = sorted([cmath.sqrt((-C + cmath.sqrt(-Z)*cmath.cos(cmath.acos(Y/cmath.sqrt(-Z*Z*Z))/3 - 2*math.pi/3))/3),
                cmath.sqrt((-C + cmath.sqrt(-Z)*cmath.cos(cmath.acos(Y/cmath.sqrt(-Z*Z*Z))/3 - 4*math.pi/3))/3),
                cmath.sqrt((-C + cmath.sqrt(-Z)*cmath.cos(cmath.acos(Y/cmath.sqrt(-Z*Z*Z))/3))/3)], key=abs)
    K = X[2]
if abs(K) < h and Z == 0:
    K += h
'''
def d_fun(x):
    h = 1e-6
    return (fun(x+h)-fun(x-h))/(2*h)


def algorithm(seed):
    previous = seed
    seed += -fun(seed)/d_fun(seed)
    return seed if math.fabs(previous-seed) < 1e-6 else algorithm(seed)


def cubic_root(n):
    return math.pow(n, 1/3) if n >= 0 else -math.pow(-n, 1/3)

try:
    K = cmath.sqrt((-2*C + cubic_root(Y + math.sqrt(Y*Y + Z*Z*Z)) + cubic_root(Y - math.sqrt(Y*Y + Z*Z*Z)))/6)
    if math.fabs(K.real) < 0.00001:
        K = cmath.sqrt((-C + cmath.sqrt(-Z)*cmath.cos(cmath.acos(Y/cmath.sqrt(-Z*Z*Z))/3))/3)
        print('if')
except ValueError:
    print('exceptr')
