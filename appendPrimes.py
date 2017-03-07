'''
Mason Kam
appendPrimes.py

Created on Feb 24, 2017
Last updated on Mar 6, 2017

Description: This program appends the amount of numbers that is requested to the already existing 
list of primes and its category (prime or composite) denoted by 1 or 0. The method used here is the 
brute force checking up to the sqrt of the given number to determine whether it is a prime or not.

Instructions: Simply run the program and user input the amount of numbers to append to the given files
under the append definition. Change the file names to change the course.

These are python references to assist in coding notations
-https://docs.python.org/3/tutorial/
-https://www.tutorialspoint.com/python/
-https://docs.python.org/3/library/index.html

'''

import math

def getVal():
    while(True):
        try:
            value = int(input("Please insert num to append to prime list:"))
            if(value >= 2):
                break
    
        except ValueError:
            print("Bad input, try again.") #if it was a string, not an int.

    return value

#Check if prime
def testPrime(num):
    #Only look up to sqrt of num
    for test in range(2,int(math.sqrt(num))+1,1):
        if (num % test) == 0:
            return False
    return True

#Append the amount of numbers specified in the parameter
def append(numToAppend):
    #Change these file names to change the files that are appended to
    fh = open("primes2.txt",'a')
    fh2 = open("numPrimes2.txt",'r+')
    
    fh2.seek(0)
    maxNum = int(fh2.readline())
    
    if(numToAppend < 1):
        print('invalid number to append')
        return
    else:
        print('Appending: {0}..'.format(numToAppend))
     
    #Test whether next num is prime and append to file
    for it in range(maxNum + 1,maxNum + numToAppend + 1,1):
        if(testPrime(it)):
            fh.write(str(it) + ':' + str(1) + '\n')
        else:
            fh.write(str(it) + ':' + str(0) + '\n')
    
    #Update Max Number
    fh2.seek(0)
    fh2.write(str(maxNum + numToAppend))
    
    fh.close()
    fh2.close()
    
    print('Done appending')
    
    
    
def main():
 
    num = getVal()
    append(num)
    


if __name__ == '__main__': main()
    
