# we're building algorithm to know if a number is a perfect square
#we want a user to input  value and algorithm to check if the number i a perfect square

# user_input = int(input("input the number you want to check if its a perfect square"))


# # first check if input its positive or negative
# if user_input < 0:
# #here we're saying if its negative make the input positive then run the while loop to check for possible integers till it meets an integer that the square is equal to or greater than the user input
#     user_input = -user_input
#     guess = 0
#     while guess** 2 < user_input:
#         guess += 1
#     if guess * guess == user_input:
# # We're changing the input back to negative for he user
#         user_input = -user_input
#         guess = -guess
#         print(f"{user_input} is a perfect square of {guess}")
#     else:
# # We're changing the input back to negative for he user
#         user_input = -user_input
#         guess = -guess
#         print(f"{user_input} is not a perfect square ")
# else:
# #here we're saying run the while loop to check for possible integers till it meets an integer that the square is equal to or greater than the user input
#     guess = 0
#     while guess** 2< user_input:
#         guess += 1
#     if guess * guess == user_input:
#         print(f"{user_input} is a perfect square of {guess}")
#     else:
#         print(f"{user_input} is not a perfect square ")


#Classwork: Hardcode a number and run and loop that checks if the number is less than or equals 0

secret_number = 2

for index in range(0,11):
    if index == secret_number:
        print(f'i found the number its {index}')
    elif index == 10 and index != secret_number:
        print('i cant find the number ')
