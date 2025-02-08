prime_numbers = sorted([2, 3] + [6*x - 1 for x in range(1, 6)] + [6*x + 1 for x in range(1, 6)])


random_numbers = range(1, 6)


# create a function that checks for prime numbers by brute force

def find_prime(numbers):
    prime_numbers = [2, 3]
    for number in numbers:
        if number <= 0:
            pass
        else:
            prime_numbers.append((6*number + 1))
            prime_numbers.append((6*number - 1))


    return sorted(prime_numbers)

print(find_prime(random_numbers))

# create a filter object and filter through the list of numbers with a function

def is_prime(number):
    for x in range(2, number):
        if x%2 == 0:
            return False
    return True

primes = filter(is_prime, random_numbers)
print(primes)