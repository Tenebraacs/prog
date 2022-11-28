print("Ez egy konzolra kiírt mondat")

"""
Ez egy
több
soros
komment
"""

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x = 5
y = "John"
print(type(x))
print(type(y))

"""
Változó szabályok:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
"""

x, y, z = 1, 2, 3

print(x)
print(y)
print(z)

x = y = z = "Alma"
print(x)
print(y)
print(z)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
print(x + y + z)

x = 5
y = "John"
print(x, y)

#Ha egy függvényen belül adunk meg egy változót akkor az lokális lesz.
#A "global" parancsot használva tudjuk elérhetővé tenni a kód többi részére.

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)