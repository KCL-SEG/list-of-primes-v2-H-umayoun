"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    current_num = 0
    i=2
    while current_num != number_of_primes:
        prime = True
        for j in range(2, i-1):
            if i % j == 0:
                prime = False
                j=j+1
            else:
                j=j+1
    if prime == True:
        list.append(i)
    i=i+1

    print(list)    
                
    
    return list

primes(5)


