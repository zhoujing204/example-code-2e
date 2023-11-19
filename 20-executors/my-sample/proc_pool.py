import sys
from concurrent import futures #1
from time import perf_counter
from typing import NamedTuple

from primes import is_prime, NUMBERS

class PrimeResult(NamedTuple): #2
    number: int
    flag: bool
    elapsed: float
    
def check(n: int) -> PrimeResult:
    t0 = perf_counter()
    res = is_prime(n)
    elapsed = perf_counter() - t0
    return PrimeResult(n, res, elapsed)

def main(workers = None) -> None: #3
    executor = futures.ProcessPoolExecutor(workers) #4
    actual_workers = executor._max_workers #5
    
    print(f'Checking {len(NUMBERS)} numbers using {actual_workers} workers')
    
    t0 = perf_counter()
    
    numbers = sorted(NUMBERS, reverse=True)
    with executor:
        for number, prime, elapsed in executor.map(check, numbers):
            label = 'P' if prime else ' '
            print(f'{number:16}  {label} {elapsed:9.6f}s')
    time = perf_counter() - t0
    print(f'Total time: {time:.2f}s')
    

if __name__ == '__main__':
    main(10)    