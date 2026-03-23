#Recursion is the opposite of Iteration in recursion you for a base case foe your problem and build back up using multiple function calls instead of using one like loops


#What is recursion?

#Recursion is a way to solve problems by using divide and conquer or decrease and conquer mostly by writing a function in terms of itself 2



#===============
#Example 1
#===============

#using recursion to find factorials
# def factorial(number):
#     #The base case here will be 1 as 1! is 1 that will be the simplest case we want to achieve when solving this
#     if number == 1:
#         return 1
#     else:
#         return number*factorial(number-1) #this is to create another function environment that keep going until we get to base case. When it gets to base case it returns the value to the function that called them
# print(factorial(4))


#===============
#Recursion with lists
#===============

# def sum_list(L):
#     if len(L) == 1:
#         return len(L[0])
#     else:
#         return len(L[0]) + sum_list(L[1:])
    
# lists = ['b','be','ben2']
# print(sum_list(lists))

#Example 2

def element_check(list,element,new_list = []):
    if element in new_list:
        return True
    elif len(list) ==1 and element not in list:
        return False
    else:
        new_list += list[0]
        return element_check(list[1:],element,new_list)
 
list = [[1,2],[3,4],[5,7],[9,10]]
print(element_check(list,7))