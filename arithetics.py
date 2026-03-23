# We're running a python code to solve arithmetics
# Bola,sam and Ada sell 10 tickets
# if Bola sells 2 less than sam
#    Ada sells twice as much as sam 
#    how many tickets did bola sam and ada sell


#we're using for loops for Bola,Ada and Sam. This runs various numbers to look for the set of numbers that matches the solution


flag = False
# Flag is acting as a tracker to know if the solution has been found and tell the remaining loop to stop

for Bola in range(11):
    for Sam in range(11):
        for Ada in range(11):
            Ada = 2*Sam
            Bola = Sam - 2
            total = Ada + Bola + Sam
            if total == 10 and Ada and Bola:
                flag = True
                print(f'Ada sold {Ada} tickets')
                print(f'Bola sold {Bola} tickets')
                print(f'Sam sold {Sam} tickets')
                break
        if flag:
            break
    if flag:
            break
    
