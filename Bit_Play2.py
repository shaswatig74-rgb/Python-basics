# # 01- xor-identity-cancel
# # Topic: XOR Identity and Equality, XOR Cancellation

# input("XOR with 0 keeps the number. Press Enter")
# print(" 5 ^ 0 = ", 5 ^ 0)
# print(" 9 ^ 0 = ", 9 ^ 0)

# input("XOR with itself gives 0. Press Enter")
# print(" 5 ^ 5 = ", 5 ^ 5)
# print(" 9 ^ 9 = ", 9 ^ 9)

# n = int(input("Enter a number (try 6 or 11): "))
# guess = input("What is 3 ^ " + str(n) + "^ 3? ")
# input("XOR cancels - 3 appears twice so it disappears. Press Enter")
# print(" 3 ^",n,"^ 3 = ", 3 ^ n ^ 3, "your guess: ",guess)

# 02 - odd- occurring
# Topic: One odd-occurring Number

# input("XOR all numbers - pairs cancel, the odd one stays. Press Enter")
# print(" list: [2,3,4,3,2]")
# print(" odd-occurring: ",2^3^4^3^2)

# n = int(input("Enter a number (try 7 or 11): "))
# nums = [3,n,5,3,5]
# guess = input("which number in" + str(nums) + "appears once? ")
# result = 0
# for x in nums:
#     result^=x
# input("XOR cancels pairs - the odd one survives. Press Enter")
# print(" list:",nums," odd-occurring: ",result," your guess: ",guess)

# 03-two-odd-split
# Topic: XOR of Two Odd-Occuring Numbers, splitting by the Rightmost set bit

input("XOR all - pairs cancel, two odd-occurring numbers remain. Press Enter")
print(" [1,4,3,3] XOR of all: ",1^4^3^3, "binary: ",bin(1^4^3^3)[2:] )
print(" split bit 1 -> group A (bit 0 ON): 1 group B (bit 0 OFF): 4")

n = int(input("Enter a number (try 6 or 9): "))
guess = input("Is bit 0 of" + str(n) + " ON? (yes/no): ")
input("Check the split bit. Press Enter")
if n & 1:
    print(" ",n," binary: ",bin(n)[2:]," bit 0 is ON - group A your guess: ",guess)
else:
    print(" ",n," binary: ",bin(n)[2:], " bit 0 is OFF - group B your guess: ",guess)