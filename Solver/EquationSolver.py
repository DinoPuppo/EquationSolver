from math import pow, pi, sqrt as msqrt
from cmath import sqrt, cos, acos
from random import randint
from time import sleep
import tkinter as tk

# a = tkinter.Checkbutton

# Definitions:


def cubic_root(x):
    return pow(x, 1/3) if x >= 0 else -pow(-x, 1/3)


class Solver:

    def __init__(self):
        self.degree = 0
        self.solution = 0
        self.h = 1e-7
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
        self.e = 0
        self.f = 0
        self.s5 = 0
        self.C = 0
        self.D = 0
        self.E = 0
        self.W = [1e-7]
        self.X = 0
        self.Y = 0
        self.Z = 0

    @staticmethod
    def print_solution(x):
        print(str(format(x, '.4f')).replace('j', 'i').replace('+0.0000i', '').replace('-0.0000i', '').
              replace('-0.0000', '0').replace('0.0000', '0').replace('.0000', ''))

    @staticmethod
    def welcome_message():
        print('Welcome to EquationSolver Pro!\n')

    def ask_input(self):
        self.degree = int(input('Enter the degree of the polynomial equation (1-5):\n'))
        while self.degree > 5 or self.degree < 1:
            self.degree = int(input('The degree should be either 1, 2, 3, 4, or 5. Enter a new degree:\n'))
        self.a = int(input('Enter a: '))
        while self.a == 0:
            self.a = int(input('a cannot be 0. Enter a new value: '))
        self.b = int(input('Enter b: '))
        if self.degree >= 2:
            self.c = int(input('Enter c: '))
        if self.degree >= 3:
            self.d = int(input('Enter d: '))
        if self.degree >= 4:
            self.e = int(input('Enter e: '))
        if self.degree == 5:
            self.f = int(input('Enter f: '))

    def fun(self, x):
        return 0 if self.degree < 5 else self.a * x ** 5 + self.b * x ** 4 + self.c * x ** 3 + self.d * x ** 2 +\
                                         self.e * x + self.f

    def newton_algorithm(self, x):
        previous_x = x
        x += -2 * self.h * self.fun(x) / (self.fun(x + self.h) - self.fun(x - self.h))
        return x if abs(x - previous_x) < self.h else self.newton_algorithm(x)

    def find_extra_solution(self):
        while True:
            try:
                self.s5 = self.newton_algorithm(randint(-1e3, 1e3))
                break
            except RecursionError:
                pass
        self.b += self.a * self.s5
        self.c += self.b * self.s5
        self.d += self.c * self.s5
        self.e += self.d * self.s5

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
             self.s5 + 0j], key=abs)[::-1]
        for i in range(self.degree):
            self.print_solution(self.solution[i])


# EquationSolver:


solver = Solver()
Solver.welcome_message()
sleep(1)
solver.ask_input()
if solver.degree > 4:
    solver.find_extra_solution()
solver.calculate_solutions()
solver.print_solutions()

counter = 0


def counter_label(label):
    counter = 0

    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000, count)

    count()


root = tk.Tk()
root.title("Equation Solver")
label = tk.Label(root, fg="dark green")
label.pack()
counter_label(label)
button = tk.Button(root, text='Submit', width=25, command=root.destroy)
button.pack()
root.mainloop()
