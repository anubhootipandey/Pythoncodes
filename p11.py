#program to solve qudratic equation
import cmath
a = 1
b = 5
c = 6
d = (b**2) - (4*a*c)
s1 = (-b-cmath.sqrt(d))/(2*a)
s2 = (-b+cmath.sqrt(d))/(2*a)
print("The solution are {0} and {1}".format(s1, s2))