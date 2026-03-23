import sys
sys.set_int_max_str_digits(100000000)

number = int(input('type the number you\'re looking for it\'s factorial'))
original_number = str(number)
factorial = number
tracker = True
while number >1:
    number -= 1
    factorial = factorial * number
x = str(factorial)



if(len(x)> 4):
    tracker = False
    approx =int(input('Number is large How many SF do you want to approximate too'))
    if x[approx] == '5' or x[approx] == '6' or x[approx] == '7' or x[approx] == '8' or x[approx] == '9':
        y = x[0:approx]
        z = len(x[approx:len(x)])
        p = int(y) + 1
    else:
        y = x[0:approx]
        z = len(x[approx:len(x)])
        p = int(y) 
if tracker:
    print(f'{original_number}! is {factorial}')
else:
    print(f'{original_number}! is {p}x10^{z}')
    
