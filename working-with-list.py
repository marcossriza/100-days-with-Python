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



