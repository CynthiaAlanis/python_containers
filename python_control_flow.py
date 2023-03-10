# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z):
print("Enter a letter in the alphabet")
# 2. Write the code that determines whether the letter entered is a vowel
letters="aeiou"
letter = input("Enter a letter:")
if letter in "aeiou":
  print('The letter is a vowel')
else:
  print('The letter is not a vowel')
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant
# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':
if letter in letters:
  print(f"The Letter {letter} is a Vowel")
else:
  print(f"The Letter {letter} is a Consonant")


# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase:
phrase = input("Please enter a word or phrase:")
# 2. Print the following message:
#      - What you entered is xx characters long

print(f"What you entered is {len(phrase)} characters")
# 3. Return to step 1, unless the word 'quit' was entered.


# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years:
dogsAge = input('Enter a dogs age in human year: ')
dogsAge = int(dogsAge)
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
if dogsAge <= 2:
  dog_years = dogsAge *10
else:
  dog_years = ((dogsAge - 2) * 7) + 20
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx
# Hint:  Use the int() function to convert the string returned from input() into an integer
print(f"The dogs age in years is {dog_years}")

# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
a = input('Enter side 1 : ')
b = input('Enter side 2 : ')
c = input('Enter side 3 : ')

# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length


# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle
if a == b and b == c:
  print(f'A triangle with sides of {a}, {b} & {c} is a equalateral triangle')
elif a == b or b== c or c == a:
  print(f'A triangle with sides of {a}, {b} & {c} is a scalene isosceles triangle') 
else:
  print(f'A triangle with sides of {a}, {b} & {c} is a scalene triangle') 

# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.
# Hint: The next number is found by adding the two numbers before it

def fib(n):
  a = 0
  b = 1
  print(a)
  print(b)
  
  for i in range(2,n):
    c = a + b
    a = b 
    b = c 
    print(c)
fib(50)
# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the season (Jan - Dec):

month= input('Enter the month of the season (Jan - Dec): ')
# 2. Then promptshtt the user to enter the day of the month:
#      Enter the day of the month:
day= int(input('Enter the day of the month: '))
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
if (month == 'dec' and day in range(21,31) or 
    month == 'jan' or 
    month == 'fed' or 
    month == 'mar' and day in range(1,19)):
    print(f'{month},{day} is in Winter')

elif (month == 'mar' and day in range(20,30) or 
      month == 'apr' or 
      month == 'may' or 
      month == 'jun' and day in range(1,20)):
      print(f'{month},{day} is in Spring')
  
elif (month == 'jun' and day in range(1,20) or 
      month == 'jul' or 
      month == 'aug' or 
      month == 'sep' and day in range(1,21)):
      print(f'{month},{day} is in Summer')

elif (month == 'sep' and day in range(22,30) or
      month =='oct' or 
      month == 'nov' or 
      month =='dec' and day in range(1,20)):
      print(f'{month},{day} is in Fall')
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season>

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.