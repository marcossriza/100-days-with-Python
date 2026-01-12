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

