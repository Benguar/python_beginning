# We're creatigna an algorithm that approximates the square root of a number if or not it's withing a range that we set that is epsilon epsilon creates a range e.g if our number is 36 and epsilon is 0.5 itll look for numbers thats within 35.5 and 36.5

x = 4
num_guess = 0
guess = 0
epsilon = 0.01
increment = 0.0001


while abs(guess**2 -x) >= epsilon and guess**2 <= x+epsilon: # a while loop to check if the square of guess minus the initial value is within the epsilon range. So this while loop checks if the square root of the guess number is within the range of the epsilon value we set
    guess += increment
    num_guess+=1
    # if abs(guess**2) >= x+epsilon:
    #     print('you too do o :(')
    #     break
print(num_guess)
print(guess)

#always use a range while dealing with floats like i did with epsilon if you use == it will give you error cuz it wont calculae the actual value