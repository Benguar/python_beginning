#Lists are mutable indexable data types

# ================
# When you use . you cannot append what you're doing to a variable. It gives error e.g X = list.append(a) will give error
# ================


# ================
# Examples of lists
# ================


# list1 = [1,2,3,4,5]
# list2 = ['a','b','c',[1,2,3],'d']
# list3 = [12,'a',3,'r','d',4,True,None]
# y = list2[3][1]
# print(y)


# ================
# Example of how to use lists
# ================


# def sum_and_prod(L):
#     """L is a list of numbers this function calculate the sum and products of these numbers and returns them as tuples"""
#     products,sums= (1,0)
#     for numbers in L:
#         sums += numbers
#     for numbers in L:
#         products *= numbers
#     return (products,sums)
# L = [1,2,3,4,5,]
# print(sum_and_prod(L))


# ================
# Examples of lists Mutability
# ================


# list1 = [1,2,3,4,5]
# list1[3] = "mutilated"
# print(list1)
# #above Index 3 of list1 changes to "mutilated"


# ================
# Examples of how to add elements to a list
# ================

# list1 = [1,2,3,4,5]
# list1.append(6)
# print(list1)
#above, .append(element) is used to add element 6 to the list


# ================
# Examples of mutating lists
# ================

# l1 =['do','re']
# l2 =['re','mi']
# l3 =['mi']
# l4 = l1 + l2 #This gives ['do','re','re','mi']

# print(l4)
# l3.append(l4)
# L = l1.append(l3) #returns none
# print(l3)

#extend is us to add more than one element in a list

# l = [1,2,3,4,5,6]
# l.extend([7,8,9,[1,0]])
# print(l)


# ================
# Class Work 1
# ================

# def make_ordered_lists(n):
#     """Returns a list of all numbers for 0 to n"""
#     i = 0
#     l1= []
#     for index in range(0,n+1):
#         l1.append(index)
#     return l1
# print(make_ordered_lists(10))


# ================
# Class Work 1
# ================

# def remove_elem(L,e):
#     """
#     L is a list
#     Returns a new list without any element equating to e 
#     """
#     new = []
#     for index in L:
#         if e != index:
#             new.append(index)
#     return new
# P = [1,2,2,2,2,2,1,3,2,1,4,5,6,3,3,2,2]
# print(remove_elem(P,2))


# ================
# Converting lists to strings and vice-versa
# ================


# #converting strings to lists
# string = "Benguar is a boy"
# List = list(string)
# print(List)
 # #we can use split to separate elements from a string
# List1 = string.split(' ') #this adds all the elements in a string till it gets to <space> as one element in a list so his returns ['Benguar', 'is', 'a','boy']
# print(List1)

#converting lists to strings

# L = ['a','b','c','d','e']
# String = ''.join(L)
# print(String) #returns 'abcde'
# String='_'.join(L) 
# print(String) #returns 'a_b_c_d_e'
# #Join only works with lists that has string elements


# ================
# Class Work 2
# ================


# def count_words(sen):
#     """sen is a string representing a sentence returns how many words are in s"""
#     string = sen.split(' ')
#     return len(string)
# print(count_words('i am a boy'))


# ================
# List sort and reverse(mutating)
# ================


# l = [1,2,3,4,5,6]
# l.extend([7,8,9,[1,0]])
# print(l)


# L = [1,-4,7,0,-1,10,3,]
# L.sort()
# print(L) #arranges list in ascending order and mutates L. Sort cannot work with strings

# L = [1,-4,7,0,-1,10,3,'apple','pig']
# L.reverse()
# print(L)

# L = [1,-4,7,0,-1,10,3]
# New_L = sorted(L) #This allows you to store the new sorted list to a variable
# print(L,New_L)

# l = [1,2,[2,3,4]]
# print(l[2][0:2])

# l = [1,2,3,4,5]
# l.clear() #this removes all the elements in the list
# print(l)

# l = [1,2,3,4,5,6,7,2,3]
# l.remove(3) #removes the first 3 it sees in the list
# print(l)

# l = [1,2,3,4,5,6,7,2,3]
# l.pop() #removes the last element in the list 
# print(l)

# l = [1,2,3,4,5,6,7,2,3]
# a = l.pop(0) #removes the element at index 0 and also saves it to a 
# print(l,a)

# l = [1,2,3,4,5,6,7,2,3]
# del(l[3]) #removes the element a index 3
# print(l)

# l.max() #this gives the maximum value in a list works with tuples and dictionaries also

# l= ['ben','sam','tolu','bolu','max']
# index = l.index('tolu') #This is used to get the index of a particular value in the list so her index will become 2
# print(index)

#sum(list) #this is used to sum all the elements in a list it only works for integers
# ================
# Class Work 3
# ================


# def sort_words(sen):
#     """Returns words in alphabetical order"""
#     List = sen.split(' ')
#     List.sort()
#     return List
# print(sort_words("this is a word"))


# ================
# Class Work 4
# ================


# def sq(l):
#     """A function that finds the square of a list and mutates them directly from the original ist without creating another list"""
#     for index in range(len(l)):
#         l[index] = l[index]**2
#     return l
# zz = [3,5,7,9]
# # print(sq(zz))
# l =[]

# for i in range(len(zz)):
#     zz.append(i)
#     print(zz)

# ================
# Making A Copy of a List
# ================
# L = [1,2,3,4,5,6,7,8]
# Lcopy = L[:]
# print(Lcopy)
#N.B if you do L=Lcopy it makes Lcopy an alias of L. So anything you change in L will change in Lcopy. So we use Lcopy =L[:] to create a copy of a list

# ================
# Class Work 5
# ================

# def remove_all(l,e):
#     """Mutates L to remove all elements that has e"""
#     lnew = l[:]
#     l.clear()
#     for index in lnew:
#         if index != e:
#             l.append(index)
    
# lead = [1,2,2,2,2,2,3]
# remove_all(lead,2)
# print(lead)


# ================
# Class Work 6
# ================


l = [1,7,3,4,5,6]
l_c = l[1]
# l_cc = l_c[:]
l.sort()
print(l_c,l[1]) #should return 2 and 5
# l1 = [(index**2) for index in l if index%2 == 0 ]
# print(l1)


# L = [[index,index**2] for index in range(40) if index%7 ==0]
# print(L)




