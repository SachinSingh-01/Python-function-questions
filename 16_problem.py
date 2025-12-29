'''Write a function is_prime(n) that:
Returns True if the number is prime
Returns False otherwise'''
def is_prime(n):
    if n <= 1:
        print("Not a prime number")
    else:
        is_prime = True

    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")
is_prime(6)