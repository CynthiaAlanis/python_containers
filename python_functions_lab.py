# 1. Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.
def sum_to(n):
  return (n*(n+1)//2)
print(sum_to(6))
print(sum_to(10))

# 2. Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.
def largest(n):
  largest_num = n[0]
  for num in n:
    if num > largest_num:
      largest_num =num
  return largest_num
    
print(largest([1, 2, 3, 4, 0]))
print(largest([10, 4, 2, 231, 91, 54]))

#another solution to solve example 2:
list1 = [1, 2, 3, 4, 0]
largestValue = max(list1) #using Pythons list max()function
print(largestValue)

list2 = [10, 4, 2, 231, 91, 54]
maxValue = max(list2)
print(maxValue)

# 3. Write a function named occurances that takes two string arguments as input and counts the number of occurances of the second string inside the first string.
def occurances(str,sub):
  counts = 0
  for i in range( len(str)):
    if str[i:].startswith(sub):
      counts = counts + 1
      return counts
print(occurances('fleep floop', 'e'))  # returns 2
print(occurances('fleep floop', 'p'))  # returns 2
print(occurances('fleep floop', 'ee')) # returns 1
print(occurances('fleep floop', 'fe'))  # returns 0

# 4. Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product.
def product( *args):
  num =1
  for arg in args:
    num *= arg
  return num
#Using the * specifier in a parameter list allows us to pass in a varying number of arguments into a function:
print(product(-1, 4)) # returns -4
print(product(2, 5, 5)) # returns 50
print(product(4, 0.5, 5)) # returns 10.0
  

