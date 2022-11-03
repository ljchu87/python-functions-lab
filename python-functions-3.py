def occurrences (string1, string2):
  new_string = string1.replace(string2, '')
  return (len(string1) - len(new_string))

print (occurrences('fleep floop', 'e'))   # returns 2
print (occurrences('fleep floop', 'p'))   # returns 2
print (occurrences('fleep floop', 'ee'))  # returns 2
print (occurrences('fleep floop', 'fe'))  # returns 0