#!/usr/local/bin/python3
from random import randint

def joseph_sorts():
    return

def ginger_sorts():
    return

def flip(number):
    return

def print_report(name):
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
    global numFlips, avgFlipSize, numFlipped
    numFlips = numFlipped = avgFlipSize = 0
    return

def init():
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
    return

if __name__ == '__main__':
    main()
