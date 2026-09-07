# Computers store numbers using bits — tiny values that can only be 0 or 1.

# Python gives us special operators to work directly with these bits. These are called bitwise operators.

# # 1. Bits and Binary Numbers

# A bit is simply: 0 or 1

# A computer combines many bits to represent numbers.

5 = 101

# Decimal     Binary

# 0     =     000,
# 1     =     001,
# 2     =     010,
# 3     =     011,
# 4     =     100,
# 5     =     101,
# 6     =     110,
# 7     =     111,

# You can convert a number to binary using bin()

print(bin(5)) # 0b101

print(bin(12))

# The 0b simply tells Python:

"This number is written in binary."

# 2. AND and OR

# AND &
# AND follows this rule:

# A	B	A AND B
# 0	0	0
# 0	1	0
# 1	0	0
# 1	1	1

# In simple words:
# AND gives 1 only when both bits are 1.

print(5 & 3)

# 5 = 101
# 3 = 011

#   1 0 1    ← 5
# & 0 1 1    ← 3
# ---------
#   0 0 1


# OR |
# OR follows:

# A	B	A OR B
# 0	0	0
# 0	1	1
# 1	0	1
# 1	1	1

# In simple words:

# OR gives 1 if at least one bit is 1.

#   101   (5)
# | 011   (3)
# -----
#   111   (7)
print(5 | 3)

# 3. NOT and XOR

# ~   → NOT
# ^   → XOR

# NOT ~

# Flip the bit

# 0 → 1
# 1 → 0
# 101 becomes 010

# XOR ^
# XOR means Exclusive OR.

# A	B	A XOR B
# 0	0	0
# 0	1	1
# 1	0	1
# 1	1	0

# It gives 1 when the two bits are different.

# same → 0
# different → 1

#   101
# ^ 011
# -----
#   110

print(5 ^ 3) # 6

# Easy way to remember
# XOR = "Are these bits different?"

# 4. Left Shift and Right Shift

# <<   left shift
# >>   right shift

# Left shift <<

# Suppose:
# 5 = 101
# 101
# ↓
# 1010
# 1010 is 10.

print(5 << 1) # 10

# 5 << 1 = 10
# It's basically multiplying by 2:
# 5 × 2 = 10

print(5 << 2) # 20

# 5 × 2 × 2 = 20

# Right shift >>
# Move everything one position to the right:
# 1010 => 0101

print(10 >> 1) # 5

# It's roughly like integer division by 2
# 10 // 2 = 5

print(20 >> 2) # 5
# 20 // 2 // 2 = 5

# 5. Parity Check — Is a Number Odd or Even?

# 2 = 10
# 4 = 100
# 6 = 110
# 8 = 1000

# 1 = 1
# 3 = 11
# 5 = 101
# 7 = 111

# every even number ends in 0 and odd in 1

# 6 = 110

#   110
# & 001
# -----
#   000
print(6 & 1) # 0 => even

number = 17

print(bin(17)) # 10001
print(bin(1)) #  00001 => 00001

if number & 1:
    print("Odd")
else:
    print("Even")


print(12 & 10)
print(12 | 10)
print(12 ^ 10)

# Operator	Name	Simple meaning	Example
# &	AND	Both must be 1	5 & 3 → 1
# |	OR	At least one is 1	5 | 3 → 7
# ~	NOT	Flip bits	~5 → -6
# ^	XOR	Different → 1	5 ^ 3 → 6
# <<	Left shift	Multiply by 2	5 << 1 → 10
# >>	Right shift	Divide by 2	10 >> 1 → 5