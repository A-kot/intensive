n = int(input())
primes = [i for i in range(n+1)]
primes[1] = 0

for i in range(2, n+1):
    if primes[i] != 0:
        j = 2 * i
        while j <= n:
            primes[j] = 0
            j += i

primes = [primes[i] for i in range(len(primes)) if primes[i] != 0]
print(primes)
