'''
Simulating the monty hall problem with some parameters generalized
I knew how the problem worked mathematically but I wanted to show it with a program 
'''

import random
import copy

#parameters. I could do a variable number of cars, but that is lame and I don't want to B)
n = 100 #number of doors
t = 1000000 #number of iterations to test

#places goats behind all n doors, then replaces one with a car
def populateDoors():
    doors = []
    for i in range(n):
        doors.append('g')
    car_idx = random.randint(0, n-1)
    doors[car_idx] = 'c'
    return doors

#returns the index of a random door that is not the chosen door and does not contain the car
def getRevealedDoor(choice, doors):
    idx = random.randint(0, n-1)
    #remove a random non-chosen door that does not contain the car
    while doors[idx] == 'c' or idx == choice:
        idx = random.randint(0, n-1)
    return idx

#runs a single iteration of the monty hall problem where the contestant switches their initial choice of door
def runTest():
    #populate doors
    doors = populateDoors()

    #choose a random door
    init_choice = random.randint(0, n-1)

    #the host reveals which a door that for sure has a goat behind it
    revealed = getRevealedDoor(init_choice, doors)

    #reveal what is behind the door not initially chosen
    indices = range(n)
    indices.remove(init_choice)
    indices.remove(revealed)
    result = doors[indices[0]]
    return result


def __main__():
    car_count = 0
    for i in range(t):
        res = runTest()
        if res == 'c':
            car_count = car_count + 1
    print("The host reveals that " + str(1) + " out of " + str(n) + " door(s) contain goats.")
    print(str(car_count * 100.0 / t) + "%")





if __name__ == '__main__':
    __main__()