# 01- power-set
# Topic: Power Set, Binary Mask as a Subset Selector

# input(" A set with n elements has 2^n subsets. Press Enter")
# print(" 3 elements 2^3 =", 2**3, "subsets")
# print(" mask 5 = binary", bin(5)[2:], " selects position 0 and 2")

# n = int(input("Enter a number (try 4 or 5): "))
# guess = input("How may subsets does a set of " + str(n) + " elements have? ")
# input("Each element is in or out - 2 choices per element. Press Enter")
# print(" ",n," elements subsets:", 2**n, " your guess: ", guess)

# 02-bit-probe
# Topic: Bit Probe - Checking the j-th bit, Enumerating All Subsets with Two Loops

# input("Bit probe - (n >> j) & 1 checks if the bit j is ON. Press Enter")
# print(" 12 = binary", bin(12)[2:], " bit 2:", (12 >> 2) & 1, " bit 1:", (12 >> 1) & 1)
# print(" 7 = binary", bin(7)[2:], " bit 2:", (7 >> 2) & 1, " bit 1:", (7 >> 1) & 1)

# n = int(input("Enter a number (try 9 or 6): "))
# print(" binary:", bin(n)[2:])
# guess = input("What is bit 2 of " + str(n) + " ? (0 or 1): ")
# input("Bit probe: (n >> 2) & 1 gives the bit value. Press Enter")
# print(" ",n, "bit 2:", (n >> 2) & 1, " your guess: ", guess)

# 03-bit-difference
# Topic: Bit Difference

input("Bit difference - XOR shows which bits differ. Press Enter")
print(" 5 ^ 3 =", 5 ^ 3, " binary", bin(5 ^ 3)[2:], " bits different: ", bin(5 ^ 3).count("1"))
print(" 9 ^ 5 =", 9 ^ 5, "  binary", bin(9 ^ 5)[2:], " bits different:", bin(9 ^ 5).count("1"))

n = int(input("Enter a number( try 4 or 6): "))
guess = input("How many bits differ between " + str(n) + " and 7? ")
input("XOR marks the differing bits - count the 1s. Press Enter")
diff = bin(7 ^ n).count("1")
print(" ",n, "^ 7 = binary", bin(n ^ 7)[2:], " different bits: ",diff, " your guess: ",guess)