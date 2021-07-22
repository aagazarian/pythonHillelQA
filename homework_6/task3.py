def is_prime(a):
    number = 2
    while a % number > 0 and a >= number:
        number += 1
    return a == number


print(is_prime(2))
