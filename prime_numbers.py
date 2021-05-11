def prime_list(n):

    for i in range(2, n+1):
        c = 2
        is_prime = True

        while is_prime and c < i:
            if i%c == 0:
                is_prime = False
            else:
                c += 1
        
        if is_prime:
            prime.append(i)

    return f'All these numbers are primes: {prime}'

if __name__ == '__main__':
    prime = []
    number = int(input('Write a high number: '))
    print(prime_list(number))
