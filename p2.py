#program to add natural number upto nth term.
from re import I


n = int(input("Enter nth term"))
i = 1
sum = 0
while i<n:
    sum = sum + i 
    i = i+1
print("The sum is", sum)    