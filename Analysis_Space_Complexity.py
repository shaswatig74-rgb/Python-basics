# The halving sequence for n = 10:
n = 10
step = 0
while n > 1:
    n = n // 2
    step+=1
    print("After Step", step, ": remaining =", n)

# Output
# After step 1: reamaining = 5
# After step 2: reamaining = 2
# After step 3: reamaining = 1
# 3 -4 steps to reduce 10 to 1 -- That is O(log n).

# Binary Search

scores = [12, 25,33,41,50,67,72,85,91,98]
target = 98
lo,hi, steps = 0, len(scores) - 1, 0

while lo <=hi:
    mid = (lo + hi) // 2
    steps +=1
    if scores[mid] == target:
        print("Found at index", mid, "  | steps =", steps)
        break

    elif scores[mid] < target:
        lo = mid + 1              # target in right half

    else:
        hi = mid + 1              # target in left half

# Output: Found at index 9 | steps = 4
# Linear scan would take 10 steps for the same list.

# recursion

def binary_search_rec(scores, lo, hi, target, calls = 0):
    calls+=1
    if lo > hi:
        return -1, calls
    mid = (lo + hi) // 2
    if scores[mid] == target:
        return mid, calls

    elif scores[mid] < target:
        return binary_search_rec(scores, mid + 1, hi, target, calls)

    else:
        return binary_search_rec(scores, lo, mid - 1, hi, target, calls)

result, calls = binary_search_rec(scores, 0, 9, 98)

# Output: Index = 9, calls = 4