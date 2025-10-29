
name_var=input("Enter your name: ")  #String variable
print("Hello,", name_var)

age_var=(input("Enter your age: "))  #string variable
age_var_int=int(age_var)  #Converting string to integer
print("type of age_var:", type(age_var))
print("type of age_var_int:", type(age_var_int))

#print using expression
print("Your age next year will be:", age_var_int + 1)




#Excercise: Sum of two integer variables

num1_var = int(input("Enter first integer: "))  #Integer variable
num2_var = int(input("Enter second integer: "))  #Integer variable
#Sum of two integer variables
sum_var = num1_var + num2_var
#print statement
print("Sum of num1_var and num2_var is:", sum_var) 