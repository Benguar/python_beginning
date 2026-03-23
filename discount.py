user_input = int(input('Input your bill amount'))
if user_input >= 5000:
    dis = '20%'
    discount = (80/100)*user_input
    print(f'your discount for your amount{user_input} is{user_input-discount} pay {discount}')
elif user_input >= 2000 and user_input < 5000:
    dis = '20%'
    discount = (15/100)*user_input
    print(f'your discount for your amount{user_input} is{user_input-discount} pay {discount}')
else:
    print(f'you dont get any discount for {user_input}')