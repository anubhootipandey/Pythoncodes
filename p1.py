# program to reverse a given number
def rev_num(num):
    rev = 0
    while num > 0:
        remainder = num % 10
        rev = (rev * 10) + remainder
        num = num // 10
    return rev

print(f"reverse of the given number is {rev_num(456784)}")        