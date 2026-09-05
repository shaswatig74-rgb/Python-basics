# # Program to find if a number is prime

# from math import sqrt

# number = int(input("Enter a number "))

# for k in range(2, int(sqrt(number)) + 1):

#     # if divisible  by any number it is not a prime number
#     if(number % k) == 0:
#         print(number, "is not a prime number")
#         break
#     else:
#         print(number, "is a prime number")
#         break

# Program to find prime numbers from 2 to the given number

# def SieveOfEratosthenes(num):
#     prime = [True for i in range(num+1)]
#     p = 2
#     while(p * p <= num):
#         if(prime[p] == True):
#             for i in range(p * p, num + 1, p):
#                 prime[i] = False
#         p += 1

#     for p in range(2, num + 1):
#         if prime[p]:
#             print(p)

# num = int(input("Enter a number: "))
# print("Following are the prime numbers smaller")    
# print("than or equal to", num)
# SieveOfEratosthenes(num)

# # Implementation of Sieve of Eratosthenes for a given range
# a = 3000
# for num in range(1, a + 1):
#     c = 0
#     rev = 0
#     temp = num
#     for i in range(1, temp + 1):
#         if temp % i == 0:
#             c+=1
#     if c == 2:
#         while temp > 0:
#             rev = rev*10+(temp%10)
#             temp //= 10

#         if rev == num:
#             print(num)