# functions are a set of instructions in python that that are stored and can be called upon anytime to perform those set of instruction
# ===========================
# EXAMPLE1:
# ===========================



# i =3
# y = 12
# z= 0
# def multiplication(i,y):
#     """ Checking if input is """

#     return i*y 
# res = multiplication(i,y)
# print(res)

#This multiplication function does multiplication and returns the value to where the function was called, here, iand y are replaced by 3 and 4 the numbers i put in the function. The body of code in the function is then ran and we use return to send the answer that was gotten back to the user

# ===========================
# EXAMPLE 2: Function add odd numbers in a range
# ===========================

#Way 1

# odd_numbers = 0
# def odd(i):
#     return i%2 != 0

# for i in range(1,11):
#     if odd(i):
#         odd_numbers += i
#     else:
#         pass
# print(odd_numbers)

#Way 2


# def odd_add(i,j):
#     """Checking for Odd numbers"""
#     odd_numbers = 0
#     for p in range (i,j+1):
#         if p%2 != 0:
#             odd_numbers += p
#     print(odd_numbers)
#     # return odd_numbers
# A = odd_add(10,11)
# print(A)


# ===========================
# NB:
# ===========================

# Printing a function that you ruh without putting return will always return None. But if you put a print statement in the function and run the function without printing it it will print the statement in the function even without printing it. Return only have meanings in a function only one return function works in a function

# def add(a,b):
#     """Addition Function"""
#     return a+b
# def multiplication(a,b):
#     """Multiplication Function"""
#     print(a*b)
# add(1,2)
# print(add(1,2))
# multiplication(1,2)
# print(multiplication(1,2))

# here is an example of how return, prints and none works

# ===========================
# EXAMPLE 3: Bisection root with functions
# ===========================

# def bisection_root(x):
#     """Bisection root"""
#     epsilon = 0.1
#     if x < 1:
#         low = x
#         high = 0
#     else:
#         low = 0
#         high = x
#     guess = (low+high)/2.0
#     while abs(guess**2 - x) > epsilon:
#         if guess**2 > x:
#             high = guess
#         else:
#             low = guess
#         guess = (low+high)/2.0
#     return guess


# print(bisection_root(4))

# ===========================
# Class Work
# ===========================


#   
#Functions can be called in another function and can also be used as a parameter. Also, Functions can be given an assignment operator e.g 
# def add(x) 
# sum = add
# here is sum(3) is called, it performs the same function as add(3)

#example of function in a parameter

# def even(x):
#     return x%2 == 0
# def apply(op,x):
#     for i in range(0,x+1):
#         print(op(i))
# apply(even,10)

#in the example above im assigning op to the even. Then in line 125, I'm calling even as a function wrapped in i. so it is interpreted as print(even(1))....... print(even(10)) because i is in a range



# ===========================
# How to set default parameters in a function
# ===========================


# def bisection_root(x,epsilon = 0.1):   #Here we are setting the default value of epsilon to be 0.1 in-case the user forgets to add epsilon when calling the function we have a default value DEFAULT PARAMETERS MUST GO AT THE END OF THE LIST
#     """Bisection root with default epsilon"""
#     if x < 1:
#         low = x
#         high = 0
#     else:
#         low = 0
#         high = x
#     guess = (low+high)/2.0
#     while abs(guess**2 - x) > epsilon:
#         if guess**2 > x:
#             high = guess
#         else:
#             low = guess
#         guess = (low+high)/2.0
#     return guess

# root_bisection = bisection_root #This is correct because objects are data types and can be given another tag. 



# ===========================
# Making a function in a function
# ===========================

# def make_prod(a):
#     def g(b):
#         return b*a
#     return g

# Value = make_prod(2)(3) #Python first runs make_prod(2) and returns it as a function so val now becomes a function call of g val=g(3). When a function is called. it creates an environment separate from the global environment if a variable can not be found in a function it goes higher up the environment chain to look for the variable. so since a is not defined in the function parameters it goes to the immediate environment above it which is the make_prod environment to get the value of a. If a can not be found in the main_prod environment it goes to the immediate higher one which is the global environment to look for it
# print(Value)


