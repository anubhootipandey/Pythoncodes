#program to check whether the entered string is pallindrome or not.
s = input("Enter a string")
print("The old string is",s)
revstring = s[::-1]
if s == revstring:
    print("Entered string is pallindrome")
else:
    print("Entered string is not pallindrome")    
