import sys
import beginner_python_1 as bp1
def return_primes(number):

    """
    return_primes() is the the function that the function that returns the list of all primes
    smaller than number.
    list_of_primes is the list of all the prime numbers whose values are lower than number
    """
    list_of_primes = []
    for i in range(1,number):
        if ((bp1.is_prime(i))):
            list_of_primes.append(i)
        else:
            continue

    return list_of_primes

print("\n\n")

print("The list of all primes smaller than %s "%"29" " is:\n            "
                                                "list_of_primes=",return_primes(29))


print("\n\n")

