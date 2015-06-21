#print and tell in reverse order
#change the range to 10-100 if you need double digits
#works for python 2 & python 3

import random
import math
import sys

x = int (input ('how many numbers you wanna try:'))

for y in range(0,x):
    a = int (math.floor( (random.random () * 10)))
    b = str(a) + " "
    sys.stdout.write(b)
    #print (a,' ',end='')

print ('')
