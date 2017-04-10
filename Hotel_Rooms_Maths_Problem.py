import itertools
import os
roomnumber = 0
y = []
rightroom = []
xy = 0
validchecker = ""

def clear():
    if os.name != 'nt':
        os.system('clear')
    else:
        os.system('cls')
for n in range(0, 100):
    roomnumber+=1
    for x in range(1, roomnumber):
        if x != 1:
            divisor = roomnumber % x
            if divisor == 0:
                y.append(x)
    if(sum(y) > roomnumber):
        for allcombinations in range(0, len(y)+1):
          for thesubsets in itertools.combinations(y, allcombinations):
            if sum(thesubsets) != roomnumber and validchecker != "invalid":
                xy = 0
            else:
                validchecker = "invalid"
        if validchecker != "invalid":
            rightroom.append(roomnumber)
        clear()
        print('The possible room numbers are {}'.format(rightroom))

        validchecker = ""
        y = []
    else:
        y = []
