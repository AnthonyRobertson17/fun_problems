#!/usr/local/bin/python3
from random import randint
import time


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
    global stack, numPancakes, totalFlips, totalFlipped

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

    totalFlipped += index + 1
    totalFlips += 1
    return

# Prints tracked stats about the last run algorithm
def print_report(name):
    # Global Variables
    global totalFlips, totalFlipped, totalTime, numRuns

    avgFlipSize = totalFlipped / totalFlips
    avgNumFlips = totalFlips / numRuns
    avgNumFlipped = totalFlipped / numRuns
    avgTime = totalTime / numRuns
    print ('-----------------------')
    print ('     ', name)
    print ('-----------------------')
    print ('Total Flips: ', totalFlips)
    print ('Average # of flips: %.2f' % (avgNumFlips))
    print ('Average # of Pancakes / Flip: %.2f' % (avgFlipSize))
    print ('Average # of Pancakes Flipped: %.2f' % (avgNumFlipped))
    print ('Total time taken: %.5f' % (totalTime))
    print ('Average time taken: %.5f' % (avgTime))
    return

# Resets the stat tracking variables
def reset():
    # Global Variables
    global totalFlips, totalFlipped, totalTime

    totalFlips = totalFlipped = 0
    totalTime = 0
    return

# Set up a randomized stack of 0's and 1's
def create_stacks():
    global allStacks, stack, numPancakes, numRuns
    allStacks = []
    for i in range(0, numRuns):
        stack = []
        for i in range(0, numPancakes):
            stack.append(randint(0, 1))
        allStacks.append(stack[:])
    return

# Initializing data from the input file
def init():
    # Global Variables
    global numPancakes, numRuns, fileIn

    fileIn = open('input.txt', 'r')
    numPancakes = int(fileIn.readline())
    numRuns = int(fileIn.readline())
    fileIn.close()
    create_stacks()

def run_algorithms():
    # Global varaibles
    global allStacks, stack, numRuns, totalTime

    reset()
    for i in range(0, numRuns):
        stack = allStacks[i][:]
        startTime = time.time()
        ginger_sorts()
        totalTime += time.time() - startTime
    print_report('Ginger')

    reset()
    for i in range(0, numRuns):
        stack = allStacks[i][:]
        startTime = time.time()
        anthony_sorts(0)
        totalTime += time.time() - startTime
    print_report('Anthony DUMB')

    reset()
    for i in range(0, numRuns):
        stack = allStacks[i][:]
        startTime = time.time()
        anthony_sorts(1)
        totalTime += time.time() - startTime
    print_report('Anthony SMART')

    return

def main():
    # Global variables
    global numPancakes, numRuns
    init()
    print ('========================================')
    print ('                Results')
    print ('Number of Pancakes: ', numPancakes)
    print ('Number of Runs: ', numRuns)
    print ('========================================')
    run_algorithms()
    return

if __name__ == '__main__':
    main()
