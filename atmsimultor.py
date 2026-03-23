
def atm_simulator(user_input,pin):
    counter = 0
    x = False
    while counter <=3:
        counter += 1
        if user_input == pin:
            x = True
            return "correct pin"
            break
        else:
            user_input = int(input('Wrong pin input your pin'))
        
    if x == False:
        return "account blocked"
user_input = int(input('input your pin'))
pin = 1234
print(atm_simulator(user_input,pin))
