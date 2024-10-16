
# 1. Unpacking (List, Dict)
# 2. Packing
# 3. Spreading
# 4. Enumerate
# 5. Zip


## Unpacking List ##

def display_customer(name, age, place):
    print(f"Customer name is {name}, age is {age} and base location is {place}")

lst = ['abin', 32, 'Bangalore']

display_customer(*lst) #Unpacking --> restructure list into individual elements

## Unpacking Dictionary ##
dict_values = {'name': 'abin', 'age': 32, 'place': 'Bangalore'}

display_customer(**dict_values)

"""
Packing
Sometimes we never know how many arguments need to be passed to a python function. We can use the 
packing method to allow our function to take unlimited number or arbitrary number of arguments.
"""

def total_office_days(*wfh_days):
    print(wfh_days) # (1, 2, 3, 4, 5, 6, 7, 8, 9)
    print(len(wfh_days)) # 9

total_office_days(1,2,3,4,5,6,7,8,9)


## Spreading ##

lst1 = [1,2,3]

lst2 = ['abin', 'singh']

lst3 =['Bangalore']

lst4 = [*lst1, *lst2, *lst3]

print(lst4)

## Enumerate ##
## If we are interested in an index of a list, we use enumerate built-in function
## to get the index of each item in the list.

max_value = 0
max_index = 0
for index, value in enumerate([100,20,30, 80, 300, 35]):
    if value > max_value:
        max_value = value
        max_index = index
print(f"maximum value in the list is {max_value} and index at {max_index}")


# Zip #
# Sometimes we would like to combine lists when looping through them #

fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']

fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)
