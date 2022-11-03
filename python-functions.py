# 1 -------------------
def sum_to(n):
  sum = 0
  while sum <= n:
    new_sum = (n * (n + 1)//2)
    return(new_sum)

print (sum_to(6))
print (sum_to(10))

# 2 -------------------
def largest (nums):
  largest = 0
  for num in nums:
    if num > largest:
      largest = num
  return largest

print (largest([1, 2, 3, 4, 0]))
