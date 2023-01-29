# ---------------Exercise 1--------------------
# Create a list named students containing some student names (strings).
students = [ 'Fred','Tom','Ben','Cynthia']
# Print out the second student's name.
print(students[1])
# Print out the last student's name.
print (students[2])

#------------------Exercise 2-------------------------------
# Create a tuple named foodscontaining the same number of foods (strings) as there are names in the studentslist.
foodscontaining = ('pizza', 'cookies','chips')
# Use a forloop to print out the string "food goes here is a good food".
# for i in range(len(foodscontaining)):
#   print(foodscontaining[i])
for food in foodscontaining:
 print(f'{food} is a good food')
  
#-------------------Exercise 3-------------------
  #Using a forloop, print just the last two food strings from foods.
for food in foodscontaining[-2:]:
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
# Iterate over the key: value pairs in home_town and print a string for each item, for example:
for key, val in home_town.items():
 print( f'The {key} I live in is {val}')
 
 
#---------------Exercise 6--------------------
#  Create an empty list named cohort.
# Using a forloop, add one dictionary to the cohortlist for each student name. Each dictionary should have this shape:
cohort = []
for i in range(len(info)):
  cohort.append({'student':info[i],'fav_food':info[i]})

print(cohort)


