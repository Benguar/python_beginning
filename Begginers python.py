# f strings are used to include variables in a string
#e.g print(f"i am  {name}")

# sequence in string. if you want to loop through string you can do that using  a
#sequence. start, stop and step e.g
# n = 'benedict' if we want to pick ben we use ben=n[0:3]
#it creates a range of b to n. All chracters in python start with 0 and 3 stop
# at the immediate lower number = 2
#if we want to crate a range consisting of letter bndc in benedict we can do that
#using the start stop step sequence that is n[0:8:2] that is start at 0, stop at
#8 and skip to the 2nd character




# using if else statement

# guess = int(input('Guess a number'))
# number = 23
# if(guess == number):
#    print('You\'re a wizard ')
#    print('You\'re a wizard ')
# elif guess < number:
#    print('Your nuber is lower than magic number')  
# elif guess > number: 
#    print('Your nuber is higher than magic number')

# using while loop
#while loop is used to keep checking if a condition is true it should keep executing
# a condition until    false

#where = input("You are lost in a forest do you wan to go right or left")
#v = 1
#while where =  = "right":
#    where = input("You are lost in a forest do you wan to go right or left")
#    v += 1
#    if v > 2:
#        print(":(")
#print(f"you just got out of the forest passing {where}")

# n = int(input("input a non-negative number"))

# while n>0:
#    print("x")
#    n -= 1
# #if you enter n infinite loop press control + c to exit
# print(f"{n}is less than or equal to 0")

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
# mysum = 0
# for i in range(start, end+1):
#     mysum += i
# print(mysum)

name = 'bened.ict'
lenght = 0
for index in name:
    if index == '.':
        break
    lenght += 1