#An Algorithm that does guess and check using bisection guess it is faster than Approximation method

x = 5
epsilon = 0.1
num_guess = 0
if 0<x<1:
    low = x
    high = 1
else:
    low = 0
    high = x
guess = (high + low)/2
while abs(guess**2 - x) > epsilon:
    num_guess +=1
    if guess**2 > x:
        high = guess
    else:
        low = guess
    guess = (high + low)/2
    print(low,high)
print(guess)
