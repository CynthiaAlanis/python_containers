# ---------------Exercise 1--------------------
# Create a list named students containing some student names (strings).
students = [ 'Fred','Tom','Ben','Cynthia']
# Print out the second student's name.
print(students[1])
# Print out the last student's name.

# print (students[len(students)-1])
#another way is the pop method
# print(students.pop())

#---------------Exercise 2----------------------
# Create a tuple named foods containing the same number of foods (strings) as there are names in the studentslist.
# Use a forloop to print out the string "food goes here is a good food".

foods = ('pizza', 'cookies','chips', 'hamburger')
for food in foods:
 print(f'{food} is a good food')
  
#-------------------Exercise 3-------------------
  #Using a forloop, print just the last two food strings from foods.
for food in foods[-2:]:
     print(food) 

#-------------------Exercise 4---------------------
# Create a dictionary named home_town containing the keys of city, state and population.
# Print a string with this format:
# "I was born in city, state - population of population"
home_town = {
  'city' : 'Midway City',
  'state' : 'California',
  'population': 8681
}

print( f'I was born in {home_town["city"]}, {home_town["state"]}- population of {home_town["population"]}')

#----------------Exercise 5-----------------------
# Iterate over the key: value pairs in home_town and print a string for each item
for key, val in home_town.items():
 print( f'The {key} I live in is {val}')
 
 
#---------------Exercise 6--------------------
#  Create an empty list named cohort.
# Using a forloop, add one dictionary to the cohortlist for each student name. 
cohort = []

for i, student in enumerate((students)):
  print(i,student)
  
  cohort.append({
    "student":student,
    "fav_food": foods[i]
  })

print(cohort)

#---------------Exercise 7--------------------
# Using the list of students and list comprehension, assign to a variable named awesome_students a new list containing strings similar to this:
# ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]
# Iterate over awesome_students printing out each string.

awesome_students= ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]

for i in range(len(awesome_students)):
  print(awesome_students[i])
  
#---------------Exercise 8--------------------  
#Using the tuple foods and list comprehension within a forloop, print each food string that contains the letter a.
# foods = ('pizza', 'cookies','chips', 'hamburger')
a_foods = []
for food in foods:
  if 'a' in food:
    a_foods.append(food)   
print(a_foods)