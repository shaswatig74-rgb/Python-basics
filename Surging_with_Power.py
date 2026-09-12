# 01- n-and-n-1
# Topic: The n & (n-1) Trick, Power of 2- Bitwise Check

# input("n & (n-1) clears the rightmost set bit. Press Enter")
# print(" 12 & 11 = ", 12 & 11, "binary: ", bin(12 & 11)[2:])
# print(" 8 & 7 = ", 8 & 7)

# n = int(input("Enter a number (try 4 or 6): "))
# guess = input("Is" + "" + str(n) + " a power of 2? (yes/no): ")
# input("Power of 2: n & (n-1) == 0 means only one bit is ON. Press Enter")
# if n > 0 and (n & (n-1)) == 0:
#     print(" ",n,"binary: ",bin(n)[2:], "is a power of 2 your guess: ",guess)
# else:
#     print(" ",n,"binary: ",bin(n)[2:], "is not a power of 2 your guess: ",guess)

# 02-power-of-4-8.py
# Topic: Power of 4 - Even Bit Position, Power of 8 - Bit Position Divisible by 3

input("Power of 4: n % 3 == 1   Power of 8: n % 7 == 1.  Press Enter ")
print("  16  binary:", bin(16)[2:], "  16 % 3 =", 16 % 3, "  power of 4: yes")
print("  8   binary:", bin(8)[2:],  "  8 % 7 =",  8 % 7,  "  power of 8: yes")

n = int(input("Enter a number (try 64 or 32): "))
guess = input("Is " + str(n) + " a power of 4? (yes/no): ")
input("Check: n % 3 == 1.  Press Enter ")
is_pow4 = n > 0 and (n & (n - 1)) == 0 and n % 3 == 1
if is_pow4:
    print(" ", n, "  binary:", bin(n)[2:], "  power of 4: yes  your guess:", guess)
else:
    print(" ", n, "  binary:", bin(n)[2:], "  power of 4: no   your guess:", guess)
    