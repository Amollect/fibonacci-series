#Write a program to print Fibonacci series up to n terms.

num= int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0
if num <= 0:
   print("Please enter a positive integer")
else:
   print("Fibonacci sequence:")
   while count < num:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth