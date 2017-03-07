'''
Mason Kam
primeCounting.py

Created on Feb 23, 2017
Last Updated on Mar 6, 2017

Description:
This program asks for a number and lists out pi(x), x/lnx, li(x), their differences, x/pi(x) and the 
square root of the num. Currently this reads from 2 files: One containing the max number calculated 
to and one containing the numbers from 2-x and an indicator 1 or 0 of whether the number is prime 
or composite, respectively.

Currently containing up to 10 million values in primes.txt because of github's 100mb limit for files.
Another 10 million values would take around 20 minutes to compute using the appendPrimes.py file.

Instructions: Simply run the program with the numPrimes.txt and primes.txt in the local directory.
Currently with 10 million values to read from the file, the wait time is around 15 seconds before startup.
Follow instructions given on prompt.

Sources:
This helped in just getting a general sense of the connection and definitions of pi(x), li(x) and x/lnx and how they relate
-https://en.wikipedia.org/wiki/Prime-counting_function

These are python references to assist in coding notations
-https://docs.python.org/3/tutorial/
-https://www.tutorialspoint.com/python/
-https://docs.python.org/3/library/index.html

Package scipy is used for integration function li(x)
-https://docs.scipy.org/doc/scipy-0.18.1/reference/generated/scipy.integrate.quad.html

To verify my output for pi(x)
-https://primes.utm.edu/nthprime/

To verify my output for li(x)
-http://keisan.casio.com/exec/system/1180573428


'''

import math
import scipy.integrate.quadpack as quadpack


def welcome():
    print ("This is a prime comparison function")
    
def goodbye():
    print("Peace out!!")
    
#Get number to test
def getInput(maxVal):
    while(True):
        try:
            value = int(input("Please insert a number between 2 and {0}:".format(maxVal)))
            if(value <= maxVal and value >= 2):
                break
            
        except ValueError:
            print("Bad input, try again.") #if it was a string, not an int.

    return value

def retry():
    while(True):
        val = input("Again?(y/n): ")
        if val.lower() == "y":
            return True
        elif val.lower() == "n":
            return False

def pix(listOfPrimes, num):
    count = 0
    for it in range(2,num+1,1):
        if listOfPrimes[it] == 1:
            count +=1
    return count
    
    
#Returns floor of x/lnx
def XOverLNX(x):
    return math.floor(x/math.log(x))

#Returns floor of li(x)
def LiX(num):
    
    function = lambda t: (1/math.log(t))
    res=0
    
    #Special case: integration leads to 0 in denominator
    if(num == 2):
        return 1
    
    #Split into components for more precise integration for num > 1000
    if(num > 1000 and int(num/1000) > 1):
        mod = num % 1000
        div = int(num / 1000)
        
        #Add integration over 1000s
        for i in range (1,div+1,1):
            res += quadpack.quad(function,(i-1)*1000,i*1000)[0]
            
        #Add remainder
        res += quadpack.quad(function,div*1000,div*1000 + mod)[0]
    
    #Just calculate it directly
    else:
        res+=quadpack.quad(function,0,num)[0]
        
    return math.floor(res)
      
      
#Floor of sqrt
def rootNum(userVal):
    return math.floor(math.sqrt(userVal))


#Read input from files
def getFromFile():
    fh = open("primes.txt", 'r')        #holds list of numbers whether prime or composite
    fh2 = open("numPrimes.txt", 'r')    #holds count of primes
    
    maxVal = int(fh2.readline())
    line = ""   #To read set of numbers
    
    #Setup list of primes/nonprimes
    listOfPrimes = [-2 for i in range(maxVal+1)]
    for num in range(0,maxVal+1,1):
        
        line = fh.readline()
        pair = line.split(':')
        
        index = int(pair[0])
        val = int(pair[1])
        
        listOfPrimes[index] = val
    
    fh.close()
    fh2.close()
    #print (listOfPrimes)  
    return listOfPrimes, maxVal
    
    
def main():
    play = True
    
    welcome()
    listOfPrimes, maxVal = getFromFile()

    while(play):
        userVal = getInput(maxVal)

        print("Value inserted: {0}".format(userVal))
        
        actual = pix(listOfPrimes, userVal)
        print("Pi(x): {0}".format(actual))
        
        xestimate = XOverLNX(userVal)
        dif = abs(actual-xestimate)
        print("x/lnx Estimate: {0}. Difference: {1}".format(xestimate, dif))
        
        liestimate = LiX(userVal)
        dif = abs(actual-liestimate)
        print("Li(x) Estimate: {0}. Difference: {1}".format(liestimate, dif))
        
        sqroot = rootNum(userVal)
        print("sqrt(x): {0}\n".format(sqroot))
        
        play = retry()
    
    goodbye()


if __name__ == '__main__': main()
