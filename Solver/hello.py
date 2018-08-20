from cmath import cos, acos
from math import sqrt, pi
# from tkinter import *
'''
s = 'grlimkkoiepjdbjyeg'
index = 0
new = ''
maximum = ''
while index < len(s):
    new += s[index]
    while index < (len(s) - 1) and s[index] <= s[index+1]:
        new += s[index+1]
        index += 1
    index += 1
    if len(new) > len(maximum):
        maximum = new
    new = ''
print(maximum)
g ='f' + str(1)
K = [1, 4]
K += [2, 4, 5, 9]
print(K[::-1])
print(cos(4*pi/3))
iteration = 0
count = 0
sqrt(2)
str1 = 'exterminate!'
str2 = 'number one - the larch'

print(str2.index('n'))
print(str1)


def pressed():
        print('buttons are cool')

root = Tk()
button = Button(root, text='Press', command=pressed)
button.pack(pady=20, padx = 20)
pressed()
root.mainloop()



class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()

balance = 3015
annualInterestRate = 0.04
monthlyPaymentRate = 250
trial = 0
balance12=1
balance = (1+annualInterestRate/12)*(balance-monthlyPaymentRate)
balance = (1+annualInterestRate/12)*(balance-monthlyPaymentRate)
balance = (1+annualInterestRate/12)*(balance-monthlyPaymentRate)
balance = (1+annualInterestRate/12)*(balance-monthlyPaymentRate)
balance = (1+annualInterestRate/12)*(balance-monthlyPaymentRate)
balance = (1+annualInterestRate/12)*(balance-monthlyPaymentRate)
balance = (1+annualInterestRate/12)*(balance-monthlyPaymentRate)
balance = (1+annualInterestRate/12)*(balance-monthlyPaymentRate)
balance = (1+annualInterestRate/12)*(balance-monthlyPaymentRate)
balance = (1+annualInterestRate/12)*(balance-monthlyPaymentRate)
balance = (1+annualInterestRate/12)*(balance-monthlyPaymentRate)
balance = (1+annualInterestRate/12)*(balance-monthlyPaymentRate)
balance = int(balance*100+0.5)/100
print('Remaining balance: ' + str(balance))'''
'''
listA = [1, 4, 3, 0]
listB = ['x', 'z', 't', 'q']
listA = list(map(abs, listA))

print(listA)
listB.sort()'''

import tkinter as tk

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
root.title("Counting Seconds")
label = tk.Label(root, fg="dark green")
label.pack()
counter_label(label)
button = tk.Button(root, text='Stop', width=25, command=root.destroy)
button.pack()
root.mainloop()
