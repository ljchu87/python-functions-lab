def product(*args):
  product = 1
  for arg in args:
    product *= arg
  return product

print (product(-1, 4)) # returns -4
print (product(2, 5, 5)) # returns 50
print (product(4, 0.5, 5)) # returns 10.0