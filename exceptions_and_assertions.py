#Exceptions are used in places where error might occur it uses try except blocks

# def add(value):
#     total = 0
#     for index in value:
#         total += int(index)
#     return total
# print(add('123a'))
#In the function above if a letter is contained in the error it will return an error so we use the try except block

# def add(value):
#     total = 0
#     for index in value:
#         try:
#             total += int(index)
#         except:
#             print(f'can not add value {index}')
#     return total
# print(add('123a'))

#In the function above if there is an error in the try block python does not immediately give an error it moves to the except block and runs what is in there so that error will not affect the whole code by stopping without returning anything. These are useful in user inputs 


# ===========================
# Example 2 
# ===========================

# try:
#     a = int(input('Input a number'));
#     b = int(input('Input another number'));
#     print(f'The division is {a/b}')
# except:
#     print('User error input')
# print(a)

#There are different types of except blocks e.g except ValueError: is used for value errors except ZeroDivisionError: Is an error for zero division:

# ===========================
# Classwork
# ===========================

def pairwise(list1,list2):
    assert len(list1) == len(list2),"The lists are not of equal lenghts"
    assert len(list1) or len(list2) != 0,"The lists are empty"
    #assertions are used to enforce rules that must be valid before the programme contiues and also give responses if otherwise
    list_new=[]
    for index in range(len(list1)):
        try:
            list_new.append(list1[index]/list2[index])
        except:
            raise ZeroDivisionError("List contains 0 in the denominator")
        #raise is used to halt the programme immediately an exception is found and give a custom error message
    return(list_new)
print(pairwise([],[]))