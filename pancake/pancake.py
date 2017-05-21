#!/usr/local/bin/python3
from random import randint

def joseph_sorts():
    return

def ginger_sorts():
    return

def flip(number):
    # Global Variables
    global stack, numPancakes, numFlips, numFlipped

    before = stack[0 : number + 1]

    # Flip the values of the pancakes to be flipped
    for i in range(0, number + 1):
        if before[i] == 0:
            before[i] = 1
        else:
            before[i] = 0

    # Reverse the order of the pancakes to be flipped
    # and place back on the the stack
    j = number
    for i in range(0, number + 1):
        stack[i] = before[j]
        j -= 1

    numFlipped += number + 1
    numFlips += 1
    return

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

def reset():
    # Global Variables
    global numFlips, avgFlipSize, numFlipped

    numFlips = numFlipped = avgFlipSize = 0
    return

def init():
    # Global Variables
    global stack, numPancakes, numRuns, visual, fileIn

    stack = []
    fileIn = open('input.txt', 'r')
    numPancakes = int(fileIn.readline())
    numRuns = int(fileIn.readline())
    visual = int(fileIn.readline())
    fileIn.close()
    for i in range(0,numPancakes):
        stack.append(randint(0,1))
    return

def main():
    init()
    reset()
    ginger_sorts()
    print_report('Ginger')
    return

if __name__ == '__main__':
    main()
