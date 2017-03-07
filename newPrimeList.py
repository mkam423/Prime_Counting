'''
Mason Kam
newPrimeList.py

Created on Feb 24, 2017
Last update on Mar 6, 2017

Description: This program writes a new set of primes from 2-x for a given x that is requested 
by the user to a file.

Computational effort took more than half an hour by brute force method to compute and write prime 
list of 20 million to a file. For lower values it is about a minute per million numbers.

Instructions: Designate new file names to direct the writes to under the writeNew function definition.
Simply run the program and follow the prompt to given requested number of values to compute.

These are python references to assist in coding notations
-https://docs.python.org/3/tutorial/
-https://www.tutorialspoint.com/python/
-https://docs.python.org/3/library/index.html

'''

import math

def getVal():
    while(True):
        try:
            value = int(input("Please insert num to generate prime list:"))
            if(value >= 2):
                break
            
        except ValueError:
            print("Bad input, try again.") #if it was a string, not an int.

    return value

def Primes(maxVal):
    #Primes = 1, Composite = 0
    primes = [1 for x in range(maxVal+1)]   #Start off prime until proven otherwise
    
    #Non Prime or Composite
    primes[0] = -1
    primes[1] = -1
    
    #Test all the numbers if they are prime
    for num in range(2,maxVal,1):
        
        if(testPrime(num) == False):
            primes[num] = 0
            
    return primes


def writeNew(listOfPrimes, maxVal):
    #Change file names for every new write to prevent overwriting old ones
    fh = open("primes2.txt", 'w')
    fh2 = open("numPrimes2.txt", 'w')
    
    #Max val into separate file for ease
    fh2.write(str(maxVal))
    
    for it in range(0,maxVal+1, 1):
        fh.write(str(it) + ':' + str(listOfPrimes[it]) + '\n')
    
    fh.close()
    fh2.close()
    
    
def testPrime(num):
    #Only look up to sqrt of num
    for test in range(2,int(math.sqrt(num))+1,1):
        if (num % test) == 0:
            return False
    return True

    
def main():
  
    #numToCalculate = 100000
    numToCalculate = getVal()
    listOfPrimes = Primes(numToCalculate)   #Calculate primes
    writeNew(listOfPrimes, numToCalculate)     #Write to file



if __name__ == '__main__': main()
    
