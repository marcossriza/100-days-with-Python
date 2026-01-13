magicians = ["alice","daniela", "elliah"]
#FOR LOOPS
#for new declared variable fetch the variable magicians and print item inside the newly variable endlessly until no item to produce
for magician in magicians:
    print(magician)
#NAMING PRACTICES ON FOR LOOPS
#for cat in cats:
# for dog in dogs:
# for item in list_of_items:
#These naming conventions can help you follow the action being done on each item within a for loop. Using singular and plural names can help you identify whether a section of code is working with a single element from the list or the entire list.



#FOR LOOP WITH STRING
for magician in magicians:
    print(f'Hi {magician.title()}, nice trick!')
#adding another indentation to the "for loop". you can add as may as indentation you like
    print(f'I cant wait for your next trick, {magician.title()} \n')

#notice that this print of line is outside on the indentation loop so it will only print at the end of the loop. NOT ON EVERY LOOP
print(f'Thank you to all of our magicians for your performances')    

#Python’s use of indentation makes code very easy to read. Basically, it uses whitespace to force you to write neatly formatted code with a clear visual structure. In longer Python programs, you’ll notice blocks of code indented at a few different levels. These indentation levels help you gain a general sense of the overall program’s organization.

#python produce an "IndentationError" if it expects an indentation


#the colon on for loop ":" means the next line is the start of the loop


magicians = ['alice', 'david', 'carolino']
for magician in magicians:
    print(magician)




#range() funcation. 
#print the number range like 1,2,3... like its counting. the first num is the starting and the second parameter is what number to stop. it stop before 100 so the result is until 99
#if you only add a 1 parameter it will automatically start to 0. et al. range(80)
for value in range(1,10):
    print(value)

#store in a list output [1,2,3,4,5..]. rather than printing one line per number
numbers = list(range(1, 9))
print(numbers)



#EXPONENT AND APPEND. append means input to the variable
math_exponent = []
for expo in range(1,9):
    math_exponent.append(expo**2)


print(math_exponent)

#using list comprehensions. just as same output above but shorter
#To use this syntax, begin with a descriptive name for the list, such as squares. Next, open a set of square brackets and define the expression for the values you want to store in the new list. In this example the expression is value**2, which raises the value to the second power. Then, write a for loop to generate the numbers you want to feed into the expression, and close the square brackets. The for loop inthis example is for value in range(1, 11), which feeds the values 1 through 10 into the expression value**2. Note that no colon is used at the end of the for statement.
squares = [value ** 2 for value in range(1,9)]
print(squares)


#4.3 COUNTING TO TWENTY TRY IT YOUR SELF
for value in range(1,21):
    print(value)
#i tried using list and comprehension list
count_20 = [counts_20 for counts_20 in range(1,21)]
print(count_20)


#4-4 Print a list of count 1 milion

#count_1m =[counts_1m for counts_1m in #range(1, 10000001)]

#print(count_1m)


#USE AGGREVIATE TO MAKE SURE THE COUNT START AT 1 AND END IN 1M AND THE SUM OF EACH NUMBER ON 1M
aggreviate_1m = [aggreviates_1m for aggreviates_1m in range(1, 1000001)]


print(min(aggreviate_1m))
print(max(aggreviate_1m))
print(sum(aggreviate_1m))


#4-6 ODD NUMBERS
odd_num =[]
for odd_nums in range(1,21,2):
    odd_num.append(odd_nums)
       
print(odd_num)



multiple_of_3s = []
for multi in range(3,31,3):
    multiple_of_3s.append(multi)
print(multiple_of_3s)


#4-8 cubes

cubes_expo = [cube_expo**3 for cube_expo in range(1,11)]

for cube in cubes_expo:
    print(cube)



#4-9 Cube Comprehension

cube_wListComprehension = [cube_expo_compre**3 for cube_expo_compre in range(1,11)]
print(cube_wListComprehension)


#slice

players = ['anna', 'charlotte', 'angel', 'ellaine', 'riza']
#variable, bracket what index to start and what before number to stop. it retains all the item. this just fetch according what we slice. [3:] if you ommit the first parameter it automatically starts with the first item and vise versa et al. [1:], [-3:]
print(players[1:5])


#use the slicer on for loop. called the last item on the list
print('The last to finish the lane are: ')
for player in players[-3:]:
   print(player.upper())



#COPY THE LIST BY [:]
my_food = ['pizza', 'cake', 'pichi-pichi']
bfs_food = my_food[:]

print(f'This my fave food {my_food} and this is my bfs fave food, {bfs_food}')

#we added a new item on a separate list. this added separated even the second variable just copied the original list of the first var
my_food.append('matcha')
bfs_food.append('ice cream')

print('My updated fave food:')
print(my_food)

print('My bf updated food:')
print(bfs_food)


#if we want the variable to have a same item even if we append. but this is mostly unlikely to happen. slicing is better for other scenario
fave_color = ['red', 'violet', 'brown']
bfs_color = fave_color

fave_color.append('matcha')
bfs_color.append('black')

print('New set of my fave color')
print(fave_color)

print('New set of my bfs fave color:')
print(bfs_color)


#TRY IT YOURSELF
#4-10 SLICES 

print('The first three items in the list are:')
#print the first three items from the players list
print(players[0:2])
#print the three items from the middle of the list
print(players[:2])
#prin the last three items in the list
print(players[:-3])


#4-11 MY PIZZAS, YOUR PIZZAS

#copied the list of var magicians
batch2_magicians = magicians[:]

#added a new item on the original magicians
magicians.append('Arisu')
#added additional magicians to the batch 2
batch2_magicians.append('Ame')

for magician in magicians:
   print(f'The original cast for the magicians are: {magician.title()}')

for batch2_magician in batch2_magicians:
    print(f'Let me introduce the cast for the season 2 of the magicians: {batch2_magician.title()}')



#better syntax, same as above
print('-------------\n \n')
print('The original cast for the magicians are:')
for magician in magicians:
    print(magician.title())


print('Let me introduce the cast for the season 2 of the magicians:')
for batch2_magician in batch2_magicians:
    print(batch2_magician.title())

