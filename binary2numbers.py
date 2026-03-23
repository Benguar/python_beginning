#first i created an input for users to input he number they want to convert and their bases
binary =  int(input('Input a Number you want to convert to base 10 :)'))
binary = str(binary)
base = int(input('input the base of the current number2-9 :)'))
binary = binary[::-1] # here is to swap users numbers from right to left cuz thats how we'll be working on the numbers
number = 0 #this is the variable that adds the number
valid = True
for loop in range(len(binary)): # this loop is to loop the numbers the user input e.g if user input is 2 its should from from 0 to 1 we want it his way cuz string index starts from 0 and not 1 
    x = binary[loop] #adding each number in the string to x
    if base>9 or base<2: #checking if base imputed is valid
        print(f'{base} is an invalid input please input a valid one:(')
        valid = False
        break
    else:
        if x == str(base): #checking if no number imputed matches the base remember base is in int so i have to convert to string
            valid = False
            print("Mathematical error :(")
            break
        else:
            if x:
                number += int(x)* (base ** loop)
if valid:
    binary = binary[::-1]
    print(f'{binary} base {base} to base 10 is {number}')
