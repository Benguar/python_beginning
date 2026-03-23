import matplotlib.pyplot as plot #this tells python that i will like to refer to imported matplotlib.pyplot as plot
import random
# xval = [x for x in range(21) if not x%2]
# yval = [x for x  in range(51) if not x%5]
# print(plot.plot(xval,yval))
# plot.plot(xval,yval)

#random.random() is used to grab a random number between 0 and 1 
#random.check(list) is used to grab a random element in a list


#Simulation is randomness 
def simulation(x,y,z=20):
    increase= (y-x)/z
    list= [x]
    for index in range(z):
        grab= list[-1]
        list.append(grab+increase)
    print(list)
simulation(1,3)
    
