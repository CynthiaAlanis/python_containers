# ---------------Exercise 1--------------------
# Create a list named students containing some student names (strings).
students = [ 'Fred','Tom','Ben']
# Print out the second student's name.
print(students[1])
# Print out the last student's name.
print (students[2])


#------------------Exercise 2-------------------------------
# Create a tuple named foodscontaining the same number of foods (strings) as there are names in the studentslist.
foodscontaining = ('pizza', 'cookies', 'chips')
# Use a forloop to print out the string "food goes here is a good food".
# for i in range(len(foodscontaining)):
#   print(foodscontaining[i])
for food in foodscontaining:
 print(f'{food} is a good food')
  
  #Exercise 3
  #Using a forloop, print just the last two food strings from foods.
for food in foodscontaining[-2:]:
     print(food) 

# Create a dictionary named home_towncontaining the keys of city, state and population.
# Print a string with this format:
# "I was born in city, state - population of population"
home_towncontaining = {
  'city' : 'Midway City',
  'state' : 'California',
  'population': 8681
}

print( f'I was born in {home_towncontaining["city"]}, {home_towncontaining["state"]}- population of {home_towncontaining["population"]}')