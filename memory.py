import random
import math

x = int (input ('how many numbers you wanna try:'))

for y in range(0,x):
    a = math.floor( (random.random () * 10))
    print (a,end='')
    print (' ',end='')    

