# Complete the code to make the HiLo game...

import random

def main():
    # Pick a random number between 1 and 100, inclusive
    secret = random.randrange(1, 101);
    print("Can you guess my secret?")
    # put your code here
    n= int(input("Pick a number between 1 and 100:"))
    x=0
    while n!=secret:
        if n>secret:
            print("High")
        if n<secret:
            print("Low")
    x += 1
    return



main()
