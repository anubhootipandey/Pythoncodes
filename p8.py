#python program to generate password
import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@#$&*!&?/_"

total = lower + upper + numbers + symbols
length = 18
password = "".join(random.sample(total,length))
print(password)