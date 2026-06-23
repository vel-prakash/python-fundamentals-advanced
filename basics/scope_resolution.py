# Scope Resolution (LEGB)
# Scope determines where a variable can be accessed within a program.
#
# Python searches for variables using the LEGB rule:
# L - Local
# E - Enclosing
# G - Global
# B - Built-in

# -------- Local Scope --------

def func1():
    a = 1
    print(a)

def func2():
    b = 2
    print(b)

func1()
func2()

# Variables defined inside one function
# cannot be accessed from another function.

# def func1():
#     a = 1
#     print(b)  # Error: b is not defined in this scope
#
# def func2():
#     b = 2
#     print(a)  # Error: a is not defined in this scope

# -------- Enclosing Scope --------

def func1():
    x = 1

    def func2():
        x = 3
        print(x)  # Local variable inside func2()

    func2()

func1()

# -------- Global Scope --------

x = 4

def func1():
    print(x)

def func2():
    print(x)

func1()
func2()

# -------- Built-in Scope --------

from math import e

def func1():
    print(e)

func1()

# Local variables take precedence over built-in names

def func2():
    print(e)

e = 5

func2()