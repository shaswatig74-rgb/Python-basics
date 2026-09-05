# Asymptotic Simplification - keep the dominant term

# 3n^2 + 5n + 9  -> O(n^2)  (n^2 dominates for large n)
# 7n + 100       -> O(n) (n dominates, constant 100 drops)
# n*(n-1)/2      -> O(n^2) (expand : n^2 - n/2, dominant = n^2)
# 500            -> O(1)  (no n at all, always constant)

# Proof for n = 1000 :

n = 1000
full = 3*n**2 + 5*n + 9
dominant = n**2
print("Full expression: ", full) # 3,005,000
print("Dominant term:", dominant) # 3,000,000
print("Ratio :", round(full/dominant, 2)) # ~3.0

# The ratio stays near a constant - the shape is the same.