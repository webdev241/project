# Python3 program to add two numbers
num1 = 15
num2 = 12
# Adding two nos
sum = num1 + num2
# printing values
print("Sum of", num1, "and", num2 , "is", sum)


#python program to print square from 1-20 numbers.
for i in range(1, 21):
    square = i ** 2
    print(f"The square of {i} is: {square}")
    
    
#program to find cube of first 1-10 numbers.
for i in range(1, 11):
    cube = i ** 3
    print(f"The cube of {i} is: {cube}")
    
    
#4. print table of 7 like:
# Input a number
n = 7

# Initialize loop counter by 1
i = 1

# Loop to print table
while i <= 10:
    # multiply number by loop counter
    t = n * i
    # print result
    print(n, "x", i, "=", t)
    # increase loop counter by 1
    i = i + 1
    

#program to reverse python string-python --> nohtyp
def reverse(s):
	str = ""
	for i in s:
		str = i + str
	return str

s = "python"

print("The original string is : ", end="")
print(s)

print("The reversed string(using loops) is : ", end="")
print(reverse(s))


#find length of string in python (try find in 4 different ways).
#method1
str = "python"
print(len(str))

#method2
def findLen(str):
    counter = 0   
    for i in str:
        counter += 1
    return counter
 
str = "pyhton"
print(findLen(str))

#method3
def findLen(str):
    counter = 0
    while str[counter:]:
        counter += 1
    return counter

str = "python"
print(findLen(str))

#method4
def findLen(str):
    if not str:
        return 0
    else:
        some_random_str = 'py'
        return ((some_random_str).join(str)).count(some_random_str) + 1
 
str = "python"
print(findLen(str))
