def get_max_values(lists):
    return [max(lst) for lst in lists]

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def get_primes(numbers):
    return list(filter(is_prime, numbers))

lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
numbers = [3, 4, 8, 5, 5, 22, 13]
max_values = get_max_values(lists)
primes = get_primes(numbers)
print(primes) # [3, 5, 5, 13]
print(max_values) # [3, 6, 9]