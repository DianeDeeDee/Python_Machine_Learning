import sys
import beginner_python_1 as bp1

#import beginner_python_1 as bp1

#import function_1 as f_1

def function_1(number):
    return number

def return_primes(number):

    """
    return_primes() is the the function that the function that returns the list of all primes
    smaller than number.
    list_of_primes is the list of all the prime numbers whose values are lower than number
    """
    list_of_primes = []
   # bp1.f_1(number)
    for i in range(1,number):
        if ((bp1.is_prime(i))):
            list_of_primes.append(i)
        else:
            continue

    return list_of_primes

print("\n\n")

if __name__ == '__main__':
    print("What is your number again?")
    number = sys.stdin.readline()
    number = int(number)
    print('The number is ' + str(number))
    print("The list of all primes smaller than %s" %number,"is:")
    print(" list_of_primes=",return_primes(number))


print("\n\n")

