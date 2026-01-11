cars = ['bmw', 'audi', 'toyota', 'subaru']
#this sort by alpahetical order for the items
cars.sort()
print(cars)
#reverse the alphabetical order
cars.sort(reverse=True)
print(cars)

#sorted
cars = ['bmw', 'audi', 'toyota', 'subaru']
print('Original list')
print(cars)

print('Sorted list')
print(sorted(cars))
#the difference between sort and sorted is that the sorted will only display the sort item but the orginal order is still the same unlike the sort
print('Original list again')

print(cars)

#reverse the order of the item only. it reverse permanently
cars.reverse()
print(cars)
#if you want to reverse back to its original order
cars.reverse()
print(cars)


