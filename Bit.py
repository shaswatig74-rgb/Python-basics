# 01- bits-binary.py
# Topic: Bits and Binary Numbers, AND or OR

n = int(input("Enter a number(try 5 or 12): "))
guess = input("Guess its binary: ")

input("Binary. Press Enter")
print(" decimal", n, "-> binary", bin(n)[2:])
print(" your guess: ", guess)

input("AND - both bits must be 1. Press Enter")
print(" 12 =", bin(12)[2:])
print(" 10 =", bin(10)[2:])
print(" 12 & 10 =", 12 & 10)

input("OR - at least one bit must be 1. Press Enter")
print(" 12 | 10 =", 12 | 10)

# 02-not-xor-shifts.py
# Topic: NOT, XOR, Left, Right Shift

n = int(input("Enter a number (try 5 or 12): "))
guess = input("Left shift doubles it. Guess: " + str(n) + " << 1 = ? ")

input("NOT - flips every bit. Press Enter ")
print(" 12 = ", bin(12)[2:])
print(" NOT 12 = ", ~12 & 0xFF)

input("XOR - different bits give 1. Press Enter")
print("12 ^ 10", 12 ^ 10 )

input("Left shft - multiplies by 2. Press Enter")
print(" ", n, "<< 1 = ", n << 1, " your guess: ", guess)

input("Right shift  -divides by 2. Press Enter")
print(" ",n, ">> 1 = ", n >> 1)
