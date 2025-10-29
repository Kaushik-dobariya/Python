# Bitwise Operators in Python
a=5
b=7
print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)
print("Bitwise XOR:", a ^ b)
print("Bitwise NOT:", ~a)
print("Bitwise left shift:", a << 1)
print("Bitwise right shift:", a >> 1)

'''
Bitwise of 5 will be: 
5/2=2 remainder 1
2/2=1 remainder 0
1/2=0 remainder 1   
So, Bitwise of 5 is  101

Bitwise of 7 will be:
7/2=3 remainder 1
3/2=1 remainder 1
1/2=0 remainder 1
So, Bitwise of 7 is  111

& (AND) Operator:
        &
----------
1 0     0
1 1     1
0 0     0

OR | Operator:
        |
----------
1 0     1
1 1     1
0 0     0

XOR ^ Operator:
        ^
----------
1 0     1
1 1     0
0 0     0

NOT ~ Operator:
~0 = 1
~1 = 0

Left Shift << Operator:
Shifts bits to the left, adding zeros on the right and adding one on right if negative.
17 (10001) << 1 = 34 (100010)


Right Shift >> Operator:
Shifts bits to the right, discarding bits on the right.

'''