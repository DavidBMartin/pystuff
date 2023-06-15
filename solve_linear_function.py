#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 20:36:53 2023

@author: david
"""
from sympy.plotting import plot
from sympy import symbols, solve
from sys import argv


def get_input():
    imp = input("f(x) = y  enter the values of x and y (x y): ")
    a, z = imp.split(' ')
    print(a, z)
    imp = input("f(x) = y  enter the second values     (x y): ")
    c, k = imp.split(' ')
    return ({float(a): float(z), float(c): float(k)})


def do_the_math(f):
    m, b, x = symbols('m b x')
    equation = []
    vals = []

    for i in f:
        vals.append(f[i])
        equation.append((x*m + b).subs(x, i))

    R = equation[1] - equation[0]
    L = vals[1] - vals[0]
    plot(R, L)
    print(f"({equation[1]}) - ({equation[0]})  = {R} =", end=' ')
    print(f"({vals[1]}) - ({vals[0]}) = {L}")
    print(f"{L} = {R}")
    print(f"1 = {R/L}")
    if L > 1 and '/' in str(R/L):
        r, l = str(R / L).split('/')
        print(f"{l} = {r}")
    return (R/L)


def get_source():
    if len(argv) > 4:
        f = {int(argv[1]): int(argv[2]), int(argv[3]): int(argv[4])}
    else:
        f = get_input()
    return (f)


if __name__ == "__main__":
    answer = do_the_math(get_source())
    print(answer)
