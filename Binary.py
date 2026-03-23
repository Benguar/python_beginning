#Here we're creating  code to convert a number to base 2

number = int(input('Input the number you want to change to binary'))
original_number = number
b = int(input('input the base from 2 - 15'))

#We're making binary a string so we will be able to input values
binary = ''
if b > 15 or b < 2:
    b = int(input('Input a valid base'))
    base = number % b
    base = str(base)
    binary =  base + binary
    number = number//b
elif number < 0:
    number = abs(number) #we're turning he negative number to positive number
    while number > 0:
            base = number % b
            base = str(base)
            binary =  base + binary
            number = number//b
    print(f'-{binary}')
else:
    if b == 11 :
        while number > 0:
            base = number % b
            base = str(base)
            if base == '10':
                base = 'A'
                # print(base)
            binary =  base + binary
            number = number//b
        print(f'{original_number} to base {b} is {binary} :)')
    elif b == 12:
        while number > 0:
            base = number % b
            base = str(base)
            if base == '10':
                base = 'A'
            if base == '11':
                base = 'B'
                # print(base)
            binary =  base + binary
            number = number//b
        print(f'{original_number} to base {b} is {binary} :)')      
    elif b == 13:
        while number > 0:
            base = number % b
            base = str(base)
            if base == '10':
                base = 'A'
            if base == '11':
                base = 'B'
            if base == '12':
                base = 'C'
                # print(base)
            binary =  base + binary
            number = number//b
        print(f'{original_number} to base {b} is {binary} :)')      
    elif b == 14:
        while number > 0:
            base = number % b
            base = str(base)
            if base == '10':
                base = 'A'
            if base == '11':
                base = 'B'
            if base == '12':
                base = 'C'
            if base == '13':
                base = 'D'
                # print(base)
            binary =  base + binary
            number = number//b
        print(f'{original_number} to base {b} is {binary} :)')      
    elif b == 15:
        while number > 0:
            base = number % b
            base = str(base)
            if base == '10':
                base = 'A'
            if base == '11':
                base = 'B'
            if base == '12':
                base = 'C'
            if base == '13':
                base = 'D'
            if base == '14':
                base = 'E'
                # print(base)
            binary =  base + binary
            number = number//b
        print(f'{original_number} to base {b} is {binary} :)')      
    else:
        if number == 0:
            binary  =  '0'
            print(f'{original_number} to base {b} is {binary} :)')
        else:
            while number > 0:
                base = number % b
                base = str(base)
                binary =  base + binary
                number = number//b
            print(f'{original_number} to base {b} is {binary} :)')

