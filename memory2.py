#print and tell in reverse order

#check $>python -V #to know the version
#python instructions to install dictionary module
#git clone https://github.com/tomislater/RandomWords.git
#cd RandomWords
#python setup.py install
#do same for python3.x or v2.x also if you want to use the module for python3

import sys

from random_words import RandomWords

rw = RandomWords()

x = int (input ('how many words you wanna try:'))

for y in range(0,x):
    a = rw.random_word()
    a = a + " "
    sys.stdout.write(a)

print('')
