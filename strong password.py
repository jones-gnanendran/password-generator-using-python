import random
import array
print("Enter the length of the password required");
n=int(input())
print("Enter the type of data you want");
print("//******Enter ch for char ,nu for number and ss for special symbols******//");
s=input();
digits="0123456789"
lowers="abcdefghijklmnopqrstuvwxyz"
uppers="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_symbols="!@#$%^&*()-<>.,"
combine=""
if "ch" in s:
    combine+=lowers+uppers
if "nu" in s:
    combine+=digits
if "ss" in s:
    combine+=special_symbols
password=""
for i in range(n):
    password+=random.choice(combine)
print(password)
