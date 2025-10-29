#string variable
name="Kaushik Kumar"

#integer variable
age=41

#float variable
height=5.11

#boolean variable
is_student=False

#print Statement using concatenation
print("My name is "+ name+", My Age is ", age,", My Height is ",height ,"and am i student then it's ",is_student)

#print using f-string
print(f"Name: {name}, Age: {age}, Height: {height}, Is Student: {is_student}")

#print using multiple print statements
'''print("Name:", name)
print("Age:", age)  
print("Height:", height)
print("Is Student:", is_student)'''

#print with custom separator
print(name,age,height,is_student,sep="/")
