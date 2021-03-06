from math import pow, pi, sqrt as msqrt
from cmath import sqrt, cos, acos
from random import randint
from time import sleep
import tkinter as tk

# Definitions:


def cubic_root(x):
    return pow(x, 1/3) if x >= 0 else -pow(-x, 1/3)

# Main class:


# This is the main solver class. It creates an object and also the relevant operations for computing the solutions.
class Solver:

    def __init__(self):
        self.degree = 0
        self.solution = 0
        self.epsilon = 1e-7
        self.a, self.b, self.c, self.d, self.e, self.f = 0, 0, 0, 0, 0, 0
        self.initA, self.initB, self.initC, self.initD, self.initE, self.initF = 0, 0, 0, 0, 0, 0
        self.sol5 = 0
        self.C, self.D, self.E = 0, 0, 0
        self.W, self.X, self.Y, self.Z = [1e-7], 0, 0, 0

    @staticmethod
    def format_solution(x):
        return str(format(x, '.4f')).replace('j', 'i').replace('+0.0000i', '').replace('-0.0000i', '').\
            replace('-0.0000', '0').replace('0.0000', '0').replace('.0000', '')

    @staticmethod
    def welcome_message():
        print('Welcome to EquationSolver Pro!\n')

    def ask_input(self):
        self.degree = int(input('Enter the degree of the polynomial equation (1-5):\n'))
        while self.degree > 5 or self.degree < 1:
            self.degree = int(input('The degree should be either 1, 2, 3, 4, or 5. Enter a new degree:\n'))
        self.initA = self.a = int(input('Enter a: '))
        while self.a == 0:
            self.initA = self.a = int(input('a cannot be 0. Enter a new value: '))
        self.initB = self.b = int(input('Enter b: '))
        if self.degree >= 2:
            self.initC = self.c = int(input('Enter c: '))
        if self.degree >= 3:
            self.initD = self.d = int(input('Enter d: '))
        if self.degree >= 4:
            self.initE = self.e = int(input('Enter e: '))
        if self.degree == 5:
            self.initF = self.f = int(input('Enter f: '))

    def fun(self, x):
        return 0 if self.degree < 5 else self.a * x ** 5 + self.b * x ** 4 + self.c * x ** 3 + self.d * x ** 2 +\
                                         self.e * x + self.f

    # We use Newton's algorithm if the degree of the equation is greater than 4
    def newton_algorithm(self, x):
        previous_x = x
        x += -2 * self.epsilon * self.fun(x) / (self.fun(x + self.epsilon) - self.fun(x - self.epsilon))
        return x if abs(x - previous_x) < self.epsilon else self.newton_algorithm(x)

    # The initial coefficient values are adjusted if the degree of the equation is greater than 4
    def find_extra_solution(self):
        while True:
            try:
                self.sol5 = self.newton_algorithm(randint(-1e3, 1e3))
                break
            except RecursionError:
                pass
        self.b += self.a * self.sol5
        self.c += self.b * self.sol5
        self.d += self.c * self.sol5
        self.e += self.d * self.sol5

    # The first four solutions of the equation are calculated through pure algebraic manipulation
    def calculate_solutions(self):
        self.C = 3 * self.b ** 2 - 8 * self.a * self.c
        self.D = 2 * self.b ** 3 - 8 * self.a * self.b * self.c + 16 * self.a * self.a * self.d
        self.E = -3 * self.b ** 4 + 16 * self.a * self.b ** 2 * self.c - 64 * self.a ** 2 * self.b * self.d +\
                 256 * self.a ** 3 * self.e
        self.X = self.C ** 2 + 3 * self.E
        self.Y = -self.C ** 3 + 9 * self.C * self.E + 27 * self.D ** 2
        if self.X > 0:
            self.W += [sqrt((self.C + sqrt(self.X) * cos(acos(self.Y / sqrt(self.X ** 3)) / 3)) / 3),
                       sqrt((self.C + sqrt(self.X) * cos(acos(self.Y / sqrt(self.X ** 3)) / 3 - 2 * pi / 3)) / 3),
                       sqrt((self.C + sqrt(self.X) * cos(acos(self.Y / sqrt(self.X ** 3)) / 3 - 4 * pi / 3)) / 3)]
        if self.Y * self.Y >= self.X * self.X * self.X:
            self.W += [
                sqrt((2 * self.C + cubic_root(self.Y + msqrt(self.Y ** 2 - self.X ** 3)) +
                      cubic_root(self.Y - msqrt(self.Y ** 2 - self.X ** 3))) / 6)]
        self.W = sorted(self.W, key=abs)
        self.Z = self.W[-1]

    def print_solutions(self):
        print('\nSolutions:\n')
        self.solution = sorted(
            [(-self.b - self.Z - sqrt(-self.Z ** 2 + self.C + self.D / self.Z)) / self.a / 4,
             (-self.b - self.Z + sqrt(-self.Z ** 2 + self.C + self.D / self.Z)) / self.a / 4,
             (-self.b + self.Z - sqrt(-self.Z ** 2 + self.C - self.D / self.Z)) / self.a / 4,
             (-self.b + self.Z + sqrt(-self.Z ** 2 + self.C - self.D / self.Z)) / self.a / 4,
             self.sol5 + 0j], key=abs)[::-1]
        for k in range(self.degree):
            print(self.format_solution(self.solution[k]))


# EquationSolver:

solver = Solver()
Solver.welcome_message()
sleep(1)
solver.ask_input()
if solver.degree > 4:
    solver.find_extra_solution()
solver.calculate_solutions()
solver.print_solutions()

# User interface

# We create a root Tkinter object to create the GUI
root = tk.Tk()
root.title("EquationSolver")

degrees_label = tk.Label(root, fg="blue")
degrees_label.pack()

degrees_string = "Degree: " + str(solver.degree) + "\nEquation coefficients:\n"
for i in range(0, solver.degree+1):
    degrees_string += chr(ord('a')+i) + " = "
    number = ""
    if i == 0:
        number += str(solver.initA)
    if i == 1:
        number += str(solver.initB)
    if i == 2:
        number += str(solver.initC)
    if i == 3:
        number += str(solver.initD)
    if i == 4:
        number += str(solver.initE)
    if i == 5:
        number += str(solver.initF)
    degrees_string += number
    if i != solver.degree:
        degrees_string += ", "

degrees_label.config(text=degrees_string)

solutions_label = tk.Label(root, fg="red")
solutions_label.pack()
solutions = "Solutions:\n"
for i in range(0, solver.degree):
    solutions += solver.format_solution(solver.solution[i])
    solutions += "\n"

solutions_label.config(text=solutions)

button = tk.Button(root, text="Exit", width=25, command=root.destroy)
button.pack()
root.mainloop()
