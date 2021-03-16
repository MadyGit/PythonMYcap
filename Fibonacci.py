# Program to display the Fibonacci sequence up to n-th term

n = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
i = 0

if n <= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while i < n:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       i += 1
       
#Output:How many terms?  13
#Fibonacci sequence:
#0
#1
#1
#2
#3
#5
#8
#13
#21
#34
#55
#89
#144
