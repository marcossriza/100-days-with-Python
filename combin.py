

print(4_000_000_000)
print('This is also a string')

car = ['Mercedes', 'BYS', 'Ford']
print(car)
print(car[1])

#print the last index
print(car[-1])
print(f'My first car was {car[0]}')

my_friends = ['Elliah Ellaine', 'Angel', 'Charlotte']
print(my_friends[0])
print(my_friends[1])
print(my_friends[2])

print(f'Hoping to see you soon, {my_friends[0]}')
print(f'Hoing to see you soon, {my_friends[1]}')
print(f'Hoping to see you soon, {my_friends[2]}')


dream_motorcycle = ['MIO', 'Honda Click', 'PCX']
print(f'Have a {dream_motorcycle[1]} motorcycle on 2026')


#update base on their index
dream_motorcycle[1] = 'Click'
print(dream_motorcycle)

#add an item on existing array on last index
dream_motorcycle.append('Big Bike')
print(dream_motorcycle)


dream_car = []

dream_car.append('Tesla')
dream_car.append('Ford')
dream_car.append('BYS')

print(dream_car)

#Building lists this way is very common, because you often
#won’t know the data your users want to store in a program
#until after the program is running. To put your users in
#control, start by defining an empty list that will hold #theusers’ values. Then append each new value provided to the
#list you just created.


#adding base on specified index, This operation shifts every other value in the list one position to the right.
dream_car.insert(2, 'BMW')
print(dream_car)


#deleting an item based on specified index
del dream_car[3]
print(dream_car)

#We start by defining and printing the list motorcycles ❶.Then we pop a value from the list, and assign that value tothe variable popped_motorcycle ❷. We print the list ❸ to show that a value has been removed from the list. Then we print the popped value ❹ to prove that we still have access to the value that was removed. The output shows that the value 'suzuki' was removed from the end of the list and is now assigned to the variable tenure_emp. Note: It is only popping the last item
new_emp = ['Jonallyn', 'Justine', 'Daniel']
print(new_emp)
tenure_emp = new_emp.pop()
print(new_emp)
print(tenure_emp)

#How might this pop() motorcycles in the list according to when we can use the pop() meth motorcycle we bought
history_ofMyMotor = ['Click', 'Mio', 'E-Bicycle']
oldest_bought = history_ofMyMotor.pop()
print(f'The {oldest_bought} is my oldest owned MotorCycle')

#
newest_bought = history_ofMyMotor.pop(0)
print(f'My newest bought motorcycle is {newest_bought}')


# Note: Remember that each time you use pop(), the item you work with is no longer stored in the list.
print(history_ofMyMotor)

#If you’re unsure whether to use the del statement or the pop() method, here’s a simple way to decide: when you want to delete an item from a list and not use that item in any way, use the del statement; if you want to use an item as you remove it, use the pop() method.



biscuits = ['Hansel', 'Oreo', 'Pepero', 'Kitkat', 'Twix']
# use remove if removing an item based on value if you  dont know the index
too_cheap = 'Hansel'


biscuits.remove(too_cheap)

print(biscuits)
#print the reason and the item
print(f'The {too_cheap.title()} is too cheap for the biscuit category')



my_old_classmate = ['Mac', 'Resty', 'Cath']

print(f'Hi, {my_old_classmate[0]}, I miss our shared laugh during OJT days. Happy to see your love life is well')

print(f'Hi, {my_old_classmate[1]}, I am so greatful for all you help during college days. You made my college easy')

print(f'Hi {my_old_classmate[-1]}, sorry for being distant to you but I hope, if our path crosses again we can become best friends')

busy_old_classmate = my_old_classmate.pop()
print(f'Ate {busy_old_classmate} wont make it tonight guys. So you two, {my_old_classmate} will only come by')

print('But luckily, I found a bigger table')

my_old_classmate.insert(0, "Clarissa")
my_old_classmate.insert(2, 'Angelica')
my_old_classmate.append("Siara")

print(f'Hi, {my_old_classmate[0]}. I would like to invite you to my house')
print(f'Hi, {my_old_classmate[2]}. I would like to invite you to my house')
print(f'Hi, {my_old_classmate[-1]}. I would like to invite you to my house')

  

cm_1 =my_old_classmate.pop()
cm_2 =my_old_classmate.pop()
cm_3 = my_old_classmate.pop()

print(f'Hi {cm_1}, sorry for the short notice. I cant invite you the dinner anymore')
print(f'Hi {cm_2}, sorry for the short notice. I cant invite you to the dinner anymore')
print(f'Hi {cm_3}, sorry for the short notice. I cant invite you to the dinner anymore')

print(f'{my_old_classmate[0]}, your still invited')
print(f'{my_old_classmate[1]} your strill invited')
print(f'Guest to invite remaining: {my_old_classmate}')
del my_old_classmate[0]
#The key rule 🧠When you delete an item from a list, the list immediately shrinks and re-indexes. best to indext first the [-1] or index first the higher index like [1]
del my_old_classmate[0]

print(f'Guest to invite remaining: {my_old_classmate}')



<<<<<<<< HEAD:introduction_to_list.py
cars = ['bmw', 'audi', 'ford', 'DYG']
#length of the list
print(len(cars))



#3-8 try it yourself
dream_places = ['Japan', 'South Korea', 'Dubai', 'Canada', 'Vietnam']
print(f'Original List: {dream_places}')

#make it alpahebetical order

#sort the order but dont change the original order
sorted_place = sorted(dream_places)
print(sorted_place)
#still on its original list
print(dream_places)

#reverse alphabetical order
reverse_sorted_place = sorted(dream_places, reverse=True)
print(reverse_sorted_place)

print(f'Original List Copy: {dream_places}')


#reverse the original list
dream_places.reverse()
print(dream_places)

#reverse back to its original list
dream_places.reverse()
print(dream_places)

#permanently change into alphabetical order the list
dream_places.sort()
print(dream_places)
#reverse permanently the order 
dream_places.sort(reverse=True)
print(dream_places)


#3-9 Dinner Guest (TRY IT YOURSELF)
#count the length of the previous exercise
print(len(my_old_classmate))


#3-10 Every Function (TRY IT YOURSELF)
#i skipped



========
>>>>>>>> 57c8dc022e9a1af38491e69fba47df7da8ad9d2e:combin.py

