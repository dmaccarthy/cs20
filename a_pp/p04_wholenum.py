"""
CSE 2110: Procedural Programming
Pre- & Post-Conditions

"""

def smallestFactor(n: int) -> int:
	"Calculate the smallest factor of a natural number"
	f = 2
	while f * f <= n:
		if n % f == 0: return f
		f += 1
	return n

def isPrime(n: int) -> bool:
	"Check whether a number is prime"
	return n > 1 and smallestFactor(n) == n

def primes(howMany: int = 20) -> list:
	"Make a list of prime numbers"
	p = 2
	primes = []
	while howMany:
		if isPrime(p):
			primes.append(p)
			howMany -= 1
		p += 1
	return primes

def factor(n: int) -> list:
	"Make a list of a number's prime factors"
	factors = [1] if n == 1 else []
	while n > 1:
		f = smallestFactor(n)
		factors.append(f)
		n //= f
	return factors
