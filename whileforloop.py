# using while loop
#while loop is used to keep checking if a condition is true it should keep executing
# a condition until    false

# where = input("You are lost in a forest do you wan to go right or left")
# v = 1
# while where == "right":
#    where = input("You are lost in a forest do you wan to go right or left")
#    v += 1
#    if v > 2:
#        print(":(")
# print(f"you just got out of the forest passing {where}")

#n = int(input("input a non-negative number"))

#while n>0:
#    print("x")
    #same as n -= 1
#if you enter n infinite loop press control + c to exit
#print(f"{n}is less than or equal to 0")

#for loop

#for loop is a shorter way to use while it also uses start,stop and step mechanism

#for i in range(4):
#    print(i)
    # this means i will go up to but not including 4 thats 1,2,3

#for i in range(2,5):
 #   print(i)
    # this means i will start at 2 and go up to but not including 5 thats 2,3,4

#for i in range(0,8,2):
#    print(i)
    # this means i will start at 0 and skip a number
    #to the second and go up to but not including 8 thats 0,2,4,6


# start = 3
# end = 5
# my_sum = 0
# for i in range(start, end+1):
#     my_sum += i
# print(my_sum)

# Breaks statements help exit loops

# my_sum = 0

# for i in range(5,11,2):
#     my_sum += i
#     if my_sum == 5:
#         break
#     my_sum += 1
# print(my_sum)

#CW: A code to print out even numbers in a range
# even_number_tracker = 0
# for i in range(170):
#     if i%2 == 0:
#         print(i)
#         even_number_tracker +=1
#     # else:
#     #     print(f'{i} is not even')
# print(f'we have {even_number_tracker} numbers')


# looping through strings
word = "We are testing loops in strings"
# for i in range(len(word)):
#     if word[i] == 'i' or word[i] == 'u':
#         print('we have an i or u')

# a simpler way to loop through strings is using
# for char in word:
#     if char == 'i' or char == 'u':
#         print('we have an i or u')

unique = input("give me a word let me find the unique letters")

s = ''
not_seen = ''
for letter in unique:
        if letter not in s:
            s += letter
        else:
            pass
        # Pass is a keyword in python that means do nothing
p = len(s)
print(unique,'we have ',len(s),' unique letters')
