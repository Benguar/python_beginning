# Tuples are sequence of data types (can be different) that are immutable(cannot be changed). You can slice through tuples just the way you slice through strings
tuple1 = (5,) #Single value tuple
tuple2 = (5,False,'ana',3.23,None,'ben') #Multi Value Tuple
tuple3 = (5,False,'ana',3.23,None,'ben',(1,'2',3)) #Tuple inside a tuple
print(tuple3[6][0:3]) #How to call a tuple inside a tuple


# ================
# Example of how to use tuples
# ================

# def Quotient_and_remainder(x,y):
#     q = x//y
#     r = x%y
#     return(q,r)
# (Quotient, Reminder) = Quotient_and_remainder(10,3)
# print(f'Quotient is {Quotient}')
# print(f'Remainder is {Reminder}')


#In the example above, We have successfully used tuples to bind 2 different values to two different variables 

# ================
# Classwork
# ================

def char_counts(s):
    v = 0
    
    """A function that returns the numbers of vowels and consonants in a string"""
    vowels = ('a','e','i','o','u')
    for i in s:
        if i in vowels:
            v +=1
    consonant = len(s) - v
    return(v, consonant)
    
print(char_counts('elephant'))
