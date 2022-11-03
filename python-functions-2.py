def largest (nums):
  largest = 0
  for num in nums:
    if num > largest:
      largest = num
  return largest

print (largest([1, 2, 3, 4, 0]))