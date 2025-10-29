ascii_var=65  #ASCII value for character 'A'
char_var='A'  #Character variable can hold a single character
#print statement
print("Character Variable:", char_var)
print("ASCII Value Variable:", ascii_var)
print(ord(char_var))  #ord() function returns the ASCII value of the character
print(chr(ascii_var))  #chr() function returns the character for the given ASCII value

#Inbuilt Functions Examples
#Using type() function to get the data type of a variable   
print("Data type of char_var:", type(char_var))

#Using isinstance() function to check the data type of a variable
print("Is char_var a string?", isinstance(char_var, str))


#Using len() function to get the length of a string
sample_string="Hello"
print("Length of sample_string:", len(sample_string))

#Using str() function to convert other data types to string
num=100
print("String Variable:", str(num))
print("Data type of str(num):", type(str(num)))