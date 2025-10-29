#Numeric Data Types

integer_var=10  #Integer variable range is 100,-5,256
float_var=20.5  #Float variable range is 10.5, -3.14, 0.0
complex_var=3+4j  #Complex variable range is 1+2j, -3-4j, 0+0j

#print statements
print("Integer Variable:", integer_var)
print("Float Variable:", float_var)
print("Complex Variable:", complex_var) 

#String Data Type
string_var="Hello, World!"  #String variable range is "Hello", 'Python', """Multiline String"""

#print statement
print("String Variable:", string_var)

#Boolean Data Type
bool_var=True  #Boolean variable range is True, False
#print statement
print("Boolean Variable:", bool_var)

#Sequence Data Types
#list variable is defined using square brackets []
#list variable can hold multiple data types
#lists are mutable, meaning their elements can be changed
#lists support indexing and slicing
#lists can be nested
list_var=[1, 2, 3, 4, 5]  #List variable range is [1,2,3], ['a','b','c'], [True, False]

#tuple variable can't be changed after creation, hence it's immutable.
#tuple variable is defined using parentheses ()
#tuple variable can hold multiple data types
#tuples are faster than lists
#tuples use less memory than lists
#tuple variable can carry duplicate values

tuple_var=(10, 20, 30)  #Tuple variable range is (1,2,3), ('x','y','z'), (True, False)

#Set variable is defined using curly braces {}
#Set variable is unordered collection of unique elements
#Sets are mutable, meaning their elements can be changed
#Sets do not support indexing or slicing

set_var={100, 200, 300}  #Set variable range is {1,2,3}, {'a','b','c'}, {True, False}   

#print statements
print("List Variable:", list_var)
print("Tuple Variable:", tuple_var)
print("Set Variable:", set_var)

#None Data Type
none_var=None  #None variable represents the absence of a value
#print statement
print("None Variable:", none_var)

