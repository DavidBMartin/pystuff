#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
import inspect
from IPython.display import display, Image
from sympy import symbols, init_printing, diff, sin, exp

def NotAFunction():
    """
    remove checkmark from 'Mute inline plotting'
    from IPython.display import display
    from sympy import symbols, init_printing, diff, sin, exp
    """
    x, y = symbols('x y')
    init_printing()
    print("\nLet's see if this works...")
    display(diff(sin(x)*exp(x), x))
    print("\n^^ That is an image, you can't copy and paste it as text")


if __name__ == "__main__":
    print(inspect.getsource(NotAFunction))
    NotAFunction()

