#!/usr/local/bin/python3
from random import randint

def joseph_sorts():
    return

# This sort gets the top "group" of pancakes (that have the same face up),
# figures out if they need to be flipped upside down or not, and then
# flips the group to the bottom of the stack
# This is better than ginger but still inefficiant
# smart will extend the top group after making it upside down
def anthony_sorts(smart):
    # Global variables
    global stack, numPancakes

    lastIndex = numPancakes - 1
    numDone = 0
    while numDone < numPancakes:
        i = 0
        face = stack[i]
        # Find top group thats within the 'not done' stack
        while i + 1 <= lastIndex - numDone and stack[i + 1] == face:
            i += 1
        # Make sure group is upside down
        if face == 1:
            flip(i)
        if smart == 1:
            while i + 1 <= lastIndex - numDone and stack[i + 1] == 0:
                i += 1
        flip(lastIndex - numDone)
        numDone += i + 1
    return

# This sort looks at the top pancake and makes sure its upside down
# The stack is then flipped to "Thow the top pancake to the bottom"
# The process is repeated flipping 1 pancake less each time until
# the entire stack is flipped
# BAD sort, ginger should feel bad
def ginger_sorts():
    # Global Variables
    global stack, numPancakes

    lastIndex = numPancakes - 1
    for i in range(0, lastIndex + 1):
        if stack[0] == 1:
            flip(0)
        flip(lastIndex - i)
    return

# Function to flip a stack of 1's and 0's from 0 through a given index
def flip(index):
    # Global Variables
    global stack, numPancakes, numFlips, numFlipped

    before = stack[0 : index + 1]

    # Flip the values of the pancakes to be flipped
    for i in range(0, index + 1):
        if before[i] == 0:
            before[i] = 1
        else:
            before[i] = 0

    # Reverse the order of the pancakes to be flipped
    # and place back on the the stack
    j = index
    for i in range(0, index + 1):
        stack[i] = before[j]
        j -= 1

    numFlipped += index + 1
    numFlips += 1
    return

# Prints tracked stats about the last run algorithm
def print_report(name):
    # Global Variables
    global stack, numPancakes, visual
    global numFlips, avgFlipSize, numFlipped

    avgFlipSize = numFlipped / numFlips
    print ('-----------------------')
    print ('     ', name)
    print ('-----------------------')
    print ('Total Flips: ', numFlips)
    print ('Total Pancakes Flipped: ', numFlipped)
    print ('Average Pancakes / Flip: ', avgFlipSize)
    return

# Resets the stat tracking variables
def reset():
    # Global Variables
    global numFlips, avgFlipSize, numFlipped, stack
    global originalStack

    numFlips = numFlipped = avgFlipSize = 0
    stack = originalStack[:]
    return

# Set up a randomized stack of 0's and 1's
def randomize_stack():
    global stack, numPancakes
    for i in range(0, numPancakes):
        stack.append(randint(0, 1))
    return


# Initializing data from the input file
def init():
    # Global Variables
    global stack, numPancakes, numRuns, visual, fileIn
    global originalStack

    stack = []
    fileIn = open('input.txt', 'r')
    numPancakes = int(fileIn.readline())
    numRuns = int(fileIn.readline())
    visual = int(fileIn.readline())
    fileIn.close()
    randomize_stack()
    originalStack = stack[:]



def main():
    # Global variables
    global numPancakes
    init()
    reset()
    print ('========================================')
    print ('                Results')
    print ('Number of Pancakes: ', numPancakes)
    print ('========================================')
    ginger_sorts()
    print_report('Ginger')
    reset()
    anthony_sorts(0)
    print_report('Anthony DUMB')
    reset()
    anthony_sorts(1)
    print_report('Anthony SMART')
    return

if __name__ == '__main__':
    main()
