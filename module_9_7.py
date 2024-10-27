
def is_prime(func):
    def wrapper(*args, **kwargs):
        sum_t = func(*args)
        for i in range(2, sum_t - 1):
            if sum_t % i == 0:
                print('Составное')
                return sum_t
        print('Простое')
        return sum_t
    return wrapper

@is_prime
def sum_three(z, x, y):
    return z + x + y


result = sum_three(2, 3, 6)
print(result)