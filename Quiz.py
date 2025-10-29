#List 

## Simple example of List 
# first_variable=[1,2,3,4]
# second_variable=first_variable
# print("First Variable is:",first_variable)
# print("Second Variable is:"second_variable)


## Correct way to copy a list
# first_variable=[1,2,3,4]
# second_variable=first_variable.copy()
# print("First_variable is:",first_variable)
# print("Second_variable is:",second_variable)

## Another way to copy a list
# first_variable=[1,2,3,4]
# second_variable=list(first_variable)
# print("another way to copy a list")
# print("First_variable is:",first_variable)
# print("Second_variable is:",second_variable)

## Append method in list
# first_variable=[1,2,3,4,'Apple',30.5]
# first_variable.append('Banana')
# print("After appending, First_variable is:",first_variable)

## Insert method in list
# first_variable=[1,2,3,4,'Apple',30.5]
# first_variable.insert(2,'Banana')
# print("After inserting, First_variable is:",first_variable)

## Remove method in list
# first_variable=[1,2,3,4,'Apple',30.5]
# first_variable.remove('Apple')
# print("After removing, First_variable is:",first_variable)

first_variable=[1,2,3,4,'Apple',30.5]
first_variable.remove()
print("After removing, First_variable is:",first_variable)