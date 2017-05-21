#!/usr/local/bin/python3
from random import randint

def joseph_sorts():
    return

# This sort looks at the top pancake and makes sure its upside down
# The stack is then flipped to "Thow the top pancake to the bottom"
# The process is repeated flipping 1 pancake less each time until
# the entire stack is flipped
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
    print('-----------------------')
    print(' Results - ', name)
    print('-----------------------')
    print('Number of Pancakes: ', numPancakes)
    print('Total Flips: ', numFlips)
    print('Average Pancakes / Flip: ', avgFlipSize)
    return

# Resets the stat tracking variables
def reset():
    # Global Variables
    global numFlips, avgFlipSize, numFlipped

    numFlips = numFlipped = avgFlipSize = 0
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

    stack = []
    fileIn = open('input.txt', 'r')
    numPancakes = int(fileIn.readline())
    numRuns = int(fileIn.readline())
    visual = int(fileIn.readline())
    fileIn.close()
    randomize_stack()


def main():
    init()
    reset()
    ginger_sorts()
    print_report('Ginger')
    return

if __name__ == '__main__':
    main()
