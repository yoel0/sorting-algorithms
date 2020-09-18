# QUICK SORT: best/average O(n*log n) worst O(n^2)
# BASE CASE(S): length of list less than or equal to 1
# RECURSIVE CASE: Any other length
# 1. Pick a pivot element
# 2. Divide into left and right, based on the pivot element
# 3. Put it back together
#   a) Quick sort the left
#   b) Quick sort the right
#   c) Concat left + pivot + right

nums = [3, 78, 23, 466, 324, 2, 12, 546, 17, 56, 23, 123, 343, 87, 94, 45, 6, 9, 234, 36]